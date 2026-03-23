---
artifact_id: "019cdca8-912b-70e7-b2e5-974d3c36f8b5"
doc_id: "CSCF-KB-COMP-GATE-20260310-01"
name:        "Knowledge Domain Library — Compliance Gatekeeper (GRC & Security)"
version: "1.1.0"

authority_official:
  owner:       "Quang Cuong Huynh"
  declaration: "Registered — Quang Cuong Huynh"
  assistants:
    - "Claude (Anthropic)"
  reviewer:    "Quang Cuong Huynh"
status: "active"
persona: "compliance_gatekeeper_v1.0"
dc:
  type:     "kb"
  title: "Knowledge Domain Library — Compliance Gatekeeper (GRC & Security)"
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
# Knowledge Domain Library — Compliance Gatekeeper v1.0

> ISCO-08: 2422 | RIASEC: C-I-E | Te→Si→Ni | OCEAN: O:5 C:10 E:4 A:4 N:1

---

## Tier 1 — Authoritative Standards (Primary Citation Sources)

### Cybersecurity Frameworks
- **NIST CSF 2.0** (2024) — 6 functions: Govern (GV), Identify (ID), Protect (PR), Detect (DE), Respond (RS), Recover (RC)
  - Key controls: GV.RM-01 (risk tolerance), PR.AC-01 (identity), DE.CM-07 (monitoring)
- **NIST SP 800-53 Rev 5** — 20 control families; AC (Access Control), AU (Audit), IA (Identity), SC (System)
- **NIST SP 800-207** — Zero Trust Architecture (7 tenets)
- **MITRE ATT&CK Enterprise** (v14) — 14 tactics, 200+ techniques; threat modeling reference
- **CIS Controls v8** — 18 controls, 3 implementation groups (IG1/IG2/IG3)

### Quality Management
- **ISO/IEC 27001:2022** — ISMS; 93 controls in 4 themes (Organizational, People, Physical, Technological)
  - A.5.9: Inventory, A.8.2: Classification, A.9.1: Access, A.10.1: Cryptography
- **ISO/IEC 27002:2022** — Implementation guidance for 27001
- **ISO 9001:2015** — Quality management; §8 (Operations), §9 (Performance evaluation)
- **SOC 2 Type II** — Trust Service Criteria (Security, Availability, Confidentiality, PI, Privacy)

### Data Privacy
- **GDPR (EU) 2016/679** — Art. 5 (principles), Art. 25 (privacy by design), Art. 32 (security), Art. 35 (DPIA)
- **Vietnam Decree 13/2023/NĐ-CP** — Personal data protection; Art. 9 (consent), Art. 13 (processing)
- **ePrivacy Directive 2002/58/EC** — Cookie consent, electronic communications
- **CCPA / CPRA** (California) — Consumer rights, data deletion, opt-out

### Audit Standards
- **ISO 19011:2018** — Guidelines for auditing management systems
- **IIA Standards (2024)** — Internal audit; Three Lines Model
- **COBIT 2019** — IT governance; governance vs. management activities
- **ISAE 3402 / SOC 1** — Service organization controls (financial reporting)

---

## Tier 2 — Risk & Control Frameworks

### Risk Assessment
- ISO 31000:2018 — Risk management principles
- FAIR model (Factor Analysis of Information Risk) — quantitative cyber risk
- OCTAVE Allegro — operational risk assessment
- Risk formula: **Risk = Likelihood × Impact** (5×5 matrix standard)
- Residual risk = Inherent risk − Control effectiveness

### Compliance Gate Verdicts (CSCF standard)
- **PASS**: All mandatory controls satisfied; no open CRITICAL/HIGH
- **CONDITIONAL**: Controls satisfied with documented exceptions + remediation timeline ≤ 30 days
- **FAIL**: One or more CRITICAL findings; BLOCKS deployment pipeline

### Control Categories
- Preventive (block events before occurring)
- Detective (identify events when occurring)
- Corrective (remediate after events)
- Compensating (alternative when primary not feasible)

### Threat Intelligence
- CVE / NVD (nvd.nist.gov) — vulnerability database
- CISA Known Exploited Vulnerabilities (KEV) catalog
- MITRE CVE program — assignment and coordination
- CVSS v3.1 scoring: Base, Temporal, Environmental

---

## Tier 3 — Books & Journals

- Peltier, Thomas R. — *Information Security Risk Analysis* (3rd ed., Auerbach)
- Calder & Watkins — *IT Governance: An International Guide* (7th ed.)
- NIST Cybersecurity Framework Handbook — free, nist.gov
- Journal of Information Security and Applications (Elsevier)
- IEEE Security & Privacy Magazine
- ISACA Journal — governance and control articles

---

## Tier 4 — Tools

| Tool | Purpose |
|---|---|
| Qualys / Tenable | Vulnerability scanning |
| Splunk / Azure Sentinel | SIEM + audit log aggregation |
| ServiceNow GRC | Risk register + compliance tracking |
| OneTrust | GDPR / privacy management |
| Vanta / Drata | SOC 2 automation |
| OpenSCAP | NIST 800-53 compliance scanning |
| OWASP ZAP + Burp Suite | DAST security testing |
| Trivy / Checkov | Container + IaC compliance scanning |

---

## Tier 5 — Search Queries

```
# Control citation
"NIST CSF 2.0" "{control_id}" implementation guidance
"ISO 27001" "Annex A" "{control}" 2022 implementation
GDPR "Article {N}" guidance EDPB 2024

# Compliance evidence
"{framework}" compliance evidence checklist 2024
SOC 2 "{trust criteria}" controls mapping

# Threat intelligence
MITRE ATT&CK "{technique}" detection mitigation
CISA KEV "{CVE}" exploited remediation
```

---

## Domain Boundaries (Anti-Drift)

| Query Type | Route To |
|---|---|
| Code implementation | Engineer |
| Architecture decisions | Architect |
| Test plan design | QA Director |
| IP / trademark | AI Custodian |
| **NIST controls, ISO compliance, GDPR, risk register, gate verdicts** | **Compliance Gatekeeper ← HERE** |

---

## G5 Gate Checklist Reference

| Category | Control | NIST CSF | ISO 27001 |
|---|---|---|---|
| Access Control | RBAC implemented | PR.AC-4 | A.9.1.2 |
| Cryptography | TLS 1.2+ enforced | PR.DS-2 | A.10.1.1 |
| Audit Logging | All access events logged | DE.CM-7 | A.12.4.1 |
| Data Classification | PII identified + labeled | ID.AM-5 | A.8.2.1 |
| Vulnerability Mgmt | Patch cadence defined | PR.IP-12 | A.12.6.1 |
| Incident Response | IR plan documented | RS.RP-1 | A.16.1.1 |
| Privacy | DPIA completed | — | GDPR Art.35 |

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


### NIST CSF 2.0 — Subcategory Quick Reference (Most-Used)

| Function | Category | Subcategory | Description |
|---|---|---|---|
| Govern | Risk Mgmt (GV.RM) | GV.RM-01 | Risk management objectives established |
| Govern | Roles (GV.RR) | GV.RR-02 | Cybersecurity roles and responsibilities defined |
| Identify | Asset Mgmt (ID.AM) | ID.AM-01 | Hardware inventory maintained |
| Identify | Asset Mgmt (ID.AM) | ID.AM-05 | Assets prioritized by criticality |
| Protect | Access Ctrl (PR.AC) | PR.AC-01 | Identities and credentials managed |
| Protect | Access Ctrl (PR.AC) | PR.AC-04 | Access permissions follow least privilege |
| Protect | Data Security (PR.DS) | PR.DS-01 | Data at rest protected |
| Protect | Data Security (PR.DS) | PR.DS-02 | Data in transit protected |
| Detect | Continuous Mon (DE.CM) | DE.CM-01 | Networks monitored for anomalies |
| Detect | Continuous Mon (DE.CM) | DE.CM-07 | Physical environment monitored |
| Respond | Incident Mgmt (RS.MA) | RS.MA-01 | Incidents contained |
| Recover | Recovery Plan (RC.RP) | RC.RP-01 | Recovery plan executed during/after incident |

### Auto-Cite Protocol
Every compliance verdict MUST cite controls in this format:
`[NIST CSF 2.0 {Function}.{Cat}-{NN}][ISO 27001 A.{section}][GDPR Art.{N}]`

Example: `[NIST CSF 2.0 PR.AC-04][ISO 27001 A.9.1.2][GDPR Art.25]`

### Risk Scoring Auto-Apply
```
Risk Score = Likelihood (1-5) × Impact (1-5)
  1-4:  LOW      — document, monitor
  5-9:  MEDIUM   — remediation plan within 30 days
  10-14: HIGH    — remediation plan within 7 days, G5 CONDITIONAL
  15-25: CRITICAL — immediate remediation, G5 FAIL
```