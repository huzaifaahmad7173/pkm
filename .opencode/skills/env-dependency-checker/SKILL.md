---
name: env-dependency-checker
description: Checks that all project dependencies are installed and system tools are available. 
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

Run each command below and record PASS or FAIL. Do not modify the environment — this skill only reports.

### Python Packages

`pyyaml` must be installed and version `>= 6.0`:

```
python3 -c "import importlib.metadata as m; print(m.version('pyyaml'))"
```

- PASS if the printed version is `>= 6.0`.
- FAIL if the command errors (not installed) or the version is below `6.0`.

### Node Packages

`@opencode-ai/plugin` must be installed:

```
test -f .opencode/node_modules/@opencode-ai/plugin/package.json && echo PASS || echo FAIL
```

### System Tools

```
python3 --version
git --version
node --version
```

- PASS if each command prints a version.
- FAIL if a command is not found.

### Environment Variables

None required.

### Reporting

On any FAIL, suggest the appropriate fix command. See [`references/troubleshooting.md`](references/troubleshooting.md) for fixes per failure type.

## Output Format

```
=== Environment Dependency Check ===

Python Packages
  PASS  pyyaml 6.0.1

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

- Only checks the items listed in this skill.
- Report-only. Never modify the environment.
