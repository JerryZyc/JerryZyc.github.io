---
name: safe-dependency-update
description: Safely update dependencies with minor/patch versions only for Jekyll or npm projects, run build, and rollback on failure; use for low-risk maintenance upgrades.
---

# Safe Dependency Update

## Rules

- Only update minor/patch versions.
- No breaking changes.
- Build must pass after updates.
- On failure, rollback and report.

## Workflow

1) Detect project type
- If `Gemfile` exists, treat as Jekyll/Ruby project.
- If `package.json` exists, treat as npm project.
 - If both exist, update Ruby first, then npm.

2) Update dependencies
- Ruby/Jekyll: prefer conservative updates and avoid major bumps (e.g., `bundle update --patch` or `bundle update --conservative <gem>`).
- npm: use safe update commands and avoid major bumps.

3) Verify
- Jekyll: `bundle exec jekyll build`.
- npm: `npm run build` if present.

4) Rollback on failure
- Restore lock files and manifests to previous state (use git if available, otherwise backup copies).

## Output

- Write `dependency_update_report.md` with:
  - Packages updated
  - Commands run
  - Build status
  - Rollback status (if any)
