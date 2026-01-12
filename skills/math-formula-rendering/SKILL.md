---
name: math-formula-rendering
description: Configure clean math rendering in Jekyll blogs (especially Minimal Mistakes) using KaTeX or MathJax; use when users report bad formula display or ask to align with Hydejack-style math handling.
---

# Math Formula Rendering

Use this workflow to make math render cleanly in Jekyll.

## Preferred setup (Hydejack-style KaTeX pre-render)

1) Update `_config.yml`
- Set:
  - `kramdown.math_engine: katex`
  - `kramdown.math_engine_opts: {}`
  - `mathjax: false`

2) Update `Gemfile`
- Add:
  - `gem "kramdown-math-katex"`
  - `gem "duktape"`

3) Add KaTeX CSS
- Create `_includes/head/custom.html` (or append if it exists).
- Include:
  ```html
  <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/katex@0.16.10/dist/katex.min.css" crossorigin="anonymous">
  ```

4) Rebuild
- Run `bundle install`, then `bundle exec jekyll serve`.

## Fallback (MathJax runtime, best for GitHub Pages build)

- Set `kramdown.math_engine: mathjax` and `mathjax: true`.
- Remove `kramdown-math-katex` if you do not prebuild locally.

## Writing rules

- Inline: `$a_t \sim \mathcal{N}(\mu(s_t), \sigma^2 I)$`
- Block:
  ```
  $$
  \text{Attn}(Q,K,V) = \text{softmax}\left(\frac{QK^\top}{\sqrt{d}}\right)V
  $$
  ```
- Avoid `align`/`align*`; prefer `aligned` inside `$$ ... $$` if needed.
- Define symbols before use and add a variable table for key equations.
