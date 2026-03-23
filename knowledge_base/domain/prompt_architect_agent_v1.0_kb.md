---
artifact_id: "019cdca8-9133-77a5-8e49-85b9e9d89ce0"
doc_id: "CSCF-KB-PROMPT-ARCH-20260310-01"
name:        "Knowledge Domain Library — Prompt Architect Agent"
version: "1.0.0"

authority_official:
  owner:       "Quang Cuong Huynh"
  declaration: "Registered — Quang Cuong Huynh"
  assistants:
    - "Claude (Anthropic)"
  reviewer:    "Quang Cuong Huynh"
status: "active"
persona: "prompt_architect_agent_v1.0"
dc:
  type:     "kb"
  title: "Knowledge Domain Library — Prompt Architect Agent"
  date: "2026-03-10"
changes:
  - version: "1.0.0"
    date: "2026-03-10"
    author: "Quang Cuong Huynh"
    summary: "Sprint 4 — initial KB creation"
    type:     "kb"
sha256: "PENDING"
---
# Knowledge Domain Library — Prompt Architect Agent v1.0

> ISCO-08: 2513 | RIASEC: I-A-E | Ti→Ne→Si | OCEAN: O:10 C:8 E:6 A:7 N:1

---

## Tier 1 — Authoritative Sources

### Prompt Engineering Foundations
- Anthropic Prompt Engineering Guide (docs.anthropic.com/en/docs/build-with-claude/prompt-engineering)
- OpenAI Prompt Engineering Guide (platform.openai.com/docs/guides/prompt-engineering)
- DeepMind / Google Gemini Prompting Guidelines
- "Chain-of-Thought Prompting Elicits Reasoning in Large Language Models" — Wei et al. (NeurIPS 2022)
- "Least-to-Most Prompting Enables Complex Reasoning" — Zhou et al. (ICLR 2023)
- "Constitutional AI: Harmlessness from AI Feedback" — Bai et al. (Anthropic, 2022)

### Agent System Design
- LangChain / LangGraph agent patterns (docs.langchain.com)
- CrewAI role design guide (docs.crewai.com)
- AutoGen agent conversation patterns (microsoft.github.io/autogen)
- ReAct: "Synergizing Reasoning and Acting in Language Models" — Yao et al. (ICLR 2023)
- Reflexion: "Verbal Reinforcement Learning" — Shinn et al. (NeurIPS 2023)
- CAMEL: "Communicative Agents for Role Playing" — Li et al. (2023)

### Evaluation Standards
- HELM: Holistic Evaluation of Language Models (Stanford CRFM)
- BIG-Bench: Beyond the Imitation Game Benchmark
- MT-Bench: multi-turn conversation evaluation (Zheng et al., 2023)
- Anthropic Evals (github.com/anthropics/evals)

---

## Tier 2 — Prompt Patterns & Techniques

### Core Technique Matrix

| Technique | Use Case | Token Cost | Reliability |
|---|---|---|---|
| Zero-shot | Simple classification, formatting | Low | Medium |
| Few-shot (3–5 examples) | Pattern matching, style transfer | Medium | High |
| Chain-of-Thought (CoT) | Multi-step reasoning, math | Medium | High |
| Tree-of-Thought (ToT) | Complex decisions, exploration | High | Very High |
| Least-to-Most | Hierarchical decomposition | Medium | High |
| ReAct (Reason + Act) | Tool-using agents | Medium | High |
| Reflexion | Self-correction loops | High | Very High |
| Constitutional AI (CAI) | Alignment, safety boundaries | Medium | High |
| RAG (Retrieval-Augmented) | Knowledge-grounded answers | Medium | High |
| Meta-prompting | Dynamic prompt generation | Medium | Medium |

### CSCF Persona Architecture Pattern (Canonical)
```xml
[IDENTITY BLOCK]
  ISCO-08 code + role title
  Cognitive function stack (Ti/Te/Ni/Ne/Si/Se/Fi/Fe)
  RIASEC code
  OCEAN scores (1–10 per dimension)

[DOMAIN KNOWLEDGE]
  KB AUTO-LOAD: knowledge_base/domain/{persona}_kb.md

[BEHAVIORAL DIRECTIVES]
  Positive examples (3–5)
  Negative examples (3–5)
  Scope violations → route + log (never answer)

[OUTPUT CONTRACT]
  ratified_output: true → RatifiedDocumentSchema (UAS header required)
  ratified_output: false → ConversationOutputSchema

[MEMORY PROTOCOL]
  L1 auto-log: session_start, kb_access, scope_violation
  L2 auto-log: gate_decisions, ratified_outputs
  L3 auto-write: ratified_output=true AND gate >= G3

[EPISTEMIC LABELS]
  [FACT] — verifiable claim with source
  [INFERENCE] — derived from available evidence
  [HYPOTHESIS] — plausible but unverified
  [SPECULATION] — exploratory, low confidence
```

### Prompt Quality Rubric (Auto-Apply)
| Dimension | Check |
|---|---|
| Specificity | Role, task, format all explicit? |
| Grounding | KB reference loaded? Tier 1 sources cited? |
| Boundary enforcement | Out-of-scope routing defined? |
| Output contract | ratified_output flag set correctly? |
| Memory protocol | L1/L2/L3 auto-log events mapped? |
| Adversarial resistance | Injection attempt handler present? |
| Epistemic labeling | [FACT/INFERENCE/HYPOTHESIS/SPECULATION] used? |

---

## Tier 3 — Papers & Books

- Wei et al. — "Chain-of-Thought Prompting" (NeurIPS 2022) arXiv:2201.11903
- Yao et al. — "ReAct: Synergizing Reasoning and Acting" (ICLR 2023) arXiv:2210.03629
- Brown et al. — "GPT-3: Language Models are Few-Shot Learners" (NeurIPS 2020)
- Bai et al. — "Constitutional AI" (Anthropic, 2022) arXiv:2212.08073
- Schick & Schütze — "It's Not Just Size That Matters: Small Language Models Are Also Few-Shot Learners" (EACL 2021)
- Liu et al. — "Pre-train, Prompt, and Predict: A Systematic Survey" (ACM CSUR 2023)
- Weng, Lilian — "Prompt Engineering" (lilianweng.github.io, 2023) — comprehensive survey

---

## Tier 4 — Tools

| Tool | Purpose |
|---|---|
| PromptLayer | Prompt version tracking + A/B testing |
| LangSmith | LLM tracing + prompt evaluation |
| Weights & Biases Prompts | Prompt experiment tracking |
| Helicone | LLM observability + cost tracking |
| Braintrust | Eval harness for LLM outputs |
| LMSYS Chatbot Arena | Model comparison benchmarking |
| Anthropic Console | Claude prompt workbench |

---

## Tier 5 — Search Queries

- "chain of thought prompting LLM reasoning 2024 paper"
- "system prompt injection attack defense techniques"
- "ReAct agent prompting tool use language model"
- "CSCF persona design cognitive function stack MBTI"
- "prompt engineering best practices Anthropic Claude 2025"
- "LLM agent memory architecture persistent session context"
- "few-shot prompting examples selection techniques optimal"

---

## Domain Boundaries

| In Scope | Out of Scope |
|---|---|
| Persona system prompt design | Code implementation (→ engineer) |
| Prompt pattern selection + evaluation | Architecture decisions (→ architect) |
| KB structure and Tier 1–5 organization | Requirements elicitation (→ pm_ba) |
| Adversarial prompt defense patterns | Compliance enforcement (→ compliance) |
| Multi-agent conversation topology design | Sprint planning (→ planner) |