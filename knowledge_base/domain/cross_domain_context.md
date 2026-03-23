---
artifact_id: "019cdca8-912d-7957-8af9-dc27885947fd"
doc_id: "CSCF-KB-XDOMAIN-20260309-01"
name:        "Cross-Domain Context — Multi-Domain Strategic Knowledge Reference"
version: "1.0.0"

authority_official:
  owner:       "Quang Cuong Huynh"
  declaration: "Registered — Quang Cuong Huynh"
  assistants:
    - "Claude (Anthropic)"
  reviewer:    "Quang Cuong Huynh"
status: "active"
migrated_from: "Cross-Domain Context.docx"
migrated_at: "2026-03-09"
sha256: "PENDING"
dc:
  title: "Cross-Domain Context — Multi-Domain Strategic Knowledge Reference"
  type: "kb"
  date: "2026-03-09"
  subject: ["cross-domain","strategic-knowledge","multi-domain","research-assistant"]

changes:
  - version: "1.0.0"
    date:    "2026-03-11"
    author:  "Quang Cuong Huynh"
    summary: "UAS v1.2 compliance fix"
    type:    "fix"
---
# Cross-Domain Context — Unified Knowledge Reference

> **Purpose:** System prompt component for multi-domain research and strategic analysis agents.
> Used by: `strategic_data_analyst_v2.1`, `astro_data_architect_v2.0`, `lore_weaver_v2.0`

## Usage in System Prompts

```yaml
# In persona YAML v_structured:
knowledge_base_refs:
  - knowledge_base/domain/cross_domain_context.md

# The v_plain prompt should include:
# "You have access to the following knowledge domains:"
# [paste Domain Index section below]
```

## Domain Index

### Core Sciences
- **Mathematics**: Pure & Applied, Statistics, Computational Methods, Optimization, Information Theory
- **Physics**: Classical, Quantum, Relativity, Thermodynamics, Astrophysics, Condensed Matter
- **Chemistry**: Organic, Inorganic, Physical, Analytical, Advanced Materials, Electrochemistry
- **Biology**: Molecular, Evolutionary, Ecology, Biotechnology, Neuroscience
- **Astronomy & Space Science**: Cosmology, Celestial Mechanics, Observational Astronomy, Planetary Science, Exoplanet Research
- **Earth Sciences**: Geology, Geophysics, Climatology, Oceanography, Atmospheric Science

### Technology & Engineering
- **Computer Science**: Algorithms, Data Structures, Machine Learning, Software Architecture, Distributed Systems
- **Data Science & Engineering**: Big Data, Statistical Modelling, Data Pipelines, Cloud Platforms, MLOps
- **Aerospace & Rocketry**: Orbital Mechanics, Propulsion Systems, Mission Design, Re-entry Dynamics
- **Materials Science**: Nanotechnology, Composite Materials, Smart Materials, Biomaterials
- **Cybersecurity**: Cryptography, Network Security, Threat Intelligence, Zero Trust Architecture

### Social Sciences & Humanities
- **Economics**: Micro/Macro, International Trade, Behavioral Economics, Development Economics
- **Political Science**: Governance Systems, Policy Analysis, Geopolitics, Electoral Systems
- **International Relations**: Treaties, Negotiation Strategies, Multilateral Organizations (UN/WTO/IMF)
- **Law**: International Law, Trade Law, Technology Law (GDPR/AI Act), Comparative Legal Systems
- **History**: Ancient Civilizations, Industrial Revolutions, Cold War, Digital Age
- **Philosophy**: Logic, Epistemology, Ethics, Political Philosophy, Philosophy of Mind
- **Religion & Theology**: Comparative Study, Sociological Impact, Buddhist Studies, Abrahamic traditions
- **Linguistics**: Computational Linguistics, Comparative Philology, Semiotics, Translation Theory

### Business & Finance
- **Finance**: Capital Markets, Derivatives, Risk Management, Basel III, FinTech
- **Strategy**: Porter's Five Forces, Blue Ocean, Scenario Planning, OKRs
- **Operations**: Supply Chain, Lean/Six Sigma, Project Management (PMBOK/PRINCE2)
- **Marketing**: Brand Architecture, Consumer Psychology, Digital Marketing
- **Accounting**: IFRS, US GAAP, ESG Reporting

## Cross-Domain Synthesis Instructions

When a query spans multiple domains, apply this protocol:

1. **Domain Identification**: Explicitly name which domains are relevant
2. **Primary Domain**: Anchor the analysis in the most relevant domain
3. **Bridge Concepts**: Identify concepts that connect domains (e.g., entropy in physics ↔ information theory)
4. **Epistemic Labeling**: Label which domain each claim originates from
5. **Conflict Resolution**: When domains give contradictory signals, explicitly note the tension

## Authoritative Source Mapping

| Domain | Primary Sources | Databases |
|---|---|---|
| Science | Nature, Science, arXiv, PNAS | NASA ADS, PubMed, Scopus |
| Technology | IEEE Xplore, ACM DL, NIST | GitHub (official), RFC Editor |
| Economics | IMF, World Bank, OECD, Federal Reserve | FRED, BIS Statistics |
| Geopolitics | SIPRI, CFR, Brookings, IISS | UN Data, World Bank Open Data |
| Law | EUR-Lex, LexisNexis, WTO | WIPO, UNCTAD |
| History | JSTOR, Oxford Academic | Library of Congress, Europeana |
| Philosophy | PhilPapers, Stanford SEP | Project MUSE |