#!/usr/bin/env python3
"""
generate_timestamp.py — ISO 8601 timestamp generator for CSCF/GAP artifacts
Author: Quang Cuong Huynh

Usage:
    python scripts/generate_timestamp.py             # UTC now
    python scripts/generate_timestamp.py --date      # date only (YYYY-MM-DD)
    python scripts/generate_timestamp.py --tz Asia/Ho_Chi_Minh
    python scripts/generate_timestamp.py --formats   # print all formats
    python scripts/generate_timestamp.py --doc-id-date  # YYYYMMDD for doc_id
"""
import argparse, sys
from datetime import datetime, timezone, timedelta

TZOFFSETS = {
    "UTC": timezone.utc,
    "Asia/Ho_Chi_Minh": timezone(timedelta(hours=7)),
    "US/Eastern":       timezone(timedelta(hours=-5)),
    "US/Pacific":       timezone(timedelta(hours=-8)),
    "Europe/London":    timezone.utc,
    "Australia/Sydney": timezone(timedelta(hours=11)),
}

def main():
    ap = argparse.ArgumentParser(description="ISO 8601 timestamp generator")
    ap.add_argument("--tz",         default="UTC", help=f"Timezone: {list(TZOFFSETS.keys())}")
    ap.add_argument("--date",       action="store_true", help="YYYY-MM-DD only")
    ap.add_argument("--doc-id-date",action="store_true", help="YYYYMMDD (for doc_id fields)")
    ap.add_argument("--formats",    action="store_true", help="Print all available formats")
    args = ap.parse_args()

    tz  = TZOFFSETS.get(args.tz, timezone.utc)
    now = datetime.now(tz)

    if args.formats:
        print("ISO 8601 full:    ", now.strftime("%Y-%m-%dT%H:%M:%SZ"))
        print("ISO 8601 ms:      ", now.strftime("%Y-%m-%dT%H:%M:%S.%f")[:-3] + "Z")
        print("Date only:        ", now.strftime("%Y-%m-%d"))
        print("Doc ID date:      ", now.strftime("%Y%m%d"))
        print("Human readable:   ", now.strftime("%B %d, %Y at %H:%M UTC"))
        print("CHANGELOG format: ", now.strftime("%Y-%m-%d"))
        return

    if args.doc_id_date:
        print(now.strftime("%Y%m%d"))
    elif args.date:
        print(now.strftime("%Y-%m-%d"))
    else:
        print(now.strftime("%Y-%m-%dT%H:%M:%SZ"))

if __name__ == "__main__":
    main()
