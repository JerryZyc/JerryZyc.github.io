---
name: paper-to-blog-refactor
description: Convert a paper PDF or notes into a structured long-form paper reading blog post with equations, tables, and references; use when asked to generate paper notes for this site.
---

# Paper to Blog Refactor

## Inputs

- PDF at `assets/papers/xxx.pdf` (or another specified path).
- Notes at `notes/raw.md` if provided.

## Workflow

1) Extract key sections
- Abstract, problem, method, experiments, results, discussion.

2) Map into template
- Use the required sections from the site's paper template.
- Keep math in LaTeX, use `$$...$$` for blocks.

3) Add metadata
- Fill frontmatter: title, date, categories, tags, paper.pdf.

4) Output
- Write to `_posts/YYYY-MM-DD-paper-<slug>.md`.
- Include variable tables and consistent captions.

## Quality checks

- Ensure all symbols are defined before use.
- Keep headings consistent.
- Use tables for results and ablations.
