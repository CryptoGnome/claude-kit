---
name: semver
description: Decide the correct next version number using Semantic Versioning (SemVer 2.0.0). Use when versioning a release, bumping a version, tagging, publishing a package/plugin/skill, or writing a changelog entry, or when the user asks "what version is this", "should this be major/minor/patch", "bump the version", or "how do I version this". Do NOT use for calendar/date versioning (CalVer), marketing names, or git commit messages.
argument-hint: "[current-version?]"
version: 1.0.0
license: MIT
---

# semver — pick the right version number

Semantic Versioning is **`MAJOR.MINOR.PATCH`** (e.g. `2.4.1`). The number is a *promise* to whoever depends on you. Choose the bump from the **single most impactful change** since the last release — one breaking change makes the whole release MAJOR, no matter how many small fixes rode along.

## The decision — run top to bottom, first match wins

1. **MAJOR** (`x.0.0`) — you **broke backwards compatibility**. Someone upgrading might have to change their code or config.
   - Removed or renamed a public function, flag, field, endpoint, or env var.
   - Changed a default, a return shape, or behavior callers relied on.
   - Tightened validation so input that used to work now fails.
2. **MINOR** (`x.y.0`) — you **added** something, backwards-compatibly. Existing users upgrade with zero changes.
   - New feature, function, flag, endpoint, or optional field.
   - Marked something **deprecated** (it still works — actual removal is the future MAJOR).
3. **PATCH** (`x.y.z`) — backwards-compatible **fix** or no-surface change.
   - Bug fix that keeps the intended contract.
   - Performance, docs, internal refactor, dependency bump with no visible change.

When you bump a higher slot, **reset the lower ones to 0**: `1.4.2` → MAJOR `2.0.0` · MINOR `1.5.0` · PATCH `1.4.3`.

## The 0.x rule (pre-1.0 — read this if the version starts with 0)

While `0.y.z` the API is unstable and *anything may change*. The compatibility promise is relaxed:
- **Breaking** change → bump **MINOR**: `0.4.1` → `0.5.0`.
- **Anything else** (new feature, fix, wording) → bump **PATCH**: `0.4.1` → `0.4.2`.

First public drop is usually **`0.1.0`**. Cut **`1.0.0`** when the API is stable, in production, or you're ready to promise compatibility.

## Pre-release & build metadata

- Pre-release: append `-alpha.1`, `-beta.2`, `-rc.1` → `1.2.0-rc.1`. Ranks **below** the final `1.2.0`.
- Build metadata: append `+<info>` → `1.2.0+build.5`. Ignored when comparing precedence.
- Precedence: `1.0.0-alpha` < `1.0.0-alpha.1` < `1.0.0-beta` < `1.0.0-rc.1` < `1.0.0`.

## "Compatible with what?" — the API depends on the project

- **Library / package:** exported symbols, types, signatures.
- **CLI / app:** commands, flags, config keys, output others script against.
- **Service / API:** endpoints, request/response shapes, status codes.
- **A skill collection (like this kit):** each skill's `name`, triggers, and arguments. Adding a skill is a **feature**; rewording or fixing one is a **fix**; renaming/removing a skill or changing its `argument-hint`/triggers is **breaking**. Then apply the bump rules above (including the 0.x rule while pre-1.0).

## Operational flow — how a bump actually ships

1. Pick the bump using the decision above.
2. Set the version in the source of truth (`package.json`, `plugin.json`, `pyproject.toml`, `Cargo.toml`, …).
3. Add a dated `CHANGELOG.md` entry under the new version (Added / Changed / Fixed).
4. Commit, then tag: `git tag vX.Y.Z && git push --tags`.
5. **One version = one tag = one changelog entry.** Never move or reuse a published tag.

## Litmus check before you commit the bump

- Could a user's working setup break on upgrade? → **MAJOR** (or MINOR pre-1.0), however small the diff.
- Did you only *add*, nothing removed or changed? → **MINOR** (PATCH pre-1.0).
- Only a fix or invisible change? → **PATCH**.
- Stuck between two levels? **Pick the higher one** — under-bumping silently breaks people.
