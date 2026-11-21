#!/usr/bin/env python3
"""Validate the exact private generic-only source surface; never approve a release."""
from __future__ import annotations

import json
from pathlib import Path
import re
import sys

import yaml

ROOT = Path(__file__).resolve().parents[1]
FORBIDDEN_COMPONENTS = {"private", "owner-private", "owner_private", "reconciliation",
                        "legacy-2026-11-01", "incident-archive", "session-history"}
FORBIDDEN_FILENAMES = {"ATLAS_CONTEXT_PROFILE.md", "ATLAS_INTAKE_PROFILE.md",
                       "ATLAS_CANDIDATE_DELTA.md", "PRIVATE_BUILD_README.md",
                       "OWNER_PRIVATE_GOOGLE_DRIVE_OPERATING_POLICY.md"}
MANIFESTS = ("plugin.json", ".codex-plugin/plugin.json", ".claude-plugin/plugin.json",
             ".antigravity-plugin/plugin.json", "gemini-extension.json")
SKILL_NAME = re.compile(r"^[a-z0-9]+(?:-[a-z0-9]+)*$")
SECRET = re.compile(r"(?:ghp|gho|ghs|github_pat)_[A-Za-z0-9_]{20,}|sk-proj-[A-Za-z0-9_-]{30,}")
PRIVATE_LOCATOR = re.compile(
    r"https?://(?:docs|drive)\.google\.com/(?:document/d/|file/d/|drive/folders/)[A-Za-z0-9_-]{16,}"
)
ASSETS = ("assets/loom-foo-mark-v2.png", "assets/loom-foo-mark-v3.png")


def check(root: Path = ROOT) -> dict:
    errors, warnings = [], []
    def fail(msg: str):
        errors.append(msg)
    def read_json(path: str):
        try:
            data = json.loads((root / path).read_text(encoding="utf-8"))
            if not isinstance(data, dict):
                raise ValueError("expected object")
            return data
        except (OSError, ValueError) as exc:
            fail(f"invalid/missing {path}: {exc}")
            return {}

    inventory = read_json("SKILL_INVENTORY.json")
    expected = {}
    if inventory.get("bundle") != "loom-foo" or len(inventory.get("skills", [])) != 40:
        fail("expected 40-item loom-foo inventory")
    for obj in inventory.get("skills", []):
        if not isinstance(obj, dict) or not isinstance(obj.get("id"), str):
            fail("malformed inventory item")
            continue
        key = obj["id"]
        if key in expected or not isinstance(obj.get("version"), str):
            fail(f"invalid/duplicate inventory entry: {key}")
        expected[key] = obj.get("version")
    ver = inventory.get("bundle_version")
    if not isinstance(ver, str):
        fail("bundle version must be a string")
    for name in MANIFESTS:
        manifest = read_json(name)
        if manifest.get("name") != "loom-foo" or manifest.get("version") != ver:
            fail(f"manifest name/version mismatch: {name}")

    skills_root = root / "skills"
    actual = {p.name for p in skills_root.iterdir() if p.is_dir()} if skills_root.is_dir() else set()
    if set(expected) != actual:
        fail(f"Skill IDs mismatch: missing={sorted(set(expected) - actual)}, extra={sorted(actual - set(expected))}")
    for skill_id in sorted(expected):
        file = skills_root / skill_id / "SKILL.md"
        try:
            text = file.read_text(encoding="utf-8")
            if not text.startswith("---\n") or "\n---\n" not in text[4:]:
                raise ValueError("frontmatter delimiters missing")
            frontmatter = yaml.safe_load(text.split("---", 2)[1])
            if not isinstance(frontmatter, dict) or frontmatter.get("name") != skill_id:
                fail(f"SKILL.md name drift: {skill_id}")
                continue
            metadata = frontmatter.get("metadata", {})
            if not isinstance(metadata, dict) or metadata.get("version") != expected[skill_id]:
                fail(f"SKILL.md version drift: {skill_id}")
            description = frontmatter.get("description")
            if not isinstance(description, str) or not description.strip():
                fail(f"SKILL.md description missing: {skill_id}")
            if not SKILL_NAME.fullmatch(skill_id):
                fail(f"invalid Skill ID: {skill_id}")
        except (OSError, ValueError, yaml.YAMLError) as exc:
            fail(f"cannot validate SKILL.md {skill_id}: {exc}")

    for path in root.rglob("*"):
        if ".git" in path.relative_to(root).parts:
            continue
        rel = path.relative_to(root)
        if path.is_symlink():
            fail(f"symlink in distribution: {rel}")
            continue
        if any(part.lower() in FORBIDDEN_COMPONENTS for part in rel.parts) or path.name in FORBIDDEN_FILENAMES:
            fail(f"forbidden private path: {rel}")
            continue
        if path.is_file() and path.suffix.lower() in {".md", ".json", ".yaml", ".yml", ".py", ".toml", ".txt", ".sh"}:
            try:
                text = path.read_text(encoding="utf-8")
            except UnicodeDecodeError:
                fail(f"non-UTF8 source: {rel}")
                continue
            if SECRET.search(text) or PRIVATE_LOCATOR.search(text):
                fail(f"secret or owner document locator: {rel}")

    for mandatory in ("README.md", "AGENTS.md", "LICENSE", "PRIVACY.md", "SECURITY.md",
                      "SUPPORT.md", "TERMS.md", "RELEASE_STATUS.md",
                      "scripts/build_public_release.py"):
        if not (root / mandatory).is_file():
            fail(f"missing distribution control document: {mandatory}")

    missing_assets = [p for p in ASSETS if not (root / p).is_file()]
    if missing_assets:
        warnings.append("RELEASE_BLOCKED_MISSING_ORIGINAL_ASSETS: " + ", ".join(missing_assets))
    return {
        "status": "STATIC_PASS_PRIVATE_CANDIDATE" if not errors else "STATIC_FAIL",
        "skills": len(actual),
        "bundle_version": ver,
        "manifests": len(MANIFESTS),
        "errors": errors,
        "warnings": warnings,
        "public_release_approved": False,
    }


if __name__ == "__main__":
    result = check()
    print(json.dumps(result, indent=2, ensure_ascii=False))
    sys.exit(0 if not result["errors"] else 1)
