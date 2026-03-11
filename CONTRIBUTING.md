# Contributing to Prompt Library

Welcome! This project is designed to stay maintainable, bilingual, and governance-ready. Read the sections below before opening an issue or pull request.

## Code of conduct

Be patient, respectful, and curious. We are building a community that values inclusivity and shared learning while keeping high standards for safety and auditability.

## Reporting issues and suggesting improvements

1. Search existing issues or discussions for similar topics.
2. Open a new issue with a clear title, reproducible steps (if applicable), expected versus actual results, and any relevant files or models.
3. Mention which part of the library is affected (`docs/`, `prompts/`, `scripts/`, `schemas/`).
4. Label whether the issue is a bug, enhancement, documentation gap, or governance request.

## Documentation & publication work

- Focus on the folders under `docs/` when improving frameworks, governance packages, or audit trails. Keep English and Vietnamese versions aligned in the same file whenever possible.
- Use the report naming conventions (e.g., `REPORT_01_...` and `OFFICIAL_PUBLICATION_PACKAGE.md`) when publishing new documents.
- Link improvements to the appropriate schema (`schemas/prompt_v1.3.schema.json`, `agent_contract.schema.json`, `provenance_record.schema.json`).

## Prompt contributions

Each persona in `prompts/` includes YAML metadata plus `v_plain` and `v_structured` sections. When you add or edit a prompt:

1. Follow the metadata fields defined in `schemas/prompt_v1.3.schema.json` (e.g., `artifact_id`, `roles`, `ocean`).
2. Keep responses available in both English and Vietnamese, with consistent terminology and guardrails.
3. Reference the Psychometric Stack layers (ISCO-08, RIASEC, Jungian cognitive stack, OCEAN) where applicable.
4. Add regression checks to `prompts/tests/` to capture expected answers for at least three sample queries.
5. Run `python scripts/validate_agents.py <file>` (or `--all-personas`) before submitting to confirm metadata completeness.

## Scripts & automation

- `scripts/validate_agents.py` is the canonical prompt validator.
- `scripts/generate_sha256.py`, `scripts/generate_timestamp.py`, and `scripts/register_artifact.py` help stamp releases and can be extended for new automation needs.
- Avoid adding secrets or proprietary credentials to the repo.

## Development workflow

```bash
git clone https://github.com/organization/prompt-library.git
cd prompt-library
git checkout -b codex/<feature-name>
```
After editing, run the applicable validators and tests (see next section) and push your branch.
Create a clean pull request that briefly summarizes what changed, why, and how to validate.

## Testing & validation

- Run `python scripts/validate_agents.py --all-personas` to ensure every persona has required metadata.
- Use YAML-based regression checks in `prompts/tests/` to replay typical prompts.
- When adding code (scripts or schema updates), include unit tests or small Python scripts that prove the change works.

## Documentation standards

- Use GitHub Flavored Markdown (`.md`) with consistent heading hierarchies.
- Keep English and Vietnamese sections close together and clearly labeled.
- Reference the metadata schema whenever you describe a prompt's structure.

## Commit & release notes

- Follow conventional commit prefixes such as `feat`, `fix`, `docs`, or `chore`.
- Include bullet summaries when there are multiple changes.
- Mention related issues or PRs in the commit body (e.g., "Closes #123" when applicable).

## License & support

- Prompt Library is released under the [MIT License](/LICENSE.md).
- Need different licensing (commercial, academic, or partner)? Mention it in your issue or PR, and the maintainers will respond.

Thank you for helping maintain a clear, governed, and reusable prompt catalog. Let us know if you need help polishing a contribution!
