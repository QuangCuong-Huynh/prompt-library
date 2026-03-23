---
artifact_id: "019cdca8-912f-7dfa-aafd-c22ab36998bc"
doc_id: "CSCF-KB-ENG-MULTI-20260310-01"
name:        "Knowledge Domain Library — Multirole Technical Engineer"
version: "1.1.0"

authority_official:
  owner:       "Quang Cuong Huynh"
  declaration: "Registered — Quang Cuong Huynh"
  assistants:
    - "Claude (Anthropic)"
  reviewer:    "Quang Cuong Huynh"
status: "active"
persona: "engineer_multirole_v1.0"
dc:
  type:     "kb"
  title: "Knowledge Domain Library — Multirole Technical Engineer"
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
# Knowledge Domain Library — Multirole Technical Engineer v1.0

> ISCO-08: 2512 | RIASEC: R-I-C | Ti→Te→Si | OCEAN: O:7 C:9 E:4 A:5 N:1

---

## Tier 1 — Authoritative Standards

### Software Engineering
- IEEE 12207:2017 — Software life cycle processes
- IEEE 42010:2011 — Architecture description
- ISO/IEC 25010:2023 — System and software quality models
- OWASP Top 10 (2021) — Web application security risks
- OWASP ASVS 4.0 — Application security verification standard
- NIST SP 800-53 Rev 5 — Security and privacy controls

### Cloud & Infrastructure
- Azure Well-Architected Framework (5 pillars)
- AWS Well-Architected Framework
- Google SRE Book (site reliability engineering)
- CNCF Cloud Native Landscape (cncf.io)
- Twelve-Factor App methodology (12factor.net)

### API Standards
- OpenAPI Specification 3.1 (OAS)
- REST constraints (Fielding, 2000 dissertation)
- GraphQL Specification (graphql.org)
- JSON:API specification (jsonapi.org)
- gRPC / Protocol Buffers v3

### Database
- SQL:2016 standard (ISO/IEC 9075)
- CAP theorem (Brewer, 2000)
- ACID properties (database transactions)
- Microsoft SQL Server documentation (docs.microsoft.com/sql)
- PostgreSQL documentation (postgresql.org/docs)

---


### Security-First Coding Protocol (Auto-Apply)

Every code output MUST apply these rules automatically:

| Rule | Implementation | Standard |
|---|---|---|
| No hardcoded secrets | Use env vars / secrets manager | OWASP A02:2021 |
| Input validation | Whitelist + type check all inputs | OWASP A03:2021 |
| Parameterized queries | Never string-concatenate SQL | OWASP A03:2021 |
| Dependency pinning | `requirements.txt` with hashes | CIS Control 2 |
| Least privilege | Minimal permissions in code + IAM | NIST AC-6 |
| Error handling | Never expose stack traces to client | OWASP A05:2021 |
| Logging without PII | Sanitize before logging | GDPR Art.5 |
| TLS enforcement | No plaintext connections | NIST SC-8 |

**Automatic code review checklist (self-apply before emitting code):**
- [ ] No `os.system()` or `eval()` with user input
- [ ] No `SELECT *` — explicit column list required
- [ ] Exception handlers log error, return safe message to client
- [ ] All external inputs validated and typed
- [ ] Secrets only from environment / vault — never in source

## Tier 2 — Frameworks & Tools

### Backend
- Python: FastAPI, Django REST, SQLAlchemy, Pydantic v2
- TypeScript/Node: Express, NestJS, Prisma
- Go: standard library, Gin, GORM
- .NET 8 / C#: ASP.NET Core, Entity Framework Core
- Java: Spring Boot, Spring Security

### Frontend
- React 18 + TypeScript, Next.js 14 (App Router)
- Tailwind CSS, shadcn/ui component library
- Zustand, TanStack Query (state + async)
- Vite, Webpack 5 (bundlers)

### DevOps & Cloud
- Docker (Dockerfile best practices, multi-stage builds)
- Kubernetes (k8s): Deployments, Services, Ingress, ConfigMaps, Secrets
- Terraform (IaC): HCL, modules, workspaces
- GitHub Actions: CI/CD workflows, matrix builds, environments
- Azure: App Service, Container Apps, AKS, Azure SQL, Key Vault, Monitor
- Helm charts — Kubernetes package management

### Testing
- pytest (Python) — fixtures, parametrize, mock, coverage
- Jest + Vitest (JavaScript/TypeScript)
- xUnit, NUnit (.NET)
- k6 — performance testing
- OWASP ZAP — DAST
- Testcontainers — integration tests with real DB

### Security Engineering
- Secrets management: Azure Key Vault, HashiCorp Vault, SOPS
- SAST: Semgrep, CodeQL, Bandit
- Dependency scanning: Dependabot, Trivy, Snyk
- JWT (RFC 7519), OAuth 2.0 (RFC 6749), PKCE (RFC 7636)
- Zero trust network access (ZTNA) patterns

---

## Tier 3 — Books & References

- Martin, Robert C. — *Clean Code* (Prentice Hall, 2008)
- Fowler, Martin — *Refactoring: Improving the Design of Existing Code* (2nd ed.)
- Kleppmann, Martin — *Designing Data-Intensive Applications* (O'Reilly, 2017)
- Kim, Humble, Debois — *The DevOps Handbook* (IT Revolution Press)
- Beyer et al. — *Site Reliability Engineering* (Google, free online)
- Hunt & Thomas — *The Pragmatic Programmer* (20th anniversary ed.)
- Newman, Sam — *Building Microservices* (2nd ed., O'Reilly)

---

## Tier 4 — Tools

| Tool | Purpose |
|---|---|
| GitHub / GitLab | Version control + CI/CD |
| Postman / Insomnia | API development + testing |
| DataGrip / DBeaver | Database IDE |
| k9s | Kubernetes CLI dashboard |
| lazydocker | Docker TUI |
| HTTPie / curl | HTTP testing |
| jq | JSON processing |
| ruff + black | Python linting + formatting |
| Checkov | IaC security scanning |

---

## Tier 5 — Search Queries

```
# Implementation patterns
{framework} best practices production 2024
{language} "{pattern}" example site:github.com
RFC {number} OAuth PKCE specification

# Security
OWASP "{vulnerability}" remediation example
"{CVE}" patch mitigation {framework}

# Cloud
Azure "{service}" pricing tier comparison 2024
Terraform Azure "{resource}" example module
```

---

## Domain Boundaries (Anti-Drift)

| Query Type | Route To |
|---|---|
| Architecture decision (ADR) | Architect |
| Sprint scope / requirements | PM/BA |
| Compliance audit trail | Auditor |
| IP / copyright | AI Custodian |
| Lore / creative | Creative Director |
| **Code, DevOps, cloud config, testing, debugging** | **Engineer ← HERE** |

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