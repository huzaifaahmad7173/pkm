---
name: file-summary
description: Generates a detailed analysis summary of a specific Knowledge base Markdown file. Produces structured output covering purpose, structure, key concepts, dependencies, and domain context. Use when asked to summarize, analyze, or explain a file under the Knowledge/ directory.
---

# File Summary

Generates a detailed analysis of a Knowledge base Markdown file.

## When to Invoke

- User asks to summarize a file under `Knowledge/`.
- User asks for an overview or analysis of a Knowledge doc.
- User wants to understand what a specific document covers.
- Files outside `Knowledge/` directory.

## When Not to Invoke

- Non-Markdown files (JSON, images, scripts).
- Domain `AGENTS.md` files — these are config, not content docs.
- User asks to edit, validate, or commit a file (use other skills/tools).

## Schema

Reference: `schema.yaml` in this skill directory.

The schema defines the output structure for file summaries, including required sections, field sources, and fallback values. Read the YAML file for the full field definitions. The schema defines:

- **Output sections:** `summary`, `structure`, `key_concepts` (required); `related_files` (optional)
- **Field sources:** frontmatter, file path, or content scan
- **Fallback values:** Used when frontmatter fields are missing

## Procedure

1. **Locate the file.** Confirm the target file exists under `Knowledge/`. If the user provides a relative path, resolve it against the repo root. If the file does not exist, report the error and stop.

2. **Read the file.** Load the full content including YAML frontmatter.

3. **Analyze the content.** Extract:
   - Frontmatter fields: `title`, `description`, `tags`, `status`, `related`
   - Heading structure (H1, H2, H3 levels)
   - Key concepts, rules, patterns, or guidelines documented
   - References to other files (inline links or mentions)
   - Domain context (which subdirectory: `api/`, `frontend/`, `backend/`, `database/`, `ai/`, `knowledge/`)

4. **Generate the summary.** Use the Output Format below.

## Output Format

```
## Summary: <title>
**Domain**: <domain> | **Status**: <status>
**Tags**: <tags>

### Purpose
<1-2 sentence description of what this document covers, derived from frontmatter description and content>

### Structure
- <Section 1 heading>: <brief note on what it covers>
- <Section 2 heading>: <brief note on what it covers>
- ...

### Key Concepts
- <Concept 1>: <one-line explanation>
- <Concept 2>: <one-line explanation>
- ...

### Related Files
- <filename.md>: <relationship or shared topic>
- ...
```

## Rules

- Do not fabricate content. Base the summary only on what the file actually contains.
- If frontmatter is missing fields, note them as `—` in the output.
- If the file has no related files, omit the Related Files section.
- Keep each bullet point to one sentence maximum.
- Do not include the full file content in the summary.
