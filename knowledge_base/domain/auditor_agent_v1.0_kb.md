---
artifact_id: "019cdca8-9129-7923-b678-91a007d744f9"
doc_id: "CSCF-KB-AUDITOR-20260310-01"
name:        "Knowledge Domain Library — Pipeline Auditor Agent"
version: "1.1.0"

authority_official:
  owner:       "Quang Cuong Huynh"
  declaration: "Registered — Quang Cuong Huynh"
  assistants:
    - "Claude (Anthropic)"
  reviewer:    "Quang Cuong Huynh"
status: "active"
persona: "auditor_agent_v1.0"
dc:
  type:     "kb"
  title: "Knowledge Domain Library — Pipeline Auditor Agent"
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
# Knowledge Domain Library — Auditor Agent v1.0

> ISCO-08: 2422 | RIASEC: C-I-S | Te→Si→Ti | OCEAN: O:5 C:10 E:3 A:6 N:1

---

## Tier 1 — Authoritative Standards

### Audit Standards
- **IIA International Standards for the Professional Practice of Internal Auditing (2024)**
  - Standard 1100: Independence and objectivity
  - Standard 2200: Engagement planning
  - Standard 2300: Performing the engagement (evidence collection)
  - Standard 2400: Communicating results
- **ISO 19011:2018** — Guidelines for auditing management systems
  - §6: Performing an audit (opening meeting → document review → on-site → findings → report)
  - §7.2: Auditor competence
- **ISAE 3000** — Assurance engagements (non-financial)
- **ISAE 3402 / SOC 1** — Service organization controls (financial reporting relevant)

### IT Audit & Evidence Standards
- **COBIT 2019** — IT governance framework; EDM (Evaluate/Direct/Monitor) + APO/BAI/DSS/MEA domains
- **ITAF (IT Assurance Framework, ISACA)** — IT audit standards, guidelines, tools
- **NIST SP 800-92** — Guide to Computer Security Log Management
- **RFC 3161** — Internet X.509 PKI Time-Stamp Protocol (TSP) — timestamp evidence
- **SHA-256 / SHA-3** — NIST FIPS 180-4 — cryptographic hashing for evidence integrity

### Evidence & Chain of Custody
- **ISO/IEC 27037:2012** — Guidelines for identification, collection, acquisition of digital evidence
- **ACFE Fraud Examination Manual** — evidence handling procedures
- Legal admissibility standards: FRE 901 (US), similar EU Digital Evidence Framework
- Hash chaining for append-only audit logs (WORM pattern)
- Merkle tree structures for tamper-evident audit trails

---

## Tier 2 — Provenance & Artifact Standards

### CSCF Artifact Standard (internal)
- UAS Header v1.1 — doc_id, version, author, authority, sha256, ratified_output
- doc_id format: `{DOMAIN}-{TYPE}-{YYYYMMDD}-{NN}` — canonical; L3 immutable after ratification
- Memory tiers: L1 (session, 90d) | L2 (project+1yr) | L3 (permanent, WORM)
- Ratified output schema: `schemas/output/ratified_doc_schema.json`

### Cryptographic Provenance
- SHA-256 hash generation: `scripts/generate_sha256.py`
- Artifact registration: `scripts/register_artifact.py` → `artifact_registry/`
- Signing: `scripts/sign_artifact.py` — ed25519 or RSA-PSS
- Timestamp: ISO 8601 UTC; UUIDv7 for time-ordered artifact IDs

### Audit Trail Patterns
- Append-only log files (never DELETE, never UPDATE)
- Sequence numbering for gap detection
- Cross-reference hash: each record hashes previous record (blockchain-lite)
- Tamper detection: hash recalculation on demand

---

## Tier 3 — References

- Sawyer, Robert — *Internal Audit: Efficiency Through Automation*
- Champlain, Jack J. — *Auditing Information Systems* (2nd ed., Wiley)
- Coderre, David — *Computer-Aided Fraud Prevention and Detection*
- ISACA — *IS Audit and Assurance Standards* (isaca.org/resources)
- Journal of Information Systems Audit, Control and Security

---

## Tier 4 — Tools

| Tool | Purpose |
|---|---|
| ACL Analytics / IDEA | Data analytics for audit |
| Splunk | Log search + anomaly detection |
| AuditBoard | Audit workflow management |
| Python hashlib | SHA-256 / SHA-3 generation |
| OpenTimestamps | Blockchain-anchored timestamps |
| GPG / age | Artifact signing |
| jq | JSON audit log processing |
| sqlite3 | Lightweight audit database |

---

## Tier 5 — Search Queries

```
# Evidence standards
"ISO 19011" audit evidence collection procedure 2018
"chain of custody" digital evidence standard
SHA-256 "append-only" audit log implementation

# COBIT
"COBIT 2019" "{domain}" audit objectives
"COBIT" MEA01 monitoring controls evidence

# Artifact integrity
"Merkle tree" audit log tamper detection implementation
RFC 3161 timestamp token verification Python
```

---

## Domain Boundaries (Anti-Drift)

| Query Type | Route To |
|---|---|
| Compliance gate verdict | Compliance Gatekeeper |
| Security test design | QA Director |
| IP ownership | AI Custodian |
| Code implementation | Engineer |
| **Artifact signing, hash verification, provenance records, L3 audit trail** | **Auditor Agent ← HERE** |

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


### Hash-Chain Audit Trail Protocol (Auto-Apply)

Every L3 artifact chain MUST follow this integrity model:

```python
# Each record contains hash of previous record — tamper-evident chain
record = {
    "artifact_id": uuidv7(),
    "doc_id": "...",
    "timestamp": datetime.utcnow().isoformat() + "Z",
    "content_sha256": sha256(content_body),
    "previous_sha256": sha256(previous_record_content),  # chain link
    "chain_position": sequence_number,
    "signed_by": "scripts/sign_artifact.py"
}
# Verify chain: recalculate all hashes bottom-up
# Mismatch at position N = tamper at or before N
```

### IIA Three Lines Model (Auto-Reference in Audit Reports)

| Line | Owner | Function |
|---|---|---|
| **First Line** | Operational management (Engineer, PM/BA) | Owns and manages risks; day-to-day controls |
| **Second Line** | Risk & Compliance (Compliance Gatekeeper) | Oversees, monitors, supports first line |
| **Third Line** | Internal Audit (Auditor Agent) | Independent assurance to governance authority |

Every audit report MUST declare: "This review constitutes Third Line assurance per IIA Three Lines Model."

### Evidence Quality Tiers
| Quality | Criteria | Weight in Findings |
|---|---|---|
| Strong | Original source, hash-verified, timestamped | 100% |
| Moderate | Corroborated by second source, undisputed | 70% |
| Weak | Single unverified source, no chain of custody | 30% — must flag |
| Inadmissible | Hearsay, no documentation, reconstructed | 0% — exclude |