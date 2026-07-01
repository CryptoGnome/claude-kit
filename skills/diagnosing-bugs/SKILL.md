---
name: diagnosing-bugs
description: A disciplined loop for hard bugs and performance regressions — build a reliable red/green feedback loop FIRST, then reproduce → minimise → hypothesise → instrument → fix + regression-test → clean up. Use when a bug is hard to pin down, intermittent/flaky, a perf regression, or you've been staring at it. Do NOT use for trivial obvious fixes, for building a green-field feature, or as a security review (use security-audit).
version: 1.0.0
license: MIT
---

# diagnosing-bugs — feedback loop first, then hunt

The move that makes debugging mechanical: **get a fast, deterministic pass/fail signal before you theorise.** Reading code before you have a red-capable loop is the failure this prevents. (Distilled in our own way from Matt Pocock's `diagnosing-bugs`, MIT.)

## 1. Build a feedback loop (spend the most effort here)
A command that runs the bug's code path and asserts the **exact** symptom. Prefer, in order: a failing test at the bug's seam → an HTTP/curl script → a CLI + fixture + snapshot → a headless-browser script → replay a captured trace → a throwaway harness → a property/fuzz loop → a **bisection harness** → an old-vs-new differential loop.
- **Tighten it like a product:** fast (aim ~2s, not 30s flaky), sharp (assert the specific symptom, not "didn't crash"), deterministic (pin time, seed RNG, isolate FS/network).
- **Flaky bug?** Raise the reproduction *rate* (loop 100×, parallelize, add stress) — a 50% flake is debuggable, 1% isn't.
- **Can't build a loop? STOP.** List what you tried and ask the user for access to a reproducing env, a captured artifact (HAR / log / core dump), or permission to instrument. **Never hypothesise without a loop.**

## 2. Reproduce + minimise
Run the loop; confirm it's the user's *exact* symptom, not a nearby failure. Then shrink to the smallest scenario that still fails — cut inputs/callers/config/steps **one at a time**, re-running after each. Done when every remaining element is load-bearing. (The minimal repro becomes your regression test.)

## 3. Hypothesise
Generate **3–5 ranked, falsifiable hypotheses before testing any.** Each states a prediction: "if X is the cause, changing Y makes it disappear." Can't state the prediction? Discard it. Show the ranked list to the user (they have context) before probing.

## 4. Instrument (one variable at a time)
Each probe maps to one prediction. Prefer a **debugger/REPL breakpoint** (one beats ten logs) over logging; never "log everything and grep." Tag every debug log with a unique prefix (`[DEBUG-a4f2]`) so cleanup can grep-and-remove them. **Performance regressions:** logs lie — establish a baseline measurement (profiler / `performance.now()` / query plan), then bisect. Measure first, fix second.

## 5. Fix + regression-test
Write the regression test **before** the fix — but only at a **correct seam** (one that exercises the real bug pattern as it occurs at the call site; a too-shallow seam gives false confidence). If no correct seam exists, that's an architecture finding — flag it (see [`codebase-design`](../codebase-design/SKILL.md)) rather than faking it. Then: repro → failing test → watch it fail → apply fix → watch it pass → re-run the loop against the *original* (un-minimised) scenario.

## 6. Clean up + post-mortem
Before "done": original repro no longer reproduces · regression test passes (or its absence is documented) · all `[DEBUG-…]` instrumentation removed · throwaway harnesses deleted · the correct hypothesis stated in the commit/PR. Then ask **"what would have prevented this?"** — if the answer is architectural (a missing seam, tangled callers), recommend it *after* the fix lands, not before.
