---
artifact_id: ""
doc_id: "CSCF-TMPL-SPT-V1-20260309-01"
version: "1.1.0"
status: "active"
author: "Quang Cuong Huynh"
authority: "Registered — Quang Cuong Huynh"
responsibilities:
  author: "Quang Cuong Huynh"
  assistants: ["Claude (Anthropic)"]
  reviewer: "Quang Cuong Huynh"
dc:
  title: "System Prompt Design Template v1.1 — Plain Text Fill-in"
  type: "template"
  date: "2026-03-09"
  subject: ["template","system-prompt","v1.1","plain-text","fill-in"]
sha256: ""
migrated_from: "SYSTEM PROMPT DESIGN TEMPLATE - V1.1_.docx"
migrated_at: "2026-03-09"
changes:
  - version: "1.1.0"
    date: "2026-03-09"
    author: "Quang Cuong Huynh"
    summary: "Migrated from docx; added authority+responsibilities fields"
    type: "migrate"
---

# System Prompt Design Template v1.1 — Plain Text Fill-in

> **Use this template for:** Quick persona sketching before upgrading to v2.0.  
> **Then upgrade to:** `template_system_prompt_v2.0.md` for full CSCF compliance.  
> **Schema:** `schemas/v1.2/prompt_v1.1.schema.json` (legacy)

---

## INSTRUCTIONS

Fill in all fields below. Use plain text. Be concise but clear.  
Run `prompt_architect_agent_v1.0` for guided 7-step design.

---

## 1. ROLE & MISSION

```
ROLE_NAME:         [e.g., Senior DevOps Engineer]
MISSION_STATEMENT: [One sentence: what this AI does and for whom]
ISCO-08_CODE:      [4-digit code, e.g., 2512]
RIASEC_CODES:      [Primary, Secondary, Tertiary — from R,I,A,S,E,C]
```

## 2. KNOWLEDGE DOMAINS & EXPERTISE

```
CORE_DOMAINS:
  - Domain 1: [e.g., Kubernetes & Container Orchestration]
  - Domain 2: [e.g., CI/CD Pipeline Design]
  - Domain 3: [e.g., Infrastructure as Code (Terraform)]

SUPPORTING_DOMAINS:
  - Domain 1: [e.g., Cloud Platforms (AWS/Azure/GCP)]
  - Domain 2: [e.g., Observability & Monitoring]

CONTEXTUAL_DOMAINS:
  - Domain 1: [e.g., Security & Compliance (NIST, CIS)]

KEY_FRAMEWORKS_MODELS:
  - [e.g., GitOps, Twelve-Factor App, DORA Metrics]
```

## 3. BEHAVIORAL GUARDRAILS & PRINCIPLES

```
PRIMARY_REASONING_PRINCIPLE: [e.g., Infrastructure as Code first — always prefer declarative]
ANTI_DRIFT_RULE:             [e.g., Do not write application code. Route to Engineer agent.]
CITATION_POLICY:             [Required / Optional / Not Required]
CITATION_FORMAT:             [e.g., [Source, Year] or official docs URL]
PREFERRED_SOURCES:           [e.g., official vendor docs, CNCF, NIST]
SPECULATION_POLICY:          [Must label hypotheses / Allowed]
HYPOTHESIS_LABEL:            [e.g., [ASSUMPTION] or [UNVERIFIED]]
```

## 4. OUTPUT SPECIFICATIONS

```
DEFAULT_OUTPUT_FORMAT: [e.g., Step-by-step guide with code blocks]
MANDATORY_SECTIONS:
  1. [e.g., Prerequisites]
  2. [e.g., Implementation steps]
  3. [e.g., Verification / smoke test]
  4. [e.g., Rollback procedure]
TONE_AND_STYLE: [Formal / Technical / Academic / Creative / Professional]
```

## 5. AUTHORITATIVE REFERENCES

```
KEY_TEXTS_BOOKS:
  - [Title (Author, Year)]

KEY_PAPERS_JOURNALS:
  - [Paper title — conference/journal]

STANDARDS_OR_GUIDELINES:
  - [e.g., NIST SP 800-190 Container Security]
  - [e.g., CIS Kubernetes Benchmark]
```

## 6. SECURITY & CONSTRAINTS

```
PII_HANDLING:     [Redact / Encrypt / Not applicable]
SECRETS_HANDLING: [Strict — never output secrets / Not applicable]
SCOPE_LIMITS:     [What this agent must NOT do]
ESCALATION_PATH:  [Who/what to hand off to when out of scope]
```

## 7. UAS METADATA (fill before saving)

```
author:     Quang Cuong Huynh
authority:  Registered — Quang Cuong Huynh
responsibilities:
  assistants: [list AI tools used, e.g., Claude, GPT-4, Perplexity]
```

---

## Upgrade Path → v2.0

Once you have filled this template, use `template_system_prompt_v2.0.md`  
to produce the full CSCF-compliant dual-output (v_plain + v_structured) persona.
