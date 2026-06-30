# Changelog

All notable changes to claude-kit. Versions track `plugin.json`; `/plugin update` keys on them.

## [0.2.0] — 2026-06-30

### Removed
- **`concept-to-3d`** — dropped from the kit; it's niche game-art tooling (Blender + Hyper3D → Godot) that doesn't fit a general, shareable kit. Stays local-only in `~/.claude/skills/`.

> _Graveyard: `concept-to-3d` removed in v0.2.0 — out of scope for a general kit._
> **Versioning:** removing a published skill is a breaking change, so pre-1.0 this is a **minor** bump (`0.1.2 → 0.2.0`) per the `semver` skill's 0.x rule.

## [0.1.2] — 2026-06-30

### Added — the planned skill set (five skills)
- **`lazy-surgical`** `v1.0.0` — coding-discipline mode synthesizing Karpathy's guidelines + ponytail's YAGNI ladder, in our own voice: reuse-before-write ladder, surgical diffs, simple-first, goal-driven/verifiable, "when NOT to be lazy" guardrails, `lite`/`full`/`ultra` intensity. No secrets.
- **`frontend-taste`** `v1.0.0` — slim house distillation of anti-slop frontend rules (credit: Leonxlnx/taste-skill, MIT): design read, 3 dials (8/6/4), real-design-system honesty, font/color/layout banlists, countable rules (eyebrow/zigzag/hero caps; one-accent/radius/theme locks), em-dash ban, pre-flight. Scoped to NEW builds. No secrets.
- **`redesign-existing-projects`** `v1.0.0` — upgrade an existing site without breaking it. Split per governance into a slim `SKILL.md` (workflow, fix-priority, rules) + `references/audit-checklist.md` (the full category audit). No secrets.
- **`design-mockup`** `v1.0.0` — generate concept/mockup images via OpenRouter + Gemini, project-agnostic. Ported clean: genericized the Python path; key via `OPENROUTER_API_KEY` env or gitignored `key.txt` (never committed). Ships `scripts/generate.py` + `references/prompt-templates.md`.
- **`concept-to-3d`** `v1.0.0` — 2D concept → game-ready `.glb` in Godot via Blender (blender-mcp) + Rodin/Hyper3D. Depends on `design-mockup`. No committed secrets (Hyper3D key set in the Blender panel).

### Notes
- **Versioning:** five additions, but the kit is pre-1.0 and all are backwards-compatible, so this is a **patch** (`0.1.1 → 0.1.2`) per the 0.x rule — dogfooding the `semver` skill.
- `generate-image` is **not** ported — on audit it's pure TerraCore brand tooling (brand suffix, on-disk TerraCore asset paths, the TerraCore game API). It stays **local-only**; `design-mockup` covers neutral image generation.

## [0.1.1] — 2026-06-30

### Added
- **`semver`** `v1.0.0` — the kit's first real skill. Teaches Semantic Versioning (SemVer 2.0.0): a top-to-bottom decision procedure for the right major/minor/patch bump, the 0.x rule, pre-release/build metadata, what counts as "the API" per project type, and the changelog→tag release flow. No secrets.

### Changed
- `GOVERNANCE.md` versioning section made SemVer-exact: split post-1.0 vs pre-1.0 (0.x) bump rules, consistent with the new `semver` skill.

> This release is a **patch** under the 0.x rule — a pre-1.0, backwards-compatible addition. (Dogfooding the skill we just shipped.)

## [0.1.0] — 2026-06-30

### Added
- Repo scaffold: `.claude-plugin/` marketplace + plugin manifests, README, MIT license, `.gitignore` (secrets-aware).
- **Governance rules** ([GOVERNANCE.md](GOVERNANCE.md)) — the bar for adding/updating/removing a skill.
- **Roadmap** ([PLAN.md](PLAN.md)) — curation buckets and the porting order for the kit.

### Notes
- No skills are bundled in the scaffold. Several personal skills are intentionally kept **local-only** (in `~/.claude/skills/`) and are not part of the shared kit: `devlog`, `hive-post`, `peakd-publish`, `discord-update` — all tuned to a personal Hive/Discord/TerraCore workflow and/or secret-heavy. The first curated skill ships in v0.2.
