---
name: handoff
description: Compact the current conversation into a standalone handoff document so a fresh agent or session can continue the work with zero prior context. Use when the user says "hand off", "handoff", "compact this session", "write a handoff", or "continue this in a new session". Invoke-only — it does not auto-fire.
argument-hint: "What will the next session focus on?"
version: 1.0.0
license: MIT
disable-model-invocation: true
---

# handoff — compact this session for a fresh agent

Produce a standalone document a cold agent can act on with **zero prior context**. (Distilled in our own way from Matt Pocock's `handoff`, MIT.)

## Where to write it
Save to the **OS temp directory** (`%TEMP%` on Windows, `$TMPDIR` / `/tmp` on macOS/Linux) — **never** the workspace/repo. Handoff docs are ephemeral; they don't belong in git.

## Skeleton
```markdown
# Handoff — <one-line topic>

## Goal
What we're trying to achieve (the destination, not the history).

## Current status
Where things stand now; what works, what's half-done.

## Key decisions & rationale
Choices already made and *why* — so the next agent doesn't relitigate them.

## Files touched
`path` — one line on what changed and why. (List, don't paste diffs.)

## Next steps
Ordered, actionable. The first thing the next agent should do.

## Open questions & blockers
Anything unresolved or waiting on the user.

## Suggested skills
Which skills the next agent should invoke to continue (e.g. /lazy-surgical, /grill).

## References
Existing artifacts (PRDs, plans, ADRs, issues, commits, diffs) linked by path/URL.
```

## Rules
- **Reference, don't duplicate.** If it's already in a PRD, plan, ADR, issue, commit, or diff, link it by path/URL — don't re-summarize. The handoff is an index/launchpad, not a transcript.
- **Redact secrets/PII** before writing to disk — API keys, tokens, passwords, personal data.
- If an argument was passed, treat it as the **next session's focus** and bias the doc toward it.
- Keep it terse. A cold agent should be productive after one read.
