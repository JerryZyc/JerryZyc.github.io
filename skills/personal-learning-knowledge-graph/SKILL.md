---
name: personal-learning-knowledge-graph
description: Build and maintain a structured personal learning knowledge tree for a long-term engineering/ML knowledge graph, with extensible modules, cross-references, and strict knowledge-node page templates; use when asked to create or update the knowledge tree, node templates, or engineer-grade knowledge pages.
---

# Personal Learning Knowledge Graph Builder

Use this skill to design and evolve a structured, layered knowledge graph and generate engineer-grade knowledge node pages.

## Knowledge Node Page Standard (engineer-grade)

**Required section order (no deviations):**
1) One-line definition
2) Problem setting
3) Mathematical formulation
4) Algorithmic interpretation
5) Optimization & implementation details
6) Connections & boundaries
7) Failure modes
8) Minimal pseudo-code
9) Decision checklist
10) Personal notes (leave TODO)

## Mandatory constraints

- No vague explanations or generic motivation.
- Math derivations must state origin (e.g., MLE, MAP, constrained optimization).
- Explicitly state:
  - Problem boundary
  - Failure modes
  - Differences vs adjacent methods
- Writing target: algorithm engineers and researchers.
- Use LaTeX for math: `$...$`, `$$...$$` only.
- No Unicode math symbols.
- Define symbols before use.

## Required output sections

1) Knowledge Tree
- Output a Markdown tree.
- Annotate each level with a short learning goal.

2) Module Descriptions
- Provide descriptions for each first- and second-level module.
- Focus on engineering scope and cross-links.

3) Single Node Page Spec
- Provide the Knowledge Node Page Standard above.

4) Extension Rules
- Explain how to add new modules (e.g., Robotics/Control/LLM/VLM).
- Require cross-references and consistent naming.

## Maintenance conventions

- Use consistent naming and symbols across nodes.
- Cross-link adjacent nodes explicitly (e.g., linear regression <-> ridge/lasso, MLE <-> MAP).
- Prefer concise, verifiable statements over pedagogy.
