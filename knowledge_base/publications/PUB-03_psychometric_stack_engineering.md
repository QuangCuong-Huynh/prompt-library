---
artifact_id: "019cdca8-9175-73c6-a358-7b2e7a8cf3b0"
doc_id: "CSCF-PUB-03-20260309-01"
name:        "Kỹ Nghệ Psychometric Stack: Tâm lý học + Tiêu chuẩn Quốc tế trong Thiết kế Prompt AI"
version: "1.0.0"

authority_official:
  owner:       "Quang Cuong Huynh"
  declaration: "Registered — Quang Cuong Huynh"
  assistants:
    - "Claude (Anthropic)"
  reviewer:    "Quang Cuong Huynh"
status:      "active"
migrated_from: "Kỹ_Nghệ_Psychometric_Stack.pdf"
migrated_at: "2026-03-09"
dc:
  title: "Kỹ Nghệ Psychometric Stack: Tâm lý học + Tiêu chuẩn Quốc tế trong Thiết kế Prompt AI"
  type: "standard"
  date:     "2026-03-08"
  language: "vi"
  subject: ["psychometric-stack","ISCO-08","RIASEC","Jungian","OCEAN","prompt-engineering"]
sha256: "PENDING"

changes:
  - version: "1.0.0"
    date:    "2026-03-11"
    author:  "Quang Cuong Huynh"
    summary: "UAS v1.2 compliance fix"
    type:    "fix"
---
# Kỹ Nghệ "Psychometric Stack"

> **Publication Type:** LinkedIn flagship post — methodology credibility  
> **Target Audience:** AI/ML community, HR tech, enterprise architects  
> **Key Claim:** Scientific Persona Design = deterministic, testable, auditable AI agents

## The 5-Layer Psychometric Stack (Summary)

```
Layer 1: Job Identity      → ISCO-08 + O*NET KSAs
Layer 2: Career Orientation → RIASEC operational mindset
Layer 3: Cognitive Engine  → Jungian Function Stack (Dominant/Auxiliary/Tertiary/Reference)
Layer 4: Personality Params → OCEAN Big Five sliders (1–10)
Layer 5: PAC Lifecycle     → Monorepo + SemVer + CI/CD + Schema validation
```

## Case Study Referenced: "Ruthless Code Reviewer"
```yaml
role: "Senior Software Engineer (ISCO-08: 2512)"
riasec: "CIR"
cognitive_stack:
  dominant: "Te — objective logic, execution focus"
  reference: "Si — standards corpus grounding"
ocean: {C: 10, A: 1, N: 1}
rule: "No softening language. Imperative commands only: 'Fix this. Delete this.'"
```

## Key Insight for Community
> "I don't write prompts. I architect them."
> When we treat prompts as Technical Legacy, we truly master AI.

## CSCF Implementation
All personas in `personas/roles/` implement this 5-layer stack.
See `cognitive/functions/psychometric_stack_v2.1.md` for the canonical reference.