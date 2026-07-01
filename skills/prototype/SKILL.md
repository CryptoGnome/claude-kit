---
name: prototype
description: Build a THROWAWAY prototype to answer ONE design question — a runnable terminal app to sanity-check state/logic, or several structurally-different UI variants toggled on one route. Use when unsure whether a state model feels right, or what a screen should look like. Do NOT use for production code, for building a real feature, or for a spike you intend to keep — the code is deleted; only the answer survives.
version: 1.0.0
license: MIT
---

# prototype — throwaway code that answers a question

A prototype is throwaway code that answers a design question. **The question decides the shape**, and only the *answer* is kept. (Distilled in our own way from Matt Pocock's `prototype`, MIT. Pairs with `grill` — align by code instead of interview.)

## Pick the branch (get this right — the wrong branch wastes the whole prototype)
- **"Does this logic / state model feel right?"** → a tiny interactive **terminal app** → [`references/logic.md`](references/logic.md).
- **"What should this look like?"** → several **UI variants on one route** → [`references/ui.md`](references/ui.md).

If ambiguous and the user's unreachable, default by surrounding code (a backend module → logic; a page/component → UI) and state the assumption at the top of the prototype.

## Six rules (both branches)
1. **Throwaway from day one, clearly marked.** Put it next to what it prototypes; name it so a reader sees it's not production. Obey the project's existing routing/structure.
2. **One command to run**, via the project's existing task runner — the user starts it without thinking.
3. **No persistence by default** — state lives in memory (unless persistence *is* the question; then a scratch DB/file named "PROTOTYPE — wipe me").
4. **Skip the polish** — no tests, no error handling beyond runnable, no abstractions.
5. **Surface the state** — after every action (logic) or on every variant switch (UI), show the full relevant state so the user sees what changed.
6. **Delete or absorb when done** — delete it, or fold only the validated decision into real code. Don't let it rot.

## Keep the answer
The answer is the only durable output. Capture it (a commit message, a `NOTES.md` next to the prototype, or wherever your team records decisions) *with the question it answered* before deleting the prototype. The surprised reaction while running it — "wait, that shouldn't be possible" — is the signal: a bug in the *idea*.
