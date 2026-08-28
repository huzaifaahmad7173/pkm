# Project Guide

This is a personal knowledge base vault. Structure is defined in `knowledgebase.json`; domain rules live in `Knowledge/<domain>/AGENTS.md`; templates in `Templates/`.

## Epic and subtask pipeline

Any work that produces an epic or subtask draft **must** run through the review pipeline. Follow `.opencode/PIPELINE.md` exactly.

The rules in short:

1. **All writing is delegated** to the `general-task` agent. Never write draft content yourself.
2. **Every draft is reviewed** by `@kb-editor`, `@kb-tech-lead`, and `@kb-architect` in cycles, max **10 cycles**, with **fresh reviews each cycle**.
3. **Escalate to the user** via AskQuestion on reviewer conflict, issue recurrence, or adjudication.
4. Finalize only when all three reviewers approve, or the user decides after max cycles.
5. **Grounding (anti-hallucination):** drafts must cite every claim (`path:line`), writers and reviewers must read actual vault files before drafting/judging, and no one may approve content that is not verifiable from the vault. Assumptions are labeled, never stated as fact.

## Knowledge audit pipeline

Verification of existing `Knowledge/` docs runs through the **audit mode** in `.opencode/PIPELINE.md`. The same three reviewers check each doc for: link/citation integrity, frontmatter conventions, consistency with its domain `AGENTS.md`, and cross-doc contradictions. Fixes are delegated to `general-task`; max 10 cycles; escalate to the user on conflict, recurrence, or adjudication. Confirm scope with the user before starting an audit.

## Agents

- `@kb-editor` — editorial review (clarity, structure, consistency).
- `@kb-tech-lead` — technical review (feasibility, correctness, risk).
- `@kb-architect` — architectural review (decomposition, scope, system fit).
- `@general-task` — the writing agent; does all drafting and revision.