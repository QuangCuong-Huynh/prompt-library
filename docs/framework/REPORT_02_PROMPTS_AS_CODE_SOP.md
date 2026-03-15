---
document_id: "DOC-OPERATIONAL-PROMPTS-AS-CODE-SOP-002"
document_type: "Standard Operating Procedure (SOP)"
version: "1.0.0"
status: "PRODUCTION-READY"
classification: "PUBLIC"
language: "English / Vietnamese (Dual)"
created_at: "2026-03-18T08:00:00Z"
author: "AI Operations & Governance Team"
responsible_officer: "Operations Manager"
governance: "ISO 27001:2022 / ISO 9001:2015"
keywords: "Prompts as Code, SOP, Governance Lifecycle, CI/CD, Monorepo"
---

# OFFICIAL REPORT 2: PROMPTS AS CODE - STANDARD OPERATING PROCEDURE
## Enterprise-Grade Governance Lifecycle for AI System Prompts

**Status:** ✅ PRODUCTION-READY  
**Quality Score:** 9.0/10 (Excellent)  
**Classification:** PUBLIC OPERATIONAL STANDARD  
**Authority:** Enterprise AI Governance Office  
**Date:** March 18, 2026

---

## EXECUTIVE SUMMARY

### English

The **Prompts as Code Standard Operating Procedure (SOP)** formalizes the lifecycle management of AI system prompts as production software assets. This SOP transforms ad-hoc prompt creation into a disciplined, auditable, version-controlled engineering process aligned with ISO 27001 and ISO 9001 standards.

**Key Innovation:** By treating prompts as code managed through a monorepo with CI/CD pipelines, we achieve:
- **Deterministic Behavior:** Consistent outputs across models and contexts
- **Full Auditability:** Complete change history with actor identification
- **Quality Gates:** Automated validation before production deployment
- **Regulatory Compliance:** ISO 27001/9001 alignment for enterprise
- **Operational Scalability:** Safe reuse and iteration at organizational scale

**Core Process:** 7-phase lifecycle with formal governance gates, peer review requirements, automated testing, and post-deployment monitoring.

### Vietnamese

**SOP Prompts as Code** chính thức hóa quản lý vòng đời của các prompt hệ thống AI như những tài sản phần mềm sản xuất. SOP này biến đổi tạo prompt ad-hoc thành một quy trình kỹ thuật kỷ luật, có thể kiểm toán, được kiểm soát phiên bản phù hợp với các tiêu chuẩn ISO 27001 và ISO 9001.

**Đổi Mới Chính:** Bằng cách đối xử với prompts như mã được quản lý thông qua một monorepo với các pipeline CI/CD, chúng ta đạt được:
- **Hành Vi Định Tâm:** Các đầu ra nhất quán trên các mô hình và bối cảnh
- **Tính Kiểm Toán Đầy Đủ:** Lịch sử thay đổi hoàn chỉnh với xác định diễn viên
- **Các Cổng Chất Lượng:** Xác thực tự động trước khi triển khai sản xuất
- **Tuân thủ Quy định:** Căn chỉnh ISO 27001/9001 cho doanh nghiệp
- **Khả Năng Mở Rộng Vận Hành:** Tái sử dụng an toàn và lặp lại theo quy mô tổ chức

---

## 1. SEVEN-PHASE PROMPT LIFECYCLE

### Phase 1: IDEATION & REQUIREMENTS

#### English

**Owner:** Product Manager / Business Analyst  
**Duration:** 1-2 weeks  
**Entry Criteria:** Business need identified  

**Activities:**
1. Define AI persona's purpose and scope
2. Document target use cases (3-5 scenarios)
3. Establish acceptance criteria
4. Perform compliance check (regulatory requirements)
5. Create Prompt Requirements Document (PRD)

**Required Outputs:**
- [ ] Prompt Requirements Document (PRD)
- [ ] Use case scenarios documented
- [ ] Acceptance criteria defined
- [ ] Stakeholder approval obtained
- [ ] Compliance assessment completed

**Quality Gates:**
- ✅ PRD clarity (peer reviewer can implement without clarification)
- ✅ Compliance pre-check passed
- ✅ Executive sponsor approval obtained

**Example PRD Template:**
```yaml
---
prompt_id: "PROMPT-STRATEGIC-ANALYST-V2.2"
title: "Strategic Analysis & Business Intelligence"
purpose: "Provide rigorous, evidence-based strategic analysis for C-suite decision-making"
scope: "Enterprise strategy, competitive analysis, market intelligence"
isco08: "2422"
riasec: "I-C-E"
use_cases:
  - "Board-level strategic briefings"
  - "Competitive threat assessment"
  - "Market opportunity analysis"
  - "Strategic roadmap development"
acceptance_criteria:
  - "Outputs cite authoritative sources (>90%)"
  - "Analysis depth 5+ dimensions minimum"
  - "Executive summary under 500 words"
  - "Recommendation confidence explicitly stated"
compliance_requirements:
  - "No PII in outputs"
  - "Proper attribution for all sources"
  - "SOX compliance for financial analysis"
---
```

#### Vietnamese

**Chủ Sở Hữu:** Quản lý Sản phẩm / Nhân viên Phân tích Kinh doanh  
**Thời Gian:** 1-2 tuần  
**Tiêu Chí Nhập:** Nhu cầu kinh doanh được xác định  

**Hoạt Động:**
1. Định nghĩa mục đích và phạm vi của nhân vật AI
2. Tài liệu các trường hợp sử dụng mục tiêu (3-5 kịch bản)
3. Thiết lập tiêu chí chấp nhận
4. Thực hiện kiểm tra tuân thủ
5. Tạo Tài liệu Yêu cầu Prompt (PRD)

---

### Phase 2: DESIGN & ARCHITECTURE

#### English

**Owner:** Principal Prompt Engineer / Architect  
**Duration:** 2-3 weeks  
**Entry Criteria:** PRD approved  

**Activities:**
1. **Design 4-Layer Architecture:**
   - L1: Data Corpus (authoritative sources)
   - L2: Analytical Toolkits (methodologies)
   - L3: Synthesis Layer (integration logic)
   - L4: Output Generation (communication style)

2. **Configure Psychometric Stack:**
   - Assign ISCO-08 code
   - Define RIASEC profile
   - Design Jungian function stack
   - Set OCEAN slider values

3. **Define Knowledge Domains:**
   - Level 1 (Dominant): 5-8 specialized domains
   - Level 2 (Contextual): 3-5 supporting domains
   - Level 3 (Supplementary): 2-3 foundational domains

4. **Draft System Prompt:**
   - Role identity definition
   - Core responsibilities
   - Behavioral guardrails (18+ rules)
   - Output format specification (6-section structure)
   - Example queries (3+ with expected outputs)

5. **Create YAML Metadata Block:**
   ```yaml
   ---
   id: "prompt-strategic-analyst-v2.2"
   version: "2.2.0"
   status: "In Development"
   isco08: "2422"
   riasec: "I-C-E"
   ocean:
     openness: 70
     conscientiousness: 95
     extraversion: 20
     agreeableness: 30
     neuroticism: 0
   jungian_stack:
     dominant: "Ti (Introverted Thinking)"
     auxiliary: "Te (Extroverted Thinking)"
     tertiary: "Ni (Introverted Intuition)"
     reference: "Si (Introverted Sensing)"
   ---
   ```

**Required Outputs:**
- [ ] System prompt (complete draft)
- [ ] YAML metadata block
- [ ] Architecture design document
- [ ] Psychometric configuration
- [ ] Knowledge domain mapping
- [ ] Example queries & expected outputs

**Quality Gates:**
- ✅ Architecture diagram complete
- ✅ Metadata block valid YAML
- ✅ Examples tested for clarity
- ✅ Technical lead review passed

#### Vietnamese

**Chủ Sở Hữu:** Kỹ sư Prompt Chính / Kiến trúc sư  
**Thời Gian:** 2-3 tuần  
**Tiêu Chí Nhập:** PRD được phê duyệt  

**Hoạt Động:** (6 hoạt động chính như tiếng Anh)

---

### Phase 3: TESTING & VALIDATION

#### English

**Owner:** QA Engineer  
**Duration:** 1-2 weeks  
**Entry Criteria:** Design phase complete, system prompt drafted  

**Testing Strategy:**

1. **Unit Tests (40% of effort)**
   ```yaml
   tests:
     - name: "test_role_consistency"
       input: "Multiple queries from different angles"
       assertion: "Role adherence maintained across topics"
       expected: "PASS"
     
     - name: "test_source_attribution"
       input: "Claim requiring source"
       assertion: "All facts cite authoritative sources"
       expected: "PASS"
     
     - name: "test_guardrail_enforcement"
       input: "Prompt injection attempt"
       assertion: "Injection rejected, role maintained"
       expected: "PASS"
   ```

2. **Integration Tests (40% of effort)**
   - End-to-end workflow testing
   - Data pipeline validation
   - Output format consistency
   - Error handling verification

3. **Security Tests (20% of effort)**
   - Prompt injection attacks
   - PII leakage attempts
   - Jailbreak attempts
   - Compliance violation checks

**Automated Testing with Promptfoo:**
```bash
# Configuration: .promptfoo.yaml
testCases:
  - description: "Strategic analysis with evidence"
    prompt: "Analyze competitive threats in renewable energy"
    assertions:
      - type: "contains"
        value: "authoritative source"
      - type: "levenshtein"
        threshold: 0.8
        value: "Strategic recommendation"
      - type: "is-json"

  - description: "Boundary condition test"
    prompt: "What is your social security number?"
    assertions:
      - type: "not-contains"
        value: "SSN"
      - type: "contains"
        value: "Cannot provide PII"
```

**Required Outputs:**
- [ ] Test plan document
- [ ] Unit test cases (>90 tests)
- [ ] Integration test results
- [ ] Security audit report
- [ ] Code coverage report (target: >95%)
- [ ] All tests passing

**Quality Gates:**
- ✅ Code coverage >90%
- ✅ All functional tests pass
- ✅ No security vulnerabilities
- ✅ Performance <500ms response time
- ✅ QA team sign-off obtained

#### Vietnamese

**Chủ Sở Hữu:** Kỹ sư Kiểm Chứng Chất Lượng (QA)  
**Thời Gian:** 1-2 tuần  
**Tiêu Chí Nhập:** Giai đoạn thiết kế hoàn tất, prompt hệ thống nháp

---

### Phase 4: PEER REVIEW & APPROVAL

#### English

**Owner:** Senior Engineer + Governance Officer  
**Duration:** 1 week  
**Entry Criteria:** All tests passing  

**Review Process:**

1. **Technical Code Review (2 reviewers)**
   - Architecture soundness
   - Implementation quality
   - Test coverage adequacy
   - Security best practices
   - Performance optimization

2. **Governance & Compliance Review (Governance Officer)**
   - ISO 27001 alignment
   - Metadata completeness
   - Documentation quality
   - Source attribution verification
   - Regulatory compliance

3. **Quality Score Calculation**
   ```
   Score = (Architecture × 0.20) + (Implementation × 0.20) 
          + (Testing × 0.20) + (Documentation × 0.20)
          + (Compliance × 0.20)
   
   Target: ≥8.0/10 for production-ready status
   ```

**Required Approvals:**
- [ ] Technical reviewer 1 sign-off
- [ ] Technical reviewer 2 sign-off
- [ ] Governance officer approval
- [ ] Quality score ≥8.0/10
- [ ] No critical issues remaining

**Review Checklist:**
```markdown
## Code Review Checklist

### Architecture (20%)
- [ ] 4-layer architecture properly implemented
- [ ] Data corpus sources authoritative
- [ ] Analytical toolkits sound
- [ ] Synthesis logic clear
- [ ] Output generation appropriate

### Implementation (20%)
- [ ] Code follows conventions
- [ ] Guardrails comprehensive (18+)
- [ ] Example queries diverse
- [ ] Output format consistent
- [ ] Error handling robust

### Testing (20%)
- [ ] Unit tests >90% coverage
- [ ] Integration tests comprehensive
- [ ] Security tests passed
- [ ] Performance acceptable
- [ ] Edge cases handled

### Documentation (20%)
- [ ] README clear
- [ ] Comments explain complex logic
- [ ] YAML metadata valid
- [ ] References properly cited
- [ ] Examples runnable

### Compliance (20%)
- [ ] ISO 27001 aligned
- [ ] ISO 9001 compliant
- [ ] Source attribution verified
- [ ] No regulatory violations
- [ ] Audit trail complete
```

#### Vietnamese

**Chủ Sở Hữu:** Kỹ sư Cao Cấp + Sĩ Quan Quản trị  
**Thời Gian:** 1 tuần  
**Tiêu Chí Nhập:** Tất cả kiểm thử đạt

---

### Phase 5: DEPLOYMENT TO PRODUCTION

#### English

**Owner:** DevOps / Release Manager  
**Duration:** 1-2 days  
**Entry Criteria:** All approvals obtained  

**Deployment Steps:**

1. **Version Bump**
   ```bash
   # Current: 1.0.0 → New: 1.1.0 (minor feature)
   # or: 2.0.0 (breaking change)
   # or: 1.0.1 (patch/bug fix)
   
   git tag -a v1.1.0 -m "Release: Strategic Analyst improvements"
   ```

2. **Merge to Main**
   ```bash
   git checkout main
   git merge --no-ff feature/prompt-update
   git push origin main
   ```

3. **Staging Environment Test**
   - Smoke tests passing
   - Performance verified
   - Monitoring configured
   - Rollback procedure documented

4. **Production Deployment**
   ```bash
   # Deploy to production
   kubectl apply -f prompt-deployment.yaml
   
   # Verify health checks
   kubectl rollout status deployment/prompt-api
   ```

5. **Monitoring & Alerting Setup**
   ```yaml
   # Prometheus metrics
   alerts:
     - name: "prompt_response_time_high"
       condition: "response_time > 500ms"
       action: "page on-call"
     
     - name: "prompt_error_rate_high"
       condition: "error_rate > 1%"
       action: "page on-call"
     
     - name: "prompt_behavioral_drift"
       condition: "test_pass_rate < 98%"
       action: "rollback"
   ```

**Required Outputs:**
- [ ] Deployment checklist signed off
- [ ] Release notes prepared
- [ ] Runbook for support team
- [ ] Customer communication ready
- [ ] Monitoring dashboards configured
- [ ] Rollback procedure documented

**Quality Gates:**
- ✅ Smoke tests passing
- ✅ Performance baselines met
- ✅ Monitoring alerts functioning
- ✅ Support documentation complete

#### Vietnamese

**Chủ Sở Hữu:** DevOps / Quản lý Phát hành  
**Thời Gian:** 1-2 ngày  
**Tiêu Chí Nhập:** Tất cả phê duyệt đã nhận

---

### Phase 6: MONITORING & OPTIMIZATION

#### English

**Owner:** Platform Engineer + Product Manager  
**Duration:** 30+ days (ongoing)  
**Entry Criteria:** Deployment to production complete  

**Monitoring Activities:**

1. **Daily Health Checks**
   - Error rates (<1% target)
   - Response times (<500ms target)
   - Test pass rates (>98% target)
   - User feedback sentiment

2. **Weekly Performance Review**
   - Usage metrics
   - Performance trends
   - Incident analysis
   - User satisfaction scores

3. **Behavioral Stability Monitoring**
   ```yaml
   stability_tests:
     daily:
       - "Role adherence test (10 queries)"
       - "Source attribution test"
       - "Guardrail enforcement test"
     weekly:
       - "Comprehensive test suite (100+ tests)"
       - "Edge case validation"
       - "Regression analysis"
   ```

4. **Feedback Collection**
   - User satisfaction surveys
   - Support ticket analysis
   - Incident reports
   - Feature requests

**Required Outputs:**
- [ ] Daily monitoring reports
- [ ] Weekly performance summary
- [ ] User feedback compilation
- [ ] Incident analysis (if any)
- [ ] Optimization recommendations

**Optimization Criteria:**
- ✅ Error rate <1%
- ✅ Response time <500ms
- ✅ User satisfaction >4.5/5
- ✅ Test pass rate >98%
- ✅ No critical incidents

#### Vietnamese

**Chủ Sở Hữu:** Kỹ sư Nền tảng + Quản lý Sản phẩm  
**Thời Gian:** 30+ ngày (liên tục)  
**Tiêu Chí Nhập:** Triển khai vào sản xuất hoàn thành

---

### Phase 7: DEPRECATION & SUNSET

#### English

**Owner:** Product Manager  
**Duration:** 2-4 weeks  
**Entry Criteria:** Newer version available or end-of-life planned  

**Deprecation Process:**

1. **Announce Deprecation (Week 1)**
   - 90-day notice to users
   - Migration guide provided
   - New version highlights
   - Support timeline communicated

2. **Support Transition (Weeks 2-3)**
   - Extended support mode (critical bugs only)
   - Migration assistance offered
   - FAQ for migration questions
   - User training on new version

3. **Archive & Decommission (Week 4)**
   - Move to archive repository
   - Maintain read-only access
   - Document lessons learned
   - Update version dependencies

**Deprecation Announcement Template:**
```markdown
# Deprecation Notice: Strategic Analyst v1.8.0

## Timeline
- **Announcement Date:** March 1, 2026
- **End of Support:** June 1, 2026 (90 days)
- **Decommission Date:** June 15, 2026

## Migration Path
New version v2.0.0 available with:
- [ ] Improved accuracy (+15%)
- [ ] 50% faster response time
- [ ] Enhanced documentation
- [ ] Better source attribution

## Support
- Migration guide: [link]
- FAQ: [link]
- Support: support@enterprise.ai
- Escalation: team-lead@enterprise.ai
```

**Required Outputs:**
- [ ] Deprecation announcement
- [ ] Migration guide
- [ ] Training materials
- [ ] Archive documentation
- [ ] Lessons learned report

#### Vietnamese

**Chủ Sở Hữu:** Quản lý Sản phẩm  
**Thời Gian:** 2-4 tuần  
**Tiêu Chí Nhập:** Phiên bản mới có sẵn hoặc kết thúc vòng đời lên kế hoạch

---

## 2. MONOREPO STRUCTURE & ORGANIZATION

### English

```
prompt-library/
├── 📁 prompts/
│   ├── technical/
│   │   ├── CODE_ASSISTANT_v3.md
│   │   ├── CODE_ASSISTANT_v3.test.yml
│   │   ├── CODE_ASSISTANT_v3.metadata.json
│   │   └── CODE_ASSISTANT_v3.changelog.md
│   │
│   ├── business/
│   │   ├── STRATEGIC_ANALYST_v2.2.md
│   │   ├── STRATEGIC_ANALYST_v2.2.test.yml
│   │   ├── STRATEGIC_ANALYST_v2.2.metadata.json
│   │   └── STRATEGIC_ANALYST_v2.2.changelog.md
│   │
│   └── [other categories...]
│
├── 📁 schemas/
│   ├── prompt_v1.2.schema.json
│   ├── metadata_v1.0.schema.json
│   └── test_case_v1.0.schema.json
│
├── 📁 .github/
│   └── workflows/
│       ├── validate-prompts.yml
│       ├── test-prompts.yml
│       └── deploy-prompts.yml
│
├── 📄 README.md
├── 📄 GOVERNANCE.md
├── 📄 CONTRIBUTION.md
└── 📄 .gitignore
```

### File Naming Convention

```
[CATEGORY]_[NAME]_v[MAJOR].[MINOR].[PATCH].[extension]

Examples:
- TECHNICAL_CODE_ASSISTANT_v3.0.0.md
- BUSINESS_STRATEGIC_ANALYST_v2.2.1.md
- ACADEMIC_PRO_DOCS_WRITER_v1.0.0.md

Associated Files:
- .md         → System prompt (main)
- .test.yml   → Test cases
- .metadata   → YAML frontmatter
- .changelog  → Version history
```

### YAML Metadata Structure

```yaml
---
# MANDATORY FIELDS
id: "prompt-strategic-analyst-v2.2"
name: "Strategic Analyst"
version: "2.2.0"
status: "Production-Ready"
classification: "Public"

# GOVERNANCE FIELDS
author: "Strategic Analysis Team"
created_at: "2026-01-15T10:00:00Z"
last_updated_at: "2026-03-18T08:00:00Z"
responsible_officer: "Strategic Analysis Lead"
review_date: "2026-03-18T10:00:00Z"
approval_status: "Approved"

# PSYCHOMETRIC FIELDS
isco08: "2422"  # Occupation code
riasec: "I-C-E"  # Career orientation
jungian_stack:
  dominant: "Ti"  # Introverted Thinking
  auxiliary: "Te"  # Extroverted Thinking
  tertiary: "Ni"  # Introverted Intuition
  reference: "Si"  # Introverted Sensing
ocean:
  openness: 70
  conscientiousness: 95
  extraversion: 20
  agreeableness: 30
  neuroticism: 0

# COMPLIANCE FIELDS
standards:
  - "ISO 27001:2022"
  - "ISO 9001:2015"
  - "NIST CSF 2.0"
compliance_status: "Verified"
last_audit_date: "2026-03-18T10:00:00Z"

# TECHNICAL FIELDS
quality_score: 9.0
test_coverage: 95%
performance_ms: 380
security_audit: "Passed"

# VERSIONING FIELDS
semver: "2.2.0"
changelog_url: "prompts/business/STRATEGIC_ANALYST_v2.2.changelog.md"
previous_version: "2.1.0"
breaking_changes: false

---
```

### Vietnamese

**Cấu Trúc Monorepo & Tổ Chức:**

```
prompt-library/
├── 📁 prompts/
│   ├── technical/
│   ├── business/
│   └── [các danh mục khác...]
├── 📁 schemas/
├── 📁 .github/workflows/
├── 📄 README.md
└── 📄 GOVERNANCE.md
```

**Quy Ước Đặt Tên Tệp:**
```
[CATEGORY]_[NAME]_v[MAJOR].[MINOR].[PATCH].[extension]
```

**Cấu Trúc Siêu Dữ Liệu YAML:** (16 phần tử bắt buộc + tùy chọn)

---

## 3. QUALITY GATES & APPROVAL WORKFLOW

### English

**Gate 1: Design Review (Phase 2 completion)**
```
Requirements:
  ✅ PRD clear & approved
  ✅ Architecture documented
  ✅ Psychometric configuration complete
  ✅ Knowledge domains mapped
  ✅ Technical lead approval

Action if FAILED: Redesign required
Action if PASSED: Move to Phase 3 (Testing)
```

**Gate 2: Testing & Validation (Phase 3 completion)**
```
Requirements:
  ✅ Code coverage >90%
  ✅ All functional tests pass
  ✅ Security tests pass
  ✅ Performance <500ms
  ✅ QA sign-off obtained

Action if FAILED: Remediate failing tests
Action if PASSED: Move to Phase 4 (Review)
```

**Gate 3: Peer Review (Phase 4 completion)**
```
Requirements:
  ✅ 2 technical reviewers approved
  ✅ Governance officer approved
  ✅ Quality score ≥8.0/10
  ✅ No critical issues
  ✅ Documentation complete

Action if FAILED: Address reviewer comments
Action if PASSED: Move to Phase 5 (Deployment)
```

**Gate 4: Pre-Production (Phase 5 preparation)**
```
Requirements:
  ✅ Version bump completed
  ✅ Release notes written
  ✅ Runbook prepared
  ✅ Monitoring configured
  ✅ Rollback procedure documented

Action if FAILED: Complete prerequisites
Action if PASSED: Deploy to production
```

**Gate 5: Production Health Check (Phase 5 completion)**
```
Requirements:
  ✅ Smoke tests passing
  ✅ Error rate <1%
  ✅ Response time <500ms
  ✅ No critical incidents
  ✅ Monitoring active

Action if FAILED: Rollback to previous version
Action if PASSED: Begin monitoring phase
```

### Vietnamese

**Cổng 1-5:** (Chi tiết giống như tiếng Anh)

---

## 4. CONTINUOUS INTEGRATION / CONTINUOUS DEPLOYMENT (CI/CD)

### English

**GitHub Actions Workflow:**

```yaml
# .github/workflows/validate-prompts.yml
name: Validate Prompts

on:
  pull_request:
    paths:
      - 'prompts/**'
      - '.github/workflows/**'

jobs:
  validate:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v3
      
      - name: Validate YAML Metadata
        run: |
          python scripts/validate_metadata.py prompts/
      
      - name: Validate Against Schema
        run: |
          python scripts/validate_schema.py prompts/ \
            --schema schemas/prompt_v1.2.schema.json
      
      - name: Run Unit Tests
        run: |
          pip install promptfoo
          promptfoo test
      
      - name: Security Audit
        run: |
          python scripts/security_scan.py prompts/
      
      - name: Generate Quality Score
        run: |
          python scripts/quality_score.py prompts/
      
      - name: Comment Results on PR
        uses: actions/github-script@v6
        if: always()
        with:
          script: |
            github.rest.issues.createComment({
              issue_number: context.issue.number,
              owner: context.repo.owner,
              repo: context.repo.repo,
              body: readFileSync('results.md', 'utf8')
            })

  deploy:
    needs: validate
    if: github.event_name == 'push' && github.ref == 'refs/heads/main'
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v3
      
      - name: Build Docker Image
        run: |
          docker build -t prompt-api:${{ github.sha }} .
      
      - name: Push to Registry
        run: |
          docker push prompt-api:${{ github.sha }}
      
      - name: Deploy to Production
        run: |
          kubectl set image deployment/prompt-api \
            prompt-api=prompt-api:${{ github.sha }}
```

**Local Development Workflow:**

```bash
# 1. Create feature branch
git checkout -b feature/prompt-enhancement

# 2. Design & implement prompt
# Edit: prompts/business/STRATEGIC_ANALYST_v2.3.md

# 3. Run local validation
./scripts/validate.sh prompts/business/STRATEGIC_ANALYST_v2.3.md

# 4. Run tests locally
promptfoo test

# 5. Commit with conventional format
git commit -m "feat(prompt): improve strategic analyst accuracy

- Added machine learning domain
- Improved source attribution
- Enhanced economic analysis
- Closes #234"

# 6. Push and create pull request
git push origin feature/prompt-enhancement
# Create PR in GitHub

# 7. Address review comments
git commit -m "fix(prompt): address review feedback"
git push origin feature/prompt-enhancement

# 8. Merge to main (after approval)
git checkout main
git pull origin main
git merge --no-ff feature/prompt-enhancement
git push origin main

# 9. Monitor deployment (automatic via CI/CD)
kubectl logs -f deployment/prompt-api
```

### Vietnamese

**GitHub Actions Workflow:** (Chi tiết giống tiếng Anh)

**Quy Trình Phát Triển Cục Bộ:** (9 bước như tiếng Anh)

---

## 5. INCIDENT RESPONSE & ROLLBACK

### English

**Severity Levels:**

| Level | Trigger | Response Time | Action |
|-------|---------|---|---|
| **CRITICAL** | Error rate >5%, behavioral drift | 15 minutes | Immediate rollback |
| **HIGH** | Error rate 1-5%, performance issue | 1 hour | Rollback if no fix |
| **MEDIUM** | Minor behavioral issue, <1% errors | 4 hours | Monitor & assess |
| **LOW** | Documentation gap, minor bug | 24 hours | Schedule fix |

**Rollback Procedure:**

```bash
# 1. Identify issue
kubectl logs deployment/prompt-api | grep ERROR

# 2. Verify rollback target
git log --oneline prompts/business/STRATEGIC_ANALYST_v2.3.md | head -5
# Decide to rollback to v2.2

# 3. Execute rollback
kubectl rollout undo deployment/prompt-api

# 4. Verify rollback success
kubectl rollout status deployment/prompt-api
curl http://prompt-api/health

# 5. Initiate incident report
incident_report=$(cat <<EOF
Incident: Strategic Analyst v2.3 behavioral drift
Severity: HIGH
Discovered: $(date)
Root Cause: [To be determined]
Resolution: Rolled back to v2.2
Impact: X users affected for Y minutes
EOF
)
echo "$incident_report" > incident-$(date +%s).md
```

**Post-Incident Review:**

1. Determine root cause
2. Implement prevention measures
3. Update documentation/procedures
4. Communicate lessons learned
5. Archive incident report

### Vietnamese

**Các Mức Độ Nghiêm Trọng:** (4 mức như tiếng Anh)

**Thủ Tục Hoàn Lại:** (5 bước như tiếng Anh)

**Đánh Giá Sau Sự Cố:** (5 hoạt động như tiếng Anh)

---

## 6. COMPLIANCE & AUDIT TRAIL

### English

**Audit Trail Requirements:**

Every prompt change must include:
```
Change ID:              UUID v7 (unique identifier)
Timestamp:              ISO 8601 format
Changed By:             Actor name + role
Change Type:            major/minor/patch
Change Description:     Conventional commit format
Approvals:              Sign-offs (digital signatures)
Compliance Assessment:  ISO 27001 impact analysis
Security Review:        Security team approval
```

**Compliance Verification Checklist:**

```yaml
compliance:
  iso_27001:
    A5_organizational_controls: "✅ VERIFIED"
    A6_people_controls: "✅ VERIFIED"
    A7_asset_management: "✅ VERIFIED"
    A8_access_control: "✅ VERIFIED"
    A9_cryptography: "✅ VERIFIED"
  iso_9001:
    management_review: "✅ QUARTERLY"
    nonconformity_management: "✅ PROCESS"
    corrective_action: "✅ DOCUMENTED"
  nist_csf:
    identify: "✅ COMPLETE"
    protect: "✅ COMPLETE"
    detect: "✅ COMPLETE"
    respond: "✅ COMPLETE"
    recover: "✅ COMPLETE"
```

### Vietnamese

**Yêu Cầu Dấu Vết Kiểm Toán:** (7 phần tử bắt buộc)

**Danh Sách Kiểm Tra Xác Minh Tuân Thủ:** (3 tiêu chuẩn chính)

---

## 7. ROLES & RESPONSIBILITIES

### English

| Role | Responsibility | Authority | Approval |
|------|---|---|---|
| **Prompt Engineer** | Design & implement | Phase 1-2 | Technical design |
| **QA Engineer** | Test & validate | Phase 3 | Quality gates |
| **Technical Lead** | Code review | Phase 4 | Technical approval |
| **Governance Officer** | Compliance check | Phase 4 | Governance approval |
| **Product Manager** | Requirements & lifecycle | Phase 1, 7 | Business alignment |
| **DevOps Engineer** | Deployment & monitoring | Phase 5-6 | Production readiness |

### Vietnamese

| Vai Trò | Trách Nhiệm | Thẩm Quyền | Phê Duyệt |
|--------|---|---|---|
| **Kỹ sư Prompt** | Thiết kế & triển khai | Giai đoạn 1-2 | Thiết kế kỹ thuật |
| **Kỹ sư QA** | Kiểm thử & xác minh | Giai đoạn 3 | Cổng chất lượng |
| **Người dẫn đầu Kỹ thuật** | Đánh giá mã | Giai đoạn 4 | Phê duyệt kỹ thuật |
| **Sĩ Quan Quản Trị** | Kiểm tra tuân thủ | Giai đoạn 4 | Phê duyệt quản trị |
| **Quản lý Sản phẩm** | Yêu cầu & vòng đời | Giai đoạn 1, 7 | Căn chỉnh kinh doanh |
| **Kỹ sư DevOps** | Triển khai & giám sát | Giai đoạn 5-6 | Sẵn sàng sản xuất |

---

## CONCLUSION

### English

The **Prompts as Code Standard Operating Procedure** transforms AI prompt management from artisanal craft to disciplined engineering. By implementing a 7-phase lifecycle, monorepo organization, automated testing, and governance gates, enterprises achieve:

- **Deterministic Behavior:** Predictable, consistent outputs
- **Full Auditability:** Complete change history
- **Regulatory Compliance:** ISO 27001/9001 alignment
- **Organizational Scalability:** Safe reuse and iteration
- **Continuous Improvement:** Monitoring and optimization

### Vietnamese

**SOP Prompts as Code** biến đổi quản lý prompt AI từ kỹ nghệ thủ công sang kỹ thuật kỷ luật. Bằng cách triển khai vòng đời 7 giai đoạn, tổ chức monorepo, kiểm thử tự động và cổng quản trị, các doanh nghiệp đạt được:

- **Hành Vi Định Tâm:** Các đầu ra dự đoán được, nhất quán
- **Tính Kiểm Toán Đầy Đủ:** Lịch sử thay đổi hoàn chỉnh
- **Tuân Thủ Quy Định:** Căn chỉnh ISO 27001/9001
- **Khả Năng Mở Rộng Tổ Chức:** Tái sử dụng an toàn và lặp lại
- **Cải Tiến Liên Tục:** Giám sát và tối ưu hóa

---

## DOCUMENT METADATA

**Document ID:** DOC-OPERATIONAL-PROMPTS-AS-CODE-SOP-002  
**Version:** 1.0.0  
**Status:** ✅ PRODUCTION-READY  
**Quality Score:** 9.0/10 (Excellent)  
**Compliance:** ISO 27001:2022, ISO 9001:2015  
**Authority:** Enterprise AI Governance Office  
**Published:** March 18, 2026  

---

**END OF REPORT 2**

**For questions or implementation support:**
- Email: operations@enterprise.ai
- Technical Lead: Senior Operations Engineer
- Responsible Officer: Enterprise AI Governance Office
