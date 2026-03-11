#!/usr/bin/env python3
"""
sign_artifact.py — Universal Artifact Signature generator
Produces: UUIDv7 + ISO-8601 timestamp + SHA-256 + YAML frontmatter patch

Author:    Quang Cuong Huynh (Registered IP Authority)
Authority: Registered — Quang Cuong Huynh
Usage:
    # Sign a single file (patch frontmatter in-place)
    python scripts/sign_artifact.py --path docs/myfile.md

    # Sign and print provenance JSON (no file modification)
    python scripts/sign_artifact.py --path docs/myfile.md --dry-run

    # Batch sign all unsigned files in a directory
    python scripts/sign_artifact.py --batch --dir personas/roles/

    # Generate standalone signature record
    python scripts/sign_artifact.py --path docs/myfile.md --provenance
"""
import argparse, hashlib, json, os, re, sys, time
from datetime import datetime, timezone
from pathlib import Path


# ─── UUIDv7 (RFC 9562) ────────────────────────────────────────────────────────
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


# ─── SHA-256 ──────────────────────────────────────────────────────────────────
def sha256_file(path: Path) -> str:
    """Hash file content excluding the YAML frontmatter block."""
    raw = path.read_text(encoding="utf-8")
    # Strip frontmatter (--- ... ---) for stable hash across registration runs
    body = re.sub(r"^---\n.*?\n---\n", "", raw, flags=re.DOTALL)
    return hashlib.sha256(body.encode("utf-8")).hexdigest()


def sha256_str(s: str) -> str:
    return hashlib.sha256(s.encode("utf-8")).hexdigest()


# ─── ISO-8601 timestamp ───────────────────────────────────────────────────────
def iso_now() -> str:
    return datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")


# ─── Frontmatter patch ────────────────────────────────────────────────────────
def patch_frontmatter(path: Path, artifact_id: str, sha256: str) -> bool:
    """Patch artifact_id and sha256 fields in YAML frontmatter. Returns True if changed."""
    text = path.read_text(encoding="utf-8")
    if not text.startswith("---"):
        print(f"  ⚠ No frontmatter: {path}", file=sys.stderr)
        return False

    changed = False
    # Patch artifact_id if empty
    if re.search(r'^artifact_id:\s*""', text, re.MULTILINE):
        text = re.sub(r'^artifact_id:\s*""', f'artifact_id: "{artifact_id}"', text, flags=re.MULTILINE)
        changed = True
    # Patch sha256 if empty
    if re.search(r'^sha256:\s*""', text, re.MULTILINE):
        text = re.sub(r'^sha256:\s*""', f'sha256: "{sha256}"', text, flags=re.MULTILINE)
        changed = True

    if changed:
        path.write_text(text, encoding="utf-8")
    return changed


# ─── Provenance record ────────────────────────────────────────────────────────
def make_provenance(path: Path, artifact_id: str, sha256: str, agent: str = "register_artifact.py") -> dict:
    return {
        "artifact_id":      artifact_id,
        "file_path":        str(path),
        "created_by_agent": agent,
        "supervised_by":    "Quang Cuong Huynh",
        "outputs_hash":     f"sha256:{sha256}",
        "timestamp":        iso_now(),
        "signatures": [{"type": "timestamp", "signer": "sign_artifact.py", "fingerprint": sha256[:16]}]
    }


# ─── CLI ──────────────────────────────────────────────────────────────────────
def main():
    ap = argparse.ArgumentParser(description="Universal Artifact Signature generator")
    ap.add_argument("--path",       help="Single file to sign")
    ap.add_argument("--batch",      action="store_true", help="Sign all .md/.yml/.yaml/.json in --dir")
    ap.add_argument("--dir",        default=".", help="Directory for batch mode (default: .)")
    ap.add_argument("--dry-run",    action="store_true", help="Print actions, no file writes")
    ap.add_argument("--provenance", action="store_true", help="Write .provenance.json alongside file")
    ap.add_argument("--agent",      default="sign_artifact.py", help="Agent ID for provenance record")
    args = ap.parse_args()

    targets = []
    if args.path:
        targets = [Path(args.path)]
    elif args.batch:
        d = Path(args.dir)
        targets = list(d.rglob("*.md")) + list(d.rglob("*.yml")) + list(d.rglob("*.yaml")) + list(d.rglob("*.json"))
        # Skip schema files themselves, node_modules, .git
        targets = [t for t in targets if ".git" not in str(t) and "node_modules" not in str(t) and "schema.json" not in t.name]
    else:
        ap.print_help()
        sys.exit(1)

    total, signed, skipped = 0, 0, 0
    for p in targets:
        if not p.is_file():
            continue
        total += 1
        text = p.read_text(encoding="utf-8", errors="replace")
        # Only process files with frontmatter containing empty artifact_id
        if not (text.startswith("---") and 'artifact_id: ""' in text):
            skipped += 1
            continue

        uid    = uuidv7()
        digest = sha256_file(p)
        prov   = make_provenance(p, uid, digest, args.agent)

        if args.dry_run:
            print(f"[DRY-RUN] {p}")
            print(f"  artifact_id : {uid}")
            print(f"  sha256      : {digest}")
        else:
            changed = patch_frontmatter(p, uid, digest)
            if changed:
                signed += 1
                print(f"  ✓ SIGNED  {p}  →  {uid[:18]}...")
                if args.provenance:
                    prov_path = p.with_suffix(".provenance.json")
                    prov_path.write_text(json.dumps(prov, indent=2), encoding="utf-8")
                    print(f"  ✓ PROV    {prov_path}")
            else:
                skipped += 1

    if not args.dry_run:
        print(f"\nSummary: {signed} signed | {skipped} skipped | {total} total")


if __name__ == "__main__":
    main()
