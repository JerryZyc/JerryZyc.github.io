---
name: blog-health-check
description: Scan a Jekyll-based personal blog for build health, unused images, dead links, and outdated dependencies; use for periodic maintenance or after a long break; output a report only.
---

# Blog Health Check

## Goal

Produce a health report without modifying the project.

## Inputs

- Project root path (current workspace by default).

## Checks

1) Build status
- Run the Jekyll build command (prefer `bundle exec jekyll build`).
- Record whether it succeeds and capture any errors.

2) Unused images
- Scan common image directories (e.g., `assets/images`, `public/images`, `assets/img`).
- Find image files not referenced in Markdown/HTML/CSS/JS.
- List potential unused images.

3) Dead links
- Scan Markdown/HTML for links.
- Flag obviously broken internal links (missing targets) and malformed URLs.

4) Dependency freshness
- Inspect `Gemfile`/`Gemfile.lock` (and `package.json` if present).
- Identify clearly outdated dependencies (major versions behind).

## Output

- Write `blog_health_report.md` in the project root.
- Include: summary, findings per category, and recommended next actions.
- Do not auto-fix.
