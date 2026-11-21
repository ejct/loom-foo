#!/usr/bin/env python3
"""Strict static package + fixture integrity checks. Does not run model behavior."""
from __future__ import annotations

from pathlib import Path
import json
import re
import sys
import tokenize

try:
    import yaml
except ImportError:
    sys.exit("STATIC_BLOCKED: PyYAML is required; cannot claim metadata validation")

ROOT = Path(__file__).resolve().parents[1]
ALLOWED_FIELDS = {"name", "description", "license", "compatibility", "metadata", "allowed-tools"}
MODES = {"ASSESS", "CREATE", "REVISE", "DIAGNOSE", "PACKAGE/DELIVER", "FIRST_USE", "PORTFOLIO"}
DECISIONS = {"NEW_SKILL", "REVISE_EXISTING", "COMPOSE_EXISTING", "EXISTING_OWNER", "STANDING_INSTRUCTIONS", "REFERENCE_ONLY", "DETERMINISTIC_TOOL", "RUNTIME_OR_TOOL_FIX", "NO_SKILL_NEEDED", "NEED_EVIDENCE"}


class UniqueKeyLoader(yaml.SafeLoader):
    """Reject ambiguous duplicate YAML keys instead of silently overriding them."""


def _unique_mapping(loader, node):
    mapping = {}
    for key_node, value_node in node.value:
        key = loader.construct_object(key_node, deep=True)
        if key in mapping:
            raise ValueError(f"duplicate YAML key: {key}")
        mapping[key] = loader.construct_object(value_node, deep=True)
    return mapping


UniqueKeyLoader.add_constructor(yaml.resolver.BaseResolver.DEFAULT_MAPPING_TAG, _unique_mapping)


def safe_file(root, rel):
    p = root / rel
    if ".." in Path(rel).parts or not p.is_file() or not p.resolve().is_relative_to(root.resolve()):
        raise ValueError(f"unsafe or missing file: {rel}")
    return p


def validate() -> str:
    main = ROOT / "SKILL.md"
    text = main.read_text(encoding="utf-8")
    if text.startswith("\ufeff"):
        raise ValueError("UTF-8 BOM in SKILL.md")
    m = re.match(r"\A---\n(?P<front>.*?)\n---\n(?P<body>.*)\Z", text, re.S)
    if not m:
        raise ValueError("missing or malformed YAML frontmatter")
    front = yaml.load(m.group("front"), Loader=UniqueKeyLoader)
    if not isinstance(front, dict):
        raise ValueError("frontmatter not a mapping")
    if set(front) - ALLOWED_FIELDS:
        raise ValueError(f"unsupported frontmatter fields: {sorted(set(front)-ALLOWED_FIELDS)}")
    name, desc = front.get("name"), front.get("description")
    if not isinstance(name, str) or len(name) > 64 or not re.fullmatch(r"[a-z0-9]+(?:-[a-z0-9]+)*", name):
        raise ValueError("invalid skill name")
    if name != ROOT.name:
        raise ValueError("skill name != containing folder")
    if not isinstance(desc, str) or not desc.strip() or len(desc) > 1024:
        raise ValueError("invalid description")
    if not isinstance(front.get("compatibility", ""), str) or len(front.get("compatibility", "")) > 500:
        raise ValueError("invalid compatibility")
    for key in ("license", "allowed-tools"):
        if key in front and not isinstance(front[key], str):
            raise ValueError(f"{key} must be string")
    metadata = front.get("metadata", {})
    if not isinstance(metadata, dict) or not all(isinstance(k, str) and isinstance(v, str) for k,v in metadata.items()):
        raise ValueError("metadata must map strings to strings")
    version = metadata.get("version")
    if not isinstance(version, str) or not re.fullmatch(r"\d+\.\d+\.\d+", version):
        raise ValueError("version must be x.y.z")
    body = m.group("body")
    if not body.strip() or not re.search(r"(?m)^# ", body):
        raise ValueError("missing substantive skill body")

    # Inspect local-file pointers in every Markdown document, not only SKILL.md.
    # This is only a conservative literal-path check, not a Markdown renderer.
    for doc in ROOT.rglob("*.md"):
        for rel in set(re.findall(r"(?<![A-Za-z0-9_])(?:references|scripts|tests)/[A-Za-z0-9_./-]+\.(?:md|py|json)", doc.read_text(encoding="utf-8"))):
            if rel == 'scripts/validate_skill_taxonomy.py' and 'plugin root' in doc.read_text(encoding='utf-8'):
                # Shared bundle-level optional validator, not a self-package dependency.
                continue
            safe_file(ROOT, rel)
    for f in ROOT.rglob("*"):
        if f.is_symlink():
            raise ValueError(f"symlink in distributable skill: {f.relative_to(ROOT)}")
    for f in (ROOT / "scripts").glob("*.py"):
        with tokenize.open(f) as stream:
            compile(stream.read(), str(f), "exec")

    cases = json.loads(safe_file(ROOT, "tests/routing_cases.json").read_text(encoding="utf-8"))
    if not isinstance(cases, list) or len(cases) < 12:
        raise ValueError("insufficient routing fixtures")
    ids = set()
    for case in cases:
        if not isinstance(case, dict):
            raise ValueError("fixture must be mapping")
        if not isinstance(case.get("id"), str) or not case["id"] or case["id"] in ids:
            raise ValueError("missing or duplicate fixture ID")
        ids.add(case["id"])
        if not isinstance(case.get("prompt"), str) or not case["prompt"].strip():
            raise ValueError("missing fixture prompt")
        owner = case.get("expected_owner")
        if not isinstance(owner, str) or not owner.strip():
            raise ValueError("missing expected owner")
        mode, decision = case.get("expected_mode"), case.get("expected_decision")
        if owner == name:
            if mode not in MODES:
                raise ValueError("skill-engineering fixture requires supported mode")
            if decision is not None and (mode != "ASSESS" or decision not in DECISIONS):
                raise ValueError("decision must be an ASSESS disposition")
        elif mode is not None or decision is not None:
            raise ValueError("other owner cannot have skill-engineering mode or disposition")
    files = [f for f in ROOT.rglob("*") if f.is_file() and "__pycache__" not in f.parts]
    return f"STATIC_PASS: YAML/metadata, local paths, scripts, fixture separation ({len(cases)} cases), {len(files)} files"


if __name__ == "__main__":
    try:
        print(validate())
        print("NOT_TESTED: automatic routing, execution, independent lift, install/discovery")
    except Exception as exc:
        print(f"STATIC_FAIL: {exc}", file=sys.stderr)
        sys.exit(1)
