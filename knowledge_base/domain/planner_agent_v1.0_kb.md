---
artifact_id: "019cdca8-9131-7e30-a9fd-c7dd0b702b53"
doc_id: "CSCF-KB-PLANNER-20260310-01"
name:        "Knowledge Domain Library — Planner Agent"
version: "1.0.0"

authority_official:
  owner:       "Quang Cuong Huynh"
  declaration: "Registered — Quang Cuong Huynh"
  assistants:
    - "Claude (Anthropic)"
  reviewer:    "Quang Cuong Huynh"
status: "active"
persona: "planner_agent_v1.0"
dc:
  type:     "kb"
  title: "Knowledge Domain Library — Planner Agent"
  date: "2026-03-10"
changes:
  - version: "1.0.0"
    date: "2026-03-10"
    author: "Quang Cuong Huynh"
    summary: "Sprint 4 — initial KB creation"
    type:     "kb"
sha256: "PENDING"
---
# Knowledge Domain Library — Planner Agent v1.0

> ISCO-08: 2421 | RIASEC: E-C-I | Ni→Te→Si | OCEAN: O:8 C:9 E:7 A:7 N:1

---

## Tier 1 — Authoritative Standards

### Planning Frameworks
- PMI PMBOK Guide 7th Edition (2021) — 12 principles, performance domains
- SAFe 6.0 — PI Planning, Feature decomposition, Release Train Engineer role
- Scrum Guide (Schwaber & Sutherland, 2020) — sprint planning, velocity
- PRINCE2 7th Edition (2023) — stage planning, work packages
- ISO 21500:2021 — Guidance on project management

### Task Decomposition
- Work Breakdown Structure (WBS) — MIL-STD-881 / PMI standard
- Critical Path Method (CPM) — network diagram scheduling
- PERT (Program Evaluation and Review Technique) — 3-point estimation
- Function Point Analysis (IFPUG) — effort sizing
- Story Points + Planning Poker (Cohn, 2005)

### Dependency Management
- Sequencing types: FS / FF / SS / SF (Finish-to-Start / etc.)
- Lag and lead time modeling
- Critical chain method (Goldratt, *Critical Chain*, 1997)
- Kanban dependency mapping

---

## Tier 2 — Techniques & Protocols

### Sprint Planning Protocol (Auto-Apply in GAP Pipeline)
Every planner output MUST include:

| Artifact | Format | Destination |
|---|---|---|
| Task Graph | Mermaid gantt/DAG | L2 broadcast |
| Agent Assignments | YAML role→task map | agents/{id}/AGENT.md |
| Dependency List | FS/FF/SS/SF pairs | workflow YAML |
| Risk Register (initial) | RAID log | specs/feature_spec |
| Definition of Done | Checklist | gate criteria |

### Task Decomposition Hierarchy
```
Epic → Feature → User Story → Task → Sub-task
  Epic: 3–6 months | Feature: sprint | Story: 1–3 days | Task: 2–8h
```

### Agent Assignment Matrix
| Stage | Primary Agent | Backup | Gate Authority |
|---|---|---|---|
| S0 Spec | planner | pm_ba | G1: reviewer |
| S1 Requirements | pm_ba | planner | G2: reviewer |
| S2 Architecture | architect | engineer | G3: reviewer |
| S3 Implementation | engineer | architect | G4: qa_director |
| S4 Release Prep | auditor + compliance | — | G5: compliance |

### Estimation Models
- Story points: Fibonacci scale (1,2,3,5,8,13,21)
- Three-point: `E = (O + 4M + P) / 6` where O=optimistic, M=most likely, P=pessimistic
- T-shirt sizing: XS=0.5d, S=1d, M=3d, L=5d, XL=10d
- Velocity baseline: use team's last 3 sprint average

---

## Tier 3 — Books & Papers

- Goldratt, Eli — *Critical Chain* (1997) — constraint-based scheduling
- DeMarco & Lister — *Peopleware* (3rd ed.) — team capacity planning
- Reinertsen, Donald — *The Principles of Product Development Flow* (2009)
- Sutherland, Jeff — *Scrum: The Art of Doing Twice the Work in Half the Time*
- Cohn, Mike — *Agile Estimating and Planning* (Addison-Wesley, 2005)

---

## Tier 4 — Tools

| Tool | Purpose |
|---|---|
| Jira / Azure DevOps | Sprint board + backlog management |
| Mermaid.js | DAG / Gantt chart generation |
| draw.io | Architecture + dependency diagrams |
| MS Project / SmartSheet | Gantt + resource scheduling |
| Linear | Modern issue tracking |
| GitHub Projects | Kanban + milestone tracking |

---

## Tier 5 — Search Queries

- "PI planning SAFe 6.0 feature decomposition"
- "WBS work breakdown structure best practices PMI"
- "critical path method CPM calculation example"
- "sprint velocity estimation story points Fibonacci"
- "PERT three-point estimation project management"
- "multi-agent pipeline task graph dependency mapping"

---

## Domain Boundaries

| In Scope | Out of Scope |
|---|---|
| Task decomposition and assignment | Requirements elicitation (→ pm_ba) |
| Pipeline stage sequencing | Architecture decisions (→ architect) |
| Sprint planning + velocity | Quality verification (→ qa_director) |
| L2 broadcast of task graph | Compliance judgments (→ compliance) |
| Initial risk identification | Compliance gate authority (→ G5) |