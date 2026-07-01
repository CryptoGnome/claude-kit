---
name: grill
description: Interrogate the user about a plan or design until there's shared understanding, BEFORE writing any code. Use when starting non-trivial work, or when the user says "grill me", "stress-test this plan", "interrogate me", or "align before building". Do NOT use for tiny or obvious changes, or once the plan is already clear and agreed.
version: 1.0.0
license: MIT
---

# grill — align before you build

The #1 failure mode is building the wrong thing because agent and human never truly aligned. Close that gap first. (Distilled in our own way from Matt Pocock's `grill-me` / `grilling`, MIT.)

## Method
Interview the user relentlessly about the plan, walking the design as a **decision tree** — resolve dependencies one branch at a time (the answer to one question opens or closes the next).

1. **One question at a time.** Ask, wait for the answer, then ask the next. Batching questions is bewildering — never do it.
2. **Always give your recommended answer** with each question, so the user reacts and corrects rather than authoring from scratch. This also surfaces your assumptions where they can be caught.
3. **Answer it yourself from the code when you can.** If exploring the codebase resolves a question, go read the codebase — never ask the human what the repo already knows. Only ask what the human alone can decide.
4. **Sharpen the language as you go.** When a term is vague or overloaded, pin it to one canonical meaning before moving on — shared words are shared understanding.
5. **Stop when every branch is resolved.** Restate the agreed plan in a few bullets and get confirmation. Only then start coding.

## When to stop early
If it's a one-line or obvious change, skip the interrogation — use judgment. This is for work where misalignment would be expensive. Pairs with `lazy-surgical` (which then keeps the build minimal and surgical).
