---
artifact_id: "019cdca8-9176-7934-85bf-957d8f46bd42"
doc_id: "CSCF-PUB-04-20260309-01"
name:        "SOP: Quản Lý Prompt Dưới Dạng Mã Nguồn (Prompts as Code)"
version: "1.0.0"

authority_official:
  owner:       "Quang Cuong Huynh"
  declaration: "Registered — Quang Cuong Huynh"
  assistants:
    - "Claude (Anthropic)"
  reviewer:    "Quang Cuong Huynh"
status:      "active"
migrated_from: "QUY_TRÌNH_VẬN_HÀNH_TIÊU_CHUẨN_SOP_PROMPTS_AS_CODE.pdf"
migrated_at: "2026-03-09"
dc:
  title: "SOP: Quản Lý Prompt Dưới Dạng Mã Nguồn (Prompts as Code)"
  type: "sop"
  date:     "2026-03-08"
  language: "vi"
  subject: ["SOP","prompts-as-code","CI/CD","monorepo","governance","ISO-27001"]
sha256: "PENDING"

changes:
  - version: "1.0.0"
    date:    "2026-03-11"
    author:  "Quang Cuong Huynh"
    summary: "UAS v1.2 compliance fix"
    type:    "fix"
---
# SOP: Quản Lý Prompt Dưới Dạng Mã Nguồn (Prompts as Code)

> **Publication Type:** Enterprise SOP — signals professional governance maturity  
> **Target Audience:** AI Platform teams, CTOs, compliance officers  
> **Enterprise Signal:** ISO 27001 + CI/CD + Monorepo for AI governance

## The 3 Supreme Architecture Principles

1. **Prompts as Code**: Every prompt version-controlled, auto-tested, CI/CD-deployed
2. **Quality by Design**: Quality is a constant built into cognitive structure, not a post-hoc test
3. **Governance as Enabler**: Governance reduces failure cost — enables innovation at scale

## 5-Phase Lifecycle

| Phase | Activity | Gate |
|---|---|---|
| P1 Design & Requirements | Role profiling (ISCO-08/RIASEC), PRD, PGC approval | Linting Gate |
| P2 Development | Cognitive-Scientific Architecture, OCEAN tuning | Schema validation |
| P3 V&V | Functional/Robustness/Safety tests (Promptfoo) | Quality Gate |
| P4 Deployment | Git workflow, peer review, GitHub Actions | Merge Gate |
| P5 Monitoring | Anti-drift, ISO 27001 audit log, deprecation | Continuous |

## ISCO-08 × RIASEC Enterprise Reference Table

| AI Role | ISCO-08 | RIASEC | Core Skills |
|---|---|---|---|
| Data Scientist | 2521 | I, C | Statistical Modeling, Data Mining |
| Software Architect | 2511 | I, R, C | System Design, Connectivity Standards |
| Strategic Analyst | 2422 | I, E, C | Policy Analysis, Economic Forecasting |
| Project Manager | 1219 | E, C, S | Resource Allocation, Stakeholder Management |
| QA Engineer | 2519 | C, I, R | Root Cause Analysis, Regression Testing |

## SemVer for Prompts

| Change Type | Version Bump | Example |
|---|---|---|
| MAJOR | Breaking: change reasoning engine (Te→Ti) | v1.x.x → v2.0.0 |
| MINOR | Add knowledge domain, new capability | v1.1.x → v1.2.0 |
| PATCH | Style fix, minor wording | v1.1.0 → v1.1.1 |

> See: `governance/PROMPTS_AS_CODE.md` for full implementation in this repo.
> See: `.github/workflows/validate.yml` for CI/CD implementation.