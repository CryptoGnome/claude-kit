---
name: react-best-practices
description: Fix React and Next.js performance and component-architecture problems in impact order — parallelize data fetching, cut bundle bloat, secure server actions, then re-render hygiene, plus compound-component patterns over boolean-prop soup. Use when writing, reviewing, or optimizing React / Next.js (App Router / RSC) code, or when the user mentions slow renders, waterfalls, bundle size, or messy component props. Do NOT use for non-React code or visual/design work (use anti-slop-frontend / redesign-existing-projects for that).
version: 1.0.0
license: MIT
---

# react-best-practices

Apply fixes in **impact order** — don't spend the budget on MEDIUM re-render tweaks while a CRITICAL data waterfall or barrel import is unfixed. (Distilled in our own way from Vercel Labs' `react-best-practices` + `composition-patterns`, MIT. If **React Compiler is on**, skip the Tier-3 memoization rules — it handles them.)

## Tier 1 — CRITICAL (2–10× wins)
- **Parallelize independent awaits.** Don't `await a()` then `await b()` — start both, then await (`Promise.all`, or kick off promises before awaiting). Defer an `await` into the branch that needs it, after cheap synchronous guards / early returns.
- **Chain per-item nested fetches** so one slow item doesn't block the rest: `ids.map(id => getChat(id).then(c => getUser(c.author)))`.
- **RSC parallelism.** Sibling awaits in one Server Component run *sequentially* — split them into separate async child components (or pass a shared promise + `use()`). Wrap only the data-dependent subtree in `<Suspense>` so the shell paints immediately.
- **Kill barrel imports.** A single `import { X } from 'lucide-react' | '@mui/*' | 'lodash' | 'date-fns' | '@radix-ui/*'` can pull 1500–2000 modules (200–800ms cold start). Use Next's `optimizePackageImports`, or import the exact subpath.
- **`next/dynamic`** (with `ssr:false`) for heavy client-only components (editors, charts) and non-critical third-party (analytics). Keep import paths statically analyzable.

## Tier 2 — HIGH
- **Server Actions are public endpoints** — authenticate, authorize, and validate (zod) *inside every action*. Never rely on middleware/layout guards.
- **No request/user data in module-level mutable variables** — concurrent renders leak across requests.
- **Hoist static I/O** (fonts, config, templates) to module scope so it runs once, not per request.
- **`React.cache()`** to dedupe within a request (pass stable refs); LRU/Redis across requests.
- **Serialize only the RSC→client props the client uses.** Don't pass both an array and its `.toSorted()` — transform on the client.
- **Long lists:** `content-visibility:auto` + `contain-intrinsic-size` (~10× initial render). Script `defer`/`async`; resource hints (`preconnect`/`preload`).

## Tier 3 — MEDIUM (skip if React Compiler is on)
- **Never define a component inside another component** (new type each render → remount, lost state/focus).
- Derive values during render; don't sync state with `useEffect`. Put user-action side effects in **event handlers**, not effects.
- Functional `setState` (`setX(c => …)`); lazy `useState(() => expensive())`; narrow effect deps to primitives (`[user.id]` not `[user]`).
- `useDeferredValue`/`useTransition` to keep input responsive; `useRef` for high-frequency transient values. Don't `useMemo` a cheap primitive.

## Component architecture (composition over flags)
When a component grows **3+ boolean mode flags** (`isThread`, `isEditing`…), the state space is combinatorial — refactor:
- **Compound components:** `const Composer = { Provider, Frame, Input, Footer, Submit }`, each reading a shared context via `use(Context)`; consumers compose only the pieces they need.
- **Explicit named variants** (`ThreadComposer`, `EditMessageComposer`) instead of one component with mode flags.
- Standardize context on three keys — **`state`, `actions`, `meta`** — as a generic interface, so different providers (local `useState` vs synced store) satisfy the same UI. Sharing is by **provider boundary, not visual nesting** (kills prop drilling).
- Prefer `children` over `renderX` props for static composition; reserve render props for passing data back (`renderItem({item, index})`).

## React 19 / Next.js notes
`ref` is a plain prop — drop `forwardRef`. Use `use(Context)` over `useContext` (callable conditionally). Next-specific APIs (`optimizePackageImports`, `after()`, `next/dynamic`) apply only on Next.js App Router.

Full 70-rule reference: https://github.com/vercel-labs/agent-skills
