#!/usr/bin/env python3
"""Read-only, bounded evidence probe for the *current local file*, not remote effects.

Exit: 0 match, 2 unsupported/missing/mismatch, 1 bad arguments.
"""
import argparse
import hashlib
import json
from pathlib import Path
from typing import Optional


def probe(root: str, path: str, expected_hash: Optional[str] = None) -> dict:
    base = Path(root).resolve(strict=False)
    target = Path(path)
    target = (target if target.is_absolute() else base / target).resolve(strict=False)
    result = {"status": "NOT_VERIFIED", "subject": str(target), "scope": "local_file_bytes"}
    if not target.is_relative_to(base):
        return result | {"reason": "path_outside_root"}
    if not target.is_file():
        return result | {"reason": "file_not_found_or_not_regular"}
    h = hashlib.sha256()
    size = 0
    try:
        with target.open("rb") as fp:
            while chunk := fp.read(1024 * 1024):
                h.update(chunk)
                size += len(chunk)
    except OSError as err:
        return result | {"reason": "read_failed", "error_type": type(err).__name__}
    actual_hash = h.hexdigest()
    result.update({"size_bytes": size, "sha256": actual_hash})
    if expected_hash is not None and actual_hash != expected_hash.lower():
        return result | {"reason": "sha256_mismatch"}
    return result | {"status": "OBSERVED", "reason": "local_file_exists_and_hash_checked"}


def main() -> int:
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument("--root", required=True, help="authorized local workspace directory")
    p.add_argument("--path", required=True, help="file under root")
    p.add_argument("--sha256", help="optional expected sha256 hex digest")
    args = p.parse_args()
    if args.sha256 is not None:
        if len(args.sha256) != 64 or any(c not in "0123456789abcdefABCDEF" for c in args.sha256):
            p.error("--sha256 must be a 64-character hex digest")
    result = probe(args.root, args.path, args.sha256)
    print(json.dumps(result, ensure_ascii=False))
    return 0 if result["status"] == "OBSERVED" else 2


if __name__ == "__main__":
    raise SystemExit(main())
