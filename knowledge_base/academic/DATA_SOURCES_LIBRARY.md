---
artifact_id: "019cdca8-9123-79bd-a673-951fb9e7e373"
doc_id: "KB-CSCF-DATASRC-20260308-01"
name:        "Strategic Data Analyst — Data Sources Library"
version: "1.0.0"

authority_official:
  owner:       "Quang Cuong Huynh"
  declaration: "Registered — Quang Cuong Huynh"
  assistants:
    - "Claude (Anthropic)"
  reviewer:    "Quang Cuong Huynh"
status: "active"
migrated_from: "STRATEGIC-DATA-ANALYST-DATA SOURCES LIBRARY.docx"
migrated_at: "2026-03-08"
dc:
  title: "Strategic Data Analyst — Data Sources Library"
  type: "kb"
  subject: ["economics","geopolitics","finance","social-science","legal","data-sources"]
  date: "2026-03-08"
sha256: "PENDING"

changes:
  - version: "1.0.0"
    date:    "2026-03-11"
    author:  "Quang Cuong Huynh"
    summary: "UAS v1.2 compliance fix"
    type:    "fix"
---
# Strategic Data Analyst — Data Sources Library

*Authoritative data sources for `strategic_data_analyst_v2.1`, `tech_strategist_v1.0`, `strategic_analyst_v1.0`.*

---

## Economic & Financial Sources

| Source | Category | Access | Trust | URL |
|---|---|---|---|---|
| World Bank Open Data | Macro indicators | Public | Authoritative | data.worldbank.org |
| IMF Data | Economic/financial stats | Public | Authoritative | imf.org/en/Data |
| OECD Data | Economic/social/innovation | Public | Authoritative | data.oecd.org |
| Bloomberg Terminal | Financial markets | Licensed | Authoritative | — |
| Statista | Market/industry | Public/paid | High | statista.com |
| FRED (St. Louis Fed) | US macroeconomic series | Public | Authoritative | fred.stlouisfed.org |
| BIS Statistics | Banking/financial stability | Public | Authoritative | bis.org/statistics |
| Eurostat | EU economic statistics | Public | Authoritative | ec.europa.eu/eurostat |

---

## Geopolitics, Diplomacy & Security

| Source | Category | Trust |
|---|---|---|
| UN Data Portal | Global governance, treaties | Authoritative |
| CIA World Factbook | Country profiles | Authoritative |
| Correlates of War (COW) | Historical conflict data | Authoritative |
| Polity IV / V-Dem | Democracy indices | Authoritative |
| Freedom House | Political freedom | Authoritative |
| SIPRI | Arms, military expenditure | Authoritative |
| ICJ / International Court | Legal rulings | Authoritative |
| WTO Dispute Settlement | Trade law | Authoritative |

---

## Technology & Innovation

| Source | Category | Trust |
|---|---|---|
| OECD STI Outlook | Science/tech/innovation | Authoritative |
| USPTO / EPO / WIPO | Patent data | Authoritative |
| Gartner Research | Technology trends | High |
| IDC Research | Market sizing | High |
| IEEE Xplore | Technical publications | Authoritative |
| GitHub Octoverse | Developer/open-source trends | High |
| Stack Overflow Developer Survey | Developer ecosystem | High |

---

## Academic & Research Databases

| Source | Scope | Cluster (SEARCH_METHODS_LIBRARY) |
|---|---|---|
| JSTOR | Social sciences, humanities | C1 |
| SSRN | Economics, law, finance preprints | C2 |
| NBER Working Papers | Economics research | C2 |
| ProQuest Dissertations | Graduate research | C2 |
| Semantic Scholar | Cross-domain AI-indexed | C5 |
| Dimensions.ai | Research analytics | C5 |
| Our World in Data | Curated global indicators | High |

---

## Legal & Regulatory

| Source | Scope | Trust |
|---|---|---|
| EUR-Lex | EU law & legislation | Authoritative |
| LexisNexis / Westlaw | Case law (licensed) | Authoritative |
| UN Treaty Collection | International agreements | Authoritative |
| OECD Tax Database | Tax policy | Authoritative |
| WTO Legal Texts | Trade agreements | Authoritative |

---

## Citation Format

All sources cited as: `[Source Name, Year, Report/Dataset Title, URL or DOI]`

**Trust hierarchy:** Authoritative > High > Medium (use with caveats) > Low (avoid)

**Anti-patterns to avoid:**
- Wikipedia as primary source
- Unattributed blog posts or opinion pieces
- Undated datasets
- Sources without methodology disclosure