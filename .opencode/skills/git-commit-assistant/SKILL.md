---
name: git-commit-assistant
description: Analyzes the staged diff and suggests meaningful Conventional Commits messages. Use when the user asks to write, suggest, or create a commit message, or says "help me commit", "what should I commit", "suggest a commit", or "commit message for this change".
---

# Git Commit Assistant

Suggests Conventional Commits-style commit messages based on the staged changes only.

## When to Invoke

- User asks to write, suggest, or draft a commit message.
- User says they are ready to commit or have staged changes.
- User asks to review what they should commit.

## When Not to Invoke

- No staged changes — report that the index is empty and stop.
- User wants to create the commit itself (this skill only suggests; the user commits manually).
- Directory is not a git repository.

## Procedure

1. **Verify the repo.** Confirm the current directory is inside a git work tree. If not, report the error and stop.

2. **Check the index.** Run `git diff --staged --stat`. If there are no staged changes, report that nothing is staged and stop.

3. **Read the diff.** Run `git diff --staged` and read the full diff, including changed filenames and hunks. For very large diffs, skim each hunk and classify by file path.

4. **Classify the change.** Pick the single best Conventional Commits type: `feat`, `fix`, `docs`, `refactor`, `perf`, `test`, `build`, `ci`, `chore`, `style`, or `revert`. Add an optional scope derived from the modified area, e.g. `feat(database):`.

5. **Write 3 candidate messages.** Each will be presented as an option for the user to choose from:
   - **A — concise:** subject only, imperative mood, 50 characters or less.
   - **B — detailed:** subject plus a body of short bullets covering what changed and why.
   - **C — breaking:** subject with `!` and a `BREAKING CHANGE:` footer — but only when the diff actually warrants it (removed behavior, renamed interface, changed output). If it does not warrant a breaking change, make C a second alternative subject instead.

## Output Format

Present the candidates as a labeled block with a one-line rationale per option, tied to the actual diff:

```
A — <subject>            (concise, <NN> chars)
B — <subject>
     <body bullets>      (detailed)
C — <subject>            (breaking, <reason>)
```

## Examples

### Good Examples

feat: add user login
fix: resolve database connection error
docs: update installation guide
refactor: simplify authentication logic
test: add login validation tests

### Bad Examples

update stuff
fixed bug
changes
added some files

## Rules

- Imperative mood: "Add pagination", not "Added pagination" or "Adds pagination".
- Describe only what the staged diff actually does. Never fabricate intent or features not present in the diff.
- Keep subjects under 50 characters where possible; lowercase after any `type(scope):` prefix.
- Suggest only. Never run `git commit` or modify the index.