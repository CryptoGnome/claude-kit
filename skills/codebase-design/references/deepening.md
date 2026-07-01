# Deepening shallow modules

Companion to `codebase-design`. How to merge a cluster of shallow modules into a deep one safely — the **dependency category** dictates the test strategy. (From Matt Pocock's `codebase-design` / DEEPENING.md, MIT.)

## Category → strategy
1. **In-process** (pure computation, in-memory) — always deepenable. Merge and test through the new interface. No adapter.
2. **Local-substitutable** (PGLite for Postgres, in-memory FS) — test with the stand-in; the seam is internal; no port at the external interface.
3. **Remote-but-owned** (your own service over HTTP/gRPC/queue) — Ports & Adapters: keep the logic in the deep module, define a **port** at the seam, inject the transport as an adapter. In-memory adapter for tests, real transport adapter for prod.
4. **True-external** (Stripe / Twilio you don't control) — inject as a port; tests provide a mock adapter.

## Seam discipline
The two-adapters rule again: don't expose an *internal* seam through the interface just because your tests use it. A single-adapter seam is just indirection.

## Testing: replace, don't layer
- Once interface-level tests exist, **delete** the old unit tests on the shallow modules.
- Write new tests at the deepened interface; assert on **observable outcomes**, not internal state.
- Tests should survive internal refactors. If a test must change when the implementation changes, it's testing past the interface — move it to the seam.
