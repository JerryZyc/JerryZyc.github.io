---
name: paper-reading-blog-generator
description: Build a local-previewable, GitHub Pages-ready paper reading blog using Astro + Markdown/MDX with KaTeX, code highlighting, TOC/anchors, references, images, templates, and components; use when the user asks for a "paper reading blog generator", "paper deep reading blog", or to convert paper notes into a structured long-form post with equations, tables, and callouts.
---

# Paper Reading Blog Generator

Follow these steps to create a complete Astro-based paper reading blog and a detailed paper-reading post from user notes.

## Inputs and assumptions

- Prefer PDF at `/assets/papers/xxx.pdf` (current workspace convention). If `/papers/xxx.pdf` is used, adapt paths.
- Expect raw notes at `/notes/raw.md`; if missing or empty, create it and leave TODO placeholders.
- Use clean LaTeX math only; no Unicode math symbols.

## Workflow

1) Decide publishing target
- Default to the existing Jekyll blog (`_posts`) unless the user explicitly asks for a new Astro site.
- For Jekyll, follow the "Jekyll math + formatting" section below.

2) Configure Markdown/MDX (Astro path)
- Enable KaTeX rendering for inline `$...$` and block `$$...$$`.
- Enable syntax highlighting for code blocks.
- Enable headings anchors and auto-generated TOC (if available).
- Allow footnotes and references (Markdown or simple References section).

3) Create routing and content structure (Astro path)
- Create a route like `/posts/paper-reading-xxx/` (slug is editable).
- Use content collections (Astro) or an MDX page, whichever is simpler.
- Store images in `/public/images/`.

4) Create shared components (Astro path)
- `Callout` for Tip/Note/Warning blocks.
- `EquationBlock` for equation + explanation + variable table.
- `Figure` for images with captions.
- Optional TOC component or auto-TOC integration.

5) Create templates and examples (Astro path)
- Add `/templates/paper-reading-template.mdx` with all required sections.
- Add an example post at `/src/content/posts/paper-reading-xxx.mdx`.
- Ensure the example includes all required sections and placeholder content.

6) Populate the post from raw notes
- Read `/notes/raw.md` and map content into the required sections.
- If missing content, keep TODO markers and placeholders.

7) Add README instructions (Astro path)
- Include local dev, build, and GitHub Pages deployment steps.
- Document how to add a new paper post.

## Required sections in the post template

- Title + Abstract (200-300 words)
- 1. Problem Setting
- 2. Motivation & Key Challenges
- 3. Method Overview (system diagram + text)
- 4. Core Components
  - 4.1 Perception / Encoder (I/O shapes)
  - 4.2 Spatial Attention (self-attn + cross-attn equations)
  - 4.3 Memory (SRU) vs LSTM/GRU (equations + intuition)
  - 4.4 RL Training Design (reward, dropout, DML, asym actor-critic)
- 5. Experiments & Results (tables, ablations, failure cases)
- 6. Discussion (strengths/limitations)
- 7. Reproducibility Checklist (hyperparams, setup, code layout, hardware)
- 8. My Takeaways (transferable ideas)
- References (manual entries are fine)

## Formatting requirements

- Inline math: `$a_t \sim \mathcal{N}(\mu(s_t), \sigma^2 I)$`
- Block math:
  ```
  $$
  \text{Attn}(Q,K,V) = \text{softmax}\left(\frac{QK^\top}{\sqrt{d}}\right)V
  $$
  ```
- Define symbols before use.
- Add a variable table for important equations.

## Output checklist

- For Jekyll, see the Jekyll-specific checklist below.
- For Astro, keep the original checklist.

## Jekyll math + formatting (Minimal Mistakes)

1) Ensure MathJax loads
- Add MathJax loader + config in `_includes/head/custom.html`.
- Use:
  - inline: `$...$` or `\\(...\\)`
  - block: `$$...$$` or `\\[...\\]`

2) Set math engine
- In `_config.yml`:
  - `kramdown.math_engine: mathjax`
  - `mathjax: true`

3) Keep math blocks clean
- Put display math in its own block with blank lines before/after.
- Avoid `align/align*` in KaTeX mode; for MathJax, `aligned` is still safer.

4) Tables and variable tables
- For variable tables, prefer HTML `<table>` to avoid Markdown parsing issues with math.
- Always add a blank line before and after the table.

## Jekyll post authoring checklist

- File name: `_posts/YYYY-MM-DD-paper-<slug>.md`
- Frontmatter includes: title, date, categories, tags, paper.pdf path
- Use Markdown lists for bullets; avoid long inline paragraphs with many formulas.
- For large formulas, use `$$...$$` blocks.

- Astro project initializes and runs with `npm install` + `npm run dev`.
- KaTeX works for inline and block math.
- Example post and template include all required sections.
- Components exist and are used in the sample post.
- README explains preview, build, and deploy steps.
