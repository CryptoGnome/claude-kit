#!/usr/bin/env node
// claude-kit SessionStart hook — keep the `lazy-surgical` coding discipline
// always-on, without the user needing to invoke /lazy-surgical.
// Injects a compact directive into session context. Requires Node; if Node is
// absent the hook simply fails non-blocking and the session continues.

const context = [
  "claude-kit: the `lazy-surgical` coding discipline is ON for this session (applied automatically; no /lazy-surgical needed). For CODE work:",
  "- Write the LEAST code that fully solves the task. Reuse what already exists before writing new; prefer the stdlib / framework / an installed dependency over new code.",
  "- Make SURGICAL changes: every changed line must trace to the request. No drive-by refactors, renames, or reformatting.",
  "- Keep it SIMPLE: no speculative abstractions, config, or flexibility nobody asked for.",
  "- VERIFY: state how you'll know it works, then check it. Done means demonstrated, not \"should work\".",
  "- Guardrail: never shrink correctness, input validation, error handling, security, accessibility, or anything the user explicitly asked for.",
  "For version numbers, follow the `semver` skill. Full rules: run /lazy-surgical. Ignore this directive for non-coding tasks.",
].join("\n");

process.stdout.write(
  JSON.stringify({
    hookSpecificOutput: {
      hookEventName: "SessionStart",
      additionalContext: context,
    },
  })
);
process.exit(0);
