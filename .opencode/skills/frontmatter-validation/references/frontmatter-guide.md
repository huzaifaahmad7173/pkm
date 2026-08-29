# Frontmatter Guide

Quick reference for writing valid YAML frontmatter in `Knowledge/*.md` files.

## Quick Reference

Copy this block and fill in each field:

```yaml
---
title: Your Title Here          # Title Case, required
description: A short summary.   # Ends with ".", required
tags:                           # Kebab-case list, optional
  - topic-one
  - topic-two
status: Draft                   # One of 5 values, optional
related:                        # Bare .md filenames, optional
  - other-doc.md
---
```

## Field Reference

| Field | Type | Required | Rules | Example |
|-------|------|----------|-------|---------|
| `title` | string | Yes | Non-empty, Title Case | `SQLite3` |
| `description` | string | Yes | Non-empty, must end with `.` | `Overview of SQLite3, its purpose, and conventions.` |
| `tags` | list | No | Kebab-case (`a-z0-9` + hyphens), min 1 item if present | `[database, sqlite]` |
| `status` | string | No | Must be one of the allowed values | `Draft` |
| `related` | list | No | Bare `.md` filenames, no paths or `..` | `[conventions.md]` |

## Status Values

- `Draft` — not yet finalized
- `active` — current, in-use
- `fleeting` — temporary or quick note
- `seed` — early idea, needs development
- `planning` — being planned, not implemented

## Writing Tips

**Title**
- Use Title Case: capitalize major words, keep small words (`a`, `and`, `the`) lowercase.
- Keep acronyms uppercase (`API`, `SQL`, `LLM`).
- Make it specific and descriptive — avoid generic titles like `Overview` alone.

**Description**
- Write a complete sentence that ends with a period.
- State what the doc covers, not just what the title says.
- Keep it 1-2 sentences max.

**Tags**
- Use domain or concept keywords, not document titles.
- Prefer fewer tags (3-5) over many.
- All lowercase, hyphen-separated: `data-fetching`, not `DataFetching`.

**Related**
- Use for cross-domain docs or files that depend on each other.
- Only list files that exist in the same domain or across domains.
- No directory paths, no file extensions beyond `.md`.

## Valid vs. Invalid Examples

**Valid:**
```yaml
---
title: Query Patterns
description: Common patterns for writing efficient database queries.
tags:
  - database
  - queries
  - performance
status: active
related:
  - technology.md
  - schema-conventions.md
---
```

**Invalid (and why):**
```yaml
---
title: query patterns              # Not Title Case
description: Common patterns      # Missing trailing "."
tags: []                           # Empty list
status: draft                      # Not an allowed value (use "Draft")
related:
  - ../Knowledge/database/tech.md  # Has path separators
  - .hidden.md                     # Leading dot
category: database                 # Unexpected field
---
```

## Auto-Fix

The validation script can automatically fix missing frontmatter. After running validation, if invalid files are found, the script asks:

```
Found N invalid file(s). Would you like to fix them? [y/N]
```

If you choose `y`, it shows a numbered list and asks which files to fix:

```
Enter file numbers to fix (comma-separated) or 'all':
```

### What Auto-Fix Does

| Scenario | Fix |
|----------|-----|
| No frontmatter block | Inserts frontmatter derived from file content |
| Frontmatter inside `` ``` `` markers | Strips the code block markers |
| Missing `description` | Extracts from first paragraph after H1 heading |
| Missing `tags` | Generates from domain folder + filename |
| Missing `status` | Defaults to `Draft` |

### How Content Is Extracted

**Title** — from the first `# Heading` in the file:
```markdown
# Deployment
```
→ `title: Deployment`

**Description** — first non-empty, non-heading line after the H1:
```markdown
# Deployment

How the backend gets built, released, and monitored.
```
→ `description: How the backend gets built, released, and monitored.`

**Tags** — from folder name + filename:
- File: `Knowledge/backend/deployment.md`
- → `tags: [backend, deployment]`

### Limitations

- Cannot fix invalid values (e.g., wrong Title Case, missing period on description)
- Files with no H1 heading get `title: TODO: Add Title`
- Files with no description paragraph get `description: TODO: Add description.`
- Always review auto-fixed files for accuracy

## Scope & Validation

**Applies to:** All `*.md` files in `Knowledge/`, excluding `AGENTS.md`, `.opencode/`, and `Templates/`.

**Validate by running:**
```bash
python3 .opencode/skills/frontmatter-validation/scripts/validate_frontmatter.py
```

Output: `VALID` or `INVALID` with numbered findings per file. If invalid files exist, the script prompts to fix them.
