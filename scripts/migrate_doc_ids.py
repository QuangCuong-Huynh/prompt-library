#!/usr/bin/env python3
"""
doc_id Format Migration Script — CSCF repo1
Migrates deprecated PERSONA-CSCF-* format to canonical CSCF-PERS-* format.
doc_id: CSCF-SCRIPT-MIGRATE-DOCID-20260310-01
"""
import os, sys, argparse

MIGRATIONS = {
    "personas/roles/technical/architect_enterprise_v1.1.md":
        ("PERSONA-CSCF-ARCH-20260308-01",      "CSCF-PERS-ARCH-ENT-20260308-01"),
    "personas/roles/technical/code_assistant_v3.0.md":
        ("PERSONA-CSCF-CODE-20260308-01",       "CSCF-PERS-CODE-ASST-20260308-01"),
    "personas/roles/technical/engineer_multirole_v1.0.md":
        ("PERSONA-CSCF-ENG-20260308-01",        "CSCF-PERS-ENG-MULTI-20260308-01"),
    "personas/roles/technical/data_architect_v1.0.md":
        ("PERSONA-CSCF-DAARCH-20260308-01",     "CSCF-PERS-DATA-ARCH-20260308-01"),
    "personas/roles/technical/planner_agent_v1.0.md":
        ("PERSONA-CSCF-PLANNER-20260308-01",    "CSCF-PERS-PLANNER-20260308-01"),
    "personas/roles/business/auditor_agent_v1.0.md":
        ("PERSONA-CSCF-AUDIT-20260308-01",      "CSCF-PERS-AUDITOR-20260308-01"),
    "personas/roles/business/compliance_gatekeeper_v1.0.md":
        ("PERSONA-CSCF-COMPGATE-20260308-01",   "CSCF-PERS-COMP-GATE-20260308-01"),
    "personas/roles/business/pm_ba_v1.0.md":
        ("PERSONA-CSCF-PMBA-20260308-01",       "CSCF-PERS-PM-BA-20260308-01"),
    "personas/roles/business/qa_director_v1.1.md":
        ("PERSONA-CSCF-QA-20260308-01",         "CSCF-PERS-QA-DIR-20260308-01"),
    "personas/roles/business/qa_pm_po_ba_v1.0.md":
        ("PERSONA-CSCF-QAMULTI-20260308-01",    "CSCF-PERS-QA-MULTI-20260308-01"),
    "personas/roles/business/strategic_data_analyst_v2.1.md":
        ("PERSONA-CSCF-SDA-20260308-01",        "CSCF-PERS-SDA-20260308-01"),
    "personas/roles/business/tech_strategist_v1.0.md":
        ("PERSONA-CSCF-TECHSTR-20260308-01",    "CSCF-PERS-TECH-STRAT-20260308-01"),
    "personas/roles/business/personal_assistant_v1.0.md":
        ("PERSONA-CSCF-PASST-20260308-01",      "CSCF-PERS-PERS-ASST-20260308-01"),
    "personas/roles/business/professional_docs_writer_v1.0.md":
        ("PERSONA-CSCF-PROFWRITE-20260308-01",  "CSCF-PERS-PROF-DOCS-20260308-01"),
    "personas/roles/business/prompt_architect_agent_v1.0.md":
        ("PERSONA-CSCF-PROMPTARCH-20260308-01", "CSCF-PERS-PROMPT-ARCH-20260308-01"),
    "personas/roles/research/astro_data_architect_v2.0.md":
        ("PERSONA-CSCF-ASTROARCH-20260308-01",  "CSCF-PERS-ASTRO-ARCH-20260308-01"),
    "personas/roles/research/buddhist_linguist_v1.1.md":
        ("PERSONA-CSCF-BUDHLING-20260308-01",   "CSCF-PERS-BUDD-LING-20260308-01"),
    "personas/roles/character/space_commander_v2.0.md":
        ("PERSONA-CSCF-SPACECMD-20260308-01",   "CSCF-PERS-SPACE-CMD-20260308-01"),
    "personas/roles/character/lore_weaver_v2.0.md":
        ("PERSONA-CSCF-LORE-20260308-01",       "CSCF-PERS-LORE-WEAV-20260308-01"),
}

def main():
    p = argparse.ArgumentParser()
    p.add_argument("--dry-run", action="store_true")
    p.add_argument("--apply", action="store_true")
    args = p.parse_args()
    if not args.dry_run and not args.apply:
        print("Usage: --dry-run or --apply"); sys.exit(1)
    for rel, (old, new) in MIGRATIONS.items():
        if not os.path.exists(rel):
            print(f"SKIP (not found): {rel}"); continue
        content = open(rel).read()
        if old in content:
            if args.apply:
                open(rel,"w").write(content.replace(f'doc_id: "{old}"', f'doc_id: "{new}"', 1))
            print(f"  {"APPLY" if args.apply else "WOULD"}: {rel} → {new}")
        else:
            print(f"  SKIP (not found in file): {rel}")

if __name__ == "__main__":
    main()
