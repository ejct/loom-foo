#!/usr/bin/env python3
"""Conservative offline identification of YouTube URL referents.

No network requests, authentication, media download, or arbitrary URL fetching.
"""
from __future__ import annotations
import json
import ipaddress
import re
import sys
from urllib.parse import urlsplit, parse_qs

VIDEO_ID = re.compile(r"^[A-Za-z0-9_-]{11}$")
PLAYLIST_ID = re.compile(r"^[A-Za-z0-9_-]{8,150}$")
PART = re.compile(r"^(?:(\d+)h)?(?:(\d+)m)?(?:(\d+)s)?$", re.I)
YOUTUBE_HOSTS = {"youtube.com", "www.youtube.com", "m.youtube.com", "music.youtube.com", "youtube-nocookie.com", "www.youtube-nocookie.com"}
SHORT_HOSTS = {"youtu.be", "www.youtu.be"}


def _time_seconds(v: str | None) -> int | None:
    if not v:
        return None
    if v.isascii() and v.isdigit():
        return int(v)
    m = PART.fullmatch(v)
    if not m or not any(x is not None for x in m.groups()):
        return None
    h, mn, s = (int(x or 0) for x in m.groups())
    return h * 3600 + mn * 60 + s


def classify(raw: str) -> dict:
    if not isinstance(raw, str) or len(raw) > 8192:
        return {"type": "INVALID"}
    raw = raw.strip()
    try:
        u = urlsplit(raw)
        host = (u.hostname or "").lower().rstrip(".")
        if u.scheme not in {"http", "https"} or not host or u.username or u.password:
            return {"type": "INVALID"}
        if u.port not in {None, 80, 443}:
            return {"type": "INVALID"}
    except ValueError:
        return {"type": "INVALID"}
    if host in {"localhost", "metadata.google.internal"} or host.endswith((".local", ".localhost", ".internal")):
        return {"type": "UNSAFE_INTERNAL_URL"}
    try:
        addr = ipaddress.ip_address(host)
    except ValueError:
        addr = None
    if addr is not None and not addr.is_global:
        return {"type": "UNSAFE_INTERNAL_URL"}
    if host not in YOUTUBE_HOSTS | SHORT_HOSTS:
        return {"type": "OTHER_URL", "host": host}
    q = parse_qs(u.query, keep_blank_values=True)
    path = u.path.strip("/").split("/") if u.path.strip("/") else []
    vid: str | None = None
    if host in SHORT_HOSTS and len(path) == 1:
        vid = path[0]
    elif host in YOUTUBE_HOSTS:
        if path == ["watch"]:
            vids = q.get("v", [])
            vid = vids[0] if len(vids) == 1 else None
        elif len(path) == 2 and path[0] in {"shorts", "live", "embed", "v"}:
            vid = path[1]
    if vid is not None:
        if not VIDEO_ID.fullmatch(vid):
            return {"type": "INVALID_YOUTUBE_VIDEO"}
        out = {"type": "YOUTUBE_VIDEO", "video_id": vid,
               "canonical_url": f"https://www.youtube.com/watch?v={vid}"}
        t = _time_seconds((q.get("t") or q.get("start") or q.get("time_continue") or [None])[0])
        if t is not None:
            out["start_seconds"] = t
        lst = (q.get("list") or [None])[0]
        if lst and PLAYLIST_ID.fullmatch(lst):
            out["playlist_context"] = lst
        return out
    if host in YOUTUBE_HOSTS and path == ["playlist"]:
        lst = (q.get("list") or [None])[0]
        if lst and PLAYLIST_ID.fullmatch(lst):
            return {"type": "YOUTUBE_PLAYLIST", "playlist_id": lst}
        return {"type": "INVALID_YOUTUBE_COLLECTION"}
    if host in YOUTUBE_HOSTS and len(path) >= 1 and (path[0].startswith("@") or path[0] in {"channel", "user", "c"}):
        return {"type": "YOUTUBE_CHANNEL", "channel_path": "/".join(path[:2])}
    return {"type": "YOUTUBE_OTHER", "host": host}


if __name__ == "__main__":
    for arg in sys.argv[1:]:
        print(json.dumps(classify(arg), ensure_ascii=False, sort_keys=True))
