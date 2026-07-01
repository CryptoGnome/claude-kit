---
name: plan-to-issues
description: Turn a discussion or spec into a shipping plan — synthesize a PRD from the current conversation (no interview), then break it into independently-grabbable, end-to-end VERTICAL-SLICE issues. Publishes GitHub issues via `gh`, or writes markdown files if there's no tracker. Use when the user says "plan this", "write a PRD", "break this into issues/tickets", or "cut this into slices". Do NOT interview the user (synthesize what's already been discussed), and do NOT use for a trivial change that needs no plan or for implementing the code itself.
version: 1.0.0
license: MIT
---

# plan-to-issues — PRD, then vertical slices

Synthesize a plan from what's already been discussed, then cut it into thin end-to-end slices an agent (or human) can grab independently. (Distilled in our own way from Matt Pocock's `to-prd` + `to-issues`, MIT — with his personal issue-tracker setup stripped out.)

**Do NOT interview** — synthesize the current conversation + codebase understanding. If the repo has a domain glossary or ADRs, use them; otherwise carry on.

## Phase 1 — the PRD
Explore the repo for current state, then write a PRD with these sections:
1. **Problem statement** — from the user's perspective.
2. **Solution** — from the user's perspective.
3. **User stories** — a long numbered list, each "As an `<actor>`, I want `<feature>`, so that `<benefit>`." Extensive; cover every aspect.
4. **Implementation decisions** — modules built/modified and their interfaces, technical clarifications, schema changes, API contracts. **No file paths or code snippets** (they go stale) — *exception:* a prototype-derived state machine / reducer / schema / type that encodes a decision more precisely than prose.
5. **Testing decisions** — what makes a good test (test external behaviour, not implementation details), which modules get tested, and similar tests already in the codebase.
6. **Out of scope.**
7. **Further notes.**

**Seam checkpoint (the one interactive gate):** before finalizing, name the seams you'll test the feature through — prefer existing seams, use the highest one possible, aim for **one**. Confirm with the user they match expectations.

## Phase 2 — vertical slices
Break the PRD into **tracer-bullet** issues. Three rules:
1. Each slice delivers a **narrow but COMPLETE path through every layer** (schema → API → UI → tests) — a vertical slice, never a horizontal slice of one layer.
2. A completed slice is **demoable / verifiable on its own**.
3. Any **prefactoring first** ("make the change easy, then make the easy change").

**Granularity checkpoint:** present the breakdown as a numbered list — each slice's Title, "Blocked by", and "User stories covered". Ask: right granularity? dependencies correct? merge/split any? Iterate until approved.

## Output
- **If `gh` is available in a GitHub repo:** create issues with `gh issue create` — the PRD as a parent issue first, then each slice in **dependency order** (so "Blocked by" references resolve to real issue numbers). Cross-link. Apply a label only if the user asked. Don't modify parent/other issues.
- **Otherwise:** write `PRD.md` + one markdown file per slice into `docs/plans/<feature>/` (or a path the user picks).

Each issue: **## What to build** (end-to-end behaviour, no file paths) · **## Acceptance criteria** (checkbox list) · **## Blocked by** (blocking issue refs, or "None — can start immediately").
