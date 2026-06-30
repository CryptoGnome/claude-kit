# Changelog

All notable changes to claude-kit. Versions track `plugin.json`; `/plugin update` keys on them.

## [0.1.0] — 2026-06-30

### Added
- Repo scaffold: `.claude-plugin/` marketplace + plugin manifests, README, MIT license, `.gitignore` (secrets-aware).
- **Governance rules** ([GOVERNANCE.md](GOVERNANCE.md)) — the bar for adding/updating/removing a skill.
- **Roadmap** ([PLAN.md](PLAN.md)) — curation buckets and the porting order for the kit.

### Notes
- No skills are bundled in the scaffold. `devlog` is intentionally kept **local-only** (`~/.claude/skills/devlog`) — it's tuned to a personal workflow and is not part of the shared kit. The first curated skill ships in v0.2.
