#!/usr/bin/env python3
"""Offline, read-only GitHub URL classification. Does not resolve or fetch URLs.

The path after tree/blob/raw is opaque until live GitHub ref resolution;
branch names can contain '/' and must not be guessed from URL segments.
"""
from __future__ import annotations
import ipaddress
import json
import re
import sys
from urllib.parse import unquote, urlsplit

OWNER = re.compile(r"[A-Za-z0-9](?:[A-Za-z0-9-]{0,37}[A-Za-z0-9])?\Z")
REPO = re.compile(r"[A-Za-z0-9_.-]{1,100}\Z")
SHA = re.compile(r"[a-fA-F0-9]{7,64}\Z")
NUMBER = re.compile(r"[1-9][0-9]*\Z")
KNOWN = {"github.com", "www.github.com", "raw.githubusercontent.com", "gist.github.com"}
RESERVED = {"orgs", "organizations", "topics", "features", "explore", "marketplace", "settings", "search", "apps", "login", "signup", "enterprise", "notifications", "codespaces", "sponsors"}


def classify(url: str) -> dict:
    if not isinstance(url, str) or len(url) > 8192:
        return {"type": "INVALID"}
    try:
        p = urlsplit(url.strip())
        host = (p.hostname or "").lower().rstrip(".")
        if p.scheme not in {"https", "http"} or not host or p.username or p.password or p.port not in {None, 80, 443}:
            return {"type": "INVALID"}
    except ValueError:
        return {"type": "INVALID"}
    if host in {"localhost", "metadata.google.internal"} or host.endswith((".local", ".localhost", ".internal")):
        return {"type": "UNSAFE_INTERNAL_URL"}
    try:
        ip = ipaddress.ip_address(host)
        if not ip.is_global:
            return {"type": "UNSAFE_INTERNAL_URL"}
    except ValueError:
        pass
    if host not in KNOWN:
        return {"type": "OTHER_URL", "host": host}
    # Reject ambiguous encoded separators, URL userinfo, path traversal and backslashes.
    if re.search(r"%(?:2f|5c|00)", p.path, re.I) or "\\" in p.path:
        return {"type": "INVALID"}
    parts = [unquote(x) for x in p.path.split("/") if x]
    if any(x in {".", ".."} or "/" in x or "\\" in x or any(ord(c) < 32 for c in x) for x in parts):
        return {"type": "INVALID"}
    if host == "gist.github.com":
        if len(parts) >= 2 and OWNER.fullmatch(parts[0]) and SHA.fullmatch(parts[1]):
            return {"type": "GITHUB_GIST", "owner": parts[0], "gist_id": parts[1]}
        return {"type": "GITHUB_OTHER"}
    if len(parts) < 2 or (host != "raw.githubusercontent.com" and parts[0].lower() in RESERVED) or not OWNER.fullmatch(parts[0]) or not REPO.fullmatch(parts[1]):
        return {"type": "GITHUB_OTHER"}
    owner, repo = parts[0], parts[1]
    if repo.endswith(".git") and len(repo) > 4:
        repo = repo[:-4]
    if repo in {".", ".."} or repo.startswith(".") or repo.endswith("."):
        return {"type": "GITHUB_OTHER"}
    out = {"type": "GITHUB_REPO", "owner": owner, "repo": repo, "canonical_url": f"https://github.com/{owner}/{repo}"}
    if len(parts) == 2:
        return out
    if host == "raw.githubusercontent.com":
        # Raw files have a treeish followed by path. Slashed refs cannot be resolved here.
        if len(parts) >= 4:
            out.update(type="GITHUB_RAW_FILE", raw_tail="/".join(parts[2:]), ref_status="UNRESOLVED")
        else:
            out["type"] = "GITHUB_OTHER"
        return out
    head = parts[2]
    kinds = {"issues": "GITHUB_ISSUE", "pull": "GITHUB_PULL_REQUEST", "discussions": "GITHUB_DISCUSSION"}
    if head in kinds and len(parts) >= 4 and NUMBER.fullmatch(parts[3]):
        out.update(type=kinds[head], number=int(parts[3]))
    elif head == "commit" and len(parts) >= 4 and SHA.fullmatch(parts[3]):
        out.update(type="GITHUB_COMMIT", sha=parts[3])
    elif head in {"blob", "tree", "raw"} and len(parts) >= 4:
        out.update(type={"blob": "GITHUB_BLOB", "tree": "GITHUB_TREE", "raw": "GITHUB_RAW_FILE"}[head],
                   raw_tail="/".join(parts[3:]), ref_status="UNRESOLVED")
    elif head == "releases":
        out["type"] = "GITHUB_RELEASES" if len(parts) == 3 else "GITHUB_RELEASE"
        if len(parts) >= 5 and parts[3] == "tag":
            out["tag"] = "/".join(parts[4:])
    elif head in {"actions", "security", "compare", "projects", "wiki", "tags", "branches"}:
        out.update(type="GITHUB_SECTION", section=head)
    else:
        out.update(type="GITHUB_SECTION", section=head)
    return out


if __name__ == "__main__":
    for raw in sys.argv[1:]:
        print(json.dumps(classify(raw), ensure_ascii=False, sort_keys=True))
