# Prompt catalog overview

This folder contains the persona definitions that make Prompt Library reusable. Each Markdown file pairs metadata with English and Vietnamese output sections so you can plug the persona into assistants, guardrails, or evaluation harnesses.

## Directory structure

- cademic/: prompts tuned for research, documentation, or educational support.
- usiness/: strategic analysts, compliance agents, QA directors, and similar enterprise roles.
- characters/: narrative or story-driven personas with shaped voices and behaviors.
- 	echnical/: architects, engineers, and code assistants with deep domain grounding.
- 	emplates/system_prompt/ & 	emplates/output/: starter templates for crafting new persona files and structured response patterns.
- 	ests/: YAML regression suites that validate how each persona should behave in guardrail scenarios.

## Prompt format

Every persona begins with YAML metadata that mirrors schemas/prompt_v1.3.schema.json. Required fields include rtifact_id, doc_id, ersion, oles, knowledge_domains, ehavior_rules, output_spec, and security_constraints. Each oles entry should describe the persona's ISCO-08, RIASEC, OCEAN, and cognitive stack values.

The body of the file should provide:

1. A ### v_plain section (natural language instructions).
2. A ### v_structured section (bulleted or tabular field-by-field guidance).
3. Dual-language coverage so English and Vietnamese readers share the same guardrails.
4. Example queries and expected outputs when possible.

## Validation & tests

- Run python scripts/validate_agents.py --all-personas from the repository root to confirm metadata completeness across the catalog.
- Examine prompts/tests/<persona>_test.yml for sample guardrail test cases. Reuse these YAML files in your preferred testing harness (LLM evaluation, automated assertions, etc.).

## Adding new personas

1. Use the templates under prompts/templates/ to scaffold the YAML front matter.
2. Reference docs/framework/REPORT_01_PSYCHOMETRIC_STACK_FRAMEWORK.md for the guiding architecture of ISCO-08 → RIASEC → cognitive stack → OCEAN.
3. Keep the persona bilingual and include at least three example prompts.
4. Add or update a regression test in prompts/tests/.
5. Run python scripts/validate_agents.py <path> before submitting to ensure compliance with the schema.

Thanks for helping grow a governed, versioned prompt catalog—feel free to open an issue if you need a hand with tooling or metadata updates!
