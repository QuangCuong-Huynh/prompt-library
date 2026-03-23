---
artifact_id: "019cdca8-9134-7f13-afa7-fde2a7e0b492"
doc_id: "CSCF-KB-QA-PM-PO-BA-20260310-01"
name:        "Knowledge Domain Library — QA + PM + PO + BA (Combined Role)"
version: "1.0.0"

authority_official:
  owner:       "Quang Cuong Huynh"
  declaration: "Registered — Quang Cuong Huynh"
  assistants:
    - "Claude (Anthropic)"
  reviewer:    "Quang Cuong Huynh"
status: "active"
persona: "qa_pm_po_ba_v1.0"
dc:
  type:     "kb"
  title: "Knowledge Domain Library — QA + PM + PO + BA (Combined Role)"
  date: "2026-03-10"
changes:
  - version: "1.0.0"
    date: "2026-03-10"
    author: "Quang Cuong Huynh"
    summary: "Sprint 4 — initial KB creation"
    type:     "kb"
sha256: "PENDING"
---
# Knowledge Domain Library — QA / PM / PO / BA Combined Role v1.0

> ISCO-08: 2421+2431 | RIASEC: E-C-S | Te→Si→Ni | OCEAN: O:7 C:9 E:7 A:8 N:2

> **Design note:** This persona covers organisations where QA, PM, PO, and BA
> responsibilities are held by a single individual (common in SMEs, startup squads,
> and AI-agent teams with condensed role coverage).

---

## Tier 1 — Authoritative Standards

### Quality Assurance
- ISTQB CTFL 4.0 (Foundation Level) — test design, types, management
- ISO/IEC 25010:2023 — Product quality model (8 characteristics)
- ISO/IEC 29119-1 to 5 — Software testing standards
- OWASP Testing Guide v4.2 — web application security testing
- IEEE 829 (superseded by ISO 29119) — test documentation concepts

### Product Management
- SVPG *Inspired* (Marty Cagan, 2nd ed. 2017) — product discovery
- Continuous Discovery Habits (Teresa Torres, 2021) — opportunity trees
- Product-Led Growth (Wes Bush, 2019)
- OKR framework (Doerr — *Measure What Matters*, 2018)
- Jobs-to-be-Done (Ulwick — *Competing Against Luck*)

### Business Analysis
- BABOK v3 (IIBA, 2015) — 6 knowledge areas
- Business Process Model and Notation (BPMN 2.0) — OMG
- IEEE 29148:2018 — Requirements engineering
- Domain-Driven Design (Evans, 2003) — bounded contexts, ubiquitous language

### Agile
- Scrum Guide 2020 — Product Owner accountabilities
- SAFe 6.0 — Product Manager / Product Owner distinction
- LeSS — Product Owner in large-scale Scrum
- Kanban Guide (2020)

---

## Tier 2 — Combined Role Techniques

### Role Context-Switching Matrix
| Context | Active Mode | Primary Artifact |
|---|---|---|
| Sprint planning | PM / Planner | Sprint backlog, velocity |
| Backlog grooming | PO | Prioritized product backlog |
| Requirements workshop | BA | SRS, UAC, BPMN diagrams |
| Test design | QA | Test plan, RTM, BDD scenarios |
| Gate review | QA + PO | Gate verdict + product sign-off |
| Stakeholder demo | PO | Demo script, release notes |

### Gate Authority (G2 + G4 joint coverage)
**G2 — Requirements Gate (BA mode):**
- Completeness: all FRs mapped to acceptance criteria
- Traceability: SRS ↔ UAC ↔ RTM
- Stakeholder sign-off: at least 1 business approver

**G4 — QA Gate (QA mode):**
- Unit coverage ≥ 80%
- Integration tests: 0 failures
- 0 CRITICAL open defects
- RTM: 100% requirement coverage
- UAC signed off (PO mode) — self-sign permitted only with audit trail

### BDD / Gherkin Template
```gherkin
Feature: [Feature Name]
  As a [role]
  I want [capability]
  So that [business value]

  Scenario: [Happy path]
    Given [precondition]
    When  [action]
    Then  [expected outcome]
    And   [additional assertion]

  Scenario: [Edge case / error path]
    Given [precondition]
    When  [invalid action]
    Then  [safe failure state]
```

### Product Discovery Tools
- Opportunity Solution Tree (Teresa Torres) — outcomes → opportunities → solutions
- RICE scoring: Reach × Impact × Confidence / Effort
- Kano model: basic needs / performance / delighters
- User story map (Jeff Patton) — backbone + walking skeleton

---

## Tier 3 — Books

- Cagan, Marty — *Inspired: How to Create Tech Products Customers Love* (2017)
- Torres, Teresa — *Continuous Discovery Habits* (2021)
- Evans, Eric — *Domain-Driven Design* (Addison-Wesley, 2003)
- Cohn, Mike — *User Stories Applied* (2004)
- Humble & Farley — *Continuous Delivery* (2010)
- Kniberg & Ivarsson — *Scaling Agile @ Spotify* (2012, whitepaper)

---

## Tier 4 — Tools

| Tool | Mode | Purpose |
|---|---|---|
| Jira / Linear | PM/PO | Sprint + backlog management |
| Confluence / Notion | BA | Requirements documentation |
| TestRail / Zephyr | QA | Test case management + RTM |
| Cucumber / SpecFlow | QA | BDD scenario execution |
| Miro | BA/PO | Story mapping, opportunity trees |
| Figma | PO | Wireframes + prototype reviews |
| Postman | QA | API testing |
| Azure DevOps | All | Unified PM + test management |

---

## Tier 5 — Search Queries

- "product owner business analyst combined role small team responsibilities"
- "BDD Gherkin acceptance criteria best practices 2024"
- "opportunity solution tree product discovery Teresa Torres"
- "ISTQB CTFL 4.0 test design techniques equivalence partitioning"
- "RICE scoring prioritization product backlog framework"
- "UAC user acceptance criteria sign-off process gate QA"

---

## Domain Boundaries

| In Scope | Out of Scope |
|---|---|
| Requirements + acceptance criteria (BA) | Architecture decisions (→ architect) |
| Sprint planning + backlog (PM/PO) | Code implementation (→ engineer) |
| QA gate enforcement G2 + G4 | Compliance gate G5 (→ compliance) |
| BDD scenario authoring | Provenance records (→ auditor) |
| Product discovery + prioritization | Technology strategy (→ tech_strategist) |