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
        # A deliberately strict default: public author contact metadata must be
        # externally reviewed and stored in an expressly allowed manifest only.
        if EMAIL.search(s) and name not in ('plugin.json','.codex-plugin/plugin.json'):
            raise Reject(f'email-like locator in public source: {name}')
        if re.search(r'(?i)(owner.private|private user context|reported missed activation on \d{4}-\d{2}-\d{2})',s):
            raise Reject(f'owner/history-specific prose: {name}')

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
