---
name: permission-operations
description: Define and enforce allowed operations and command permissions in this workspace; use when a user asks to codify approval rules, allowed paths, or permitted commands so Codex can proceed without repeated confirmations.
---

# Permission Operations

Follow these rules whenever this skill is triggered.

## Allowed file operations

- Create/modify only: `src/**`, `public/**`, `templates/**`, `README.md`, `package.json`.
- Do not delete files.
- Do not edit `.env`.
- Do not edit `~/.ssh` or any SSH-related files.
- Do not run destructive commands (e.g., `rm`, disk formatting).

## Allowed commands

- `npm install`
- `npm run dev`
- `npm run build`

## Confirmation policy

- If an operation is within the allowed scope above, proceed without asking for confirmation.
- If an operation is outside the allowed scope, ask the user for confirmation before proceeding.
