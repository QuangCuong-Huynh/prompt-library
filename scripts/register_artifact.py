#!/usr/bin/env python3
"""
register_artifact.py — Full artifact registration: UUIDv7 + SHA-256 + frontmatter patch + provenance log

Author:    Quang Cuong Huynh (Registered IP Authority)
Authority: Registered — Quang Cuong Huynh
Usage:
    python scripts/register_artifact.py --path <file>
    python scripts/register_artifact.py --batch --dir personas/
    python scripts/register_artifact.py --path <file> --agent architect --stage S2
"""
import argparse, hashlib, json, os, re, sys, time
from datetime import datetime, timezone
from pathlib import Path

# Re-use core functions from sign_artifact.py (or inline them here for standalone)
def uuidv7() -> str:
    ms = int(time.time() * 1000)
    rand = int.from_bytes(os.urandom(10), "big")
    uuid_int = (ms << 80) | (0x7 << 76) | ((rand >> 62) << 64) | (0b10 << 62) | (rand & 0x3FFFFFFFFFFFFFFF)
    h = f"{uuid_int:032x}"
    return f"{h[:8]}-{h[8:12]}-{h[12:16]}-{h[16:20]}-{h[20:]}"

def sha256_body(path: Path) -> str:
    raw = path.read_text(encoding="utf-8", errors="replace")
    body = re.sub(r"^---\n.*?\n---\n", "", raw, flags=re.DOTALL)
    return hashlib.sha256(body.encode()).hexdigest()

def iso_now() -> str:
    return datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")

def register(path: Path, agent: str, stage: str, dry_run: bool, registry_path: Path) -> dict | None:
    text = path.read_text(encoding="utf-8", errors="replace")
    if not text.startswith("---"):
        return None

    uid    = uuidv7()
    digest = sha256_body(path)

    if not dry_run:
        # Patch frontmatter
        if 'artifact_id: ""' in text:
            text = text.replace('artifact_id: ""', f'artifact_id: "{uid}"', 1)
        if 'sha256: ""' in text:
            text = text.replace('sha256: ""', f'sha256: "{digest}"', 1)
        path.write_text(text, encoding="utf-8")

        # Append to registry JSONL
        record = {
            "artifact_id": uid, "file": str(path),
            "sha256": digest, "registered_at": iso_now(),
            "registered_by": agent, "stage": stage,
            "supervised_by": "Quang Cuong Huynh"
        }
        with open(registry_path, "a", encoding="utf-8") as f:
            f.write(json.dumps(record) + "\n")
        return record
    else:
        print(f"  [DRY] {path}: uid={uid[:18]} sha256={digest[:16]}")
        return {"artifact_id": uid, "sha256": digest}

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--path")
    ap.add_argument("--batch",     action="store_true")
    ap.add_argument("--dir",       default=".")
    ap.add_argument("--agent",     default="register_artifact.py")
    ap.add_argument("--stage",     default="S0")
    ap.add_argument("--dry-run",   action="store_true")
    ap.add_argument("--registry",  default="memory/logs/artifact_registry.jsonl")
    args = ap.parse_args()

    registry_path = Path(args.registry)
    registry_path.parent.mkdir(parents=True, exist_ok=True)

    targets = []
    if args.path:
        targets = [Path(args.path)]
    elif args.batch:
        d = Path(args.dir)
        targets = [t for t in list(d.rglob("*.md")) + list(d.rglob("*.yml")) + list(d.rglob("*.yaml"))
                   if ".git" not in str(t)]

    count = 0
    for p in targets:
        if not p.is_file(): continue
        text = p.read_text(encoding="utf-8", errors="replace")
        if not (text.startswith("---") and 'artifact_id: ""' in text): continue
        r = register(p, args.agent, args.stage, args.dry_run, registry_path)
        if r:
            count += 1
            print(f"  ✓ {p}  →  {r['artifact_id'][:18]}...")

    print(f"\n{'[DRY] ' if args.dry_run else ''}Registered: {count} artifacts")

if __name__ == "__main__":
    main()
