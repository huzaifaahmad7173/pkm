---
name: frontmatter-validation
description: Validates YAML frontmatter in Knowledge/ Markdown docs against the canonical schema. Checks required fields, field names, value formats, and returns VALID or INVALID. Use when reviewing files during audit mode, before committing Knowledge/ docs, or when a reviewer needs frontmatter verified. Don't use for files outside Knowledge/, non-Markdown files, or domain AGENTS.md files.
---

# Frontmatter Validation

Validates the YAML frontmatter of Markdown files against the project's canonical schema.

## When to Invoke

- Audit pipeline — verifying frontmatter on existing docs.
- After `general-task` creates or revises a Markdown document.
- Before a reviewer (`kb-editor`, `kb-tech-lead`, `kb-architect`) signs off.
- When migrating a doc from `Ideas/`, `Research/`, or `Projects/`.

## When Not to Invoke

- Non-Markdown files (JSON, images, `.gitkeep`).
- Domain `AGENTS.md` files (no frontmatter by convention).
- Files under `.opencode/` (config, not content).
- Files under `Templates/` (use different schema, not content docs).
- Files with no YAML frontmatter block — report `INVALID: no frontmatter block found` and stop. Do not attempt to fix or suggest content.

## Schema

Reference: `schema.yaml` in this skill directory.

For a human-readable quick reference with writing tips and examples, see [`references/frontmatter-guide.md`](references/frontmatter-guide.md).

Read the YAML file for the full field definitions, types, and allowed values. The schema defines:

- **Required fields:** `title`, `description`, `tags`, `status`
- **Optional fields:** `related`
- **Allowed status values:** `Draft`, `active`, `fleeting`, `seed`, `planning`
- **Scope:** All `*.md` files in the repo, excluding `AGENTS.md` and `.opencode/`

Any field name not in `required_fields` or `optional_fields` is an error.

## Procedure

1. **Run the validation script.** Execute:
   ```
   python3 .opencode/skill/frontmatter-validation/scripts/validate_frontmatter.py
   ```
   The script reads `schema.yaml`, scans all `*.md` files in the repo (excluding `AGENTS.md` and `.opencode/`), and outputs `VALID` or `INVALID` with numbered findings per file.

2. **Return the output.** Use the script's output as the verdict. No manual parsing needed.

3. **If fixing invalid files**, consult [`references/frontmatter-guide.md`](references/frontmatter-guide.md) for:
   - The quick-reference snippet to copy-paste
   - Writing tips for titles, descriptions, and tags
   - Valid vs. invalid examples

## Output Format

**Valid:**
```
VALID  — <file-path>
  All required fields present. No unexpected fields. Values conform to schema.
```

**Invalid:**
```
INVALID — <file-path>
  1. [MISSING] Required field `<field>` not found
  2. [UNEXPECTED] Field `<name>` is not in the allowed schema
  3. [INVALID VALUE] `<field>` = `<value>` — <reason>
```

Number each finding. Use the tag in brackets: `[MISSING]`, `[UNEXPECTED]`, `[INVALID VALUE]`.

## Examples

**Valid — `Knowledge/overview.md`:**

```yaml
---
title: Project Overview
description: High-level summary of the project structure and goals.
tags: [overview, architecture]
status: active
---
```

Output:
```
VALID  — Knowledge/overview.md
  All 4 required fields present. No unexpected fields. Values conform to schema.
```

**Invalid — `Knowledge/setup.md`:**

```yaml
---
title: setup guide
tags: []
category: getting-started
---
```

Output:
```
INVALID — Knowledge/setup.md
  1. [MISSING] Required field `description` not found
  2. [MISSING] Required field `status` not found
  3. [UNEXPECTED] Field `category` is not in the allowed schema
  4. [INVALID VALUE] `title` = `setup guide` — not in Title Case
  5. [INVALID VALUE] `tags` = `[]` — must contain at least one item
```

## Scope

- Only validates frontmatter content. Does not check whether `related` files actually exist on disk.
- Processes all `.md` files in the repo. Skips `AGENTS.md`, `.opencode/`, and `Templates/`.
- Only processes `.md` files. Skips all other file types.
