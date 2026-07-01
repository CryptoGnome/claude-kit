# Prototype — UI branch (multi-variant, one route)

For the `prototype` skill, when the question is "what should this look like?" Generate several **structurally different** UI variations on a single route, switchable from a floating bottom bar.

## Prefer sub-shape A (adjust an existing page)
Render the variants on the **same route**, gated by a `?variant=` param; keep the existing data-fetching / params / auth, swap only rendering. A variant is far easier to judge against the real app (header, sidebar, data, density) than in a vacuum. A new section that lives *inside* a page is still A. Sub-shape B (a new throwaway route) is a last resort when there's genuinely no existing page — follow the project's routing convention and put "prototype" in the path.

## Steps
1. **State the question; pick N.** Default **3** variants, cap at **5** (more stops being radically different).
2. **Make them structurally different** — different layout, information hierarchy, primary affordance, not just colours ("three tweaked card grids is wallpaper, not a prototype"). Use the project's component/styling system; export `VariantA/B/C`.
3. **Wire one switcher:** `variant = searchParams.get('variant') ?? 'A'`, render the match + a `<PrototypeSwitcher>`.
4. **Build the floating switcher:** a fixed bottom-centre bar — prev arrow (wraps), a label ("B — Sidebar layout"), next arrow (wraps); clicking updates the URL param via the router (shareable, reload-stable); left/right arrow keys cycle too, but **not** while an input/textarea is focused; visually distinct (high-contrast pill); **hidden in production** (`process.env.NODE_ENV !== 'production'`) so a stray merge can't ship it.
5. **Hand over the URL + `?variant=` keys.** The best feedback is usually "the header from B with the sidebar from C" — that's the real design.
6. **Capture the winner and why, then clean up:** A → delete losing variants + switcher, fold the winner into the page; B → promote the winner to a real route, delete the throwaway + switcher. **Rewrite prototype code properly when folding in — don't promote it as-is.**

Anti-patterns: variants differing only in colour/copy; wiring variants to real mutations (use read-only stubs); a shared `<Layout>` that defeats the comparison.
