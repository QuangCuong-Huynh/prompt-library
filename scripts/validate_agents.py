#!/usr/bin/env python3
"""
validate_agents.py — Validate persona YAML frontmatter against schema v1.3
Usage:
  python validate_agents.py [file.md]
  python validate_agents.py --all-personas
  python validate_agents.py --check-schema
"""
import sys, argparse, yaml
from pathlib import Path

REPO_ROOT = Path(__file__).parent.parent
SCHEMA_PATH = REPO_ROOT / "schemas" / "prompt_v1.3.schema.json"

REQUIRED = ["artifact_id","doc_id","version","name","status","roles",
            "knowledge_domains","behavior_rules","output_spec","security_constraints"]
REQUIRED_ROLE = ["id","name","is_primary","isco08","riasec","ocean","cognitive_stack"]
OCEAN_DIMS = ["openness","conscientiousness","extraversion","agreeableness","stability"]

def parse_fm(path: Path):
    text = path.read_text(encoding="utf-8")
    if not text.startswith("---"):
        return None, "No YAML frontmatter"
    rest = text[3:]
    fm_text = rest[:rest.index("---")] if "---" in rest else rest
    try:
        return yaml.safe_load(fm_text), None
    except yaml.YAMLError as e:
        return None, f"YAML error: {e}"

def validate(path: Path):
    data, err = parse_fm(path)
    if err: return [f"PARSE: {err}"]
    errors = [f"missing:{f}" for f in REQUIRED if f not in data]
    for role in data.get("roles", []):
        errors += [f"role.{r}" for r in REQUIRED_ROLE if r not in role]
        for d in OCEAN_DIMS:
            if d not in role.get("ocean", {}):
                errors.append(f"ocean.{d}")
    return errors

def main():
    p = argparse.ArgumentParser()
    p.add_argument("file", nargs="?")
    p.add_argument("--all-personas", action="store_true")
    p.add_argument("--check-schema", action="store_true")
    p.add_argument("--check-required-fields", action="store_true")
    args = p.parse_args()

    if args.check_schema:
        ok = SCHEMA_PATH.exists()
        print(f"{'✅' if ok else '❌'} Schema: {SCHEMA_PATH}")
        sys.exit(0 if ok else 1)

    files = [Path(args.file)] if args.file else list((REPO_ROOT/"prompts").rglob("*.md"))
    total = passed = failed = 0
    for f in sorted(files):
        total += 1
        errors = validate(f)
        rel = f.relative_to(REPO_ROOT)
        if errors:
            failed += 1; print(f"❌ {rel}\n   {errors}")
        else:
            passed += 1; print(f"✅ {rel}")
    print(f"\nResults: {passed}/{total} passed, {failed} failed")
    sys.exit(1 if failed else 0)

if __name__ == "__main__":
    main()


def check_dual_output(path: str) -> list:
    """Check that persona file has v_plain + v_structured sections."""
    errors = []
    try:
        text = open(path, encoding="utf-8").read()
        if "### v_plain" not in text and "v_plain:" not in text:
            errors.append("MISSING: v_plain output version (required by schema v1.3)")
        if "### v_structured" not in text and "v_structured:" not in text:
            errors.append("MISSING: v_structured output version (required by schema v1.3)")
        if 'author: "Quang Cuong Huynh"' not in text and "author:" not in text:
            errors.append("MISSING: author field")
    except Exception as e:
        errors.append(f"Read error: {e}")
    return errors


# Inject dual-output check into main validation
_orig_validate = None
try:
    _orig_validate = validate_persona_file
except NameError:
    pass

if _orig_validate:
    def validate_persona_file_with_dual(path):
        errors = _orig_validate(path)
        errors.extend(check_dual_output(path))
        return errors
    validate_persona_file = validate_persona_file_with_dual
