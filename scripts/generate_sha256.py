#!/usr/bin/env python3
"""
generate_sha256.py — SHA-256 hash generator for artifact files
Author: Quang Cuong Huynh

Usage:
    python scripts/generate_sha256.py --path docs/myfile.md
    python scripts/generate_sha256.py --string "text to hash"
    python scripts/generate_sha256.py --batch --dir personas/
    python scripts/generate_sha256.py --verify --path docs/myfile.md --expected abc123...
"""
import argparse, hashlib, re, sys
from pathlib import Path

def sha256_body(path: Path) -> str:
    """Hash file content excluding YAML frontmatter (stable hash across re-registration)."""
    raw = path.read_text(encoding="utf-8", errors="replace")
    body = re.sub(r"^---\n.*?\n---\n", "", raw, flags=re.DOTALL)
    return hashlib.sha256(body.encode("utf-8")).hexdigest()

def sha256_str(s: str) -> str:
    return hashlib.sha256(s.encode("utf-8")).hexdigest()

def sha256_full(path: Path) -> str:
    """Hash full file including frontmatter (for external verification)."""
    return hashlib.sha256(path.read_bytes()).hexdigest()

def main():
    ap = argparse.ArgumentParser(description="SHA-256 hash generator for artifacts")
    ap.add_argument("--path",     help="Single file to hash")
    ap.add_argument("--string",   help="Hash a raw string")
    ap.add_argument("--batch",    action="store_true")
    ap.add_argument("--dir",      default=".")
    ap.add_argument("--full",     action="store_true", help="Hash full file (incl. frontmatter)")
    ap.add_argument("--verify",   action="store_true", help="Verify against --expected hash")
    ap.add_argument("--expected", help="Expected hash for --verify mode")
    ap.add_argument("--format",   choices=["hex","prefixed","short"], default="hex",
                    help="hex=raw | prefixed=sha256:... | short=first 16 chars")
    args = ap.parse_args()

    def fmt(h):
        if args.format == "prefixed": return f"sha256:{h}"
        if args.format == "short":    return h[:16]
        return h

    if args.string:
        h = sha256_str(args.string)
        print(fmt(h))
        return

    targets = []
    if args.path:
        targets = [Path(args.path)]
    elif args.batch:
        d = Path(args.dir)
        targets = [t for t in list(d.rglob("*.md")) + list(d.rglob("*.yml"))
                   if ".git" not in str(t) and t.is_file()]

    for p in targets:
        h = sha256_full(p) if args.full else sha256_body(p)
        if args.verify:
            match = (h == args.expected) or (h == args.expected.removeprefix("sha256:"))
            status = "✓ MATCH" if match else "✗ MISMATCH"
            print(f"{status}  {p}  got={h[:16]}  expected={args.expected[:16]}")
        else:
            print(f"{fmt(h)}  {p}")

if __name__ == "__main__":
    main()
