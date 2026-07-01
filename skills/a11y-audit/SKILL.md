---
name: a11y-audit
description: Audit existing UI code for accessibility and UX violations (semantics/ARIA, keyboard & focus, contrast, forms, motion, images, headings, target sizes) and emit terse file:line findings with fixes. Use when the user asks to check accessibility, audit a11y, review UI for a11y/UX, or find accessibility issues in existing code. Do NOT use for generating new design (anti-slop-frontend) or aesthetic redesign (redesign-existing-projects) — this is a compliance audit.
version: 1.0.0
license: MIT
---

# a11y-audit

An accessibility/UX **audit** for existing UI code — read it, grep it against the checklist, report violations. (Distilled in our own way from Vercel Labs' web-interface-guidelines, MIT.) This is the compliance layer; `anti-slop-frontend` and `redesign-existing-projects` are the aesthetic layers.

## How to run
1. Read the target file(s) or glob (components, pages, CSS).
2. Do the **fast-pass grep** below.
3. Then read against the full themed checklist in [`references/a11y-rules.md`](references/a11y-rules.md).
4. Emit findings in the output contract. No preamble.

## Fast-pass anti-patterns (cheap sweep first)
`user-scalable=no` / `maximum-scale=1` · `onPaste` + `preventDefault` · `transition: all` · `outline: none` / `outline-none` with no `:focus-visible` replacement · `<div>`/`<span>` with `onClick` (should be `<button>`/`<a>`) · `<img>` without `width`+`height` · icon-only `<button>` without `aria-label` · inputs without a `<label>` · hardcoded date/number formats · `.map()` over >50 items with no virtualization · `autoFocus` without justification.

## Output contract
- Group findings **by file**.
- One line per issue: `path:line - short problem → fix`.
- Sacrifice grammar for brevity; high signal, no preamble.
- Print `✓ pass` for a clean file.

The full checklist (semantics/ARIA, keyboard & focus, color & contrast, forms, motion, images, headings, target sizes) is in [`references/a11y-rules.md`](references/a11y-rules.md).
