---
artifact_id: "019cdca8-9131-7713-b441-6c6f55958444"
doc_id: "CSCF-KB-PM-BA-20260310-01"
name:        "Knowledge Domain Library — Project Manager & Business Analyst"
version: "1.1.0"

authority_official:
  owner:       "Quang Cuong Huynh"
  declaration: "Registered — Quang Cuong Huynh"
  assistants:
    - "Claude (Anthropic)"
  reviewer:    "Quang Cuong Huynh"
status: "active"
persona: "pm_ba_v1.0"
dc:
  type:     "kb"
  title: "Knowledge Domain Library — Project Manager & Business Analyst"
  date: "2026-03-10"
sha256: "PENDING"

changes:
  - version: "1.1.0"
    date:    "2026-03-08"
    author:  "Quang Cuong Huynh"
    summary: "Initial version"
    type:     "kb"
  - version: "1.1.0"
    date:    "2026-03-11"
    author:  "Quang Cuong Huynh"
    summary: "UAS v1.2 compliance fix"
    type:     "kb"
---
# Knowledge Domain Library — PM / BA v1.0

> ISCO-08: 2421 | RIASEC: E-S-C | Te→Si→Ni | OCEAN: O:7 C:9 E:7 A:8 N:2

---

## Tier 1 — Authoritative Standards

### Project Management
- PMBOK Guide 7th Edition (PMI, 2021) — 12 principles, 8 performance domains
- PRINCE2 7th Edition (Axelos, 2023) — 7 principles, themes, processes
- ISO 21500:2021 — Project, programme and portfolio management
- PMI Agile Practice Guide (2017) — agile + hybrid delivery
- Scrum Guide (Schwaber & Sutherland, 2020) — official Scrum framework

### Business Analysis
- BABOK v3 (IIBA, 2015) — 6 knowledge areas, 50 techniques
- Business Process Model and Notation (BPMN 2.0) — OMG standard
- UML 2.5.1 — use cases, activity diagrams, sequence diagrams
- IEEE 29148:2018 — Requirements engineering
- ISO/IEC/IEEE 29148:2018 — Systems and software requirements

### Agile Frameworks
- SAFe 6.0 (Scaled Agile Framework) — PI Planning, ARTs, Lean portfolio
- LeSS (Large-Scale Scrum) — scaling guide
- Kanban Method (Anderson) — WIP limits, flow metrics
- OKR framework (Doerr — *Measure What Matters*)

---

## Tier 2 — Techniques & Templates

### Requirements
- User Story format: "As a [role], I want [feature], so that [benefit]"
- Acceptance Criteria: Given/When/Then (Gherkin)
- MoSCoW prioritization: Must / Should / Could / Won't
- Story mapping (Jeff Patton)
- Event storming (Alberto Brandolini) — domain discovery

### Estimation
- Story points + Planning Poker (relative sizing)
- T-shirt sizing (XS/S/M/L/XL)
- Three-point estimation: O + 4M + P / 6 (PERT)
- Velocity tracking + burn-down / burn-up charts

### Stakeholder Management
- RACI matrix (Responsible, Accountable, Consulted, Informed)
- Stakeholder register + power/interest grid
- Change request process: CR form → impact assessment → approval → implement

### Risk Management
- Risk register: ID, description, likelihood (1–5), impact (1–5), score, mitigation, owner
- Risk heat map (5×5 matrix)
- RAID log: Risks, Assumptions, Issues, Dependencies

---

## Tier 3 — Books

- Cohn, Mike — *User Stories Applied* (Addison-Wesley, 2004)
- Patton, Jeff — *User Story Mapping* (O'Reilly, 2014)
- DeMarco & Lister — *Peopleware* (3rd ed.) — team dynamics
- Brooks, Fred — *The Mythical Man-Month* — schedule estimation
- Reinertsen, Donald — *The Principles of Product Development Flow*
- Gothelf & Seiden — *Lean UX* (3rd ed., O'Reilly)

---

## Tier 4 — Tools

| Tool | Purpose |
|---|---|
| Jira / Linear / Azure DevOps | Backlog + sprint management |
| Confluence / Notion | Documentation + requirements |
| Miro / FigJam | Story mapping, event storming |
| Lucidchart / draw.io | BPMN, process diagrams |
| Excel / Google Sheets | RAID log, stakeholder register |
| Slack / Teams | Stakeholder comms |

---

## Tier 5 — Search Queries

```
PMBOK 7th edition "{knowledge area}" best practice
BABOK v3 "{technique}" template example
SAFe PI planning "{artifact}" guide
Gherkin acceptance criteria "{domain}" example
Agile estimation "{technique}" when to use
```

---

## Domain Boundaries (Anti-Drift)

| Query Type | Route To |
|---|---|
| Technical architecture | Architect |
| Code implementation | Engineer |
| Compliance risk | Compliance Gatekeeper |
| IP rights | AI Custodian |
| **Sprint planning, requirements, stakeholder, estimation, RAID** | **PM/BA ← HERE** |

---

## Memory & Logging Auto-Protocol

**This section is machine-read by the agent at session start.**

```yaml
memory_protocol:
  l1_log: "memory/logs/{agent_id}/{session_id}.jsonl"
  l2_log: "memory/shared/{project_id}/cooperative.jsonl"
  l3_permanent: "memory/decisions/{project_id}/"
  auto_log_events:
    - session_start
    - kb_access         # log: kb_file + section + query
    - gate_decision     # log: gate + verdict + rationale → L2
    - ratified_output   # log: doc_id + sha256 → L1 + L3
    - scope_violation   # log: attempted_action + routed_to → L1
  pii_policy: redact_before_write
  secrets_policy: never_log
  l3_mutability: WORM   # amend via superseding doc only
```

### Mandatory Auto-Apply Rules
1. Log KB access immediately on read: `[KB: {this_file} § {section}]`
2. Never fabricate content not present in this file — label `[NOT IN KB — VERIFY]`
3. Cite tier on every claim: `[T1-ESTABLISHED]` through `[T5-SPECULATIVE]` where applicable
4. All gate verdicts: **PASS / CONDITIONAL / FAIL** — no other strings accepted
5. Scope violations routed silently + logged — never answered outside role boundary


### DORA Four Key Metrics (Auto-Track per Sprint)

| Metric | Elite Performer | High | Medium | Low |
|---|---|---|---|---|
| Deployment Frequency | Multiple/day | Weekly | Monthly | < Monthly |
| Lead Time for Changes | < 1 hour | < 1 week | 1-6 months | > 6 months |
| Change Failure Rate | 0–5% | 5–10% | 10–15% | > 15% |
| Time to Restore Service | < 1 hour | < 1 day | < 1 week | > 1 week |

Report DORA metrics in every sprint retrospective. Cite: `[DORA-{metric_name}]`

### OKR Structure (Auto-Apply for Quarterly Planning)
```
Objective: Qualitative, inspirational, time-bound (1 quarter)
  Key Result 1: Measurable, 0→100% scale, owner assigned
  Key Result 2: Measurable, 0→100% scale, owner assigned
  Key Result 3: Measurable, 0→100% scale, owner assigned

OKR grading: 0.0–0.4 = Failed | 0.5–0.7 = Partial | 0.7–1.0 = Success
"Stretch goal" OKRs: 0.7 = success (not 1.0) — maintains ambition
```

### Sprint Health Metrics (Auto-Report)
```
Velocity: story points completed / planned (target: 80-90%)
Scope creep: new stories added mid-sprint (target: < 10%)
Bug escape rate: defects found in prod / total defects (target: < 5%)
Sprint goal met: binary Y/N (target: 85%+ over rolling 6 sprints)
```