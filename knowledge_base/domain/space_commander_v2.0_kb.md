---
artifact_id: "019cdca8-9135-7e2c-b92c-4be477e64e2c"
doc_id: "CSCF-KB-SPACE-CMD-20260309-01"
name:        "Knowledge Domain Library — Space Commander v2.2"
version: "2.2.0"

authority_official:
  owner:       "Quang Cuong Huynh"
  declaration: "Registered — Quang Cuong Huynh"
  assistants:
    - "Claude (Anthropic)"
  reviewer:    "Quang Cuong Huynh"
status: "active"
dc:
  title: "Knowledge Domain Library — Space Commander v2.2"
  type: "kb"
  date: "2026-03-10"
  subject: ["space-exploration","mission-design","astrodynamics","human-spaceflight","propulsion"]
changes:
  - version: "2.1.0"
    date: "2026-03-10"
    author: "Quang Cuong Huynh"
    summary: "Added memory block"
    type: "amend"
  - version: "2.2.0"
    date: "2026-03-10"
    author: "Quang Cuong Huynh"
    summary: "Full enrichment: Tier 1 expanded, propulsion matrix, abort decision tree, Tier 5"
    type: "amend"
sha256: "PENDING"
---
# Knowledge Domain Library — Space Commander
> ISCO-08: 0110 | RIASEC: R-I-E | Te→Ni→Se | OCEAN: O:7 C:9 E:6 A:5 N:1
> **Load at session start. Cite as:** `[KB: space_commander_v2.0_kb § T{N}/{Section}]`

---

## Tier 1 — Authoritative Mission References

| Source | Domain | Access | Quality |
|---|---|---|---|
| NASA Technical Reports Server (NTRS) | All space technology | ntrs.nasa.gov | T1 — NASA official |
| ESA Technical Memoranda & publications | European space technology | esamultimedia.esa.int | T1 — ESA official |
| AIAA Journal / Journal of Spacecraft & Rockets | Aerospace engineering | aiaa.org | T1 — peer-reviewed |
| Acta Astronautica | Space systems engineering | Elsevier / IAA | T1 — peer-reviewed |
| IAU resolutions & definitions | Astronomical standards | iau.org | T1 — authoritative |
| NASA Human Integration Design Handbook | Human factors, EVA | NASA SP-2010-3407 | T1 — NASA official |
| CCSDS (Consultative Committee for Space Data Systems) | Space communications | ccsds.org | T1 — standards body |
| Space Mission Analysis and Design (SMAD) | Mission design handbook | Larson & Wertz (Microcosm) | T1 — canonical text |
| NASA NPR 7120.5 | Program/project management | nodis.nasa.gov | T1 — NASA procedural |

---

## Tier 2 — Mission Design & Systems Engineering

### Propulsion Technology Matrix
| System | ISP (s) | TRL (2025) | Best Use Case | T-Tier |
|---|---|---|---|---|
| Solid rocket | 250–290 | 9 | Launch boosters, kick stages | T1 |
| Liquid biprop (LOX/LH2) | 450–465 | 9 | Upper stages (RL-10, Vulcain) | T1 |
| Liquid biprop (LOX/CH4) | 380 | 9 | Starship, Terran R | T1 |
| Ion thruster (Xenon) | 1,500–10,000 | 9 | Deep space cruise, station-keeping | T1 |
| Hall-effect thruster | 1,500–3,000 | 8–9 | Commercial GEO, lunar | T1 |
| Nuclear Thermal Propulsion (NTP) | 800–900 | 4–5 | Crewed Mars transit | T2 |
| Nuclear Electric Propulsion (NEP) | 5,000–10,000 | 3–4 | Deep space science | T2-T3 |
| Solar sail | N/A (momentum) | 6–7 | Trajectory shaping, science | T2 |
| Fusion drive | 10,000–100,000 | 2–3 | Rapid interplanetary | T3 |
| Antimatter drive | 1,000,000+ | 1 | Interstellar precursor | T4–T5 |

### Delta-V Budget Reference
```
LEO (200km circular):        ~7,800 m/s from ground
GTO injection:               ~8,900 m/s from ground
GEO:                         ~11,000 m/s from ground
Trans-Lunar Injection (TLI): ~3,130 m/s from LEO
Lunar orbit insertion:       ~900 m/s
Lunar surface landing:       ~1,870 m/s from lunar orbit
Trans-Mars Injection (TMI):  ~3,600 m/s from LEO
Mars orbit insertion:        ~900–2,000 m/s (varies)
Mars surface:                ~5,600 m/s from Mars orbit
```

### Mission Phase Framework (SMAD-aligned)
```
Phase A: Concept Study — mission objectives, constraints, feasibility
Phase B: Preliminary Design — trade studies, system architecture
Phase C: Detailed Design — CDR, full specifications
Phase D: Development & Test — build, qualification, acceptance
Phase E: Operations — launch, cruise, mission, contingency
Phase F: Disposal — deorbit, data archiving, lessons learned

Key Reviews:
  SRR (System Requirements Review)    — Phase A complete
  SDR (System Definition Review)      — Phase A/B transition
  PDR (Preliminary Design Review)     — Phase B complete
  CDR (Critical Design Review)        — Phase C complete
  MRR (Mission Readiness Review)      — Phase D/E transition
  FRR (Flight Readiness Review)       — 72h before launch
```

### Abort Decision Tree (crewed missions)
```
NOMINAL → CONTINGENCY → EMERGENCY → ABORT

Abort modes (ascending severity):
  Return-to-Launch-Site (RTLS)  — first ~2 min ascent
  Transatlantic Abort Landing (TAL) — 2–8 min ascent
  Abort-to-Orbit (ATO)          — near-nominal orbit achievable
  Abort-Once-Around (AOA)       — single orbit then land
  Abort-to-Surface (ATS)        — Mars/Moon surface contingency

Decision authority: Mission Commander (crew safety) > Flight Director (mission) > Range Safety
```

---

## Tier 3 — Canonical Texts

1. **Larson & Wertz** — *Space Mission Analysis and Design* (3rd ed., Microcosm, 1999) — **mission design bible**
2. **Curtis, Howard** — *Orbital Mechanics for Engineering Students* (3rd ed., Butterworth-Heinemann) — orbital mechanics
3. **Bate, Mueller, White** — *Fundamentals of Astrodynamics* (Dover, 1971) — astrodynamics classic
4. **Markley & Crassidis** — *Fundamentals of Spacecraft Attitude Determination and Control* (Springer, 2014)
5. **Zubrin, Robert** — *The Case for Mars* (Simon & Schuster, 1996) — Mars direct architecture
6. **Larson & Pranke** — *Human Spaceflight: Mission Analysis and Design* (McGraw-Hill, 1999)
7. **Sellers, Jerry** — *Understanding Space: An Introduction to Astronautics* (3rd ed.) — accessible overview
8. **Roach, Mary** — *Packing for Mars* (Norton, 2010) — human factors, readability
9. **von Braun, Wernher** — *The Mars Project* (1952) — historical/architectural interest

---

## Tier 4 — T1–T5 Plausibility Framework (CSCF Space Extension)

```
[T1-ESTABLISHED]         Current operational; flight-proven; in-service hardware
                         Examples: ISS systems, Falcon 9, JWST, ion thrusters
[T2-NEAR-TERM]           5–15 year horizon; funded/announced programs; TRL ≥ 5
                         Examples: Artemis lunar surface, NTP demos, Starship crewed
[T3-MID-TERM]            15–50 year horizon; credible extrapolation; TRL 2–4
                         Examples: nuclear electric interplanetary, orbital habitats, Mars colony
[T4-FAR-FUTURE]          50–100 year horizon; physics allows; no credible roadmap
                         Examples: terraforming, generation ships, laser highways
[T5-HIGHLY-SPECULATIVE]  Requires new physics or currently falsified science
                         Examples: FTL travel, reactionless drive, negative mass propulsion
```

**Rule:** All technical claims in narrative or analysis MUST carry T-tier label.
**Anti-hallucination:** Never describe T3+ technology as currently operational.

---

## Tier 5 — Search Queries

```
# Current missions
"NASA Artemis lunar surface mission status 2025 2026"
"SpaceX Starship orbital refueling test results"
"nuclear thermal propulsion NTP program NASA DARPA 2024"
"JWST science results exoplanet biosignature 2025"

# Mission design
"delta-v budget Mars mission architecture comparison"
"lunar gateway assembly sequence NASA ESA 2025"
"Hall effect thruster performance comparison commercial GEO"
"life support closed loop ECLSS ISS upgrade"

# Human spaceflight
"NASA human integration design handbook EVA protocols"
"cognitive performance degradation long duration spaceflight"
"radiation shielding Mars transit astronaut dose limits"
"artificial gravity rotating habitat design tradeoffs"

# Propulsion
"nuclear thermal propulsion ISP flight demo 2025"
"electric propulsion Hall thruster xenon efficiency"
"solar sail trajectory optimization interplanetary"
```

---

## Domain Boundaries (Anti-Drift)

| Query Type | Route To |
|---|---|
| Astrophysics data analysis | Astro-Data Architect |
| Space narrative / fiction | Lore Weaver |
| Materials science | Astro-Data Architect |
| **Mission operations, propulsion, systems engineering, crewed spaceflight, abort protocols** | **Space Commander ← HERE** |

---

## Memory & Logging Auto-Protocol

```yaml
memory_protocol:
  policy_ref: "governance/MEMORY_LOGGING_POLICY.md"
  l1_log: "memory/logs/space_commander_v2.0/{session_id}.jsonl"
  l2_log: "memory/shared/{project_id}/cooperative.jsonl"
  l3_permanent: "memory/decisions/{project_id}/"
  auto_log_events: [session_start, kb_access, ratified_output, scope_violation]
  pii_policy: redact_before_write
  secrets_policy: never_log
  l3_mutability: WORM
```

**Auto-apply rules:**
1. Every technical claim: `[T1]` through `[T5]` tier label
2. Never describe unflown technology as operational
3. Abort decisions: always cite Decision Authority chain
4. Log KB access: `[KB: space_commander_v2.0_kb § T{N}/{Section}]`