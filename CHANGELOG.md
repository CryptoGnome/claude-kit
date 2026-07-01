# Changelog

All notable changes to claude-kit. Versions track `plugin.json`; `/plugin update` keys on them.

## [1.0.0] — 2026-07-01

**First stable release.** Sixteen curated, self-contained Claude Code skills across Discipline, Frontend, Content, and Web3, plus an always-on `lazy-surgical` hook. The set is settled — from here, SemVer's post-1.0 rules apply (new skill = minor, rename/removal = major, fix = patch).

### Changed
- **`seo-geo-aeo` deepened → `v1.1.0`.** Added a **Technical SEO** section (indexability, canonical / robots / sitemap correctness, 301s / redirect chains, HTTPS / mobile, hreflang), **AI-crawler & GEO** specifics (`robots.txt` for GPTBot / OAI-SearchBot / ClaudeBot / PerplexityBot / Google-Extended / CCBot, `llms.txt`, Bing + IndexNow since ChatGPT search reads Bing), **search-intent matching**, and named the Core Web Vitals metrics (LCP / INP / CLS). Enriched `references/schema-snippets.md` with **Product** and **LocalBusiness**. Same skill, same triggers.
- **`GOVERNANCE.md` versioning** updated to the post-1.0 rules.

## [0.5.5] — 2026-07-01

### Added
- **`security-audit`** `v1.0.0` — an agent-powered vulnerability audit rebuilt to run on **free tools you already have**: ripgrep triage → parallel Claude subagents that trace source→sink → an adversarial skeptic pass that culls false positives → severity-ranked findings (`file:line` + exploit + fix). Method inspired by Vercel's **deepsec** pipeline (scan → process → revalidate), but with **no paid scanner, no external CLI, no API keys, no per-file billing** — it uses your own subagents. Slim `SKILL.md` + `references/patterns.md` (the CWE triage catalog). Pairs with `ethereum`/`solana` for chain-specific security and the built-in `/security-review` for quick diffs.

### Note
- Deliberately **not** a wrapper around the deepsec CLI: deepsec's deep pass is paid (it bills your LLM account — potentially thousands on large repos). We took the *methodology*, not the cost. Additive + pre-1.0 ⇒ **patch** (`0.5.4 → 0.5.5`).

## [0.5.4] — 2026-07-01

### Added — three skills (crypto + SEO)
- **`ethereum`** `v1.0.0` — production EVM: Solidity security (CEI/reentrancy, `SafeERC20`, 6-decimal tokens, oracle/MEV/proxy rules), Foundry testing (`bound` not `vm.assume`, fork tests, fuzz/invariant), Scaffold-ETH 2 / viem / wagmi frontend + four-state tx UX, plus a verify-live current-network reference. Slim `SKILL.md` + `references/reference.md`. (from Austin Griffith's ethskills)
- **`solana`** `v1.0.0` — production Solana: `@solana/kit` over web3.js, Anchor + Pinocchio, PDA/bump canonicalization, the security vuln catalog (no `init_if_needed`, signer/owner checks, close-to-prevent-revival, Token-2022), Codama codegen, LiteSVM/Mollusk/Surfpool testing, tx-safety guardrails. Slim `SKILL.md` + `references/security-and-troubleshooting.md`. (from the Solana Foundation's solana-dev-skill, MIT)
- **`seo-geo-aeo`** `v1.0.0` — search & AI-answer readiness audit: SEO + AEO + GEO checklists (hard numbers + schema types), a 1–10 scored markdown report, and copy-paste JSON-LD snippets. **Rebuilt from a safety-audited source** (SNLabat/SEO-GEO-AEO-Skill — verified pure markdown, no scripts/hooks/network; we dropped its docx/PDF + machine-specific paths). Zero-dependency, WebFetch-only, consent-gated. Slim `SKILL.md` + `references/schema-snippets.md`.

All self-contained; no committed secrets (crypto skills reference external toolchains the project already has). Additive + pre-1.0 ⇒ **patch** (`0.5.3 → 0.5.4`).

## [0.5.3] — 2026-07-01

### Added
- **`remotion`** `v1.0.0` — rules & gotchas for Remotion (programmatic video in React → MP4): one clock only (`useCurrentFrame`; CSS/Tailwind animation forbidden), deterministic rendering (`random(seed)`, not `Math.random`), `interpolate`/`spring`, `useVideoConfig`, Studio-editable animation, `<Sequence>`/`<Series>` timing, `@remotion/media` assets, `calculateMetadata` for async data, and the `npx remotion` workflow. Self-contained, no deps/secrets; pairs with `react-best-practices`. (from remotion-dev/skills) Additive + pre-1.0 ⇒ **patch** (`0.5.2 → 0.5.3`).

## [0.5.2] — 2026-07-01

### Added — six skills (curated from the Firecrawl "best Claude Code skills" list, authored in our own voice)
- **`handoff`** `v1.0.0` — compact a session into a standalone handoff doc (OS temp dir, "suggested skills" routing, secret redaction). Invoke-only. (from mattpocock/skills)
- **`grill`** `v1.0.0` — interrogate the plan one question at a time (each with a recommended answer) until aligned, before coding. (from mattpocock/skills)
- **`caveman`** `v1.0.0` — terse-output mode; strips filler, keeps facts/code byte-exact; `lite`/`full`/`ultra`; pairs with `lazy-surgical`. (from JuliusBrussee/caveman)
- **`react-best-practices`** `v1.0.0` — React/Next.js performance + component architecture in impact order (waterfalls, bundle, RSC, server actions, compound components). (from vercel-labs/agent-skills)
- **`a11y-audit`** `v1.0.0` — accessibility/UX audit → terse `file:line` findings; slim `SKILL.md` + `references/a11y-rules.md`. (from vercel-labs/web-interface-guidelines)
- **`marketing-copy`** `v1.0.0` — high-converting copy (positioning, headline/CTA formulas, page structure, offer & objection frameworks); slim `SKILL.md` + `references/copy-frameworks.md`. (from coreyhaines31/marketingskills)

All self-contained, no external deps, no secrets. Additive + pre-1.0 ⇒ **patch** (`0.5.1 → 0.5.2`).

### Removed
- **`PLAN.md`** — the roadmap/curation doc is retired; the kit's shape is settled and `GOVERNANCE.md` holds the rules. (A repo doc, not a skill — no consumer impact.)

### Skipped from the list (already covered or out of scope)
- Firecrawl · Karpathy (→ `lazy-surgical`) · Anthropic Frontend Design (official plugin + `anti-slop-frontend`) · PDF/DOCX/XLSX/PPTX, Skill Creator, code-simplifier, Webapp Testing (official/built-in) · Superpowers (too heavy) · Remotion (niche) · Trail of Bits (needs external CodeQL/Semgrep) · Context Mode (→ `handoff`).

## [0.5.1] — 2026-07-01

### Fixed
- **SessionStart hook now loads cleanly.** Removed the `"hooks"` field from `plugin.json` — Claude Code auto-loads the standard `hooks/hooks.json`, so declaring it too caused a "Duplicate hooks file detected" error at install/enable. The always-on `lazy-surgical` hook now loads without error. Bug fix ⇒ **patch** (`0.5.0 → 0.5.1`).

## [0.5.0] — 2026-07-01

### Changed
- **Renamed `frontend-design` → `anti-slop-frontend`** to avoid a name + purpose clash with Anthropic's official `frontend-design` plugin. Folder, frontmatter `name`, and all cross-references (README, `redesign-existing-projects`) updated. Renaming a published skill is breaking ⇒ **minor** bump (`0.4.1 → 0.5.0`).

## [0.4.1] — 2026-07-01

### Added
- **`SessionStart` hook** (`hooks/hooks.json` + `hooks/session-start.js`) — injects the `lazy-surgical` coding discipline into every session's context so it's always applied without invoking `/lazy-surgical`. Compact directive scoped to coding work, with a pointer to the full skill and a nudge to use `semver` for version bumps. Requires Node.js; non-blocking if absent. Additive + pre-1.0 ⇒ **patch** (`0.4.0 → 0.4.1`).

## [0.4.0] — 2026-06-30

### Changed
- **Renamed `frontend-taste` → `frontend-design`** — a clearer, less loaded name. Skill folder, frontmatter `name`, and every cross-reference (README, `redesign-existing-projects`) updated. Renaming a published skill is breaking, so pre-1.0 this is a **minor** bump (`0.3.1 → 0.4.0`) per the `semver` skill.

## [0.3.1] — 2026-06-30

### Changed
- **De-duped `redesign-existing-projects` against `frontend-taste`.** The shared "AI design tells" (fonts, color, layout clichés, interactive states, copy voice) now live once in `frontend-taste`; `redesign`'s `references/audit-checklist.md` was rewritten to cover only what's specific to auditing/repairing existing code — surface & alignment craft, component swaps, iconography, code quality, accessibility & strategic omissions, and premium upgrade techniques — and points to `frontend-taste` for the rest. Same skill, same triggers ⇒ a **patch** (`0.3.0 → 0.3.1`).

## [0.3.0] — 2026-06-30

### Added
- **`image-gen`** `v1.0.0` — one general image generator via OpenRouter. Verified model menu (Gemini 3.1 Flash / 3 Pro / 2.5 Flash, GPT-5 image, FLUX.2, Seedream 4.5, Grok Imagine — confirmed against OpenRouter's live catalog, June 2026), a **stdlib-only** `scripts/generate.py` that auto-selects the right endpoint (chat + `modalities` for Gemini/GPT, `/api/v1/images` for the rest — no `pip install`), and a folded prompt/style guide (`references/prompt-guide.md`). Key via `OPENROUTER_API_KEY` env or gitignored `key.txt` (never committed).

### Removed / folded
- **`design-mockup`** — folded into `image-gen`; its game-art/UI templates now live in `image-gen/references/prompt-guide.md`. Local copy untouched. `frontend-taste` repointed to `image-gen`.

> _Graveyard: `design-mockup` merged into `image-gen` in v0.3.0._
> **Versioning:** removing a published skill is breaking, so pre-1.0 this is a **minor** bump (`0.2.0 → 0.3.0`) per the `semver` skill's 0.x rule — even though on net a skill was added.

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
- **Roadmap** (PLAN.md — since retired in v0.5.2) — curation buckets and the porting order for the kit.

### Notes
- No skills are bundled in the scaffold. Several personal skills are intentionally kept **local-only** (in `~/.claude/skills/`) and are not part of the shared kit: `devlog`, `hive-post`, `peakd-publish`, `discord-update` — all tuned to a personal Hive/Discord/TerraCore workflow and/or secret-heavy. The first curated skill ships in v0.2.
