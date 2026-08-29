# Common Frontmatter Errors

Quick troubleshooting reference when validation fails.

## Quick Diagnosis

| Error Tag | Likely Cause | Fix Strategy |
|-----------|-------------|--------------|
| `[MISSING] No frontmatter block` | File has no `---` delimiters | Add frontmatter block at top of file |
| `[MISSING] Required field` | Field omitted from frontmatter | Add the missing field with correct format |
| `[UNEXPECTED] Field` | Wrong field name used | Check `schema.yaml` for allowed field names |
| `[INVALID VALUE] title` | Not in Title Case | Capitalize major words, keep small words lowercase |
| `[INVALID VALUE] description` | Missing trailing period | Add `.` at end of description |
| `[INVALID VALUE] tags` | Empty list or not kebab-case | Use lowercase alphanumeric with hyphens |
| `[INVALID VALUE] status` | Value not in allowed list | Use: `Draft`, `active`, `fleeting`, `seed`, or `planning` |
| `[INVALID VALUE] related` | Contains path separators or dots | Use bare `.md` filenames only |

---

## 1. Missing Frontmatter Block

**Error message:**
```
[MISSING] No frontmatter block found
```

**Cause:** The file has no YAML frontmatter between `---` delimiters.

**Wrong:**
```markdown
# Deployment

How the backend gets built, released, and monitored.

## Environments
...
```

**Correct:**
```markdown
---
title: Deployment
description: How the backend gets built, released, and monitored.
tags:
  - backend
  - deployment
status: Draft
---

# Deployment

How the backend gets built, released, and monitored.

## Environments
...
```

**Fix:** Add a frontmatter block at the very top of the file, before the `# Heading`.

---

## 2. Missing Required Fields

### Missing title

**Error message:**
```
[MISSING] Required field `title` not found
```

**Wrong:**
```yaml
---
description: Common patterns for writing efficient database queries.
tags:
  - database
  - queries
status: active
---
```

**Correct:**
```yaml
---
title: Query Patterns
description: Common patterns for writing efficient database queries.
tags:
  - database
  - queries
status: active
---
```

### Missing description

**Error message:**
```
[MISSING] Required field `description` not found
```

**Wrong:**
```yaml
---
title: Query Patterns
tags:
  - database
  - queries
status: active
---
```

**Correct:**
```yaml
---
title: Query Patterns
description: Common patterns for writing efficient database queries.
tags:
  - database
  - queries
status: active
---
```

---

## 3. Unexpected Fields

**Error message:**
```
[UNEXPECTED] Field `category` is not in the allowed schema
```

**Cause:** Field name is not in the allowed schema. Common mistakes: `category`, `author`, `date`, `type`, `priority`.

**Wrong:**
```yaml
---
title: Deployment
description: How the backend gets built, released, and monitored.
tags:
  - backend
  - deployment
status: Draft
category: backend
---
```

**Correct:**
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

**Allowed fields only:** `title`, `description`, `tags`, `status`, `related`.

---

## 4. Invalid Title

**Error message:**
```
[INVALID VALUE] `title` = `query patterns` — not in Title Case
```

**Cause:** Title does not follow Title Case rules.

### Not Title Case

**Wrong:**
```yaml
title: query patterns
```

**Correct:**
```yaml
title: Query Patterns
```

### Small words capitalized

**Wrong:**
```yaml
title: Authentication And Authorization
```

**Correct:**
```yaml
title: Authentication and Authorization
```

**Rules:**
- Capitalize major words.
- Keep small words lowercase: `a`, `an`, `and`, `as`, `at`, `but`, `by`, `for`, `in`, `nor`, `of`, `on`, `or`, `so`, `the`, `to`, `up`, `yet`.
- Keep acronyms uppercase: `API`, `SQL`, `LLM`.

---

## 5. Invalid Description

### Missing trailing period

**Error message:**
```
[INVALID VALUE] `description` — must end with `.`
```

**Wrong:**
```yaml
description: Common patterns for writing efficient database queries
```

**Correct:**
```yaml
description: Common patterns for writing efficient database queries.
```

### Empty description

**Error message:**
```
[INVALID VALUE] `description` — must be a non-empty string
```

**Wrong:**
```yaml
description: ""
```

**Correct:**
```yaml
description: Overview of query patterns and optimization strategies.
```

---

## 6. Invalid Tags

### Empty list

**Error message:**
```
[INVALID VALUE] `tags` — must be a non-empty list
```

**Wrong:**
```yaml
tags: []
```

**Correct:**
```yaml
tags:
  - database
  - queries
```


## 7. Invalid Status

**Error message:**
```
[INVALID VALUE] `status` = `draft` — must be one of: Draft, active, fleeting, seed, planning
```

**Cause:** Status value does not match an allowed value exactly (case-sensitive).

**Wrong:**
```yaml
status: draft
```

**Correct:**
```yaml
status: Draft
```

**Allowed values:**

| Value | Meaning |
|-------|---------|
| `Draft` | Not yet finalized |
| `active` | Current, in-use |
| `fleeting` | Temporary or quick note |
| `seed` | Early idea, needs development |
| `planning` | Being planned, not implemented |

Note: `Draft` is capitalized; all others are lowercase.

---

## 8. Invalid Related

### Contains path separators

**Error message:**
```
[INVALID VALUE] `related` item `../database/tech.md` — must be a bare .md filename
```

**Wrong:**
```yaml
related:
  - ../database/tech.md
  - Knowledge/backend/deployment.md
```

**Correct:**
```yaml
related:
  - tech.md
  - deployment.md
```

### Leading dot

**Error message:**
```
[INVALID VALUE] `related` item `.hidden.md` — must be a bare .md filename
```

**Wrong:**
```yaml
related:
  - .hidden.md
```

**Correct:**
```yaml
related:
  - hidden.md
```

**Rules:** Bare `.md` filenames only. No `/`, `..`, `\`, or leading dots.

---

## 9. Frontmatter in Code Block

**Cause:** Frontmatter wrapped in ` ``` ` markers, usually from copy-paste.

**Wrong:**
~~~markdown
```
---
title: Deployment
description: How the backend gets built, released, and monitored.
tags:
  - backend
  - deployment
status: Draft
---
```
~~~

**Correct:**
```markdown
---
title: Deployment
description: How the backend gets built, released, and monitored.
tags:
  - backend
  - deployment
status: Draft
---

# Deployment
```

**Fix:** Remove the ` ``` ` markers around the frontmatter block.

---

## Auto-Fixable vs Manual

| Error | Auto-Fixable | Fix Action |
|-------|-------------|------------|
| No frontmatter block | Yes | Inserts frontmatter derived from file content |
| Frontmatter in code block | Yes | Strips ` ``` ` markers |
| Missing `title` | Yes | Extracts from first `# Heading` |
| Missing `description` | Yes | Extracts from first paragraph after H1 |
| Missing `tags` | Yes | Generates from domain folder + filename |
| Missing `status` | Yes | Defaults to `Draft` |
| Invalid title (wrong case) | No | Manual edit required |
| Description missing period | No | Manual edit required |
| Invalid tags (wrong format) | No | Manual edit required |
| Invalid status (wrong value) | No | Manual edit required |
| Invalid related (has paths) | No | Manual edit required |
| Unexpected fields | No | Manual removal required |

Auto-fix only handles missing fields and structural issues. Invalid values always require manual correction.
