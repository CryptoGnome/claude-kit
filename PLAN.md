# claude-kit — plan & roadmap

The goal: one minimal repo you own, that installs on any project in two lines, stays in sync via `/plugin update`, and is clean enough to share. Built by curating two piles into one kit.

## The two source piles

**Pile 1 — your existing skills** (`~/.claude/skills/`, already yours, proven):
`devlog`, `design-mockup`, `generate-image`, `design-taste-frontend`, `redesign-existing-projects`, `hive-post`, `peakd-publish`, `discord-update`, `concept-to-3d`.

**Pile 2 — reference repos to strip for parts** (don't re-vendor wholesale; take the best mechanics):
- **taste-skill** (Leonxlnx) — numeric dials w/ baselines, countable rules, banlists of tells, a terminal pre-flight checklist, one signature hard ban.
- **karpathy-guidelines** — one temperament per skill, rules as negations, a litmus test per principle, imperative→verifiable-goal tables, an explicit "when not to apply".
- **ponytail** — the YAGNI decision ladder, reuse-before-write, "when NOT to be lazy" guardrails, tunable intensity (lite/full/ultra), terse output discipline.
- **deepsec / deepsec-skill** — wrap a CLI don't reimplement it, generic body + per-project context file, trigger-dense description + non-triggers, an activation canary, a free-recon→paid-step approval gate, a `security:` frontmatter block.
- **shadcn** — copy-and-own distribution; we keep updates clean via plugin marketplace + semver instead of shadcn's manual re-add pain.

## Distribution model (decided)

Structure the repo as **both** a native Claude Code plugin/marketplace **and** `npx skills add`-compatible — same `skills/` folders serve both. This gives the cleanest "install in two lines, update via `/plugin`" path without building a custom CLI/registry. We revisit a custom updater only if the native flow ever isn't enough.

## Curation decisions (pile 1)

| Skill | Decision | Secret audit | Priority |
|---|---|---|---|
| `devlog` | **Local-only** — stays in `~/.claude/skills/`, not part of the shared kit (tuned to a personal workflow) | none | — |
| `design-mockup` | **Keep** — strip hard-coded Python path; keep env/`key.txt` key handling | OpenRouter key (env/gitignored) | v0.2 |
| `generate-image` | **Merge → deprecate** — `design-mockup` is the neutral superset; keep only if a thin brand wrapper is truly wanted | OpenRouter key | v0.2 |
| `design-taste-frontend` | **Slim rewrite** — it's essentially taste-skill; either depend on upstream or distill our own shorter house version (don't re-vendor 13 skills) | none | v0.3 |
| `redesign-existing-projects` | **Keep / slim** — pairs with taste; audit-first redesign | none | v0.3 |
| `hive-post` | **Local-only** — Hive/PeakD blogging, niche to your workflow; not part of the shared kit | — | — |
| `peakd-publish` | **Local-only** — Hive broadcast via hive-js (posting key); too personal + secret-heavy to share | — | — |
| `discord-update` | **Local-only** — TerraCore Discord webhook; not part of the shared kit | — | — |
| `concept-to-3d` | **Keep** — heavier (Blender + Rodin/Hyper3D); audit for API keys | possible Hyper3D key | v0.4 |

## New skills to graft from pile 2 (written our way)

- **`lazy-surgical`** (or similar) — a house coding-discipline skill synthesizing karpathy (think-first, surgical, simple, goal-driven) + ponytail (reuse-before-write ladder, "when not to be lazy", tunable intensity). Shareable, no secrets, high value. **Best showcase of the "best parts" approach → port as skill #2.**
- **`security-review`** (optional) — deepsec-skill model: wrap the `deepsec` CLI with a free-recon→approval→paid-process gate. Add only if you actually run security passes.

## Porting order

- **v0.1 (done):** scaffold + governance + roadmap (no bundled skill; `devlog` stays local-only).
- **v0.2:** `lazy-surgical` (the graft) + `design-mockup` (secret hygiene); fold in `generate-image`.
- **v0.3:** `design-taste-frontend` (slim) + `redesign-existing-projects`.
- **v0.4:** `concept-to-3d` (heavier; Blender + Rodin/Hyper3D).

> **Local-only (not in the kit):** `devlog`, `hive-post`, `peakd-publish`, `discord-update` — all tuned to a personal Hive/Discord/TerraCore workflow and/or secret-heavy. They live in `~/.claude/skills/` and are deliberately excluded from the shared, public kit.

Each port follows [GOVERNANCE.md](GOVERNANCE.md): audit for secrets/paths → trigger-engineer the description → minimize the body → test triggering → changelog + version bump.
