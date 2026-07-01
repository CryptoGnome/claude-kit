# claude-kit

> CryptoGnome's curated, minimal, opinionated Claude Code skills. Install once, use on every project, keep in sync, share with anyone.

This is **not** a kitchen-sink mega-pack. It's a small, ruthlessly-curated set of skills written *our way* — taking the best parts of the skills worth borrowing, stripped to their essence, portable across projects, and free of machine-specific defaults and secrets.

## Install

**Option A — native plugin (recommended, cross-project, auto-updates):**

```
/plugin marketplace add CryptoGnome/claude-kit
/plugin install claude-kit@claude-kit
```

Skills are then available everywhere as `/<skill-name>` (e.g. `/devlog`).

**Option B — the `skills` CLI (copy-and-own a single skill):**

```
npx skills add CryptoGnome/claude-kit                   # the whole kit
npx skills add CryptoGnome/claude-kit --skill semver    # just one
```

**Option C — manual (copy into your skills folder):**

```bash
git clone https://github.com/CryptoGnome/claude-kit.git
cp -r claude-kit/skills/semver ~/.claude/skills/      # personal (all projects)
# or into a project:  cp -r claude-kit/skills/semver .claude/skills/
```

## Update

- **Plugin install:** `/plugin marketplace update claude-kit` (or enable auto-update in `/plugin`). New version, new skills, improvements — all pulled in.
- **Manual / CLI install:** `git pull` and re-copy, or re-run `npx skills add`.

See [CHANGELOG.md](CHANGELOG.md) for what changed in each version.

## Skills

| Skill | What it does | Secrets |
|---|---|---|
| [`semver`](skills/semver/SKILL.md) | Decide the correct next version with Semantic Versioning — major/minor/patch, the 0.x rule, pre-release tags, the changelog→tag flow | none |
| [`lazy-surgical`](skills/lazy-surgical/SKILL.md) | Coding-discipline mode: the least code that fully solves it — reuse before writing, surgical diffs, simple-first, verifiable done (`lite`/`full`/`ultra`) | none |
| [`frontend-design`](skills/frontend-design/SKILL.md) | Anti-slop guardrails for NEW frontend UI — design read, variance/motion/density dials, countable layout rules, em-dash ban | none |
| [`redesign-existing-projects`](skills/redesign-existing-projects/SKILL.md) | Upgrade an EXISTING site to premium quality without breaking it — audit, prioritized fixes, works with any stack | none |
| [`image-gen`](skills/image-gen/SKILL.md) | Generate any kind of image via OpenRouter — pick from several models (Gemini / GPT / FLUX / Seedream / Grok), built-in prompt & style help | OpenRouter key (env / gitignored `key.txt`) |

_Curated deliberately — see [PLAN.md](PLAN.md) for the roadmap and [GOVERNANCE.md](GOVERNANCE.md) for the bar every skill must clear before it's added._

## Philosophy

- **Subtraction over accumulation.** A skill earns its place or it's cut.
- **One skill = one job.** Split anything that does two things.
- **Rules as countable checks, not vibes.** "≤ 4 elements", "trace every line to the request" — not "use good judgment".
- **Trigger-engineered descriptions.** Each skill says exactly when to fire and when *not* to.
- **Portable & safe by default.** No machine-specific paths, no committed secrets, ever.

## License

[MIT](LICENSE) © CryptoGnome
