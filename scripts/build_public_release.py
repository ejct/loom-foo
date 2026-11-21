#!/usr/bin/env python3
"""Fail-closed public distribution builder for loom-foo.

Build from a reviewed *generic* source tree and exact SHA-256 manifest.
Never use an installed owner-private plugin archive as public source.
This script is effective only when invoked by the actual release pipeline.
"""
from __future__ import annotations
import argparse
import hashlib
import json
from pathlib import Path, PurePosixPath
import re
import sys
import zipfile

# Structural red flags, not an exhaustive PII scanner. Unknown source/bytes fail
# independently through the exact-path + exact-hash approval index.
FORBIDDEN_COMPONENTS = {
    "private", "owner-private", "owner_private", "personal",
    "incident-archive", "incident_archive", "session-history", "session_history",
    "__pycache__", ".git", ".env", ".secrets",
    "reconciliation", "legacy-2026-11-01", "private-plugin-v0.40.0",
}
FORBIDDEN_NAMES = {
    "PRIVATE_BUILD_README.md", "OWNER_PRIVATE_GOOGLE_DRIVE_OPERATING_POLICY.md",
    "ATLAS_CONTEXT_PROFILE.md", "ATLAS_INTAKE_PROFILE.md",
}
BLOCKED_SUFFIXES = {".pyc", ".p12", ".pem", ".key", ".sqlite"}
DRIVE_ID = re.compile(r"https?://(?:docs|drive)\.google\.com/(?:document/d/|file/d/|drive/folders/)[A-Za-z0-9_-]{16,}")
EMAIL = re.compile(r"[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}")
# Internal source identifiers must never enter the generic reviewed public payload.
PRIVATE_SOURCE_REFERENCE = re.compile(r"ejct/" + r"LoomDev|plugin" + r"rel_[A-Za-z0-9_\-]+")

class Reject(ValueError): pass

def safe_path(s: str) -> PurePosixPath:
    p=PurePosixPath(s)
    if not s or s.startswith('/') or '\\' in s or any(c in ('', '.', '..') for c in s.split('/')):
        raise Reject(f"unsafe path: {s!r}")
    if any(c.lower() in FORBIDDEN_COMPONENTS for c in p.parts) or p.name in FORBIDDEN_NAMES:
        raise Reject(f"private/unsafe path: {s}")
    if p.suffix.lower() in BLOCKED_SUFFIXES:
        raise Reject(f"restricted extension: {s}")
    if s.startswith('tests/') or s.startswith('docs/2026-') or '/tests/' in s:
        raise Reject(f"unreviewed fixtures/history in public candidate: {s}")
    return p

def load_index(path: Path) -> dict[str,str]:
    data=json.loads(path.read_text(encoding='utf-8'))
    if data.get('schema') != 1 or data.get('origin') != 'reviewed-generic-source' or data.get('approved_by_owner') is not True:
        raise Reject('approved generic source index missing explicit owner review')
    files=data.get('files')
    if not isinstance(files,dict) or not files:
        raise Reject('empty/invalid approved file index')
    for name,h in files.items():
        safe_path(name)
        if not isinstance(h,str) or not re.fullmatch(r'[0-9a-f]{64}',h):
            raise Reject(f'invalid SHA-256 for {name}')
    return files

def scan_content(name: str, raw: bytes):
    if name.endswith(('.md','.json','.yaml','.yml','.txt','.py','.toml','.sh')):
        try: s=raw.decode('utf-8')
        except UnicodeDecodeError: raise Reject(f'non-UTF8 text: {name}')
        if DRIVE_ID.search(s): raise Reject(f'private source locator detected: {name}')
        if PRIVATE_SOURCE_REFERENCE.search(s):
            raise Reject(f'private development source identifier: {name}')
        # A deliberately strict default: public author contact metadata must be
        # externally reviewed and stored in an expressly allowed manifest only.
        if EMAIL.search(s) and name not in ('plugin.json','.codex-plugin/plugin.json'):
            raise Reject(f'email-like locator in public source: {name}')
        if re.search(r'(?i)(owner.private|private user context|reported missed activation on \d{4}-\d{2}-\d{2})',s):
            raise Reject(f'owner/history-specific prose: {name}')

REQUIRED_PUBLIC_FILES = {
    "README.md", "LICENSE", "PUBLISHER.md", "ATTRIBUTION.md", "PRIVACY.md", "TERMS.md", "SUPPORT.md", "SECURITY.md",
    "SKILL_INVENTORY.json", "plugin.json", ".codex-plugin/plugin.json",
    ".claude-plugin/plugin.json", ".antigravity-plugin/plugin.json", "gemini-extension.json",
}

def validate_complete_release(source: Path, contents: dict[str, bytes]):
    """Ensure approved bytes also form a complete, installable Skills source package."""
    missing = REQUIRED_PUBLIC_FILES - set(contents)
    if missing:
        raise Reject("INCOMPLETE_RELEASE: missing reviewed files: " + ", ".join(sorted(missing)))

    try:
        inventory = json.loads(contents["SKILL_INVENTORY.json"])
        entries = inventory["skills"]
        bundle_version = inventory["bundle_version"]
        if inventory["bundle"] != "loom-foo" or not isinstance(entries, list) or not entries:
            raise ValueError("invalid skill inventory")
        ids = [x["id"] for x in entries]
        if len(ids) != len(set(ids)) or not all(isinstance(x, str) for x in ids):
            raise ValueError("duplicate/invalid Skill IDs")
    except (KeyError, TypeError, ValueError, json.JSONDecodeError) as exc:
        raise Reject(f"INCOMPLETE_RELEASE: invalid Skill inventory: {exc}") from exc

    skills_dir = source / "skills"
    if not skills_dir.is_dir() or skills_dir.is_symlink():
        raise Reject("INCOMPLETE_RELEASE: missing skills root")
    current_roots = {p.name for p in skills_dir.iterdir() if p.is_dir()}
    if current_roots != set(ids):
        raise Reject("INCOMPLETE_RELEASE: source Skill roots differ from inventory")
    source_paths = set()
    for file in skills_dir.rglob("*"):
        if file.is_symlink():
            raise Reject(f"INCOMPLETE_RELEASE: symlink in skills/: {file}")
        if file.is_file():
            rel = file.relative_to(source).as_posix()
            safe_path(rel)
            source_paths.add(rel)
    if not source_paths.issubset(contents):
        raise Reject("INCOMPLETE_SKILL_TREE: missing reviewed files: " +
                     ", ".join(sorted(source_paths - set(contents))))
    for name in ids:
        if f"skills/{name}/SKILL.md" not in contents:
            raise Reject("INCOMPLETE_RELEASE: Skill root missing: " + name)

    manifests = {}
    for rel in ("plugin.json", ".codex-plugin/plugin.json", ".claude-plugin/plugin.json",
                ".antigravity-plugin/plugin.json", "gemini-extension.json"):
        try:
            manifests[rel] = json.loads(contents[rel])
        except (ValueError, TypeError) as exc:
            raise Reject(f"INCOMPLETE_RELEASE: invalid manifest {rel}: {exc}") from exc
        if manifests[rel].get("name") != "loom-foo" or manifests[rel].get("version") != bundle_version:
            raise Reject("INCOMPLETE_RELEASE: native manifest identity/version drift: " + rel)

    root = manifests["plugin.json"]
    codex = manifests[".codex-plugin/plugin.json"]
    try:
        openai_interface = root["extensions"]["com.openai"]["interface"]
        codex_interface = codex["interface"]
        logo_paths = [
            openai_interface["logo"], openai_interface["composerIcon"],
            codex_interface["logo"], codex_interface["composerIcon"],
            manifests[".antigravity-plugin/plugin.json"]["logo"],
        ]
        if any(not isinstance(value, str) or not value.strip() for value in logo_paths):
            raise ValueError("missing brand asset field")
    except (KeyError, TypeError, ValueError) as exc:
        raise Reject(f"INCOMPLETE_RELEASE: missing native brand reference: {exc}") from exc
    for path in logo_paths:
        rel = path.removeprefix("./")
        safe_path(rel)
        if rel not in contents:
            raise Reject("MISSING_BRAND_ASSET: " + rel)

def build(source:Path, index_path:Path, output:Path):
    source=source.resolve();output=output.resolve()
    if (source/'PRIVATE_BUILD_README.md').exists() or (source/'docs/OWNER_PRIVATE_GOOGLE_DRIVE_OPERATING_POLICY.md').exists():
        raise Reject('PRIVATE PLUGIN SOURCE: use separately reviewed generic source tree')
    if any((source / p).exists() for p in ('private', 'reconciliation', 'legacy-2026-11-01')):
        raise Reject('MIXED PRIVATE DEVELOPMENT SOURCE: export a clean generic-only tree first')
    approved=load_index(index_path)
    all_source={str(p.relative_to(source)).replace('\\','/') for p in source.rglob('*') if p.is_file()}
    if not (set(approved)<=all_source):
        raise Reject('approved file missing in generic source tree')
    # No extras in package: emit ONLY exact reviewed entries; no globbing.
    contents={}
    for rel,expected in sorted(approved.items()):
        p=source/rel
        if p.is_symlink() or not p.is_file() or p.resolve().is_relative_to(source) is False:
            raise Reject(f'unsafe file resolution: {rel}')
        raw=p.read_bytes()
        actual=hashlib.sha256(raw).hexdigest()
        if actual!=expected: raise Reject(f'UNREVIEWED_BYTES: {rel}')
        scan_content(rel,raw)
        contents[rel]=raw
    if 'plugin.json' not in contents and '.codex-plugin/plugin.json' not in contents:
        raise Reject('no reviewed plugin manifest')
    validate_complete_release(source, contents)
    output.parent.mkdir(parents=True,exist_ok=True)
    if output.exists(): raise Reject('refuse to overwrite an existing release archive')
    with zipfile.ZipFile(output,'w',compression=zipfile.ZIP_DEFLATED) as z:
        for rel,raw in contents.items():
            info=zipfile.ZipInfo(rel,date_time=(1980,1,1,0,0,0));info.compress_type=zipfile.ZIP_DEFLATED
            info.external_attr=(0o100644 << 16)
            z.writestr(info,raw)
    return len(contents)

def main():
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument('--generic-source',required=True,type=Path)
    p.add_argument('--approved-index',required=True,type=Path)
    p.add_argument('--output',required=True,type=Path)
    a=p.parse_args()
    try: n=build(a.generic_source,a.approved_index,a.output)
    except (Reject,OSError,ValueError) as e:
        print(f'PUBLIC_EXPORT_BLOCKED: {e}',file=sys.stderr);return 2
    print(f'PUBLIC_EXPORT_READY: {n} reviewed files (package only; not published)')
    return 0
if __name__=='__main__':raise SystemExit(main())
