---
name: env-dependency-checker
description: Checks that all project dependencies are installed and system tools are available. Use when setting up the project, after cloning, or when the user asks "are all deps installed?" or "check dependencies". Only works on this project (pkm).
---

# Environment Dependency Checker

Verifies the project's runtime environment.

## When to Invoke

- After cloning or setting up a new machine.
- When things break mysteriously.
- Before starting a work session.

## When Not to Invoke

- When the user wants to install or manage dependencies.

## Procedure

1. Run the check script:
   ```
   python3 .opencode/skills/env-dependency-checker/scripts/check_deps.py
   ```

2. Review output — each check shows PASS or FAIL.

3. On failure, suggest the appropriate fix command. See [`references/troubleshooting.md`](references/troubleshooting.md) for fixes per failure type.

4. This skill only reports. Never modify the environment.

## Output Format

```
=== Environment Dependency Check ===

Python Packages
  PASS  pyyaml

Node Packages
  PASS  @opencode-ai/plugin

System Tools
  PASS  python3 — Python 3.11.4
  PASS  git — git version 2.42.0
  PASS  node — v20.10.0

Environment Variables
  (none required)

--- 5/5 checks passed ---
```

## Scope

- Only checks what `checks.yaml` declares.
- Report-only.
