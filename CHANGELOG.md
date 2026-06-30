# Changelog

All notable changes to claude-kit. Versions track `plugin.json`; `/plugin update` keys on them.

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
