---
artifact_id: "019cdca8-9134-7796-8da8-c67839addc1e"
doc_id: "KB-CSCF-ASTROLIB-20260308-01"
name:        "Astro-Data Architect — Reference Library v2.0"
version: "2.0.0"

authority_official:
  owner:       "Quang Cuong Huynh"
  declaration: "Registered — Quang Cuong Huynh"
  assistants:
    - "Claude (Anthropic)"
  reviewer:    "Quang Cuong Huynh"
status: "active"
migrated_from: "REFERENCE LIBRARY_ ASTRO-DATA ARCHITECT & SCIENTIFIC STORYTELLER_.docx"
migrated_at: "2026-03-08"
dc:
  title: "Astro-Data Architect — Reference Library v2.0"
  type: "kb"
  subject: ["astronomy","astrophysics","data-engineering","scientific-storytelling"]
  date: "2026-03-08"
sha256: "PENDING"

changes:
  - version: "2.0.0"
    date:    "2026-03-11"
    author:  "Quang Cuong Huynh"
    summary: "UAS v1.2 compliance fix"
    type:    "fix"
---
# Astro-Data Architect — Reference Library

*Authoritative sources, qualifications, and vocabulary for `astro_data_architect_v2.0` and `space_commander_v2.0`.*

---

## Section 1: Core Ontology Keywords

```yaml
data_science_ml:
  - statistical significance / p-value / confidence interval
  - Bayesian inference / Markov Chain Monte Carlo (MCMC)
  - supervised / unsupervised learning / time-series analysis
  - anomaly detection / feature engineering
  - convolutional neural networks (CNNs) for image classification
  - hypothesis testing / cross-validation

data_engineering:
  - ETL/ELT pipeline / data lake / data warehouse / lakehouse
  - distributed computing: Apache Spark, Dask
  - stream processing: Apache Kafka
  - schema-on-read vs schema-on-write
  - data governance / data lineage / petabyte-scale

astronomy_physics:
  - light curve / spectral analysis / redshift
  - cosmic microwave background (CMB)
  - Lambda-CDM (ΛCDM) model
  - stellar evolution / galactic morphology
  - gravitational lensing / dark matter & dark energy
  - exoplanet transit / radial velocity
  - coordinate systems: ICRS, J2000, Galactic, Ecliptic
  - catalogs: NGC, IC, SDSS J, Gaia DR3, 2MASS J, HIP

storytelling_visualization:
  - data narrative / narrative arc / explanatory power
  - Tufte's principles / information density / data-to-ink ratio
  - EDA (exploratory data analysis)
  - scientific communication / plain-language summary
```

---

## Section 2: Primary Data Surveys & Missions

| Survey/Mission | Domain | Access | Trust Level |
|---|---|---|---|
| **Gaia DR3** | Astrometry, photometry, 1.8B stars | ESA public | Authoritative |
| **SDSS DR18** | Imaging, spectroscopy, photometry | Public | Authoritative |
| **ZTF** | Time-domain, transients, variables | Public | Authoritative |
| **TESS** | Exoplanet photometry | NASA MAST | Authoritative |
| **JWST** | Infrared imaging/spectroscopy | MAST/ESA | Authoritative |
| **Chandra** | X-ray observatory | NASA CXC | Authoritative |
| **2MASS** | Near-infrared all-sky | IPAC | Authoritative |
| **WISE/NEOWISE** | Mid-infrared | IPAC | Authoritative |
| **NASA ADS** | Bibliographic | ADS public | Authoritative |
| **arXiv astro-ph** | Preprints | arXiv.org | Use with caution |
| **JPL Horizons** | Solar system ephemeris | JPL public | Authoritative |
| **IAU MPC** | Minor planet center | IAU public | Authoritative |

---

## Section 3: Seminal Technical Texts

```yaml
astrophysics:
  - "Gravitation — Misner, Thorne, Wheeler (1973)"
  - "Spacetime and Geometry — Carroll (2003)"
  - "Modern Classical Physics — Thorne & Blandford (2017)"
  - "Galactic Dynamics — Binney & Tremaine (2008)"
  - "An Introduction to Modern Astrophysics — Carroll & Ostlie (2017)"

data_engineering:
  - "Designing Data-Intensive Applications — Kleppmann (2017)"
  - "The Data Warehouse Toolkit — Kimball & Ross (2013)"
  - "Streaming Systems — Akidau et al. (2018)"

visualization:
  - "The Visual Display of Quantitative Information — Tufte (2001)"
  - "Fundamentals of Data Visualization — Wilke (2019)"

ml_statistics:
  - "Statistical Methods in Astronomy — Feigelson & Babu (2012)"
  - "Machine Learning for Physics and Astronomy — Baron (2019)"
  - "Python Data Science Handbook — VanderPlas (2016)"
```

---

## Section 4: Data Formats & Standards

```yaml
file_formats:
  - FITS (Flexible Image Transport System) — IEEE standard for astronomy
  - HDF5 — hierarchical scientific data
  - Parquet — columnar analytics
  - VOTable — Virtual Observatory XML format
  - ECSV — Enhanced CSV for astropy tables

coordinate_standards:
  - ICRS (International Celestial Reference System) — IAU 1997
  - FK5 J2000.0
  - Galactic coordinates (l, b)
  - Ecliptic J2000

software_stack:
  - astropy / astroquery — core Python astronomy toolkit
  - healpy / HEALPix — sky pixelization
  - scikit-learn / tensorflow / pytorch — ML
  - matplotlib / seaborn / plotly / bokeh — visualization
  - dask / pyspark — distributed compute
  - sqlalchemy / psycopg2 — database connectivity
```

---

## Section 5: Engineering Standards (Space Systems)

| Standard | Scope |
|---|---|
| **ECSS-E-ST-10** | Space engineering — system engineering general requirements |
| **ECSS-E-ST-40** | Space engineering — software |
| **NASA SP-2016-6105** | Systems Engineering Handbook |
| **ISO 14961** | Space data systems — parameter value language |
| **CCSDS** | Consultative Committee for Space Data Systems — telemetry protocols |

---

## Section 6: Persona Routing Map

| Query Type | Route to Persona |
|---|---|
| Astronomical data pipeline | `astro_data_architect_v2.0` |
| Space strategy / military space | `space_commander_v2.0` |
| Materials for space structures | `architect_enterprise_v1.1` (cross-ref HRMS or research corpus) |
| Academic publication (astronomy) | `astro_data_architect_v2.0` + `template_output_academic_v1.0` |