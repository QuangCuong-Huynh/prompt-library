# Prompt Library

Prompt Library is a curated collection of governance-ready system prompts, persona reports, and validation tooling for building predictable AI assistants. The collection keeps every persona alongside its metadata, evaluation checklist, and references so downstream teams can reuse or extend each asset with confidence.

## Repository layout

- `docs/framework/`: high-level reports on the Psychometric Stack, prompts-as-code workflows, and persona specification practices.
- `docs/governance/`: publication packages, authorship records, and compliance/standards overviews that tie the library to ISO/NIST best practices.
- `docs/audit/`: validation summaries, testing protocols, and architecture reviews that document how each prompt was evaluated.
- `docs/quick-reference/`: migration checklists and short-form guides for bilingual contributors.
- `prompts/`: persona definitions in English + Vietnamese, organized by `academic`, `business`, `characters`, `technical`, `templates`, and `tests` subfolders.
- `schemas/`: JSON Schemas (`prompt_v1.3.schema.json`, `agent_contract`, `provenance_record`, etc.) that describe every metadata block.
- `scripts/`: helper utilities for timestamps, hashing, artifact signing, and prompt validation.

## Quick start

```bash
git clone https://github.com/organization/prompt-library.git
cd prompt-library
```

1. Read [docs/README.md](/docs/README.md) to understand how the reports, governance paperwork, and audit trails fit together.
2. Pick a prompt category (e.g., `prompts/business/strategic_data_analyst_v2.1.md`) and open the Markdown file to inspect the YAML front matter and dual-language response sections.
3. Run the validation helper to check metadata against the schema:

```bash
python scripts/validate_agents.py --check-schema
python scripts/validate_agents.py prompts/
```

4. Explore the tests that keep each persona honest in `prompts/tests/`.

## Prompt catalog overview

Each persona document begins with a YAML metadata block (`artifact_id`, `doc_id`, `roles`, `security_constraints`, etc.) that parallels `schemas/prompt_v1.3.schema.json`. The body typically contains:

- `### v_plain`: a conversational version of the persona.
- `### v_structured`: a structured, enumeration-friendly version for automated evaluation.
- Dual-language (English + Vietnamese) sections that keep the voice consistent across markets.
- A reference table with ISCO-08, RIASEC, Jungian cognitive stack, and OCEAN tuning values.

Templates under `prompts/templates/` show how to craft new persona files, while `prompts/tests/` contains YAML-based regression checks that mirror every persona's obligations.

## Documentation highlights

- Review `docs/framework/REPORT_01_PSYCHOMETRIC_STACK_FRAMEWORK.md` for the four-layer persona architecture.
- `docs/governance/OFFICIAL_PUBLICATION_PACKAGE.md` explains the publication checklist and approvals that precede any release.
- Audit documents such as `docs/audit/TESTING-VALIDATION-REPORT.md` summarize the dataset of evaluations that produced the current quality scores.

Use `docs/README.md` or this README to navigate deeper.

## Tooling & validation

- `scripts/validate_agents.py` walks every Markdown persona, ensures required fields are present, and double-checks that the `ocean`, `roles`, and dual outputs exist.
- `schemas/` contains the authoritative contracts for metadata, gating decisions, and provenance records.
- `scripts/generate_sha256.py`, `scripts/generate_timestamp.py`, and `scripts/register_artifact.py` help automate publishing if you are stamping artifacts for release.

## Testing & quality

- Bash/CI workflows can reuse the YAML files in `prompts/tests/` to feed prompts into whichever LLM you are validating.
- Every persona is evaluated through structured tests that exercise role adherence, guardrail enforcement, and output tagging.
- Use the `schemas` folder to keep new metadata in sync with the expectations documented in the governance reports.

## Contribution & license

- See [CONTRIBUTING.md](/CONTRIBUTING.md) for issue triage, prompt contribution, and documentation guidelines.
- This repository is published under the [MIT License](/LICENSE.md) so you can adapt the work freely. If you need a different license (commercial or academic), please mention it in your pull request or open issue.

Thanks for helping us keep prompts, governance, and validation tightly aligned—let me know how I can help the next iteration!
