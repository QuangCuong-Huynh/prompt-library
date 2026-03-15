# Contributing to Prompt Library

Thank you for your interest in contributing to Prompt Library! This document explains how to participate.

## Code of Conduct

Be respectful, inclusive, and professional. We're building a community around enterprise AI governance.

## How to Contribute

### 1. Report Issues

Found a bug or have a suggestion?

1. Check [existing issues](https://github.com/organization/prompt-library/issues)
2. Create a new issue with:
   - Clear description
   - Steps to reproduce (if bug)
   - Expected vs. actual behavior
   - System information

### 2. Suggest Enhancements

Have an idea for improvement?

1. Open a GitHub Discussion
2. Describe the problem it solves
3. Explain why it's needed
4. Show how it aligns with framework

### 3. Submit Documentation

Help improve documentation:

1. Check [existing docs](docs/)
2. Identify gaps or improvements
3. Submit pull request with:
   - Clear changes
   - Proper formatting
   - Links to related docs

### 4. Contribute Prompts

Create specialized prompts:

1. Design using Psychometric Stack
2. Test thoroughly (see Testing below)
3. Document with examples
4. Submit pull request

**Requirements:**
- Quality score ≥8.0/10
- Dual-language support (EN + VI)
- Complete metadata block
- 3+ example queries
- Unit tests passing
- Governance approval

### 5. Contribute Code

Improve tools and automation:

1. Check [tools/](tools/) directory
2. Follow existing patterns
3. Add tests
4. Document usage
5. Submit pull request

## Development Workflow

### Setup

```bash
# Clone repository
git clone https://github.com/organization/prompt-library.git
cd prompt-library

# Create feature branch
git checkout -b feature/your-feature-name

# Install dependencies (if applicable)
pip install -r requirements.txt
npm install
```

### Making Changes

```bash
# Make your changes
# Edit files in appropriate directory

# Test locally
python -m pytest tests/
npm test

# Commit with conventional format
git commit -m "feat(docs): add advanced examples

- Added section on advanced use cases
- Included 5 new examples
- Updated references
- Closes #123"

# Push branch
git push origin feature/your-feature-name

# Create Pull Request on GitHub
```

### Pull Request Process

1. **Title:** Clear, descriptive title
   - `feat(prompt): add regulatory compliance analyzer`
   - `fix(docs): correct ISCO-08 reference`
   - `chore(ci): update validation workflow`

2. **Description:** Explain:
   - What changes
   - Why it's needed
   - How to test
   - Related issues

3. **Review:** Wait for 2+ approvals
   - Code/content review
   - Governance review (if applicable)

4. **Merge:** Maintainers will merge after approval

## Testing & Validation

### For Prompt Contributions

```yaml
testing_requirements:
  unit_tests:
    - Role adherence: 10 queries
    - Source attribution: 10 claims
    - Guardrail enforcement: 5 injection attempts
    - Edge cases: 5+ scenarios
  
  quality_gate:
    - Quality score: ≥8.0/10
    - Test coverage: ≥90%
    - Security audit: PASS
    - Governance: APPROVED
```

### For Code Contributions

```bash
# Run tests
python -m pytest tests/ -v

# Check coverage
pytest --cov=prompt_library tests/

# Lint code
pylint prompt_library/

# Type check
mypy prompt_library/
```

### For Documentation

```bash
# Check links
npx markdown-link-check docs/**/*.md

# Spell check
npx spellchecker docs/**/*.md

# Validate YAML
python -m yaml.safe_load < docs/**/*.yaml
```

## Standards & Guidelines

### Code Standards

- **Python:** PEP 8, type hints
- **JavaScript:** ESLint, Prettier
- **YAML:** 2-space indent, valid syntax

### Documentation Standards

- **Markdown:** GFM (GitHub Flavored Markdown)
- **Headings:** Consistent hierarchy
- **Code blocks:** Language-specific syntax highlighting
- **Examples:** Clear, runnable

### Governance Standards

- **YAML metadata:** All required fields
- **UUID v7:** For new documents
- **ISO 8601:** For timestamps
- **Dual language:** English + Vietnamese

## Commit Guidelines

Use Conventional Commits:

```
<type>(<scope>): <subject>

<body>

<footer>
```

**Types:**
- `feat`: New feature
- `fix`: Bug fix
- `docs`: Documentation
- `style`: Formatting
- `refactor`: Code restructuring
- `test`: Test additions
- `chore`: Maintenance

**Examples:**
```
feat(prompt): add regulatory compliance analyzer

- ISCO-08 code: 2421
- RIASEC: C-I-E
- Includes 15+ guardrails
- Quality: 9.2/10
- Closes #234

docs(readme): improve quick start section

- Added visual diagram
- Improved code examples
- Clarified prerequisite steps

chore(ci): update validation workflow

- Add YAML linting
- Update dependencies
- Improve error messages
```

## Review Checklist

### Code Review Checklist

```markdown
- [ ] Code follows style guidelines
- [ ] Type hints present
- [ ] Tests added and passing
- [ ] Documentation updated
- [ ] No security issues
- [ ] Performance acceptable
```

### Content Review Checklist

```markdown
- [ ] Metadata complete
- [ ] Examples tested
- [ ] References cited
- [ ] Grammar/spelling correct
- [ ] Links working
- [ ] Compliance verified
```

### Governance Review Checklist

```markdown
- [ ] ISO 27001 aligned
- [ ] ISO 9001 compliant
- [ ] No PII exposed
- [ ] Audit trail complete
- [ ] Authority approval obtained
```

## Questions?

- **📧 Email:** framework-team@enterprise.ai
- **💬 Discussions:** https://github.com/organization/prompt-library/discussions
- **📚 Docs:** https://prompt-library.org
- **🐙 Issues:** https://github.com/organization/prompt-library/issues

## Recognition

Contributors are recognized:
- In release notes
- On contributors page
- In project documentation
- In community celebrations

## License

By contributing, you agree your contributions are licensed under the same Proprietary Enterprise License.

---

Thank you for helping make Prompt Library better! 🎉
