---
artifact_id: "019cdca8-912e-7180-8724-d1403e9a9054"
doc_id: "CSCF-KB-DATA-ARCH-20260310-01"
name:        "Knowledge Domain Library — Principal Data Architect & Strategist"
version: "1.0.0"

authority_official:
  owner:       "Quang Cuong Huynh"
  declaration: "Registered — Quang Cuong Huynh"
  assistants:
    - "Claude (Anthropic)"
  reviewer:    "Quang Cuong Huynh"
status: "active"
persona: "data_architect_v1.0"
dc:
  type:     "kb"
  title: "Knowledge Domain Library — Principal Data Architect & Strategist"
  date: "2026-03-10"
changes:
  - version: "1.0.0"
    date: "2026-03-10"
    author: "Quang Cuong Huynh"
    summary: "Sprint 5 — initial KB creation (21/21 complete)"
    type:     "kb"
sha256: "PENDING"
---
# Knowledge Domain Library — Principal Data Architect & Strategist v1.0

> ISCO-08: 2511 | RIASEC: I-R-C | Ti→Te→Ni | OCEAN: O:8 C:9 E:4 A:6 N:1

---

## Tier 1 — Authoritative Standards

### Data Management
- DAMA-DMBOK 2nd Edition (2017) — 11 knowledge areas: Data Governance, Architecture, Modeling, Storage, Security, Integration, Documents, Reference/MDM, Warehousing, Metadata, Data Quality
- ISO 8000:2022 — Data quality standard (characteristic definition, measurement)
- ISO/IEC 25012:2008 — Data quality model (15 characteristics)
- ISO/IEC 38505-1:2017 — Governance of data
- DCAM (Data Management Capability Assessment Model) — EDM Council

### Data Architecture
- TOGAF 10 ADM — Data Architecture domain
- Zachman Framework columns 3 (Data) — what the enterprise uses
- The Open Group Data Integration Reference Architecture
- Lambda Architecture (Marz & Warren, 2015) — batch + speed + serving layers
- Kappa Architecture (Kreps, 2014) — streaming-only simplification
- Data Mesh (Zhamak Dehghani, 2022) — domain ownership, data as product

### Modeling Standards
- IDEF1X — entity-relationship modeling standard (NIST FIPS 184)
- UML 2.5.1 class diagrams — object-level data models
- ISO/IEC/IEEE 31320-2 — IDEF1X notation
- Dimensional Modeling (Kimball, 2013) — star/snowflake schemas
- Data Vault 2.0 (Linstedt, 2015) — enterprise DWH with auditability

### Database Standards
- ISO/IEC 9075 SQL:2016 — temporal tables, JSON support
- ISO SQL:2011 — period types, bitemporal tables
- ANSI/ISO SQL:1992 — referential integrity, normalization forms (1NF–5NF, BCNF)

---

## Tier 2 — Techniques & Frameworks

### Modeling Paradigm Decision Matrix

| Pattern | Best For | Pros | Cons |
|---|---|---|---|
| 3NF / BCNF | OLTP, core HR/ERP | Data integrity, no anomalies | Complex joins |
| Star Schema | OLAP, BI reporting | Query performance, BI tool compat | Denormalized |
| Data Vault 2.0 | Enterprise DWH, audit | Scalable, historized, agile | Complex, verbose |
| Temporal (ISO SQL:2011) | Audit, GDPR, HR records | Native history, zero custom code | DB-specific support |
| Document (NoSQL) | Semi-structured configs | Schema flexibility | Weak consistency |
| Event Sourcing | CQRS, audit trail | Complete history, replay | Storage, complexity |

### Data Quality Dimensions (ISO 8000 / DAMA-DMBOK)
| Dimension | Definition | Measurement |
|---|---|---|
| Completeness | % required fields populated | NULL count / total rows |
| Accuracy | Matches source of truth | Sample audit vs authoritative source |
| Consistency | Same value across systems | Cross-system reconciliation count |
| Timeliness | Age of data vs SLA | MAX(current_time - updated_at) |
| Uniqueness | No duplicate records | Duplicate key count |
| Validity | Conforms to domain rules | Constraint violation count |

### Orbit HRMS — Canonical Data Architecture Pattern
```sql
-- Temporal table pattern (ISO SQL:2011) — applied to all auditable entities
CREATE TABLE hr_employees (
    id              BIGINT          PRIMARY KEY,
    org_unit_id     BIGINT          NOT NULL REFERENCES org_units(id),
    -- ... business columns ...
    valid_from      DATETIME2       GENERATED ALWAYS AS ROW START,
    valid_to        DATETIME2       GENERATED ALWAYS AS ROW END,
    PERIOD FOR SYSTEM_TIME (valid_from, valid_to)
) WITH (SYSTEM_VERSIONING = ON (HISTORY_TABLE = hr_employees_history));

-- GDPR erasure: anonymize-in-place, preserve temporal history
UPDATE hr_employees
SET first_name = 'REDACTED', last_name = 'REDACTED',
    national_id_hash = HASHBYTES('SHA2_256', NEWID())
WHERE id = @employee_id;
```

### MDM (Master Data Management) Protocol
1. **Identify** master entities: Employee, OrgUnit, Position, CostCenter
2. **Source** authoritative system per entity (HRMS = system of record for Employee)
3. **Match** algorithm: deterministic (exact key) then probabilistic (fuzzy name)
4. **Merge** rules: trusted source wins; all sources preserved in lineage
5. **Govern** via data steward assignment + quality SLA
6. **Distribute** via change data capture (CDC) or API contract

### Performance Engineering Checklist
- [ ] Clustered index on PK (default SQL Server)
- [ ] Non-clustered covering indexes on FK + common filter columns
- [ ] Partitioning on date columns for large tables (payroll_pay_lines, audit_log_entries)
- [ ] Column-store index on reporting tables (fact_headcount)
- [ ] Statistics updated daily (SQL Agent job)
- [ ] Query plan review for any query > 500ms (blocking threshold)
- [ ] Max DOP set per query workload type (OLTP: 1–4, OLAP: 8–16)

---

## Tier 3 — Books & Papers

- Kimball, Ralph & Ross, Margy — *The Data Warehouse Toolkit* (3rd ed., Wiley, 2013)
- Inmon, Bill — *Building the Data Warehouse* (4th ed., Wiley, 2005)
- Linstedt & Olschimke — *Building a Scalable Data Warehouse with Data Vault 2.0* (2015)
- Dehghani, Zhamak — *Data Mesh* (O'Reilly, 2022)
- Kleppmann, Martin — *Designing Data-Intensive Applications* (O'Reilly, 2017)
- Redman, Thomas — *Data Driven: Profiting from Your Most Important Business Asset* (2008)
- DAMA International — *DAMA-DMBOK: Data Management Body of Knowledge* (2nd ed., 2017)

---

## Tier 4 — Tools

| Tool | Purpose |
|---|---|
| SQL Server Management Studio (SSMS) | SQL Server admin + query analysis |
| Azure Data Studio | Cross-platform SQL + notebook |
| dbt (data build tool) | ELT transformations + lineage |
| Apache Kafka + Debezium | CDC / event streaming |
| Azure Purview | Data catalog + lineage (enterprise) |
| Alembic / Flyway / Liquibase | Schema migration management |
| draw.io / erDiagram (Mermaid) | ERD visualization |
| Apache Superset / Power BI | OLAP reporting + data exploration |
| Great Expectations | Automated data quality validation |
| Monte Carlo / Soda | Data observability |

---

## Tier 5 — Search Queries

- "DAMA-DMBOK data architecture knowledge area enterprise"
- "Data Vault 2.0 vs Kimball dimensional modeling comparison 2024"
- "Zhamak Dehghani data mesh domain ownership data product"
- "ISO SQL:2011 temporal tables system versioning SQL Server implementation"
- "data quality dimensions ISO 8000 measurement framework enterprise"
- "master data management MDM golden record matching algorithm"
- "GDPR right to erasure temporal tables anonymization strategy"

---

## Domain Boundaries

| In Scope | Out of Scope |
|---|---|
| Enterprise data architecture strategy | Application code (→ engineer) |
| Data modeling: 3NF, star, Data Vault, temporal | UI/UX design (→ creative_products_director) |
| MDM, data quality, data governance | Sprint planning (→ planner) |
| ETL/ELT pipeline architecture | Compliance gate enforcement (→ compliance) |
| Performance: indexing, partitioning, query tuning | Requirements elicitation (→ pm_ba) |
| GDPR data architecture controls | Security auditing (→ auditor) |