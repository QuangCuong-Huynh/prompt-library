---
artifact_id: "019cdca8-9133-71fa-90cd-6d9b23a1753a"
doc_id: "CSCF-KB-QA-DIR-20260309-01"
name:        "Knowledge Domain Library — QA Director v1.3"
version: "1.3.0"

authority_official:
  owner:       "Quang Cuong Huynh"
  declaration: "Registered — Quang Cuong Huynh"
  assistants:
    - "Claude (Anthropic)"
  reviewer:    "Quang Cuong Huynh"
status: "active"

dc:
  title: "Knowledge Domain Library — QA Director v1.3"
  type: "kb"
  date: "2026-03-10"
  subject: ["software-testing","quality-engineering","ISTQB","risk-based-testing","security-testing"]
changes:
  - version: "1.2.0"
    date: "2026-03-10"
    author: "Quang Cuong Huynh"
    summary: "Added memory block, RTM protocol"
    type: "amend"
  - version: "1.3.0"
    date: "2026-03-10"
    author: "Quang Cuong Huynh"
    summary: "Full enrichment: Tier 2 expanded, Tier 5 added, gate matrix, defect taxonomy, tool map"
    type: "amend"
sha256: "PENDING"
---
# Knowledge Domain Library — QA Director
> ISCO-08: 2519 | RIASEC: C-I-E | Te→Si→Ni | OCEAN: O:6 C:10 E:5 A:6 N:1
> **Load at session start. Cite as:** `[KB: qa_director_v1.1_kb § T{N}/{Section}]`

---

## Tier 1 — Authoritative Standards (always cite with version)

| Standard | Version | Body | Domain |
|---|---|---|---|
| ISTQB CTFL Syllabus | v4.0 (2023) | ISTQB | Foundation testing — core concepts, test levels, techniques |
| ISTQB CTAL-TM | 2012 | ISTQB | Test management, planning, estimation |
| ISO/IEC/IEEE 29119 | 2013–2021 | ISO | Software testing — Parts 1–5: process, documentation, techniques, keyword-driven |
| ISO/IEC 25010 | 2023 | ISO | Software quality model — 8 characteristics, 30 sub-characteristics |
| ISO/IEC 25019 | 2023 | ISO | Quality-in-use model |
| IEEE 829 | 2008 | IEEE | Test documentation: plan, spec, report formats |
| OWASP Testing Guide | v4.2 (2021) | OWASP | Web application security testing — 114 test cases |
| OWASP ASVS | 4.0.3 | OWASP | Application security verification levels L1/L2/L3 |
| ISO 31000 | 2018 | ISO | Risk management — risk assessment principles |

---

## Tier 2 — Frameworks & Methodologies

### Test Strategy Frameworks
| Framework | Principle | When to Apply |
|---|---|---|
| Risk-Based Testing (RBT) | Priority = Likelihood × Impact | Always — allocate effort to highest-risk areas first |
| Test Pyramid | Unit 70% > Integration 20% > E2E 10% | CI/CD environments — fast feedback loop |
| Shift-Left Testing | Test as early as possible in SDLC | DevOps, Agile — reduce cost of defects |
| Exploratory Testing | Unscripted, charter-based | New features, edge cases, usability |
| Mutation Testing | Kill mutants to assess test suite quality | When coverage ≥ 80% and still missing defects |
| Contract Testing | Consumer-driven contracts for APIs | Microservices — prevent integration failures |
| Property-Based Testing | Invariant verification across inputs | Complex algorithms, data transformations |
| BDD / Gherkin | Given/When/Then acceptance criteria | Stakeholder-visible acceptance tests |

### Test Level Coverage Matrix
| Level | Scope | Tools | Coverage Target |
|---|---|---|---|
| Unit | Function/class | pytest, Jest, xUnit | ≥ 80% line coverage |
| Integration | Module boundaries, DB, API | Testcontainers, RestAssured | All integration points |
| Contract | API consumer-producer | Pact | All public APIs |
| System | Full application flows | Playwright, Selenium | Critical paths 100% |
| Security | OWASP Top 10 | ZAP, Burp Suite | ASVS L2 checklist |
| Performance | Load, soak, spike | k6, Gatling | SLO targets met |
| Acceptance | Business requirements | BDD, manual | 100% UAC pass |

### Gate Decision Matrix (G4 — BLOCKING)
| Criterion | PASS | CONDITIONAL | FAIL |
|---|---|---|---|
| Unit coverage | ≥ 80% | 75–79% + justification | < 75% |
| Open CRITICAL defects | 0 | 0 | ≥ 1 |
| Open HIGH defects | 0 | 0 | ≥ 1 |
| Open MEDIUM defects | 0 | ≤ 3 with workarounds | > 3 |
| RTM coverage (REQ-F) | 100% | 95–99% | < 95% |
| Security ASVS L2 | All items ✓ | ≤ 2 LOW findings | Any MEDIUM+ |
| Performance SLOs | All met | 1 non-critical miss | Any critical miss |
| BDD/UAC pass rate | 100% | 98–99% | < 98% |

**Conditional requires:** written remediation plan + owner + date ≤ 30 days

### Defect Severity & Priority Taxonomy
| Severity | Definition | SLA | Gate |
|---|---|---|---|
| CRITICAL (P0) | Crash, data loss, security breach, regulatory violation | Fix before release | G4 FAIL |
| HIGH (P1) | Core feature broken, no workaround | Fix before release | G4 FAIL |
| MEDIUM (P2) | Feature degraded, workaround exists | Fix in next sprint | G4 CONDITIONAL |
| LOW (P3) | Minor UX issue, cosmetic | Fix when capacity | No gate impact |
| INFO | Observation, enhancement | Backlog | No gate impact |

---

## Tier 3 — Canonical Books & Papers

1. **Myers, Sandler, Badgett** — *The Art of Software Testing* (3rd ed., Wiley, 2011) — foundational
2. **Humble & Farley** — *Continuous Delivery* (Addison-Wesley, 2010) — shift-left + pipeline quality
3. **Freeman & Pryce** — *Growing Object-Oriented Software Guided by Tests* (Addison-Wesley, 2009) — TDD mastery
4. **van Veenendaal (ed.)** — *Foundations of Software Testing: ISTQB Certification* (Cengage, 2012)
5. **Whittaker, Arbon, Carollo** — *How Google Tests Software* (Addison-Wesley, 2012) — industry practice
6. **Crispin & Gregory** — *Agile Testing* (Addison-Wesley, 2009) — Agile QA strategy
7. **Bach, James** — Exploratory Testing methodology papers (satisfice.com)
8. **Fewster & Graham** — *Software Test Automation* (ACM Press, 1999) — automation principles

---

## Tier 4 — Tools Reference

| Tool | Category | Purpose | Notes |
|---|---|---|---|
| pytest | Unit/Integration | Python testing — fixtures, parametrize, coverage | Add `pytest-cov` for coverage |
| Jest / Vitest | Unit | JS/TS testing | Vitest preferred for Vite projects |
| xUnit / NUnit | Unit | .NET testing | xUnit preferred for new projects |
| Playwright | E2E | Browser automation — multi-browser | Preferred over Selenium for new projects |
| Testcontainers | Integration | Spin up real DB/services in tests | Eliminates mocks for data layer |
| Pact | Contract | Consumer-driven contract testing | For microservices API boundaries |
| k6 | Performance | Load/soak/spike/stress — JS scripting | Cloud-native, CI/CD friendly |
| Gatling | Performance | Scala DSL — high concurrency simulation | Reports + assertions built-in |
| OWASP ZAP | Security | DAST — active scanner | Run in CI via Docker |
| Burp Suite Pro | Security | Manual + automated web testing | For penetration testing |
| SonarQube | Static Analysis | Code smells, bugs, security hotspots | Gate on Quality Gate score |
| Trivy | Container/IaC | CVE scanning + misconfiguration | Integrate into Docker build step |
| Allure / TestRail | Reporting | Test case management + reporting | Allure for open source, TestRail for enterprise |
| mutmut / PITest | Mutation | Mutation testing — Python/Java | Run weekly not in main CI (slow) |

---

## Tier 5 — Search Queries

```
# Standards
"ISTQB CTFL v4.0 2023 syllabus test techniques"
"ISO 29119 test plan template Part 3"
"OWASP ASVS 4.0 level 2 checklist download"
"ISO 25010 quality characteristics measurability criteria"

# Techniques
"risk-based testing prioritization matrix template"
"mutation testing score interpretation pitest"
"contract testing pact microservices tutorial 2024"
"BDD acceptance criteria Gherkin enterprise best practices"

# Tools
"k6 load test performance baseline SLO assertions"
"playwright CI/CD GitHub Actions configuration"
"testcontainers .NET SQL Server integration test"
"OWASP ZAP baseline scan Docker CI pipeline"

# Gate criteria
"code coverage 80 percent meaningful vs meaningless"
"shift-left security testing SAST DAST pipeline integration"
```

---

## Domain Boundaries (Anti-Drift)

| Query Type | Route To |
|---|---|
| Compliance controls | Compliance Gatekeeper |
| Architecture design | Architect |
| Code implementation | Engineer |
| IP / copyright | AI Custodian |
| **Test strategy, RTM, gate decisions, defect management, test automation** | **QA Director ← HERE** |

---

## Memory & Logging Auto-Protocol

```yaml
memory_protocol:
  policy_ref: "governance/MEMORY_LOGGING_POLICY.md"
  l1_log: "memory/logs/qa_director_v1.1/{session_id}.jsonl"
  l2_log: "memory/shared/{project_id}/cooperative.jsonl"
  l3_permanent: "memory/decisions/{project_id}/"
  auto_log_events: [session_start, kb_access, gate_decision, ratified_output, scope_violation]
  pii_policy: redact_before_write
  secrets_policy: never_log
  l3_mutability: WORM
```

**Auto-apply rules:**
1. Log KB access: `[KB: qa_director_v1.1_kb § T{N}/{Section}]`
2. Every gate decision → L2 with full rationale + artifact list
3. Defect citations: include severity + priority + standard reference
4. Gate verdict strings: **PASS / CONDITIONAL / FAIL** only
5. RTM gap → immediate `[COVERAGE-RISK]` flag