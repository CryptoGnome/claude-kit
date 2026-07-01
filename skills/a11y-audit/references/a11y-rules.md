# Accessibility & UX Rules

Reference for the `a11y-audit` skill. MUST / NEVER one-liners; check each theme. (Union distilled from vercel-labs/web-interface-guidelines `command.md` + `AGENTS.md`, MIT.)

## Semantics / ARIA
- Icon-only buttons MUST have `aria-label`.
- Use `<button>` for actions, `<a>`/`<Link>` for navigation — NEVER `<div onClick>`.
- Prefer native semantics (button / a / label / table) BEFORE reaching for ARIA.
- Decorative icons get `aria-hidden="true"`.
- Async updates (toasts, inline validation) need `aria-live="polite"`.
- An accessible name MUST exist even when the visual label is omitted.

## Keyboard & Focus
- Every interactive element needs a visible focus ring via `:focus-visible`.
- NEVER `outline:none` / `outline-none` without a focus replacement.
- Group compound controls with `:focus-within`.
- Full keyboard support per WAI-ARIA APG; manage focus (trap / move / return) in modals.
- Enter submits an input; Cmd/Ctrl+Enter submits a textarea.

## Color & Contrast
- MUST meet contrast (prefer APCA over WCAG 2).
- Interactive states MUST gain contrast on hover / active / focus.
- Status MUST NOT be color-only — add a redundant icon + text cue.
- Charts use color-blind-friendly palettes.

## Forms & Labels
- Every control needs a `<label>` (htmlFor / wrapping) or `aria-label`.
- Inputs: `autocomplete`, a meaningful `name`, correct `type` (email/tel/url/number) + `inputmode`.
- NEVER block paste (`onPaste` + `preventDefault`) — breaks 2FA / password managers.
- Keep submit enabled until the request starts, then show a spinner.
- Validate AFTER typing; show errors inline; focus the first error on submit.
- `spellCheck={false}` on emails / codes / usernames.
- Label + control are ONE hit target (no dead zones on checkbox / radio).
- Placeholders end with "…" and show an example. Warn on unsaved changes before nav. Trim trailing whitespace.

## Motion / Reduced-motion
- MUST honor `prefers-reduced-motion` (reduced variant or disable).
- Animate only `transform` / `opacity` — NEVER layout props (top/left/width/height).
- NEVER `transition: all` — list properties explicitly.
- Correct `transform-origin`; SVG transforms on a `<g>` with `transform-box:fill-box`.
- Animations are interruptible / input-driven — no autoplay.

## Images / Alt & CLS
- `<img>` needs explicit `width` + `height` (prevents CLS).
- `alt` required (`alt=""` if decorative).
- Below-fold `loading="lazy"`; above-fold `priority` / `fetchpriority="high"`.

## Headings & Landmarks
- Hierarchical `<h1>`–`<h6>`; include a "Skip to content" link.
- `scroll-margin-top` on heading anchors; `<title>` matches the current context.
- No dead ends — always offer a next step / recovery.

## Target sizes & Touch
- Hit target ≥ 24px (mobile ≥ 44px) — expand the hit area if the visual is smaller.
- Mobile `<input>` font-size ≥ 16px (prevents iOS auto-zoom).
- `touch-action: manipulation`; NEVER disable zoom.
- `overscroll-behavior: contain` in modals / drawers.

## State / URL & Nav (also flag)
- URL reflects state (filters / tabs / pagination in query params).
- Back / Forward restores scroll position.
- Destructive actions need a confirm OR an undo window — never immediate.

## Typography / content polish (optional tail)
Use "…" not "..."; curly quotes; non-breaking spaces (`10&nbsp;MB`); `tabular-nums` for number columns; `text-wrap: balance/pretty` on headings; truncate / line-clamp with `min-w-0` on flex children; `Intl.DateTimeFormat` / `NumberFormat` (never hardcoded); `translate="no"` on brand / code tokens.
