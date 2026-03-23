---
artifact_id: "019cdca8-9179-76a9-abf8-1d8c03877002"
doc_id: "CSCF-KB-PAC-20260309-01"
name:        "Prompts as Code (PAC) Framework — Project Overview"
version: "1.0.0"

authority_official:
  owner:       "Quang Cuong Huynh"
  declaration: "Registered — Quang Cuong Huynh"
  assistants:
    - "Claude (Anthropic)"
  reviewer:    "Quang Cuong Huynh"
status: "active"

migrated_from: "STAR_ _Prompts as Code_ Framework_.docx"
migrated_at: "2026-03-09"
sha256: "PENDING"
dc:
  title: "Prompts as Code (PAC) Framework — Project Overview"
  type: "kb"
  date: "2026-03-09"
  subject: ["PAC","prompts-as-code","LLMOps","governance","CI/CD","enterprise-AI"]

changes:
  - version: "1.0.0"
    date:    "2026-03-11"
    author:  "Quang Cuong Huynh"
    summary: "UAS v1.2 compliance fix"
    type:    "fix"
---
# Prompts as Code (PAC) Framework

> **Tagline:** Transforming prompt engineering from an artisanal craft into a disciplined,
> version-controlled software engineering practice.

## Problem Statement (STAR: Situation)

Organizations adopting LLMs at scale face four systemic challenges:

1. **Lack of Standardization** — Prompts as ad-hoc strings → behavioral drift, inconsistent outputs
2. **Hallucination Risks** — No formal mechanism for grounding; complex agents lose context
3. **Security & Compliance Gaps** — No PII redaction enforcement, audit trails, or standards adherence
4. **Scalability Bottlenecks** — Manual chat-based management = no versioning, regression testing, or collaboration

## Solution (STAR: Task & Action)

The PAC Framework treats every system prompt as a **production-grade software artifact**:

```
┌──────────────────────────────────────────────────────────────┐
│                    PAC ENGINEERING LIFECYCLE                  │
│                                                              │
│  Design → Review → Test → Version → Deploy → Monitor        │
│    ↓         ↓        ↓       ↓         ↓        ↓          │
│  CSCF     Human    Promptfoo  Git    CI/CD     Drift        │
│ Schema    Gate     Assertions SemVer  Actions  Detection    │
└──────────────────────────────────────────────────────────────┘
```

### Core Principles

| Principle | Implementation |
|---|---|
| **Versioned** | Semantic versioning (MAJOR.MINOR.PATCH) in YAML frontmatter |
| **Tested** | Promptfoo behavioral assertions (≥3 per persona) |
| **Auditable** | UUIDv7 artifact IDs + SHA-256 content hash |
| **Governed** | Quality gates G1–G5 before promotion to production |
| **Documented** | Dual output: v_plain + v_structured |

### Technical Stack

- **Schema:** JSON Schema (Draft-07) — `schemas/v1.2/prompt_v1.3.schema.json`
- **Validation:** Python `scripts/validate_agents.py`
- **Signing:** `scripts/sign_artifact.py` / `sign_artifact.js`
- **Testing:** Promptfoo (`tests/*.yml`)
- **CI/CD:** GitHub Actions (`.github/workflows/`)
- **Format:** YAML frontmatter + Markdown body

## Results (STAR: Result)

| Metric | Before PAC | After PAC |
|---|---|---|
| Behavioral drift incidents | Ad-hoc, untracked | < 1/month (gate-controlled) |
| Persona test coverage | 0% | 100% (45 assertions) |
| Time to validate new persona | Hours/days | Minutes (automated) |
| Audit readiness (ISO 27001) | Not possible | Full provenance chain |
| Cross-tool portability | Manual copy-paste | v_plain + v_structured |

## Keywords

Generative AI · LLMOps · Prompt Engineering · System Architecture · Python · CI/CD · 
JSON Schema · YAML · Semantic Versioning · AI Governance · Cognitive Architectures · 
Automated Testing · ISO Standards · CSCF · GAP