---
name: redesign-existing-projects
description: Upgrade an EXISTING website or app to premium quality without breaking it. Audits the current design, finds generic/AI patterns, and applies high-end fixes that work with the existing stack (any CSS framework or vanilla CSS). Use when the user wants to redesign, polish, upgrade, modernize, or "make an existing site look less generic / more premium". Do NOT use for building a brand-new site from scratch — use anti-slop-frontend for that.
version: 1.0.0
license: MIT
---

# redesign-existing-projects

Upgrade what's already there. Work with the existing stack — do not migrate frameworks or rewrite from scratch.

## Workflow
1. **Scan** — read the codebase. Identify the framework, styling method (Tailwind v3/v4, vanilla CSS, styled-components, …), and current design patterns.
2. **Diagnose** — first apply the shared aesthetic rules from the [`anti-slop-frontend`](../anti-slop-frontend/SKILL.md) skill (fonts, color, layout clichés, interactive states, copy tells — the one source of truth), then run the existing-code audit in [`references/audit-checklist.md`](references/audit-checklist.md). List every generic pattern, weak point, and missing state you find.
3. **Fix** — apply targeted upgrades within the existing stack. Improve what's there; keep changes small and reviewable.

## Fix priority (max impact, min risk)
1. **Font swap** — biggest instant win, lowest risk.
2. **Color cleanup** — remove clashing / oversaturated colors; one accent.
3. **Hover / active states** — makes the interface feel alive.
4. **Layout & spacing** — proper grid, max-width container, consistent padding.
5. **Replace generic components** — swap cliche patterns for modern alternatives.
6. **Loading / empty / error states** — makes it feel finished.
7. **Typography scale & rhythm** — the premium final touch.

## Rules
- Work with the existing tech stack. Do not migrate frameworks or styling libraries.
- Do not break functionality. Test after every change.
- Check the project's dependency file before importing any new library; check the Tailwind version (v3 vs v4) before touching config.
- Small, targeted improvements over big rewrites. Keep diffs reviewable.

The audit checklist ([`references/audit-checklist.md`](references/audit-checklist.md)) covers only what's **specific to auditing existing code** — surface/alignment craft, component swaps, iconography, code quality, accessibility & strategic omissions, and premium upgrade techniques. The shared aesthetic rules (fonts, color, layout, states, copy) live once in [`anti-slop-frontend`](../anti-slop-frontend/SKILL.md). Apply both during **Diagnose**.
