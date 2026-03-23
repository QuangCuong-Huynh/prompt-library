---
artifact_id: "019cdca8-9136-7360-bc60-655d3f6aa707"
doc_id: "CSCF-KB-TECH-STRAT-20260310-01"
name:        "Knowledge Domain Library — Technology Strategist"
version: "1.0.0"

authority_official:
  owner:       "Quang Cuong Huynh"
  declaration: "Registered — Quang Cuong Huynh"
  assistants:
    - "Claude (Anthropic)"
  reviewer:    "Quang Cuong Huynh"
status: "active"
persona: "tech_strategist_v1.0"
dc:
  type:     "kb"
  title: "Knowledge Domain Library — Technology Strategist"
  date: "2026-03-10"
changes:
  - version: "1.0.0"
    date: "2026-03-10"
    author: "Quang Cuong Huynh"
    summary: "Sprint 4 — initial KB creation"
    type:     "kb"
sha256: "PENDING"
---
# Knowledge Domain Library — Technology Strategist v1.0

> ISCO-08: 2421 | RIASEC: E-I-C | Ni→Te→Ti | OCEAN: O:9 C:8 E:8 A:6 N:1

---

## Tier 1 — Authoritative Standards

### Strategy Frameworks
- Gartner Hype Cycle (annual) — technology adoption phases
- Forrester Technology Radar — enterprise tech adoption
- ThoughtWorks Technology Radar (radar.thoughtworks.com) — quarterly
- Wardley Mapping (Simon Wardley, 2016) — value chain evolution
- Technology Readiness Levels (TRL 1–9) — NASA/ESA/EU Horizon

### Enterprise Architecture
- TOGAF 10 (The Open Group, 2022) — Architecture Development Method (ADM)
- Zachman Framework — enterprise architecture ontology
- ArchiMate 3.2 — enterprise architecture modeling language
- COBIT 2019 — governance of enterprise IT
- ITIL 4 — IT service management

### Innovation Management
- Christensen, Clayton — Disruptive Innovation Theory (*The Innovator's Dilemma*, 1997)
- Design Thinking (IDEO / Stanford d.school) — human-centered design
- Jobs-To-Be-Done (JTBD) — Christensen + Ulwick
- Open Innovation — Chesbrough (2003)
- Lean Startup — Ries (2011): Build-Measure-Learn

---

## Tier 2 — Techniques & Frameworks

### Technology Evaluation Matrix
| Criterion | Weight | Assessment Method |
|---|---|---|
| Strategic fit | 30% | Wardley position × business capability |
| Market maturity | 20% | Gartner Hype Cycle phase |
| Technical risk | 20% | TRL score + dependency analysis |
| Build vs. Buy vs. Partner | 15% | TCO model over 3 years |
| Vendor health | 15% | Gartner Magic Quadrant position |

### Wardley Mapping Stages
| Stage | Description | Strategy |
|---|---|---|
| Genesis | Novel, uncertain | Explore, experiment |
| Custom | Differentiated | Build in-house |
| Product | Commoditizing | Buy / SaaS |
| Commodity | Utility | Outsource |

### Technology Radar Rings
- ADOPT: proven, recommend for broad use
- TRIAL: worth pursuing, low risk
- ASSESS: promising, explore with a PoC
- HOLD: use with caution; avoid for new work

### Strategic Planning Cadence
- 3-year technology vision (annually reviewed)
- Annual roadmap (quarterly OKR checkpoints)
- Quarterly radar updates (ADOPT/TRIAL/ASSESS/HOLD)
- Monthly strategic review (emerging tech scan)

---

## Tier 3 — Books & Papers

- Wardley, Simon — *Wardley Maps* (2020, CC licensed — medium.com/wardleymaps)
- Christensen, Clayton — *The Innovator's Dilemma* (HBS Press, 1997)
- Moore, Geoffrey — *Crossing the Chasm* (3rd ed., 2014)
- Rogers, Everett — *Diffusion of Innovations* (5th ed., 2003)
- Brynjolfsson & McAfee — *The Second Machine Age* (2014)
- Henderson & Clark — "Architectural Innovation" (*Admin. Sci. Q.* 35, 1990)

---

## Tier 4 — Tools

| Tool | Purpose |
|---|---|
| online.wardleymaps.com | Wardley Map creation |
| Gartner Peer Insights | Vendor evaluation |
| radar.thoughtworks.com | Technology radar reference |
| Miro / Mural | Strategic workshops, mapping |
| Azure Architecture Center | Cloud strategy reference |
| CB Insights / Crunchbase | Startup / vendor intelligence |

---

## Tier 5 — Search Queries

- "Wardley mapping strategy technology evolution 2025"
- "Gartner hype cycle generative AI 2025"
- "TOGAF 10 architecture development method ADM"
- "ThoughtWorks technology radar 2025 enterprise"
- "build vs buy vs partner technology decision framework"
- "technology readiness level TRL assessment enterprise"

---

## Domain Boundaries

| In Scope | Out of Scope |
|---|---|
| 3-year technology vision | Day-to-day architecture decisions (→ architect) |
| Build/Buy/Partner decisions | Code implementation (→ engineer) |
| Technology radar maintenance | Compliance gate enforcement (→ compliance) |
| Vendor evaluation and scoring | Requirements elicitation (→ pm_ba) |
| Strategic OKR alignment | Sprint planning (→ planner) |