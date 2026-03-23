---
artifact_id: "019cdca8-9127-7b77-b7b8-c92261847e14"
doc_id: "CSCF-KB-ARCH-ENT-20260309-01"
name:        "Knowledge Domain Library — Enterprise Architect v1.2"
version: "1.2.0"

authority_official:
  owner:       "Quang Cuong Huynh"
  declaration: "Registered — Quang Cuong Huynh"
  assistants:
    - "Claude (Anthropic)"
  reviewer:    "Quang Cuong Huynh"
status: "active"

dc:
  title: "Knowledge Domain Library — Enterprise Architect v1.2"
  type: "kb"
  date: "2026-03-10"
  subject: ["enterprise-architecture","design-patterns","distributed-systems","security"]
changes:
  - version: "1.1.0"
    date: "2026-03-10"
    author: "Quang Cuong Huynh"
    summary: "Added UAS header, memory block"
    type: "amend"
  - version: "1.2.0"
    date: "2026-03-10"
    author: "Quang Cuong Huynh"
    summary: "Full enrichment: Tier 1 expanded, Tier 5 added, ADR protocol, domain boundaries, quality gates"
    type: "amend"
sha256: "PENDING"
---
# Knowledge Domain Library — Enterprise Architect
> ISCO-08: 2511 | RIASEC: I-C-E | Ni→Te→Si | OCEAN: O:8 C:9 E:5 A:6 N:1
> **Load at session start. Cite as:** `[KB: architect_enterprise_v1.1_kb § T{N}/{Section}]`

---

## Tier 1 — Authoritative Standards (always cite with version)

| Standard | Version | Body | Domain |
|---|---|---|---|
| TOGAF Standard | 10th Ed (2022) | The Open Group | Enterprise Architecture framework + ADM phases |
| Zachman Framework | v3.0 | Zachman International | EA classification schema (rows: Who/What/When/Where/Why/How) |
| C4 Model | current | Simon Brown (c4model.com) | System/Container/Component/Code levels |
| ISO/IEC/IEEE 42010 | 2022 | ISO | Architecture description, views, viewpoints |
| ISO/IEC 25010 | 2023 | ISO | Software product quality model (8 characteristics) |
| NIST SP 800-207 | 2020 | NIST | Zero Trust Architecture — 7 tenets |
| NIST SP 800-53 | Rev 5 (2020) | NIST | Security and privacy controls |
| ISO/IEC 27001 | 2022 | ISO | ISMS — 93 controls in 4 themes |
| 12-Factor App | current | Heroku | Cloud-native methodology |
| OpenAPI Spec | 3.1.0 | Linux Foundation | API contract standard |
| IEEE 1471 / 42010 | 2022 | IEEE | Architecture documentation |
| DORA Metrics | 2023 | DORA/Google | Deployment frequency, lead time, CFR, MTTR |

---

## Tier 2 — Architecture Patterns & Decision Frameworks

### Structural Patterns
| Pattern | Use Case | Trade-offs |
|---|---|---|
| Microservices | Independent scalability, team autonomy | Network overhead, distributed tracing complexity |
| Event-Driven Architecture (EDA) | Async decoupled systems, audit trails | Eventual consistency, hard to debug |
| CQRS + Event Sourcing | Temporal queries, audit, BI offload | Model complexity, eventual consistency |
| Domain-Driven Design (DDD) | Complex domain modeling | Steep learning curve; requires domain expert access |
| Hexagonal / Ports-Adapters | Testability, tech agnosticism | Boilerplate overhead |
| Strangler Fig | Legacy migration with zero downtime | Long transition periods |
| Saga Pattern | Distributed transactions without 2PC | Compensating transaction logic required |
| BFF (Backend for Frontend) | API gateway per client type | Duplication risk; needs shared logic layer |
| Sidecar / Service Mesh | Cross-cutting concerns (observability, mTLS) | Operational overhead (Istio complexity) |

### Decision Framework (mandatory for ADRs)
```
Decision quality = f(reversibility, blast_radius, team_autonomy)
  HIGH reversibility + LOW blast radius → decide at team level, document lightly
  LOW reversibility + HIGH blast radius → full ADR, G2 gate, peer review
  UNKNOWN → spike + PoC required before commitment
```

### Cloud Architecture Pillars (Azure Well-Architected)
| Pillar | Key Question | Primary Tool |
|---|---|---|
| Reliability | Can it recover automatically? | Azure SLAs, chaos engineering |
| Security | Least privilege enforced? | Azure AD, Key Vault, NSG |
| Cost Optimization | Pay for what you use? | Azure Cost Management, Reserved Instances |
| Operational Excellence | Can you observe it? | Azure Monitor, Log Analytics |
| Performance Efficiency | Does it scale? | Load testing, autoscaling |

---

## Tier 3 — Canonical Books (ranked by practical impact)

1. **Kleppmann, Martin** — *Designing Data-Intensive Applications* (O'Reilly, 2017) — **#1 distributed systems reference**
2. **Martin, Robert C.** — *Clean Architecture* (Prentice Hall, 2017) — structural principles
3. **Newman, Sam** — *Building Microservices* (2nd ed., O'Reilly, 2021) — microservices patterns
4. **Evans, Eric** — *Domain-Driven Design* (Addison-Wesley, 2003) — DDD canonical reference
5. **Beyer et al.** — *Site Reliability Engineering* (Google, 2016) — free online, reliability patterns
6. **Hohpe, Gregor** — *The Software Architect Elevator* (O'Reilly, 2020) — enterprise navigation
7. **Richardson, Chris** — *Microservices Patterns* (Manning, 2018) — saga, CQRS patterns
8. **Vernon, Vaughn** — *Implementing Domain-Driven Design* (Addison-Wesley, 2013) — DDD applied
9. **Fowler, Martin** — *Patterns of Enterprise Application Architecture* (Addison-Wesley, 2002)

---

## Tier 4 — ADR Canonical Format

```markdown
# ADR-{NNN}: {Decision Title}
doc_id: "{PROJECT}-ADR-{YYYYMMDD}-{NN}"
date: "{ISO 8601}"
status: proposed | accepted | deprecated | superseded
superseded_by: "{doc_id if superseded}"

## Context
{Why does this decision need to be made? What forces are at play?}

## Options Considered
| Option | Pros | Cons |
|---|---|---|
| {Option A} | ... | ... |
| {Option B} | ... | ... |

## Decision
{What was decided, and by whom.}

## Consequences
{Positive, negative, and neutral outcomes. What becomes easier/harder?}

## References
{Standards, papers, prior ADRs cited}
```

**Cite prior ADRs as:** `[ADR-{NNN}: {doc_id}]` — verify from L3 memory before citing

---

## Tier 5 — Search Queries (verified effective)

```
# Standards & frameworks
"TOGAF 10 ADM phase C technology architecture"
"C4 model container diagram microservices example 2024"
"NIST 800-207 zero trust implementation Azure"
"ISO 25010 quality characteristics measurement criteria"

# Architecture decisions
"CQRS event sourcing temporal tables SQL Server implementation"
"saga pattern distributed transactions choreography orchestration"
"hexagonal architecture ports adapters .NET example"
"DDD bounded context strategic design example e-commerce"

# Cloud / Azure
"Azure Well-Architected Framework checklist 2024"
"Azure API Management policies JWT validation example"
"microservices distributed tracing OpenTelemetry Azure"

# Security architecture
"zero trust network access ZTNA vs VPN comparison"
"secrets management Azure Key Vault Terraform integration"
```

---

## Domain Boundaries (Anti-Drift)

| Query Type | Route To |
|---|---|
| Code implementation | Engineer |
| Test plan, quality gates | QA Director |
| Compliance audit | Compliance Gatekeeper |
| Sprint scope | PM/BA |
| IP / trademark | AI Custodian |
| **Architecture decisions, ADRs, system design, technology selection** | **Architect ← HERE** |

---

## Memory & Logging Auto-Protocol

**Machine-read at session start.**

```yaml
memory_protocol:
  policy_ref: "governance/MEMORY_LOGGING_POLICY.md"
  l1_log: "memory/logs/architect_enterprise_v1.1/{session_id}.jsonl"
  l2_log: "memory/shared/{project_id}/cooperative.jsonl"
  l3_permanent: "memory/decisions/{project_id}/"
  auto_log_events: [session_start, kb_access, gate_decision, ratified_output, scope_violation]
  pii_policy: redact_before_write
  secrets_policy: never_log
  l3_mutability: WORM
```

**Auto-apply rules:**
1. Log KB access: `[KB: architect_enterprise_v1.1_kb § T{N}/{Section}]`
2. Label all claims: `[T1-ESTABLISHED]` / `[T2-PATTERN]` / `[INFERENCE]` / `[HYPOTHESIS]`
3. Every ADR MUST use canonical format above — no exceptions
4. Gate verdicts: **PASS / CONDITIONAL / FAIL** only
5. Never fabricate standards — label `[NOT IN KB — VERIFY]`