# claude-kit

![claude-kit — curated, minimal, opinionated Claude Code skills](assets/banner.png)

> CryptoGnome's curated, minimal, opinionated Claude Code skills. Install once, use on every project, keep in sync, share with anyone.

This is **not** a kitchen-sink mega-pack. It's a small, ruthlessly-curated set of skills written *our way* — taking the best parts of the skills worth borrowing, stripped to their essence, portable across projects, and free of machine-specific defaults and secrets.

## Install

**Option A — native plugin (recommended, cross-project, auto-updates):**

```
/plugin marketplace add CryptoGnome/claude-kit
/plugin install claude-kit@claude-kit
```

Skills are then available everywhere as `/<skill-name>` (e.g. `/semver`).

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

Twelve skills, grouped by what they're for. All auto-activate by description (or run any with `/<name>`).

### Discipline & workflow
| Skill | What it does | Secrets |
|---|---|---|
| [`lazy-surgical`](skills/lazy-surgical/SKILL.md) | The least code that fully solves it — reuse first, surgical diffs, simple, verifiable (`lite`/`full`/`ultra`). Always-on via hook | none |
| [`grill`](skills/grill/SKILL.md) | Interrogate the plan (one question at a time, with recommended answers) until aligned, before any code | none |
| [`handoff`](skills/handoff/SKILL.md) | Compact the session into a standalone handoff doc for a fresh agent (invoke-only) | none |
| [`caveman`](skills/caveman/SKILL.md) | Terse-output mode — strips filler, keeps every fact/command exact (`lite`/`full`/`ultra`) | none |
| [`semver`](skills/semver/SKILL.md) | The correct next version via SemVer — major/minor/patch, the 0.x rule, changelog→tag flow | none |

### Frontend & design
| Skill | What it does | Secrets |
|---|---|---|
| [`anti-slop-frontend`](skills/anti-slop-frontend/SKILL.md) | Anti-slop guardrails for NEW UI — design read, dials, countable layout rules, em-dash ban | none |
| [`redesign-existing-projects`](skills/redesign-existing-projects/SKILL.md) | Upgrade an EXISTING site without breaking it — audit + prioritized fixes, any stack | none |
| [`a11y-audit`](skills/a11y-audit/SKILL.md) | Audit UI code for accessibility/UX violations → terse `file:line` findings | none |
| [`react-best-practices`](skills/react-best-practices/SKILL.md) | Fix React/Next.js perf + component architecture in impact order (waterfalls, bundles, RSC) | none |

### Content & visuals
| Skill | What it does | Secrets |
|---|---|---|
| [`marketing-copy`](skills/marketing-copy/SKILL.md) | High-converting copy — positioning, headline/CTA formulas, page structure, offer & objection frameworks | none |
| [`image-gen`](skills/image-gen/SKILL.md) | Generate any image via OpenRouter (Gemini / GPT / FLUX / Seedream / Grok) + prompt/style help | OpenRouter key |
| [`remotion`](skills/remotion/SKILL.md) | Programmatic video in React (Remotion) — frame-driven animation, deterministic rendering, sequencing | none |

_Curated deliberately — see [GOVERNANCE.md](GOVERNANCE.md) for the bar every skill must clear before it's added._

## Always-on discipline (hook)

You **don't** have to invoke skills with slash commands. Most skills **auto-activate by description** when your request matches them — or run any explicitly with `/<name>` (`handoff` is invoke-only).

`lazy-surgical` is a coding *temperament* you'd want on every edit, so the kit ships a `SessionStart` hook ([`hooks/hooks.json`](hooks/hooks.json) → [`hooks/session-start.js`](hooks/session-start.js)) that injects its rules into **every session** automatically. (`hooks/hooks.json` is auto-loaded by Claude Code — it is intentionally **not** declared in `plugin.json`, which would double-load it.) To turn it off, disable the plugin in `/plugin` or delete `hooks/hooks.json` from your copy. (Requires Node.js; if Node isn't present the hook is skipped harmlessly.)

## Philosophy

- **Subtraction over accumulation.** A skill earns its place or it's cut.
- **One skill = one job.** Split anything that does two things.
- **Rules as countable checks, not vibes.** "≤ 4 elements", "trace every line to the request" — not "use good judgment".
- **Trigger-engineered descriptions.** Each skill says exactly when to fire and when *not* to.
- **Portable & safe by default.** No machine-specific paths, no committed secrets, ever.

## License

[MIT](LICENSE) © CryptoGnome
