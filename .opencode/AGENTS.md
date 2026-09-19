# Skills

Skills are invoked automatically when a matching task is detected. Load the appropriate skill before proceeding.

For pipeline rules, agents, and audit procedures, see the [main AGENTS.md](../AGENTS.md).

## Available Skills

| Skill | When to invoke | Do NOT invoke when |
|-------|---------------|-------------------|
| `env-dependency-checker` | After cloning the repo, when things break mysteriously, before starting a work session, or when the user asks "are all deps installed?" | User wants to install or manage dependencies |
| `file-summary` | User asks to summarize, analyze, or explain a file under `Knowledge/` | Non-Markdown files, `AGENTS.md` files, or when user wants to edit/validate/commit a file |
| `frontmatter-validation` | During audit pipeline, after `general-task` creates/revises a Knowledge doc, before reviewer sign-off, when migrating a doc from `Ideas/`/`Research/`/`Projects/` | Non-Markdown files, `AGENTS.md` files, files under `.opencode/` or `Templates/` |
| `git-commit-assistant` | User asks to write/suggest/draft a commit message, says they are ready to commit, or asks what they should commit | No staged changes, directory is not a git repo, user wants to run `git commit` directly |

## Invocation Rules

1. **Read the skill's SKILL.md** before executing its procedure — it contains the exact steps and output format.
2. **Report-only** — skills diagnose and suggest; they do not modify the environment unless explicitly confirmed by the user.
3. **Ask before fixing** — when a skill can auto-fix issues (e.g., `frontmatter-validation`), always confirm with the user first.
4. **Respect scope** — each skill defines what it covers. If a task falls outside that scope, use a different tool or skill instead.