---
name: cross-article-consistency
description: Scan posts for terminology and symbol inconsistencies across the blog and optionally generate a topic knowledge map; use to standardize naming and notation in related topics.
---

# Cross Article Consistency

## Goal

Find inconsistent terminology and math notation across posts.

## Workflow

1) Build a term list
- Extract key terms and symbols from posts under `_posts`.

2) Detect variations
- Find multiple names for the same concept.
- Find symbols reused with different meanings.

3) Output
- Write `consistency_report.md` with:
  - Concept name conflicts
  - Symbol conflicts
  - Suggested canonical terms
- If requested, also write `knowledge-map.md` with a Mermaid graph.
