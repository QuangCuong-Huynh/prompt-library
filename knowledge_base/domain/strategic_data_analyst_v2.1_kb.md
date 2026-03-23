---
artifact_id: "019cdca8-9136-76b1-a706-73ea34501234"
doc_id: "CSCF-KB-SDA-20260309-01"
name:        "Knowledge Domain Library — Strategic Data Analyst v2.3"
version: "2.3.0"

authority_official:
  owner:       "Quang Cuong Huynh"
  declaration: "Registered — Quang Cuong Huynh"
  assistants:
    - "Claude (Anthropic)"
  reviewer:    "Quang Cuong Huynh"
status: "active"
dc:
  title: "Knowledge Domain Library — Strategic Data Analyst v2.3"
  type: "kb"
  date: "2026-03-10"
  subject: ["strategic-analysis","data-analytics","geopolitics","forecasting","decision-science"]
changes:
  - version: "2.2.0"
    date: "2026-03-10"
    author: "Quang Cuong Huynh"
    summary: "Added memory block"
    type: "amend"
  - version: "2.3.0"
    date: "2026-03-10"
    author: "Quang Cuong Huynh"
    summary: "Full enrichment: analytical methods, forecasting protocols, Tier 5, epistemic labeling"
    type: "amend"
sha256: "PENDING"
---
# Knowledge Domain Library — Strategic Data Analyst
> ISCO-08: 2120 | RIASEC: I-E-C | Ni→Te→Ti | OCEAN: O:8 C:9 E:5 A:5 N:2
> **Load at session start. Cite as:** `[KB: strategic_data_analyst_v2.1_kb § T{N}/{Section}]`

---

## Tier 1 — Authoritative Data Sources

| Source | Domain | Access | Quality |
|---|---|---|---|
| IMF World Economic Outlook (WEO) | Global macroeconomics | imf.org/weo | T1 — biannual |
| World Bank Open Data | Development economics, poverty | data.worldbank.org | T1 — curated |
| OECD Statistics | Policy, economics, education | stats.oecd.org | T1 — OECD members |
| SIPRI Databases | Defense expenditure, arms transfers | sipri.org/databases | T1 — Stockholm Institute |
| UN Comtrade | International trade flows | comtrade.un.org | T1 — UN official |
| FRED (Federal Reserve St. Louis) | Financial, monetary, macro | fred.stlouisfed.org | T1 — Fed official |
| Our World in Data | Cross-domain synthesis, long-run data | ourworldindata.org | T2 — derived from T1 |
| V-Dem Institute | Democracy indices | v-dem.net | T1 — academic |
| Fraser Institute Economic Freedom Index | Economic freedom metrics | fraserinstitute.org | T2 — methodological debate |
| Freedom House | Political rights, civil liberties | freedomhouse.org | T2 — methodological debate |
| BIS Statistics | Banking, payments, derivatives | bis.org/statistics | T1 — Bank for Int'l Settlements |

---

## Tier 2 — Strategic & Analytical Frameworks

### Strategic Frameworks
| Framework | Use Case | Inventor / Source |
|---|---|---|
| Porter's Five Forces | Industry competitive structure | Porter, *Competitive Strategy* (1980) |
| PESTEL Analysis | Macro environment scanning | Aguilar (1967) — updated to PESTEL |
| SWOT Matrix | Strategic position | Andrews et al. (Harvard, 1960s) |
| Scenario Planning (2×2 Matrix) | Futures forecasting under uncertainty | Shell Strategic Planning Unit (1970s) |
| Game Theory (Nash Equilibrium) | Strategic interaction modeling | Nash (1950); Dixit & Nalebuff, *Thinking Strategically* |
| Diffusion of Innovations | Technology adoption S-curve | Rogers (1962) — 5th ed. 2003 |
| Gartner Hype Cycle | Technology maturity | Fenn & Raskino (Gartner, 2008) |
| McKinsey 7-S | Organizational change | Peters & Waterman (1982) |
| Blue Ocean Strategy | Market creation vs. competition | Kim & Mauborgne (2004) |
| Cynefin Framework | Decision complexity domains | Snowden & Boone (HBR, 2007) |

### Analytical Methods
| Method | Application | Tool |
|---|---|---|
| Regression analysis | Causal inference, forecasting | Python statsmodels, R lm() |
| Time-series forecasting | Economic trends, demand | Prophet, ARIMA, statsmodels |
| Cluster analysis | Segmentation, pattern detection | scikit-learn KMeans, DBSCAN |
| Network analysis | Influence mapping, supply chains | NetworkX (Python), Gephi |
| Monte Carlo simulation | Uncertainty quantification | numpy random, SciPy |
| Geospatial analysis | Regional comparisons, logistics | geopandas, Folium, QGIS |
| Sentiment analysis | Policy/market narrative | VADER, transformers (HF) |
| Comparative statics | Policy impact modeling | Mathematical economics |

### Epistemic Quality Standards for Analysis
```
CONFIDENCE LEVELS (must label every forecast):
  HIGH (>80%):   Multiple T1 sources converge; methodology validated
  MEDIUM (50-80%): T1+T2 mix; methodology sound; some uncertainty
  LOW (<50%):    T2/T3 sources only; methodology contested; label [HYPOTHESIS]
  SPECULATIVE:   No T1 basis; label [SPECULATION] explicitly

ANALYTICAL INTEGRITY RULES:
  - Never present T2/T3 estimates as T1 facts
  - Disclose conflicting evidence — do not cherry-pick sources
  - Label all forecasts with horizon: ST=0-2yr / MT=2-10yr / LT=10yr+
  - Acknowledge base rate before presenting scenario probability
```

---

## Tier 3 — Canonical Books & Academic Sources

1. **Kahneman, Daniel** — *Thinking, Fast and Slow* (FSG, 2011) — cognitive bias, dual-process theory
2. **Silver, Nate** — *The Signal and the Noise* (Penguin, 2012) — forecasting methodology
3. **Tetlock & Gardner** — *Superforecasting* (Crown, 2015) — calibrated probability estimation
4. **Diamond, Jared** — *Guns, Germs and Steel* (Norton, 1997) — comparative civilizational analysis
5. **Fukuyama, Francis** — *The Origins of Political Order* (FSG, 2011) + *Political Order and Decay* (2014)
6. **Acemoglu & Robinson** — *Why Nations Fail* (Crown, 2012) — institutional economics
7. **Taleb, Nassim Nicholas** — *The Black Swan* (Random House, 2007) — tail risk, fat tails
8. **Reinhart & Rogoff** — *This Time Is Different* (Princeton, 2009) — financial crises data
9. **Piketty, Thomas** — *Capital in the Twenty-First Century* (Harvard, 2014) — inequality data

**Key journals:** *Foreign Affairs* (CFR), *Brookings Papers*, *Journal of Economic Perspectives*, *IISS Military Balance*, *Survival* (IISS)

---

## Tier 4 — Data Tools

| Tool | Purpose | Tier |
|---|---|---|
| Python: pandas, numpy, scipy | Statistical analysis, data manipulation | Primary |
| Python: statsmodels, scikit-learn | Regression, clustering, ML | Primary |
| R: tidyverse, ggplot2 | Statistical modeling, visualization | Peer verification |
| Tableau / Power BI | Executive dashboards, KPI visualization | Presentation |
| SQL (PostgreSQL / BigQuery) | Large dataset querying | Primary |
| NetworkX + Gephi | Graph analysis, network mapping | Specialist |
| Prophet (Meta) | Time-series forecasting with seasonality | Forecasting |
| QGIS / geopandas | Geospatial analysis | Specialist |
| Obsidian / Notion | Strategic knowledge management | Personal |

---

## Tier 5 — Search Queries

```
# Macro data
"IMF World Economic Outlook 2025 GDP forecast Southeast Asia"
"World Bank poverty headcount ratio Vietnam 2024"
"SIPRI military expenditure Asia Pacific 2024"
"FRED US interest rate inflation PCE 2025"

# Strategy & frameworks
"scenario planning 2x2 matrix methodology example"
"Porter five forces digital platform economy application"
"Cynefin framework complex adaptive systems decision making"
"superforecasting calibration scoring Brier score methodology"

# Analytics
"Python statsmodels OLS regression interpretation"
"time series forecasting Prophet vs ARIMA comparison 2024"
"network analysis geopolitical influence mapping methodology"
"Monte Carlo simulation risk analysis Python numpy"

# Geopolitics / SEA focus
"Southeast Asia economic integration ASEAN 2025 trade"
"Vietnam economic development FDI inflows 2025"
"Mekong River geopolitics China downstream countries"
```

---

## Domain Boundaries (Anti-Drift)

| Query Type | Route To |
|---|---|
| Code implementation | Engineer |
| Compliance audit | Compliance Gatekeeper |
| Lore / alternate history | Creative Director / Lore Weaver |
| **Data analysis, strategic frameworks, geopolitical analysis, forecasting, economic modeling** | **Strategic Analyst ← HERE** |

---

## Memory & Logging Auto-Protocol

```yaml
memory_protocol:
  policy_ref: "governance/MEMORY_LOGGING_POLICY.md"
  l1_log: "memory/logs/strategic_data_analyst_v2.1/{session_id}.jsonl"
  l2_log: "memory/shared/{project_id}/cooperative.jsonl"
  l3_permanent: "memory/decisions/{project_id}/"
  auto_log_events: [session_start, kb_access, ratified_output, scope_violation]
  pii_policy: redact_before_write
  secrets_policy: never_log
  l3_mutability: WORM
```

**Auto-apply rules:**
1. Label confidence on every forecast: HIGH / MEDIUM / LOW / SPECULATIVE
2. Label time horizon: ST / MT / LT
3. Cite T1 sources; flag T2/T3 with `[SECONDARY-SOURCE]`
4. Log KB access: `[KB: strategic_data_analyst_v2.1_kb § T{N}/{Section}]`