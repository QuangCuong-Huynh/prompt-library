---
artifact_id: "019cdca8-9132-72f4-8846-49a9d07088f6"
doc_id: "CSCF-KB-DOCS-WRITER-20260310-01"
name:        "Knowledge Domain Library — Professional Documentation Writer"
version: "1.0.0"

authority_official:
  owner:       "Quang Cuong Huynh"
  declaration: "Registered — Quang Cuong Huynh"
  assistants:
    - "Claude (Anthropic)"
  reviewer:    "Quang Cuong Huynh"
status: "active"
persona: "professional_docs_writer_v1.0"
dc:
  type:     "kb"
  title: "Knowledge Domain Library — Professional Documentation Writer"
  date: "2026-03-10"
changes:
  - version: "1.0.0"
    date: "2026-03-10"
    author: "Quang Cuong Huynh"
    summary: "Sprint 4 — initial KB creation"
    type:     "kb"
sha256: "PENDING"
---
# Knowledge Domain Library — Professional Documentation Writer v1.0

> ISCO-08: 2641 | RIASEC: A-C-I | Si→Te→Ni | OCEAN: O:8 C:9 E:5 A:8 N:1

---

## Tier 1 — Authoritative Standards

### Documentation Standards
- IEEE 1063:2001 — Software user documentation
- IEEE 26511:2018 — Systems and software engineering — requirements for managers of user documentation
- ISO/IEC/IEEE 26511:2018 — User documentation process
- DITA (Darwin Information Typing Architecture) — structured authoring standard
- DocBook XML 5.0 — technical documentation schema
- Divio Documentation System — tutorials/how-to/reference/explanation

### Style Guides
- Microsoft Writing Style Guide (docs.microsoft.com/style-guide)
- Google Developer Documentation Style Guide
- Apple Style Guide
- Chicago Manual of Style (17th ed., 2017) — formal prose
- APA Style 7th Edition — technical reports

### API Documentation
- OpenAPI Specification 3.1 (OAS) — API docs as code
- Swagger UI — interactive API documentation
- Stoplight — API design + docs platform
- Postman Collections — runnable API examples
- AsyncAPI 2.x — event-driven API documentation

---

## Tier 2 — Document Type Matrix

### Document Types and Standards

| Doc Type | Standard | Key Sections | Audience |
|---|---|---|---|
| Software Requirements Spec (SRS) | IEEE 29148 | Purpose, Scope, FRs, NFRs, constraints | PM, Dev, QA |
| Architecture Decision Record (ADR) | Nygard/Zimmermann | Context, Decision, Consequences | Architect, Dev |
| Runbook | SRE best practices | Trigger, Steps, Rollback, Escalation | Ops, DevOps |
| Release Notes | KEEP A CHANGELOG format | Added/Changed/Fixed/Removed | All |
| API Reference | OAS 3.1 | Endpoints, parameters, responses, examples | Developer |
| User Manual | IEEE 1063 | Overview, tasks, reference, troubleshooting | End user |
| Technical Proposal | McKinsey pyramid | Situation, Complication, Resolution | Leadership |
| Post-mortem | Google SRE format | Impact, Root cause, Timeline, Actions | Team, Mgmt |

### Divio Documentation System
| Type | Question Answered | Example |
|---|---|---|
| Tutorial | How do I learn? | Getting Started Guide |
| How-to Guide | How do I accomplish X? | "How to deploy to production" |
| Reference | What is this? | API Reference, Data Dictionary |
| Explanation | Why does it work this way? | Architecture Overview, ADRs |

### Document Quality Checklist (Auto-Apply)
- [ ] UAS Header: doc_id, version, author, authority, date
- [ ] Changelog block present (version history)
- [ ] Audience identified in opening section
- [ ] All acronyms defined on first use
- [ ] Every claim: [FACT] | [INFERENCE] | [HYPOTHESIS] labeled
- [ ] Cross-references use doc_id (not relative paths)
- [ ] Code blocks: language-tagged, syntax-valid
- [ ] Tables: header row, alignment, no merged cells

---

## Tier 3 — Books & Style References

- Alred, Brusaw & Oliu — *The Technical Writer's Handbook* (10th ed.)
- Strunk & White — *The Elements of Style* (4th ed., 1999)
- Williams & Bizup — *Style: Lessons in Clarity and Grace* (12th ed.)
- Zinsser, William — *On Writing Well* (7th ed., 2006) — non-fiction clarity
- Divio — Documentation System (documentation.divio.com)
- Bernoff, Josh — *Writing Without Bullshit* (2016)

---

## Tier 4 — Tools

| Tool | Purpose |
|---|---|
| MkDocs + Material theme | Static documentation sites |
| Sphinx | Python API documentation |
| Docusaurus 3 | Developer portals |
| Writerside (JetBrains) | IDE-integrated docs |
| Vale | Prose linting (style guide enforcement) |
| Grammarly Business | Grammar + tone checking |
| Notion / Confluence | Collaborative documentation |
| Pandoc | Format conversion (md → docx → pdf) |

---

## Tier 5 — Search Queries

- "IEEE 29148 software requirements specification template"
- "Divio documentation system tutorials reference explanation"
- "architecture decision record ADR template Nygard format"
- "technical writing style guide Microsoft Google 2025"
- "docs as code approach documentation pipeline CI/CD"
- "OpenAPI 3.1 documentation best practices examples"

---

## Domain Boundaries

| In Scope | Out of Scope |
|---|---|
| Technical and professional document production | Content strategy / IA (→ tech_strategist) |
| SRS, ADR, runbook, release notes, API ref | Requirements elicitation (→ pm_ba) |
| Style guide enforcement + proofreading | Architecture decisions (→ architect) |
| UAS header + changelog maintenance | Code implementation (→ engineer) |
| Format conversion (md/docx/pdf) | Compliance auditing (→ auditor) |