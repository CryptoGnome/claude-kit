---
name: devlog
description: Generate a structured changelog/devlog from git commits since a date, tag, or commit, grouped by type, ready for a blog post, release notes, or a Discord summary. Use when the user asks for a changelog, devlog, release notes, "what shipped", or a summary of recent commits. Do NOT use for writing new code or for non-git projects.
argument-hint: "[since] [repo?]"
version: 1.0.0
license: MIT
---

# devlog

Generate a clean, readable devlog/changelog from git history. Two outputs every time: a markdown block for a post/release notes, and a short punchy Discord summary.

## Inputs

- **Since** `{{since}}` — a date (`2026-04-24`), git tag, or commit hash to start from. Defaults to the last 7 days if blank.
- **Repo** `{{repo}}` — path to the git repo. Defaults to the **current working directory**. If the cwd is not a git repo, check parent directories, then ask the user for the path. Never hard-code a personal default.

## Process

### 1 — Get the commits

```bash
git -C "{{repo}}" log --since="{{since}}" --pretty=format:"%h %s" --no-merges
```

If `{{since}}` looks like a tag or commit hash (not a date), use `{{since}}..HEAD` instead of `--since`.

### 2 — Categorize

One bucket per commit; pick the most specific.

| Category | Keywords |
|---|---|
| **Security & Integrity** | security, race, atomic, replay, duplicate, auth, guard, validate |
| **Features** | feat, add, new, implement |
| **Bug Fixes** | fix, bug, crash, error, broken, incorrect |
| **Infrastructure** | infra, deploy, ci, workflow, failover, health, node |
| **Performance** | perf, optimiz, speed, cache |
| **Cleanup** | remove, delete, clean, refactor, deprecat, unused |
| **Docs** | docs, readme, comment, changelog |

### 3 — Write it

**A) Markdown** (blog / release notes):

```markdown
## What Shipped — [date range]

### Security & Integrity
- [plain-English summary, not the raw commit message]

### New Features
- ...
```

Skip empty categories. Reword commit messages into plain English a reader (not just the committer) can follow — e.g. "Atomic claim reserve prevents duplicate payouts", not "fix: findOneAndUpdate claim atomicity".

**B) Discord summary** (5–10 bullets max, only non-empty categories):

```
🔒 Security: [1-line summary]
✨ Features: [1-line summary]
🐛 Fixes: [1-line summary]
⚙️ Infra: [1-line summary]
```

### 4 — Save & report

1. Save the markdown to `devlog-[date].md` in the repo (or cwd).
2. Print the Discord summary in the response for copy-paste.
3. Report: filename saved, total commit count, date range.

## Constraints

- Never invent or embellish commits — summarize only what's in the log.
- If there are no commits in the range, say so plainly.
- Skip merge commits and bot/dependency commits (`Merge…`, `chore(deps)…`).
