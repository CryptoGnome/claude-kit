# Changelog

All notable changes to claude-kit. Versions track `plugin.json`; `/plugin update` keys on them.

## [0.1.0] — 2026-06-30

### Added
- Repo scaffold: `.claude-plugin/` marketplace + plugin manifests, README, MIT license, `.gitignore` (secrets-aware).
- **Governance rules** ([GOVERNANCE.md](GOVERNANCE.md)) — the bar for adding/updating/removing a skill.
- **Roadmap** ([PLAN.md](PLAN.md)) — curation buckets and the porting order for the rest of the kit.
- **`devlog`** `v1.0.0` — structured changelog from git commits → markdown + Discord summary. Portable port: removed the hard-coded personal repo path (now defaults to the current working directory) and added trigger/negative-scope to the description.
