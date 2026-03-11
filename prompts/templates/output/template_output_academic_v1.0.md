---
artifact_id: ""
doc_id: "TMPL-CSCF-OUTACAD-20260308-01"
version: "1.0.0"
status: "active"
migrated_from: "TEMPLATE-OUTPUT-ACADEMIC-PAPER-V1.0_.docx"
dc:
  title: "Output Template — Academic Paper Format v1.0"
  type: "template"
  date: "2026-03-08"
---

# Output Template: Academic Paper Format

*Use in prompts when scholarly/research output is required.*  
*Include this section verbatim in the agent's system prompt.*

---

## Standard Output Structure: Academic Paper Format

You **must** structure your entire response using the following Markdown format. Adhere strictly to the specified headers, order, and content guidelines. Do not add introductory or concluding remarks outside this structure.

---

### 1. Abstract
Concise single-paragraph summary (150–250 words). State: research question, primary methods/sources, main findings, principal conclusion.

### 2. Introduction & Research Question
Problem statement, background context, significance of the question, scope.

### 3. Methodology & Data Sources
Methods used, sources consulted (with cluster classification from SEARCH_METHODS_LIBRARY), epistemic status of sources.

### 4. Analysis
Core analytical content. All empirical claims: label `[FACT]`, `[INFERENCE]`, `[HYPOTHESIS]`, `[SPECULATION]`.

### 5. Findings
Key findings structured as: **Finding**: [statement] | **Evidence**: [citation] | **Confidence**: [H/M/L]

### 6. Discussion
Interpretation, implications, limitations, alternative explanations.

### 7. Conclusion
Summary of findings, answers to research question, recommendations for further research.

### 8. References
Format: `[Author/Org, Year, Title, Source URL or DOI]`

---

*Note: This template is embedded in prompts requiring ratified output (`ratified_output: true`).*
