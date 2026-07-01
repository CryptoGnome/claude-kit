---
name: security-audit
description: Deep security audit of a codebase or diff using parallel Claude subagents — pattern-triage for vulnerability classes, per-candidate source→sink investigation, an adversarial false-positive cull, then severity-ranked findings with file:line, exploit scenario, and fix. Use when the user wants a security audit, to find vulnerabilities, or to review code for SQLi / SSRF / auth-bypass / injection / access-control issues. Do NOT use for a quick pending-diff review (use the built-in /security-review), pure dependency-CVE or secret scanning, or offensive / exploit-development work.
version: 1.0.0
license: MIT
---

# security-audit — agent-powered vulnerability review (no paid tools)

A thorough, read-only security audit built from free tools you already have: **ripgrep to triage, Claude subagents to investigate in parallel, an adversarial pass to kill false positives.** (Method inspired by Vercel's deepsec pipeline — scan → process → revalidate → export — but rebuilt to run on your own Claude subagents instead of a paid scanner: no external CLI, no API keys, no per-file billing.)

## Method

### 1. Scope
Confirm what to audit: the **whole repo**, a **directory/service**, or a **diff** (`git diff main...HEAD`). A diff is fast and cheap; a whole-repo audit is a bigger fan-out — say which and roughly how many candidates before spending the effort.

### 2. Triage (free, fast — no model calls)
Grep the scope for the security-sensitive patterns in [`references/patterns.md`](references/patterns.md) (SQLi, command/SSRF/path/SSTI injection, auth & access control, deserialization, XSS/CSRF, secrets, crypto, races, LLM/agentic). Collect candidate `file:line` hits. This is the cheap net — it over-catches on purpose.

### 3. Investigate (parallel subagents)
Dispatch subagents (Task/Agent tool) — one per candidate or cluster — **in parallel**. Each subagent reads the code around the hit, **traces data flow from source (attacker-controlled input) to sink**, checks for mitigations (validation, parameterization, authz, encoding, allow-lists), and returns: verdict (real / not), severity (Critical/High/Medium/Low), a one-line concrete exploit scenario, and the fix. Give each subagent only its candidate plus the files it needs.

### 4. Adversarially revalidate (kill false positives)
For every *surviving* finding, dispatch a **second, independent skeptic subagent** whose only job is to **refute** it: is the sink actually reachable? is the input truly attacker-controlled? is there an upstream guard the first pass missed? Default to "refuted" when uncertain. Drop anything the skeptic refutes. (This is deepsec's `revalidate` — it's what keeps the report signal-dense instead of a wall of plausible-but-unreachable noise.)

### 5. Report
Severity-ranked. Each confirmed finding: `severity · file:line · vulnerability class · concrete exploit scenario · fix`. Terse, no filler. End with **coverage notes** — what was and wasn't audited, and what needs tools this skill doesn't have (dependency CVEs → `npm audit`/Dependabot; runtime DAST; secret history → a dedicated secret scanner).

## Rules
- **Read-only.** Audit, don't edit. Propose fixes; don't apply them during the audit.
- **Every finding traces source → sink AND survives the skeptic pass.** No "this looks scary" without a reachable, attacker-controlled path — that noise is exactly what the revalidate step removes.
- **No external tools, keys, or cost** beyond normal Claude usage. Nothing is installed or sent anywhere.
- **Chain-specific security lives elsewhere:** Solidity → the `ethereum` skill's checklist; Anchor/Solana → `solana`. This skill is general application security.
