---
name: research
description: Delegate reading legwork to a background agent — investigate a question against PRIMARY sources (official docs, source code, specs, first-party APIs), follow each claim to its source, and leave a single cited Markdown note in the repo. Use when the next step is finding something out (how an API behaves, what a spec actually says, whether a claim holds) and you'd rather not stall your own thread. Do NOT use for a heavy multi-source verified report (reach for a dedicated deep-research harness), for interviewing the user about a plan (use grill), or for writing marketing/blog content.
version: 1.0.0
license: MIT
---

# research — delegate the reading, keep the cited note

The defining move: the reading runs as a **background agent**, so you keep working while it reads. You get back a document to react to, with its sources attached. Research is legwork you *delegate*, not thinking you outsource. (Distilled in our own way from Matt Pocock's `research`, MIT. It feeds the thinking skills — hand its note to `grill` to sharpen a plan.)

## How
1. **Spin up a background agent** (Task/Agent tool, run in the background) so the main thread isn't blocked.
2. **Work from primary sources only** — official docs, source code, specs, first-party APIs. Never a secondary write-up or a summary of a summary. **Follow every claim back to the source that owns it.**
3. **Write one cited Markdown file** — each claim carries its source (URL / `file:line` / spec section). Findings, not vibes.
4. **Save it where the repo already keeps such notes** — match the existing convention; if there's none, pick a sensible spot and say where.

## Scope
- Fast, in-flow, single-question reading → a cited note. For a heavy multi-source, adversarially-verified report, reach for a dedicated deep-research harness instead.
- The note is an **input** to the next step (grill, plan, design), not the decision itself.
