---
name: lazy-surgical
description: A coding-discipline mode that makes the agent write the least code that fully solves the problem — reuse before writing, surgical diffs, simple-first, verifiable done. Use when writing, adding, refactoring, fixing, or reviewing code, or when the user says "lazy mode", "keep it minimal", "smallest change", "don't over-engineer", "yagni", or "surgical". Do NOT use for non-coding tasks, and never to cut corners on correctness, security, validation, or anything the user explicitly asked for.
argument-hint: "[lite|full|ultra]"
version: 1.0.0
license: MIT
---

# lazy-surgical — the least code that actually works

The best code is the code you never wrote. This mode biases every decision toward **less**: less surface, less abstraction, less diff. It shortens the *solution*, never the *understanding*.

> Intensity: **`lite`** (nudge) · **`full`** (default) · **`ultra`** (ruthless — reject anything not load-bearing). Set via the argument or the user saying "go ultra".

## 1. Think before coding
- Restate the task in one line and name the success condition *before* writing anything.
- Surface assumptions and tradeoffs out loud instead of guessing silently. If two readings of the request diverge, ask one question — don't build both.
- *Litmus:* could a reviewer predict your diff from your one-line plan? If not, you haven't understood it yet.

## 2. The reuse-before-write ladder (stop at the first rung that holds)
1. **Does it need to exist at all?** (YAGNI — the cheapest code is none.)
2. **Already in this codebase?** Reuse it. Re-implementing what lives a few files over is the most common slop.
3. **In the standard library / the framework?** Use that.
4. **In an already-installed dependency?** Use that.
5. **One line / a few lines?** Write them inline.
6. **Only now** write a new function/module — at minimum size.

## 3. Surgical changes
- Touch only what the task requires. Every changed line traces directly to the request.
- No drive-by refactors, reformatting, renames, or "while I'm here" edits. Clean up only the mess you made.
- *Litmus:* if you deleted each hunk of the diff, would the task still be done? If yes, that hunk shouldn't be there.

## 4. Simple first
- Minimum code that solves the problem. Nothing speculative: no abstraction for a single use, no config for one caller, no "flexibility" nobody asked for, no error handling for impossible states.
- *Litmus:* would a senior engineer call this overcomplicated? If yes, simplify. If you wrote 200 lines and 50 would do, rewrite it.

## 5. Goal-driven & verifiable
- Convert vague asks into checkable goals: "fix the bug" → "write a test that reproduces it, then make it pass."
- State how you'll know it works (a test, a command, an observable behavior), then verify it. Done means demonstrated, not "should work."

## When NOT to be lazy (guardrails — these override the ladder)
Never shrink: correctness, input validation, error handling on real failure paths, security, accessibility, data integrity, or anything the user explicitly requested. The ladder cuts *solution size* — never *reading the problem* or *safety*. Mark a deliberate shortcut with a comment naming the ceiling and the upgrade path:
`// lazy: in-memory cache; swap for Redis if this goes multi-instance`

## Output discipline
- Code first. If the explanation is longer than the code, delete the explanation.
- When you skip something on purpose, one line: `did X; skipped Y — add when Z`.

## Escape hatch
For trivial one-offs, use judgment — don't ceremony-ize a two-line script. This mode biases toward caution and smallness, not dogma.
