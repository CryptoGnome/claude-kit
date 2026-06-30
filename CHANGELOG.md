# Changelog

All notable changes to claude-kit. Versions track `plugin.json`; `/plugin update` keys on them.

## [0.1.0] — 2026-06-30

### Added
- Repo scaffold: `.claude-plugin/` marketplace + plugin manifests, README, MIT license, `.gitignore` (secrets-aware).
- **Governance rules** ([GOVERNANCE.md](GOVERNANCE.md)) — the bar for adding/updating/removing a skill.
- **Roadmap** ([PLAN.md](PLAN.md)) — curation buckets and the porting order for the kit.

### Notes
- No skills are bundled in the scaffold. Several personal skills are intentionally kept **local-only** (in `~/.claude/skills/`) and are not part of the shared kit: `devlog`, `hive-post`, `peakd-publish`, `discord-update` — all tuned to a personal Hive/Discord/TerraCore workflow and/or secret-heavy. The first curated skill ships in v0.2.
