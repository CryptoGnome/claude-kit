---
name: codebase-design
description: Design DEEP MODULES — a lot of behaviour behind a small interface, at a clean seam, testable through that interface. Use when designing or restructuring a module, deciding where a seam/boundary goes, shrinking an interface, or making code more testable. Enforces a precise shared vocabulary. Do NOT use for bug-fixing (use diagnosing-bugs), aesthetic/frontend design (anti-slop-frontend), or picking a DDD bounded context.
version: 1.0.0
license: MIT
---

# codebase-design — deep modules, small interfaces

Leverage for callers, locality for maintainers, testability for everyone. (Distilled in our own way from Matt Pocock's `codebase-design`, MIT — Ousterhout's *A Philosophy of Software Design* crossed with Feathers' "seam".)

## Vocabulary (use these words exactly — consistent language is the whole point)
- **Module** — anything with an interface + implementation (function, class, package, a tier-spanning slice). Not "component / service / unit".
- **Interface** — *everything a caller must know to use it correctly*: the type signature **plus** invariants, ordering, error modes, required config, performance. Not just the "API / signature".
- **Implementation** — the code inside.
- **Seam** (Feathers) — a place you can change behaviour without editing there; where a module's interface lives. Not "boundary" (overloaded with DDD).
- **Adapter** — a concrete thing that satisfies an interface at a seam.
- **Depth** — leverage at the interface: how much behaviour a caller/test can exercise per unit of interface they must learn.
- **Leverage** — one implementation pays back across N call sites and M tests. **Locality** — change/bugs/knowledge concentrate in one place; fix once, fixed everywhere.

## Deep vs shallow
**Deep** = small interface, lots of behaviour. **Shallow** = interface nearly as complex as the implementation (a pass-through) — avoid. When shaping an interface, ask: (1) fewer methods? (2) simpler parameters? (3) hide more complexity inside?

## Rules (checkable)
- **Depth is a property of the interface, not the implementation.** A deep module can be internally composed of small swappable parts — those are *internal* seams, not part of the interface.
- **The deletion test:** imagine deleting the module. If complexity vanishes, it was a pass-through. If complexity reappears across N callers, it earned its keep.
- **The interface is the test surface** — callers and tests cross the same seam. If you want to test *past* the interface, the module is the wrong shape.
- **Two adapters, not one:** don't introduce a seam/port unless something actually varies across it. One adapter is a hypothetical seam — just indirection; two adapters means it's real.
- **Design it twice:** before committing, sketch the interface 2–3 radically different ways (minimal / most-flexible / trivial-for-the-common-caller) and pick by depth, locality, and seam placement. Your first idea is rarely the best.

## Designing for testability
1. **Accept dependencies, don't create them** — inject `paymentGateway`, don't `new StripeGateway()` inside.
2. **Return results, don't mutate** — `calculateDiscount(cart): Discount`, not `applyDiscount(cart): void`.
3. **Small surface** — fewer methods = fewer tests; fewer params = simpler setup.

When *deepening* a cluster of shallow modules (which dependency category → which test strategy, and "replace, don't layer" testing), see [`references/deepening.md`](references/deepening.md).
