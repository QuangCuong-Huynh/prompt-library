---
artifact_id: "019cdca8-9125-780b-be6d-14acf5ea7b8e"
doc_id: "CSCF-KB-AI-CUSTODIAN-20260309-01"
name:        "Knowledge Domain Library — AI Custodian (Virtual Librarian)"
version: "1.1.0"

authority_official:
  owner:       "Quang Cuong Huynh"
  declaration: "Registered — Quang Cuong Huynh"
  assistants:
    - "Claude (Anthropic)"
  reviewer:    "Quang Cuong Huynh"
status: "active"
tier: "KB-TIER-1"
persona: "ai_custodian_v1.0"
dc:
  type:     "kb"
  title: "Knowledge Domain Library — AI Custodian (Virtual Librarian)"
  date: "2026-03-09"
sha256: "PENDING"

changes:
  - version: "1.1.0"
    date:    "2026-03-11"
    author:  "Quang Cuong Huynh"
    summary: "UAS v1.2 compliance fix"
    type:     "kb"
---
# Knowledge Domain Library — AI Custodian v1.0

> ISCO-08: 2619 | RIASEC: C-I-S | Si→Te→Ni | OCEAN: O:6 C:10 E:4 A:7 N:1

---

## Tier 1 — Authoritative Standards & Law

### Intellectual Property Law
- Berne Convention for the Protection of Literary and Artistic Works (1886, amended 1979)
  - Art. 2: Definition of protected works (including AI-assisted)
  - Art. 5(2): Automatic protection — no registration required
  - Art. 9: Reproduction right
- TRIPS Agreement (WTO, 1994) — Art. 27: Patentable subject matter; Art. 9–14: Copyright
- WIPO Copyright Treaty (WCT, 1996) — digital environment protections
- Vietnam IP Law (No. 50/2005/QH11, amended 2022) — domestic enforcement
- US Copyright Act 17 U.S.C. — fair use (§107), work-for-hire (§101), registration (§408)
- EU Copyright Directive 2019/790 — Art. 17 (upload filters), Art. 4 (TDM exception)

### AI & Copyright (Emerging)
- US Copyright Office Guidance (2023): AI-generated content not copyrightable without human authorship
- Thaler v. Perlmutter (D.D.C. 2023): Confirmed human authorship requirement
- EU AI Act (2024): Risk-based AI classification; Art. 52 transparency obligations
- WIPO DABUS discussions — AI inventorship framework (ongoing)

### Data Governance & Privacy
- GDPR (EU) 2016/679 — Art. 4 (definitions), Art. 17 (right to erasure), Art. 25 (privacy by design)
- Vietnam Personal Data Protection Decree No. 13/2023/NĐ-CP
- ISO/IEC 27001:2022 — Information security management
- NIST Privacy Framework v1.0

### Trademark
- Paris Convention (1883) — Art. 6bis: well-known marks
- Madrid Protocol — international trademark registration
- US Lanham Act (15 U.S.C.) — trademark registration + enforcement
- Vietnam Trademark Law (IP Law 2005/2022, Ch. 7-8)

---

## Tier 2 — Frameworks & Methodologies

### IP Asset Management
- IP Australia: IP asset valuation methodology
- Ocean Tomo: Intellectual Capital Equity model
- WIPO IP Valuation Methodology (cost, market, income approaches)
- Creative Commons licensing spectrum (CC0 → CC BY-NC-ND)
- SPDX License List (Software Package Data Exchange) — for code licensing

### Data Classification
- NIST SP 800-60: Guide for Mapping Types of Information to Security Categories
- NATO classification analogue: PUBLIC / INTERNAL / CONFIDENTIAL / SECRET
- ISO 27001 Annex A.8.2: Information Classification
- DAMA-DMBOK2: Data Management Body of Knowledge — Chapter 7 (Data Security)

### Knowledge Management
- TOGAF 10: Architecture Knowledge Repository patterns
- CMMI-DEV v2.0: Configuration Management (CM) practice area
- ISO 9001:2015 §7.5: Documented information requirements
- Dublin Core Metadata Initiative — dc:title, dc:creator, dc:rights, dc:identifier

### Document Control
- UAS (Unified Artifact Standard) Header v1.1 — internal standard (Quang Cuong Huynh)
- ISO/IEC 26514: Requirements for designers and developers of user documentation
- IEEE 829-2008: Test documentation standard

---

## Tier 3 — Books, Journals & Reference

- Cornish, Llewelyn & Aplin — *Intellectual Property: Patents, Copyrights, Trademarks and Allied Rights* (9th ed.)
- Stim, Rich — *Patent, Copyright & Trademark: An Intellectual Property Desk Reference* (Nolo)
- Nimmer on Copyright — treatise, Matthew Bender (authoritative US commentary)
- WIPO Magazine — quarterly, open access (wipo.int/wipo_magazine)
- Journal of Intellectual Property Law & Practice (Oxford)
- Samuelson, Pamela — "AI and Copyright" (2023), Harvard Journal of Law & Technology
- Ballardini, Rosa M. — "Patenting AI" (2019), European Intellectual Property Review

---

## Tier 4 — Tools & Registries

| Tool | Purpose |
|---|---|
| USPTO Patent Full-Text Database (patents.google.com) | Prior art search |
| WIPO ROMARIN / Madrid Monitor | International trademark tracking |
| EUIPO eSearch plus | EU trademark search |
| IP Vietnam (noip.gov.vn) | Vietnam IP registration |
| Copyright.gov (US) | US copyright registration |
| IPFS / Arweave | Immutable IP evidence timestamping |
| blockchain-based notary (e.g. OpenTimestamps) | Prior creation proof |
| Creative Commons license chooser | License selection |
| SPDX tools (spdx.org/tools) | Software license compliance |

---

## Tier 5 — Search Queries (Operational)

```
# Trademark availability
"{mark_name}" site:tmdn.org OR site:tmsearch.uspto.gov
trademark "{mark_name}" "LIVE" registration

# Copyright prior art
"{work_title}" site:copyright.gov
"{work_title}" "©" "all rights reserved"

# AI copyright guidance
"AI generated" copyright "human authorship" 2023 OR 2024 site:copyright.gov

# Vietnam IP
site:noip.gov.vn "{term}" trademark

# GDPR compliance
GDPR "legitimate interest" OR "consent" "data processing" guidelines 2024

# License compatibility
"{license_A}" compatible "{license_B}" SPDX
```

---

## Domain Boundaries (Anti-Drift)

| Query Type | Route To |
|---|---|
| Write code / implement | Engineer |
| Sprint planning / backlog | PM/BA |
| System architecture decision | Architect |
| Creative lore design | Creative Director |
| Security test design | QA Director |
| **IP ownership, licensing, registration, GDPR, data classification** | **AI Custodian ← HERE** |

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