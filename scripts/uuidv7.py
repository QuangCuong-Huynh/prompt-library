#!/usr/bin/env python3
"""
uuidv7.py — Time-ordered UUID v7 generator (RFC 9562)
Author: Quang Cuong Huynh

Usage:
    python scripts/uuidv7.py           # generate 1
    python scripts/uuidv7.py 5         # generate 5
    python scripts/uuidv7.py --json    # output as JSON array
    python scripts/uuidv7.py --ts      # include parsed timestamp
"""
import os, sys, time, json
from datetime import datetime, timezone

def uuidv7() -> str:
    ms = int(time.time() * 1000)
    rand = int.from_bytes(os.urandom(10), "big")
    uuid_int = (
        (ms << 80)
        | (0x7 << 76)
        | ((rand >> 62) << 64)
        | (0b10 << 62)
        | (rand & 0x3FFFFFFFFFFFFFFF)
    )
    h = f"{uuid_int:032x}"
    return f"{h[:8]}-{h[8:12]}-{h[12:16]}-{h[16:20]}-{h[20:]}"

def parse_timestamp(uid: str) -> str:
    """Extract embedded UTC timestamp from UUIDv7."""
    hex_no_dash = uid.replace("-", "")
    ms = int(hex_no_dash[:12], 16)
    return datetime.fromtimestamp(ms / 1000, tz=timezone.utc).strftime("%Y-%m-%dT%H:%M:%S.%f")[:-3] + "Z"

if __name__ == "__main__":
    args = sys.argv[1:]
    show_ts  = "--ts"   in args
    as_json  = "--json" in args
    n_args   = [a for a in args if not a.startswith("--")]
    n        = int(n_args[0]) if n_args else 1

    results = [uuidv7() for _ in range(n)]

    if as_json:
        out = [{"uuid": u, "timestamp": parse_timestamp(u)} for u in results] if show_ts else results
        print(json.dumps(out, indent=2))
    else:
        for u in results:
            if show_ts:
                print(f"{u}  [{parse_timestamp(u)}]")
            else:
                print(u)
