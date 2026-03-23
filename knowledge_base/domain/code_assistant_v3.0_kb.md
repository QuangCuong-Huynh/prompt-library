---
artifact_id: "019cdca8-912a-77f0-952f-ef3410fa0098"
doc_id: "CSCF-KB-CODE-ASST-20260309-01"
name:        "Knowledge Domain Library — Code Assistant"
version: "3.2.0"

authority_official:
  owner:       "Quang Cuong Huynh"
  declaration: "Registered — Quang Cuong Huynh"
  assistants:
    - "Claude (Anthropic)"
  reviewer:    "Quang Cuong Huynh"
status: "active"

dc:
  title: "Knowledge Domain Library — Code Assistant"
  type: "kb"
  date: "2026-03-09"
  subject: ["knowledge-base","domain-library","persona-grounding","codeassist"]
sha256: "PENDING"

changes:
  - version: "3.2.0"
    date:    "2026-03-11"
    author:  "Quang Cuong Huynh"
    summary: "UAS v1.2 compliance fix"
    type:    "fix"
---
# Knowledge Domain Library — Code Assistant
> ISCO-08: 2512 | Use: ground this persona's responses with authoritative sources below

## Tier 1 — Canonical Documentation (always check first)
| Tech | Documentation | URL |
|---|---|---|
| Python | Official docs | docs.python.org |
| TypeScript | Official docs | typescriptlang.org/docs |
| Rust | The Rust Book | doc.rust-lang.org/book |
| Go | Official tour + spec | go.dev/doc |
| Docker | Official docs | docs.docker.com |
| Kubernetes | Official docs | kubernetes.io/docs |
| GitHub Actions | Workflow syntax | docs.github.com/actions |

## Tier 2 — Design Patterns & Principles
| Pattern | Reference |
|---|---|
| **SOLID Principles** | Robert C. Martin — Clean Code |
| **GoF Design Patterns** | Gang of Four — Design Patterns (1994) |
| **Clean Architecture** | Robert C. Martin |
| **Twelve-Factor App** | 12factor.net |
| **Test-Driven Development** | Kent Beck |
| **Continuous Integration** | Martin Fowler — CI principles |

## Tier 3 — Security Code Standards
| Standard | Domain |
|---|---|
| **OWASP Top 10** | Web application security |
| **OWASP ASVS** | Application security verification |
| **CWE/SANS Top 25** | Common weakness enumeration |
| **NIST SSDF** | Secure software development framework |
| **SAST/DAST tools** | SonarQube, Semgrep, OWASP ZAP |

## Tier 4 — Code Quality Checklist
```
□ Type hints on all functions (Python) / strict TypeScript
□ Docstrings: module, class, function level
□ Unit tests with ≥80% coverage target
□ Error handling: no bare except / panic
□ No hardcoded secrets (use env vars / vault)
□ Logging: structured JSON, no PII in logs
□ Input validation: length, type, sanitization
□ Dependency versions pinned in requirements/package-lock
```

## Tier 5 — Search Queries for Current Best Practices
```
"Python 3.12 best practices type hints 2024"
"TypeScript 5 strict mode patterns"
"Rust async tokio best practices 2024"
"GitHub Actions workflow security hardening"
"Docker multi-stage build security best practices"
```

---


---

## Domain Boundaries (Anti-Drift)

| Query Type | Route To |
|---|---|
| Architecture decision | Architect |
| Test strategy / gate | QA Director |
| Compliance assessment | Compliance Gatekeeper |
| IP / trademark | AI Custodian |
| **Code implementation, debugging, DevOps, scripts, code review** | **Code Assistant ← HERE** |

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