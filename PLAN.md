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
| `design-mockup` | **Folded into `image-gen`** (v0.3.0) — game-art templates moved into the prompt guide; skill removed | — | — |
| `generate-image` | **Local-only** — pure TerraCore brand tooling (brand suffix, on-disk asset paths, game API); `design-mockup` covers neutral gen | — | — |
| `design-taste-frontend` | **Shipped v0.1.2** as slim house skill `frontend-design` — distilled from taste-skill, not re-vendored | none | ✅ |
| `redesign-existing-projects` | **Shipped v0.1.2** — split into slim SKILL.md + `references/audit-checklist.md` | none | ✅ |
| `hive-post` | **Local-only** — Hive/PeakD blogging, niche to your workflow; not part of the shared kit | — | — |
| `peakd-publish` | **Local-only** — Hive broadcast via hive-js (posting key); too personal + secret-heavy to share | — | — |
| `discord-update` | **Local-only** — TerraCore Discord webhook; not part of the shared kit | — | — |
| `concept-to-3d` | **Removed in v0.2.0 — local-only** — niche game-art tooling, out of scope for a general kit | — | — |

## New / house skills (written our way)

- **`semver`** (shipped v0.1.1) — house/meta skill, not from pile 2: teaches SemVer so the agent versions the kit and any project correctly. Foundational discipline the kit (and its own governance) relies on.
- **`lazy-surgical`** (shipped v0.1.2) — house coding-discipline skill synthesizing Karpathy (think-first, surgical, simple, goal-driven) + ponytail (reuse-before-write ladder, "when not to be lazy", tunable intensity). The showcase of the "best parts, our way" approach.
- **`image-gen`** (shipped v0.3.0) — general OpenRouter image generator; verified multi-model menu + prompt/style guide. `design-mockup` was folded into it.
- **`security-review`** (optional) — deepsec-skill model: wrap the `deepsec` CLI with a free-recon→approval→paid-process gate. Add only if you actually run security passes.

## Porting order

- **v0.1 (done):** scaffold + governance + roadmap (no bundled skill; `devlog` stays local-only).
- **v0.1.1 (done):** `semver` — teaches SemVer so agents version the kit (and any project) correctly.
- **v0.1.2:** added `lazy-surgical`, `frontend-design`, `redesign-existing-projects`, `design-mockup`, `concept-to-3d`.
- **v0.2.0 (done):** removed `concept-to-3d` (out of scope for a general kit; stays local). Breaking ⇒ minor bump pre-1.0.
- **v0.3.0 (done):** added `image-gen` (general OpenRouter image gen) and folded `design-mockup` into it.
- **v0.3.1 (done):** de-duped `redesign-existing-projects` against `frontend-design`.
- **v0.4.0 (done):** renamed `frontend-taste` → `frontend-design`.
- **v0.4.1 (done):** added a `SessionStart` hook that keeps `lazy-surgical` always-on (no slash needed).
- **Next:** cut **`1.0.0`** once the skill set feels stable (per the `semver` skill, the pre-1.0 → 1.0 stabilization milestone). Optional later: `security-review` (deepsec wrap) if you start running security passes.

> **Local-only (not in the kit):** `devlog`, `hive-post`, `peakd-publish`, `discord-update`, `generate-image`, `concept-to-3d` — personal or niche tooling (Hive/Discord/TerraCore workflow, game-art) and/or secret-heavy. They live in `~/.claude/skills/` and are deliberately excluded from the shared, public kit.

Each port follows [GOVERNANCE.md](GOVERNANCE.md): audit for secrets/paths → trigger-engineer the description → minimize the body → test triggering → changelog + version bump.
