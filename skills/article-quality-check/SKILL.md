---
name: article-quality-check
description: Review a blog post for math syntax, undefined symbols, heading structure, figures/tables, and summary quality; use before publishing to generate improvement suggestions only.
---

# Article Quality Check

## Goal

Produce a checklist of issues and suggestions without editing files.

## Inputs

- Target post file path.

## Checks

1) Math syntax
- Verify inline vs display math usage.
- Flag malformed delimiters.

2) Undefined symbols
- List symbols used in equations without definition nearby.

3) Heading structure
- Ensure levels are consistent and not skipped.

4) Figures, tables, and equation style
- Check for captions and consistent naming (e.g., Figure/Table).
- Flag inconsistent equation formatting.
- Recommend HTML tables for variable tables if math breaks Markdown tables.

5) Summary
- Confirm there is a conclusion or takeaway section.

## Output

- Write `article_quality_report.md` with findings and suggested fixes.
