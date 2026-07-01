# Governance — how we add and update skills

These are the rules every skill in `claude-kit` must follow. They're distilled from the skills worth copying (taste-skill, karpathy-guidelines, ponytail, deepsec, shadcn) plus Anthropic's skill-authoring guidance. Keep them short; keep them enforced.

---

## The bar for adding a new skill

A new skill gets added only if it passes **all** of these:

### 1. It earns its place
- Solves a real, recurring job you actually hit. If you wouldn't use it this month, don't add it.
- **One skill = one job.** If it does two things, it's two skills (or it's split). Bundling kills triggering.
- It doesn't overlap an existing skill. If it does, **merge or replace** — never duplicate.

### 2. Structure
- Lives at `skills/<name>/SKILL.md`. Folder name = the `name:` in frontmatter, kebab-case.
- Name must **not** contain `claude` or `anthropic` (reserved words).
- Frontmatter (YAML), in this order:
  ```yaml
  ---
  name: my-skill
  description: <see rule 3>
  version: 1.0.0
  argument-hint: "[optional]"   # only if it takes args
  license: MIT
  ---
  ```

### 3. The description is trigger-engineering, not a summary
The `description` is the only thing that decides whether the skill fires. It must contain:
- **(a) Capability** — what it does, in one phrase.
- **(b) Literal triggers** — the actual phrases a user would say ("make a mockup", "what shipped", "scan for vulnerabilities").
- **(c) Negative scope** — an explicit `Do NOT use for …` clause so it doesn't over-fire.

Max 1024 chars. Third person ("Use when…"), never "I can…".

### 4. The body is minimal and checkable
- Prose skills: aim **under ~150 lines**. Detail → `references/`, code → `scripts/`, examples → `examples/` (loaded only when needed).
- Prefer **rules as negations and countable checks** over soft advice. "No abstractions for single-use code" beats "keep it simple".
- Where it fits, end with a **pre-flight / litmus gate**: "If any of these fail, you're not done."
- Assume the model is smart. Don't explain what Claude already knows.

### 5. Portable & safe (hard requirement — this repo is public)
- **No machine-specific paths.** No `C:\Users\...`, no personal default repo/output paths. Default to the cwd or an argument; ask if ambiguous.
- **No secrets, ever.** API keys, posting keys, webhook URLs, tokens, account names → resolved from an **environment variable** (preferred) or a **gitignored** `key.txt`, documented in the skill. Never committed.
- **Never read another project's `.env`.** Keys are per-project.
- If a skill needs a secret, it documents the setup and fails gracefully with instructions when the secret is missing.

### 6. Ship it
- Add a row to the **Skills table in `README.md`** (including the Secrets column).
- Add a **`CHANGELOG.md`** entry. Bump `version` in the skill and `plugin.json`.
- **Test triggering** on a real task before committing — confirm it fires from its description, and that it doesn't fire when it shouldn't.

---

## Updating an existing skill

1. **Edit in place. Subtract first.** The best change is usually deleting a line, not adding one. Only add what earns its place.
2. **Bump the version** (SemVer — see the [`semver`](skills/semver/SKILL.md) skill for the full decision). **The kit is now 1.x**, so post-1.0 rules apply:
   - **patch** = wording/fixes; **minor** = a new skill or a new capability in an existing one; **major** = a rename, removal, or a breaking change to a skill's triggers/args.
   - (History: while pre-1.0 we bumped **minor** for breaking changes and **patch** for additions/fixes; `1.0.0` was cut once the skill set stabilized.)
   - Always bump `plugin.json` `version` when anything ships (this is what `/plugin update` keys on).
3. **Record it** in `CHANGELOG.md` with the date and what changed.
4. **Tag & push:** `git tag vX.Y.Z && git push --tags` — that's how plugin consumers pull the update (the `/plugin` flow only needs the tag + `plugin.json` version). For **minor and milestone** versions, also cut a **GitHub Release** from the tag (`gh release create vX.Y.Z --notes-file <the CHANGELOG section>`) so watchers get an announcement and a clean "Latest release." **Patches stay tag-only** to avoid Releases-page noise — Releases are for humans, not the installer.
5. **Re-test triggering.**

---

## Curation philosophy (the "taste")

- **Subtraction over accumulation** — the kit gets better by removing, not hoarding.
- **Skills compose, they don't collide** — state scope boundaries ("governs X, not Y; pair with Z").
- **Keep `plugin.json` tiny** — the manifest is metadata; the skills carry the weight.
- **One signature constraint per skill** — a single memorable, verifiable rule anchors a skill's identity better than ten soft ones.
- **An escape hatch** — say when *not* to apply the skill, so it never makes the agent rigid.

---

## Removing a skill

If a skill stops being used, **cut it**. Move it to a `graveyard/` note in the CHANGELOG (one line: name, version removed, why) and delete the folder. A smaller kit is a better kit.
