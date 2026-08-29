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

## Schema

Reference: `schema.yaml` in this skill directory.

For a human-readable quick reference with writing tips and examples, see [`references/frontmatter-guide.md`](references/frontmatter-guide.md). For troubleshooting validation failures, see [`references/common-errors.md`](references/common-errors.md).

Read the YAML file for the full field definitions, types, and allowed values. The schema defines:

- **Required fields:** `title`, `description`, `tags`, `status`
- **Optional fields:** `related`
- **Allowed status values:** `Draft`, `active`, `fleeting`, `seed`, `planning`
- **Scope:** All `*.md` files in the repo, excluding `AGENTS.md` and `.opencode/`

Any field name not in `required_fields` or `optional_fields` is an error.

## Procedure

1. **Run the validation script.** Execute:
   ```
   python3 .opencode/skills/frontmatter-validation/scripts/validate_frontmatter.py
   ```
   The script reads `schema.yaml`, scans all `*.md` files in the repo (excluding `AGENTS.md` and `.opencode/`), and outputs `VALID` or `INVALID` with numbered findings per file.

2. **Review the output.** The script prints per-file results and a summary line.

3. **Ask the user before fixing.** If any invalid files are found, **you must ask the user** using the Question tool before running fixes. Example prompt:
   > "Found N invalid file(s). Would you like me to fix them?"
   >
   > Options: "Yes, fix all" / "Yes, but let me choose which files" / "No, just report"

   Only proceed with fixes after the user confirms.

4. **Run fixes with user input.** Pipe the user's choice into the script:
   ```
   echo -e "y\nall" | python3 .opencode/skills/frontmatter-validation/scripts/validate_frontmatter.py
   ```
   Use `all` to fix everything, or comma-separated file numbers (e.g., `1,3`) for specific files.

5. **Auto-fix behavior.** The script applies fixes based on the issue type:
   - **No frontmatter block:** Inserts a frontmatter block derived from file content (title from H1 heading, description from first paragraph, tags from domain + filename, status defaults to `Draft`)
   - **Frontmatter in code block:** Strips the `` ``` `` markers around the frontmatter
   - **Missing required fields:** Adds fields with values derived from content

6. **Manual review.** After auto-fix, review the files for correctness. Descriptions are extracted from content but may need refinement. Files with `TODO` placeholders require manual completion.

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

## Auto-Fix Behavior

The script can automatically fix certain types of frontmatter issues. When invoked, it asks the user before making any changes.

**Fixable issues:**

| Issue | Fix Action |
|-------|-----------|
| No frontmatter block | Inserts frontmatter derived from file content |
| Frontmatter in code block | Strips `` ``` `` markers |
| Missing `description` | Extracts from first paragraph after H1 heading |
| Missing `tags` | Generates from domain folder + filename |
| Missing `status` | Defaults to `Draft` |

**Content extraction rules:**

- **Title**: Taken from first `# Heading` in the file
- **Description**: First non-empty, non-heading line after the H1
- **Tags**: Domain folder name (e.g., `backend`) + filename stem (e.g., `deployment`)
- **Status**: Defaults to `Draft`

**Example — `backend/deployment.md` before fix:**
```markdown
# Deployment

How the backend gets built, released, and monitored.

## Environments
...
```

**After fix:**
```yaml
---
title: Deployment
description: How the backend gets built, released, and monitored.
tags:
  - backend
  - deployment
status: Draft
---
```

**Limitations:**

- Only works on `.md` files in `Knowledge/`
- Cannot fix invalid field values (e.g., wrong Title Case) — only missing fields
- Files with no H1 heading get `title: TODO: Add Title`
- Files with no description paragraph get `description: TODO: Add description.`
- Always review auto-fixed files for accuracy

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
