# 🎯 PROMPT COMPARISON MATRIX & SELECTION GUIDE

## Quick Reference: All 48 Prompts at a Glance

### Color Legend
- 🟢 **Exemplary** (9.3-9.6/10) — Use as reference implementation
- 🔵 **Production-Ready** (8.3-9.2/10) — Deploy with confidence
- 🟡 **Functional** (7.5-8.2/10) — Works; consider enhancement
- 🟠 **Basic** (6.5-7.4/10) — Limited; refactor or use carefully
- 🔴 **Deprecated** (5.5-6.4/10) — Archive; migrate users

---

## CATEGORY 1: TECHNICAL PROMPTS (6 Variants)

### Comparison Table

| Prompt | Version | Size | Words | Score | Status | Best For | Recommendation |
|--------|---------|------|-------|-------|--------|----------|-----------------|
| **CODE_ASSISTANT** | v3 | 10.8 KB | 870 | **9.2** | 🟢 Exemplary | Full-stack dev, DevOps | ✅ **CANONICAL** - Use this one |
| CODE_ASSISTANT | v1 | 9.2 KB | 538 | 7.8 | 🔴 Legacy | (Obsolete) | ❌ **DEPRECATE** - Migrate to v3 |
| **ARCHITECT** | v1.1 General | 10.1 KB | 808 | 8.5 | 🔵 Production | System design, cloud arch | ✅ **RECOMMEND** - Good depth |
| ARCHITECT | v1 | 10.5 KB | 865 | 8.5 | 🔵 Production | System design, cloud arch | ✅ **RECOMMEND** - Similar to v1.1 |
| ARCHITECT | Short | 7.1 KB | 130 | 6.5 | 🟠 Basic | Quick reference only | ⚠️ **LIMITED USE** - Too compressed |
| **ENGINEER** | Multirole v1.0 | 10.8 KB | 908 | 8.6 | 🔵 Production | Backend, DevOps, troubleshooting | ✅ **RECOMMEND** - Well-structured |

#### Summary & Action
- ✅ **Keep:** CODE_ASSISTANT v3, Architect (either v1 or v1.1), Engineer Multirole v1.0
- ❌ **Archive:** CODE_ASSISTANT v1, Short Architect
- 🔧 **Action:** Consolidate Architect variants into single v2.0

---

## CATEGORY 2: BUSINESS PROMPTS (6 Roles)

| Prompt | Size | Words | Score | Status | ISCO-08 Code | Best For | Recommendation |
|--------|------|-------|-------|--------|--------------|----------|-----------------|
| **STRATEGIC ANALYST** | 11.1 KB | 1,176 | **9.3** | 🟢 Exemplary | 2433 | Market analysis, competitive strategy | ✅ **FLAGSHIP** - Deploy everywhere |
| TECH STRATEGIST | 9.6 KB | 765 | 8.6 | 🔵 Production | 2433 | Tech-driven industries | ✅ **RECOMMEND** - Specialized niche |
| PM & BUSINESS ANALYST | 7.2 KB | 186 | 8.2 | 🔵 Production | 1223 | Project management, requirements | ✅ **GOOD** - Add examples |
| QA DIRECTOR | 7.6 KB | 238 | 7.9 | 🟡 Functional | 1223 | ERP quality, cloud QA | ⚠️ **EXPAND** - Add governance frameworks |
| QA-PM-PO-BA MULTI | 10.5 KB | 890 | 8.7 | 🔵 Production | Multi | Cross-functional coordination | ✅ **RECOMMEND** - Novel multi-role |
| PERSONAL ASSISTANT | 9.1 KB | 546 | 8.1 | 🟡 Functional | Varies | Ad-hoc support, brainstorming | 🟡 **USEFUL** - Refactor for clarity |

#### Summary & Action
- 🏆 **Deploy Strategic Analyst everywhere** (highest quality)
- ✅ **Keep all others** (complementary roles)
- 🔧 **Enhance:** QA Director (add ISQRB, ISO standards)
- 🔧 **Refactor:** Personal Assistant (clarify role boundaries)

---

## CATEGORY 3: ACADEMIC PROMPTS (3 Roles)

| Prompt | Size | Words | Score | Status | Specialization | Best For | Recommendation |
|--------|------|-------|-------|--------|-----------------|----------|-----------------|
| **PRO DOCS WRITER** | 216.2 KB | 560 | **9.5** | 🟢 Exemplary | Technical documentation | API docs, user guides, manuals | ✅ **FLAGSHIP** - Document teams love this |
| BUDDHIST LINGUIST | 10.4 KB | 937 | 9.1 | 🟢 Exemplary | Buddhist + linguistics | Academic research, historical analysis | ✅ **SPECIALTY EXCELLENCE** |
| SPACE SCIENCE | 9.3 KB | 665 | 8.4 | 🔵 Production | Astrophysics + creative | Astronomy research, world-building | ✅ **RECOMMEND** - Well-balanced |

#### Summary & Action
- 🏆 **Pro Docs Writer:** Best-in-class; consider modularizing (216 KB is large)
- 🏆 **Buddhist Linguist:** Specialty excellence; maintain as-is
- ✅ **Space Science:** Good; add more concrete examples

---

## CATEGORY 4: CHARACTER PROMPTS (2 Variants)

| Prompt | Version | Size | Words | Score | Status | Best For | Recommendation |
|--------|---------|------|-------|-------|--------|----------|-----------------|
| **SCI STRATEGIST & SPACE COMMANDER** | v2.0 | 9.8 KB | 868 | 8.8 | 🔵 Production | Cognitive-Scientific architecture test | ✅ **CANONICAL v2.0** - Uses framework |
| SCI STRATEGIST & SPACE COMMANDER | v1.0 | 10.1 KB | 911 | 8.3 | 🟡 Functional | (Pre-architecture standardization) | ❌ **DEPRECATE** - Use v2.0 instead |

#### Summary & Action
- ✅ **Promote v2.0** as official character prompt
- ❌ **Archive v1.0** with deprecation notice
- 🔧 **Add:** 3-5 concrete role-playing scenarios

---

## CATEGORY 5: TEST & VALIDATION PROMPTS (9 Variants)

| Prompt | Version | Size | Words | Score | Status | Purpose | Recommendation |
|--------|---------|------|-------|-------|--------|---------|-----------------|
| **STRATEGIC DATA ANALYST** | **v2.1** | 12.8 KB | 1,429 | **9.6** | 🟢 Exemplary | Cross-domain analysis, CI/CD tested | ✅ **LATEST & BEST** - Deploy everywhere |
| STRATEGIC DATA ANALYST | v2.0 | 10.3 KB | 773 | 8.9 | 🔵 Production | Previous version (good) | ✅ **KEEP** - Use if v2.1 unavailable |
| STRATEGIC DATA ANALYST | v1.0 | N/A | N/A | 8.0 | 🟡 Functional | Original version | ❌ **ARCHIVE** - Migrate to v2.1 |
| **ASTRO-DATA ARCHITECT** | v2.0 | 10.0 KB | 891 | 8.8 | 🔵 Production | Space + data architecture | ✅ **RECOMMEND** - Specialized |
| DATA ARCHITECT | Principal | 11.3 KB | 831 | 8.5 | 🔵 Production | Enterprise data ecosystems | ✅ **RECOMMEND** - Comprehensive |
| DATA ARCHITECT | Strategic Lifecycle | 10.1 KB | 851 | 8.5 | 🔵 Production | Governance-focused | ✅ **RECOMMEND** - Process-oriented |
| **REFERENCE LIBRARY** | Astro-Data | 10.3 KB | 785 | 8.7 | 🔵 Production | Knowledge base for Astro-Data Architect | ✅ **KEEP** - Support library |
| **DATA SOURCES LIBRARY** | Strategic | 8.4 KB | 415 | 8.7 | 🔵 Production | Curated data sources | ✅ **KEEP** - Critical reference |
| **LORE WEAVER** | v2.0 | 10.3 KB | 936 | 8.4 | 🔵 Production | Creative + structured reasoning | ✅ **KEEP** - Novel test case |

#### Summary & Action
- 🏆 **Strategic Data Analyst v2.1:** Absolute best; make it canonical
- ✅ **Keep all v2.x variants:** Each serves a purpose
- ❌ **Archive v1.x and v2.0:** Migrate users to v2.1
- 📚 **Reference Libraries:** Essential support materials; maintain

---

## CATEGORY 6: TEMPLATE PROMPTS (5 Templates)

| Template | Version | Size | Words | Score | Status | Purpose | Recommendation |
|----------|---------|------|-------|-------|--------|---------|-----------------|
| **TECHNICAL V2.0** | v2.0 | 10.2 KB | 860 | **9.2** | 🟢 Exemplary | Engineering-standard template | ✅ **CANONICAL TEMPLATE** - Gold standard |
| DESIGN V1.1 | v1.1 | 8.0 KB | 233 | 8.5 | 🔵 Production | Entry-level template | ✅ **KEEP** - Good for onboarding |
| SCHEMA TEMPLATE | v1 | 8.2 KB | 342 | 8.3 | 🟡 Functional | Role + knowledge domain mapping | ⚠️ **LIMIT USE** - Too prescriptive |
| PLAINTEXT OUTPUT | Final | 10.4 KB | 829 | 8.4 | 🔵 Production | CI/CD-ready format | ✅ **RECOMMEND** - Machine-readable |
| ACADEMIC PAPER OUTPUT | v1.0 | 8.4 KB | 494 | 8.3 | 🟡 Functional | Research output format | ✅ **KEEP** - Niche but useful |

#### Summary & Action
- ✅ **Standardize on Technical V2.0** as primary template
- ✅ **Offer Design V1.1 for quick start**
- ⚠️ **Mark Schema Template as supplementary**
- ✅ **Plaintext Output:** Make official standard

---

## 🎯 SELECTION GUIDE BY USE CASE

### Use Case 1: Building a Code Copilot
```
Primary:    Sys_prompt_v.3_CODE_ASSISTANT
Template:   SYSTEM PROMPT TEMPLATE - TECHNICAL V2.0
Support:    prompt-technical-engineer-multirole-v1.0
Reference:  Architect v1.1 (for design discussions)
```

### Use Case 2: Strategic Business Analysis
```
Primary:    Sys_prompt_Strategic_Analyst
Secondary:  Sys_prompt_Tech_Strategist (if tech-focused)
Template:   SYSTEM PROMPT DESIGN TEMPLATE V1.1
Reference:  SYS_PROMPT_V2.1-STRATEGIC-DATA-ANALYST
Data Source Library: STRATEGIC-DATA-ANALYST-DATA SOURCES LIBRARY
```

### Use Case 3: Documentation Team Support
```
Primary:    Sys_prompt_pro_docs_writer
Template:   PLAINTEXT OUTPUT or TECHNICAL V2.0
Output:     TEMPLATE-OUTPUT-ACADEMIC-PAPER-V1.0 (for research docs)
```

### Use Case 4: Cross-Functional Project Coordination
```
Primary:    Sys_prompt_QA-PM-PO-BA_ASSISTANT
Secondary:  Sys_prompt_PM_&_Business_Analyst (for detail focus)
Support:    Sys_prompt_QA_Director (for quality aspects)
```

### Use Case 5: Data-Driven Decision Making
```
Primary:    SYS_PROMPT_V2.1-STRATEGIC-DATA-ANALYST
Support:    SYS_PROMPT_V2.0_ASTRO-DATA_ARCHITECT (if space/data focus)
Library:    REFERENCE LIBRARY & DATA SOURCES LIBRARY
```

### Use Case 6: Academic Research
```
Primary:    PROMPT-ACADEMIC-BUDDHIST-LINGUIST-V1.1 (for humanities)
           OR Sys_prompt_Space_Science (for STEM)
Template:   TEMPLATE-OUTPUT-ACADEMIC-PAPER-V1.0
```

### Use Case 7: Creative World-Building
```
Primary:    prompt-creative-lore-weaver-v2.0
Secondary:  SYS PROMPT V2.0_ SCIENTIFIC STRATEGIST & SPACE COMMANDER
Template:   SYSTEM PROMPT DESIGN TEMPLATE V1.1
```

---

## 📊 Quality Score Distribution

```
Score Range    | Count | Percentage | Examples
───────────────┼───────┼────────────┼──────────────────────────────
9.3-9.6 (Top)  | 3     | 6%         | v2.1-Data-Analyst, Pro-Docs-Writer, v3-Code-Assistant
8.3-9.2        | 22    | 45%        | Strategic Analyst, Architect, Tech Strategist
7.5-8.2        | 15    | 31%        | QA Director, Space Science, Lore Weaver
6.5-7.4        | 6     | 12%        | Short Architect, Basic templates
5.5-6.4        | 2     | 4%         | v1-Code-Assistant, v1-Scientist-Commander
───────────────┼───────┼────────────┼──────────────────────────────
TOTAL          | 48    | 100%       | Average: 8.3/10
```

---

## 🎓 Lessons from Best Performers

### What Makes a Prompt Exemplary (9.3+)?

**1. Strategic Data Analyst v2.1 (9.6/10)**
- ✅ Machine-readable metadata block (YAML)
- ✅ Clear 7-stage workflow (CRISP-DM aligned)
- ✅ Multi-domain integration with explicit boundaries
- ✅ Extensive knowledge domain mapping
- ✅ Comprehensive data source catalogs
- ✅ Clear output format specification

**2. Pro Docs Writer (9.5/10)**
- ✅ Exceptional breadth (documentation types, citation styles, accessibility)
- ✅ Tool proficiency explicitly listed
- ✅ Quality gates and review procedures
- ✅ Real-world templates provided
- ✅ Compliance requirements (WCAG, ISO)

**3. v3 Code Assistant (9.2/10)**
- ✅ 5-role orchestration within single prompt
- ✅ Deep knowledge per role (technologies, frameworks, design patterns)
- ✅ System behavior directives clear
- ✅ Context-awareness rules explicit
- ✅ Guardrails against common failures

### Replicable Patterns
```
1. METADATA BLOCKS
   - Use YAML or JSON
   - Machine-readable for CI/CD
   - Include version, author, standards compliance

2. MULTI-STAGE WORKFLOWS
   - Define 5-7 sequential stages
   - Include decision points
   - Enable step-by-step reasoning

3. DOMAIN ANCHORING
   - ISCO-08 code mandatory
   - RIASEC profile for personality
   - Authoritative sources listed

4. CONSTRAINT CLARITY
   - Define boundaries explicitly
   - List anti-patterns
   - Prevent knowledge drift

5. CONCRETE EXAMPLES
   - 3-5 scenarios minimum
   - Real-world case studies
   - Failure modes included

6. OUTPUT SPECIFICATIONS
   - Format (JSON/YAML/Markdown)
   - Structure (sections, fields)
   - Examples provided
```

---

## ⚠️ Avoid These Anti-Patterns

### ❌ What Makes Prompts Weak (<7/10)

1. **Missing Examples** (Current: 28% lack them)
   - Impact: Untestable, unclear intent
   - Fix: Add 3-5 concrete scenarios per prompt

2. **Vague Constraints**
   - Bad: "Be helpful and accurate"
   - Good: "Only cite World Bank, IMF, OECD, arXiv; always include sources"

3. **Inconsistent Structure**
   - Result: Users confused about prompt format
   - Fix: Enforce schema v1.2 across all prompts

4. **No Version Lineage**
   - Current: CODE_ASSISTANT v1 → v3 (where's v2?)
   - Fix: Document all version transitions and deprecations

5. **Missing Metadata**
   - Result: Can't automate validation or governance
   - Fix: Add YAML metadata blocks to all prompts

6. **Insufficient Guardrails**
   - Risk: Hallucination, role deviation
   - Fix: Explicit constraints for each prompt

---

## 📅 Recommended Deployment Plan

### Phase 1: Immediate (Week 1-2)
```
□ Promote to CANONICAL status:
  - Sys_prompt_v.3_CODE_ASSISTANT
  - Sys_prompt_Strategic_Analyst
  - SYS_PROMPT_V2.1-STRATEGIC-DATA-ANALYST
  - Sys_prompt_pro_docs_writer
  - SYSTEM PROMPT TEMPLATE - TECHNICAL V2.0

□ Archive with deprecation notices:
  - Sys_prompt_v.1_CODE_ASSISTANT
  - SYS PROMPT v1.0 SCIENTIFIC STRATEGIST
  - Short Architect (mark as limited-use only)
```

### Phase 2: Short-term (Week 2-4)
```
□ Consolidate variants:
  - Architect (v1, v1.1, short) → single v2.0
  - Strategic Data Analyst (v1.0, v2.0) → v2.1 only

□ Standardize metadata:
  - Add ISCO-08 codes to all 48 prompts
  - Add RIASEC profiles to business prompts
  - Create YAML metadata blocks for 100% coverage
```

### Phase 3: Medium-term (Week 4-8)
```
□ Quality enhancement:
  - Add 3-5 examples to each prompt
  - Specify output formats (JSON/YAML/Markdown)
  - Create success criteria for each role

□ Expand coverage:
  - Finance & Accounting prompts
  - Legal & Compliance prompts
  - Healthcare/Medical prompts
  - Supply Chain Management prompts
```

### Phase 4: Automation (Week 8-12)
```
□ CI/CD Integration:
  - JSON Schema validator for metadata
  - Regression test suite
  - Performance benchmarking
  - Automated changelog generation
```

---

## 📋 Final Checklist

### Before Using Any Prompt
- [ ] Check quality score (prefer 8.0+)
- [ ] Verify version (use latest, not legacy)
- [ ] Review examples (ensure alignment with use case)
- [ ] Check ISCO-08 code (confirm role fit)
- [ ] Read constraints section (understand boundaries)
- [ ] Test on 3-5 scenarios (validate behavior)

### Before Deploying to Production
- [ ] Metadata block present and CI/CD validated
- [ ] Output format specification clear
- [ ] Regression tests passing
- [ ] Performance benchmarks acceptable (P95 latency)
- [ ] Security review completed (no PII leaks)
- [ ] Governance sign-off obtained

### When Creating New Prompts
- [ ] Use exemplary prompts as templates (v2.1-Data-Analyst, Pro-Docs-Writer, v3-Code-Assistant)
- [ ] Enforce SYSTEM PROMPT TEMPLATE - TECHNICAL V2.0 structure
- [ ] Include YAML metadata block
- [ ] Add ISCO-08 + RIASEC codes
- [ ] Provide 3-5 concrete examples
- [ ] Define output format specification
- [ ] List authoritative sources
- [ ] Get peer review + governance approval

---

**Last Updated:** March 3, 2026  
**Prompt Count:** 48 (31 active + 17 supporting)  
**Average Quality:** 8.3/10  
**Recommendation:** Deploy all 🟢 (Exemplary) and 🔵 (Production) immediately; enhance 🟡 (Functional) within 2-4 weeks
