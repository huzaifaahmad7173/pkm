# Epic → Subtask Review Pipeline

Authoritative process for taking any epic from idea to an approved epic draft with approved subtask drafts. Follow this for every epic and every subtask. No exceptions.

## Pipeline diagram

```
Epic Draft
  └─▶ Review Cycle (epic stage, max 10 cycles)
        ├─ @kb-editor / @kb-tech-lead / @kb-architect   (fresh, read sources)
        ├─ all APPROVE ──────────────▶ Epic APPROVED
        └─ any CHANGES REQUIRED ──▶ revise → next cycle
               └─ conflict / recurring / adjudication
                     └─▶ AskQuestion → user decision → apply → next cycle

Epic APPROVED
  └─▶ Subtask Draft(s)
        └─▶ Review Cycle (subtask stage, max 10 cycles)
              ├─ @kb-editor / @kb-tech-lead / @kb-architect   (fresh, read sources)
              ├─ all APPROVE ──────────────▶ FINALIZE
              └─ any CHANGES REQUIRED ──▶ revise → next cycle
                     └─ conflict / recurring / adjudication
                           └─▶ AskQuestion → user decision → apply → next cycle
```

## Rules (non-negotiable)

1. **I never write.** All writing and revising is delegated to the `general-task` agent. The orchestrator (main agent) only: drafts the prompt, runs reviews, collects verdicts, escalates, and finalizes.
2. **Fresh reviews every cycle.** Each cycle, `@kb-editor`, `@kb-tech-lead`, and `@kb-architect` each re-review the latest revision from scratch. No carry-over of prior conclusions; a prior APPROVE does not bind the next cycle.
3. **Max 10 cycles per stage.** Each stage (epic, then subtasks) allows up to 10 cycles. After 10 cycles in a stage the current draft is submitted to the user for a final accept/reject decision — never silently approved.
4. **Escalate to the user** (AskQuestion) when any of these occur:
   - Reviewers **conflict** (one APPROVE, another CHANGES REQUIRED) on the same item.
   - An issue **reoccurs** across two or more consecutive cycles.
   - The orchestrator needs **adjudication** on any ambiguous scope, priority, or trade-off.
   The user's decision is applied in the next revision; the decision is binding.
5. **Parallelism.** Reviews run in parallel via the Task tool (one `general`-type task per reviewer or direct subagent launch), then verdicts are collected before any revision.

## Grounding & anti-hallucination (non-negotiable)

These rules exist so drafts and verdicts are grounded in the vault, never in memory or plausibility. They apply only to content produced by this pipeline (epic and subtask drafts, reviewer verdicts) — not to the model's general behavior.

1. **Drafts must cite every claim.** Every factual or convention claim in a draft carries its source as `path:line`. Un-cited claims are defects. Anything not in the vault is written as an explicit **ASSUMPTION**, never as fact.
2. **Writers must read before writing.** `general-task` reads the source material (idea/research input, relevant domain docs, `knowledgebase.json`, `Templates/`) before drafting or revising. It reports which files it read.
3. **Reviewers must read before judging.** Each reviewer verifies the draft's claims and citations against the actual vault files (Read/Glob/Grep). A verdict that does not reference the files read is invalid.
4. **Verify citations.** Reviewers confirm each `path:line` citation exists and says what the draft claims. Missing, fabricated, or mismatched citations are CHANGES REQUIRED.
5. **No unverifiable approvals.** No reviewer APPROVEs content it cannot confirm from the vault. Unverifiable claims are CHANGES REQUIRED with the exact citation the writer must supply.
6. **Recurring grounding defects escalate.** If fabricated citations, unsourced claims, or assumptions presented as facts recur across cycles, escalate to the user via AskQuestion.

## Cycle flow (detailed)

1. **Draft** — Orchestrator launches `general-task` to produce the Epic Draft from the idea (source: `Ideas/`, `Research/`). The agent reads source material and returns the draft with citations.
2. **Subtasks** — Only after the epic draft is approved does the orchestrator launch `general-task` to decompose the approved epic into Subtask Drafts, same grounding requirements.
3. **Cycle start** — Orchestrator launches all three reviewers in parallel against the latest draft (the epic during the epic stage; the subtask drafts during the subtask stage). Each reviewer reads the referenced vault files before judging.
4. **Collect verdicts** — Each reviewer returns APPROVE or CHANGES REQUIRED with findings, referencing the files/lines they read.
5. **Decide**
   - All APPROVE → during the epic stage this approves the epic and starts the subtask stage; during the subtask stage this finalizes.
   - Any CHANGES REQUIRED → if conflict/recurrence/adjudication present → AskQuestion; then launch `general-task` with the feedback to produce the revision → increment cycle → loop.
   - Cycle count ≥ 10 in a stage → present the current draft to the user for a final decision.
6. **Finalize** — Write approved drafts to their destination (default: `Projects/` for epics, nested subtasks under the epic's file). Confirm with the user before final writing if location was not pre-agreed.

## Verdict format

Reviewers return `APPROVE` or `CHANGES REQUIRED` plus a numbered list of findings, each referencing section/line and the exact change. Findings on citations must name the correct `path:line` to use.

## Artifacts

- Epic and subtask drafts live under `Projects/` (or as agreed per epic).
- Raw material stays in `Ideas/` and `Research/`.
- Templates and conventions: `Templates/`, `knowledgebase.json`, `Knowledge/<domain>/AGENTS.md`.