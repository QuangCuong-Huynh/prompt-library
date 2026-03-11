# Documentation guide

This repository treats documentation as code. Every publication includes a metadata front matter, version history, and bilingual content. Refer to the sections below to find the right report for your need.

## Framework reports (`docs/framework/`)

- `REPORT_01_PSYCHOMETRIC_STACK_FRAMEWORK.md`: The four-layer architecture that grounds persona identity in ISCO-08, RIASEC, Jungian functions, and OCEAN.
- `REPORT_02_PROMPTS_AS_CODE_SOP.md`: Operations playbook for version control, reviews, and governance handoffs.
- `REPORT_03_PSYCHOMETRIC_ENGINEERING.md`: Engineering guidelines for building deterministic agents from psychological constructs.
- `REPORT_04_05_06_COMBINED_PERSONALITY_ARCHITECTURE_SPECIFICATION.md`: Combined reference for advanced personality modeling, specification, and cognitive architecture.

## Governance & publication (`docs/governance/`)

- `OFFICIAL_PUBLICATION_PACKAGE.md`: Release checklist, approvals, and artifact packaging details.
- `AUTHORS_AND_OFFICERS.md`: Named custodians, reviewers, and approvers.
- `GOVERNANCE_AND_STANDARDS.md`: Standards mapping (ISO, NIST, CIS) and accountability links.
- `PUBLICATION_INDEX.md`: A living index of every release and associated documentation.

## Audit & validation (`docs/audit/`)

- `ALL-PROMPTS-DETAILED-AUDIT.md`: Audit of every persona, coverage gaps, and compliance notes.
- `TESTING-VALIDATION-REPORT.md`: Outcomes of the regression suites and quality scoring.
- `PROJECT-AUDIT-REPORT.md` & `ARCHITECTURE-REFERENCE.md`: Project-level retrospectives and architecture maps.

## Quick references & migrations (`docs/quick-reference/`)

- `INDEX-VIETNAMESE-DOCS-MIGRATION.md`: Checklist for keeping Vietnamese translations aligned with the English source.

## Metadata & additions

- Every doc contains a front matter block (`document_id`, `document_type`, `status`, `version`, etc.). Use `scripts/migrate_doc_ids.py` and `schemas/prompt_v1.3.schema.json` as references when adding new material.
- Maintain the dual-language sections (English + Vietnamese) within each file so both audiences can collaborate without context switches.

## Need a new doc?

1. Copy an existing report, update the front matter, and set status/authority fields.
2. Link to the new doc from `PUBLICATION_INDEX.md` and mention it in the governance package if it introduces a new compliance requirement.
3. Run `scripts/generate_timestamp.py` and `scripts/generate_sha256.py` if you plan to reference the doc in a registry or artifact release.

Use this guide in tandem with [`README.md`](../README.md) and [`CONTRIBUTING.md`](../CONTRIBUTING.md) when extending documentation.
