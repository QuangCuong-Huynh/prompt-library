---
artifact_id: "019cdca8-9128-7dc4-a839-2f8ff6c17775"
doc_id: "CSCF-KB-ASTRO-ARCH-20260309-01"
name:        "Knowledge Domain Library — Astro-Data Architect v2.2"
version: "2.2.0"

authority_official:
  owner:       "Quang Cuong Huynh"
  declaration: "Registered — Quang Cuong Huynh"
  assistants:
    - "Claude (Anthropic)"
  reviewer:    "Quang Cuong Huynh"
status: "active"
dc:
  title: "Knowledge Domain Library — Astro-Data Architect v2.2"
  type: "kb"
  date: "2026-03-10"
  subject: ["astrophysics","data-architecture","space-systems","ISRU","materials-science"]
changes:
  - version: "2.1.0"
    date: "2026-03-10"
    author: "Quang Cuong Huynh"
    summary: "Added memory block"
    type: "amend"
  - version: "2.2.0"
    date: "2026-03-10"
    author: "Quang Cuong Huynh"
    summary: "Full enrichment: Tier 2 expanded, Tier 5 added, plausibility framework, data pipeline standards"
    type: "amend"
sha256: "PENDING"
---
# Knowledge Domain Library — Astro-Data Architect
> ISCO-08: 2111 | RIASEC: I-R-A | Ni→Ti→Ne | OCEAN: O:10 C:8 E:3 A:5 N:2
> **Load at session start. Cite as:** `[KB: astro_data_architect_v2.0_kb § T{N}/{Section}]`

---

## Tier 1 — Primary Astronomical Data Sources

| Source | Domain | Access | Quality |
|---|---|---|---|
| NASA ADS (Astrophysics Data System) | All peer-reviewed astronomy | ui.adsabs.harvard.edu | T1 — authoritative index |
| arXiv astro-ph | Preprints — latest research | arxiv.org/list/astro-ph | T2 — not yet peer-reviewed |
| ESA Gaia Archive (DR3) | Stellar astrometry + photometry 1.8B stars | gea.esac.esa.int | T1 — mission data |
| MAST — JWST/HST | Space telescope pipeline data | mast.stsci.edu | T1 — mission data |
| SDSS DR18 | Galaxy/quasar spectroscopy surveys | sdss.org | T1 — calibrated |
| IAU Minor Planet Center | Solar system small bodies | minorplanetcenter.net | T1 — authoritative |
| SIMBAD / VizieR (CDS Strasbourg) | Astronomical object database | simbad.u-strasbg.fr | T1 — curated |
| NASA Exoplanet Archive | Confirmed + candidate exoplanets | exoplanetarchive.ipac.caltech.edu | T1 — curated |
| Chandra Data Archive | X-ray astronomy | cxc.harvard.edu/cda | T1 — mission data |
| LIGO Open Science Center | Gravitational wave strain data | gw-openscience.org | T1 — mission data |
| NASA NTRS | Technical reports, mission design | ntrs.nasa.gov | T1 — NASA official |

---

## Tier 2 — Scientific Journals & Methods

### Core Journals (peer-reviewed)
| Journal | Publisher | Impact Factor (est.) | Scope |
|---|---|---|---|
| The Astrophysical Journal (ApJ) | AAS | ~5.8 | Observational + theoretical |
| ApJ Supplement (ApJS) | AAS | ~10.2 | Data-heavy surveys, catalogs |
| Monthly Notices RAS (MNRAS) | RAS / OUP | ~5.2 | All astronomy + astrophysics |
| Astronomy & Astrophysics (A&A) | EDP Sciences | ~6.2 | European astronomy community |
| Nature Astronomy | Nature | ~14.1 | High-impact discoveries |
| The Astronomical Journal (AJ) | AAS | ~3.8 | Observational, astrometry |
| Icarus | Elsevier | ~3.2 | Planetary science |
| Acta Astronautica | Elsevier | ~3.5 | Space engineering |

### Data Analysis Methodologies
| Method | Application | Reference |
|---|---|---|
| Bayesian inference | Parameter estimation, model selection | MacKay, *Information Theory* (Cambridge, 2003) |
| Markov Chain Monte Carlo (MCMC) | Posterior sampling | emcee Python library; Foreman-Mackey et al. 2013 |
| Gaussian Process Regression | Time-series fitting, interpolation | scikit-learn; Rasmussen & Williams (MIT Press, 2006) |
| PCA / ICA | Dimensionality reduction | Ivezić et al. 2014 — SDSS method |
| Lomb-Scargle Periodogram | Unequally spaced time-series | Astropy implementation |
| Source Extraction (SExtractor) | Photometry, source detection | Bertin & Arnouts 1996 |
| Cross-matching (TOPCAT/CDS Xmatch) | Multi-catalog correlation | VizieR tools |

### Space Systems Engineering Standards
| Standard | Body | Domain |
|---|---|---|
| ECSS-E-ST-10 | ESA | Space engineering — system engineering |
| NASA NPR 7120.5 | NASA | Program and project management |
| AIAA S-114 | AIAA | Mass properties |
| NASA-STD-5001 | NASA | Structural design for spaceflight hardware |
| SMAD (Space Mission Analysis and Design) | Larson & Wertz | Mission design bible |

---

## Tier 3 — Technical References

| Topic | Reference | Notes |
|---|---|---|
| Stellar Physics | Carroll & Ostlie — *Introduction to Modern Astrophysics* (2nd ed.) | Standard undergraduate text |
| Cosmology | Ryden — *Introduction to Cosmology* (2nd ed., Cambridge) | Accessible + rigorous |
| Data Analysis | Ivezić et al. — *Statistics, Data Mining, and Machine Learning in Astronomy* (Princeton) | Python-heavy, AstroML library |
| Python ecosystem | Astropy collaboration — astropy.org | Core astronomical Python library |
| FITS format | NASA FITS standard — fits.gsfc.nasa.gov | Data format for all astronomy |
| ISRU Materials | NRL/Advanced Materials for Space Systems manuscript (CSCF internal) | T1–T5 plausibility classification |
| Orbital Mechanics | Curtis — *Orbital Mechanics for Engineering Students* (3rd ed.) | Mission analysis |
| Astrodynamics | Bate, Mueller, White — *Fundamentals of Astrodynamics* | Classic reference |

---

## Tier 4 — Epistemic Plausibility Framework (ARCH-COG-SCI-V2.0 + Space Extension)

```
[T1-ESTABLISHED]        — Current operational, peer-reviewed, replicated
                          Examples: ISS operations, JWST data, Gaia catalog
[T2-NEAR-TERM]          — 5–15 year horizon, funded programs, TRL ≥ 6
                          Examples: Artemis lunar surface, NTP propulsion demos
[T3-MID-TERM]           — 15–50 year horizon, credible extrapolation, TRL 3–5
                          Examples: orbital habitats, asteroid mining infrastructure
[T4-FAR-FUTURE]         — 50–100 year horizon, physics allows but no roadmap
                          Examples: large-scale terraforming, crewed Mars colonies
[T5-HIGHLY-SPECULATIVE] — Beyond current physics consensus or requires unknown
                          Examples: FTL travel, reactionless drives, exotic matter
```

**Auto-apply rule:** Every technical claim in outputs MUST carry one of these labels.
**Anti-hallucination:** Never claim T1 for items only warranting T3+.

---

## Tier 5 — Search Queries

```
# Current discoveries
"JWST latest 2025 discovery exoplanet atmosphere composition"
"Gaia DR3 stellar kinematics galactic archaeology"
"gravitational wave detection O4 run LIGO Virgo KAGRA"
"arXiv astro-ph most cited papers 2025"

# Mission planning
"NASA Artemis lunar surface operations architecture 2026"
"nuclear thermal propulsion NTP space mission TRL 2024"
"lunar gateway ESA NASA assembly schedule"
"SpaceX Starship orbital refueling architecture"

# Data methods
"MCMC parameter estimation astrophysics emcee tutorial"
"Astropy FITS tables photometry pipeline example"
"Lomb-Scargle periodogram exoplanet transit detection"
"machine learning galaxy classification convolutional neural"

# Materials/ISRU
"in-situ resource utilization lunar regolith processing 2024"
"refractory high entropy alloys space radiation resistance"
"carbon-carbon composite re-entry vehicle thermal protection"
```

---

## Domain Boundaries (Anti-Drift)

| Query Type | Route To |
|---|---|
| Space narrative / fiction | Space Commander / Lore Weaver |
| Engineering implementation | Engineer |
| Data infrastructure code | Engineer |
| **Astrophysics data, mission design, materials science, ISRU, observational analysis** | **Astro-Data Architect ← HERE** |

---

## Memory & Logging Auto-Protocol

```yaml
memory_protocol:
  policy_ref: "governance/MEMORY_LOGGING_POLICY.md"
  l1_log: "memory/logs/astro_data_architect_v2.0/{session_id}.jsonl"
  l2_log: "memory/shared/{project_id}/cooperative.jsonl"
  l3_permanent: "memory/decisions/{project_id}/"
  auto_log_events: [session_start, kb_access, ratified_output, scope_violation]
  pii_policy: redact_before_write
  secrets_policy: never_log
  l3_mutability: WORM
```

**Auto-apply rules:**
1. Every technical claim: `[T1-ESTABLISHED]` through `[T5-HIGHLY-SPECULATIVE]`
2. Log KB access: `[KB: astro_data_architect_v2.0_kb § T{N}/{Section}]`
3. Never mix T-tiers without declaration
4. Data claims: cite source catalog + data release version