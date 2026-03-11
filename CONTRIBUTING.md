# Contributing to Prompt Library

Welcome! This project is designed to stay maintainable, bilingual, and governance-ready. Read the sections below before opening an issue or pull request.

Thank you for your interest in contributing to Prompt Library! This document explains how to participate.

## Code of Conduct

Be patient, respectful, and curious. We are building a community that values inclusivity and shared learning while keeping high standards for safety and auditability.

## How to Contribute

### 1. Report Issues and Suggest Improvements

1. Search [existing issues](https://github.com/organization/prompt-library/issues) or discussions for similar topics.
2. Open a new issue with a clear title, reproducible steps (if applicable), expected versus actual results, system information, and any relevant files or models.
3. Mention which part of the library is affected (`docs/`, `prompts/`, `scripts/`, `schemas/`).
4. Label whether the issue is a bug, enhancement, documentation gap, or governance request.

### 2. Submit Documentation & Publication Work

Help improve documentation by focusing on the folders under `docs/` when improving frameworks, governance packages, or audit trails.

1. Check [existing docs](docs/) and identify gaps or improvements.
2. Keep English and Vietnamese versions aligned in the same file whenever possible.
3. Use the report naming conventions (e.g., `REPORT_01_...` and `OFFICIAL_PUBLICATION_PACKAGE.md`) when publishing new documents.
4. Link improvements to the appropriate schema (`schemas/prompt_v1.3.schema.json`, `agent_contract.schema.json`, `provenance_record.schema.json`).
5. Submit pull request with clear changes and proper formatting.

### 3. Contribute Prompts

Create or edit specialized prompts in the `prompts/` directory. Each persona includes YAML metadata plus `v_plain` and `v_structured` sections.

1. Design using the Psychometric Stack (ISCO-08, RIASEC, Jungian cognitive stack, OCEAN).
2. Follow metadata fields defined in `schemas/prompt_v1.3.schema.json` (e.g., `artifact_id`, `roles`, `ocean`).
3. Keep responses available in both English and Vietnamese, with consistent terminology and guardrails.
4. Add regression checks to `prompts/tests/` to capture expected answers for at least three sample queries.
5. Run `python scripts/validate_agents.py <file>` (or `--all-personas`) before submitting to confirm metadata completeness.
6. Submit pull request after ensuring a quality score ≥8.0/10.

### 4. Contribute Code (Scripts & Automation)

Improve tools and automation in the `tools/` and `scripts/` directories:

1. Follow existing patterns and add tests.
2. `scripts/validate_agents.py` is the canonical prompt validator.
3. `scripts/generate_sha256.py`, `scripts/generate_timestamp.py`, and `scripts/register_artifact.py` help stamp releases and can be extended.
4. Avoid adding secrets or proprietary credentials to the repo.
5. Submit pull request.

## Development Workflow

### Setup

```bash
# Clone repository
git clone https://github.com/QuangCuong-Huynh/prompt-library.git
cd prompt-library

# Create feature branch
git checkout -b codex/your-feature-name

# Install dependencies (if applicable)
pip install -r requirements.txt
npm install
```

### Making Changes & Testing

1. Make your changes in the appropriate directory.
2. Run applicable validators and tests:

   ```bash
   # For prompt contributions
   python scripts/validate_agents.py --all-personas
   
   # For code contributions
   python -m pytest tests/ -v
   pytest --cov=prompt_library tests/
   
   # For documentation
   npx markdown-link-check docs/**/*.md
   npx spellchecker docs/**/*.md
   ```

3. Commit with conventional format (see below).
4. Push your branch and create a clean Pull Request on GitHub.

## Standards & Guidelines

### Code Standards

- **Python:** PEP 8, type hints
- **JavaScript:** ESLint, Prettier
- **YAML:** 2-space indent, valid syntax

### Documentation Standards

- **Markdown:** GFM (GitHub Flavored Markdown)
- **Headings:** Consistent hierarchy
- **Dual language:** English + Vietnamese clearly labeled
- **Code blocks:** Language-specific syntax highlighting

### Commit Guidelines

Use Conventional Commits: `<type>(<scope>): <subject>`

**Types:** `feat`, `fix`, `docs`, `style`, `refactor`, `test`, `chore`.

Example: `feat(prompt): add regulatory compliance analyzer`

## Review Checklist

### Content & Code Review

- [ ] Metadata complete and follows schemas
- [ ] Dual-language support (EN + VI) aligned
- [ ] Tests added and passing
- [ ] Documentation updated
- [ ] No security issues or secrets exposed

### Governance Review

- [ ] ISO 27001/9001 aligned
- [ ] No PII exposed
- [ ] Audit trail complete
- [ ] Authority approval obtained (if applicable)

## License & Support

- Prompt Library is released under the [MIT License](/LICENSE.md).
- Need different licensing (commercial, academic, or partner)? Mention it in your issue or PR.

## Recognition

Contributors are recognized in release notes, on the contributors page, and in community celebrations.

## Questions?

- **📧 Email:** <framework-team@enterprise.ai>
- **💬 Discussions:** <https://github.com/organization/prompt-library/discussions>
- **📚 Docs:** <https://prompt-library.org>
- **🐙 Issues:** <https://github.com/organization/prompt-library/issues>

---

Thank you for helping make Prompt Library better! 🎉
