---
name: knowledge
description: Use ONLY when authoring, updating, or maintaining documentation in the Knowledge/ folder — how-to guides, glossary entries, troubleshooting notes, or questions about doc frontmatter/format conventions. Not for reading knowledge or general questions.
---

# Knowledge & Documentation

Pointer for working with the vault's documentation. The actual rules live in the files listed below; read them before writing or reviewing docs.

## When to use

- Authoring or editing any documentation under `Knowledge/`.
- Maintaining how-to guides, glossary terms, or troubleshooting entries.
- Questions about doc conventions (frontmatter, structure, templates).

## Where the knowledge lives

- Index of all domains and their documents: `knowledgebase.json`.
- Source of truth for doc authoring: `Knowledge/knowledge/AGENTS.md`.
- Documentation practices: `Knowledge/knowledge/how-to-guides.md`, `Knowledge/knowledge/glossary.md`, `Knowledge/knowledge/troubleshooting.md`.
- Doc template: `Templates/knowledge.md`.

## How to use

1. Read `Knowledge/knowledge/AGENTS.md` first — it is the source of truth for doc authoring rules.
2. Locate the relevant domain and its documents in `knowledgebase.json`.
3. Follow the frontmatter convention (`title`, `description`, `tags`, `status`, `related`) used across `Knowledge/`.
4. For domain-specific work, use the sub-skills in this folder: `frontend`, `backend`, `database`, `api`, `ai`.
5. Do not duplicate knowledge in skills — always point to the source docs.