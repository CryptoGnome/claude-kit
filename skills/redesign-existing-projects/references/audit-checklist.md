# Redesign Audit Checklist

Reference for the `redesign-existing-projects` skill. During **Diagnose**, first apply the shared aesthetic rules, then run the existing-code checks below.

## Shared aesthetic rules → `frontend-design` (one source of truth)

The core "does this look AI-generated" tells are the same whether you build new or fix existing, so they live once in the [`frontend-design`](../../frontend-design/SKILL.md) skill — apply those first:
- **Type:** not Inter/Roboto as default (Geist / Outfit / Cabinet Grotesk / Satoshi); body ≤ 65ch; serif discipline.
- **Color:** one accent, saturation < 80%, no AI-purple/blue-glow gradient, no default premium-beige palette.
- **Layout clichés:** no centered-hero-over-mesh, no three-equal-cards, no glass-on-everything; eyebrow / zigzag / hero caps; one accent + one radius + one theme locked.
- **States:** full cycles — loading (skeletons), empty, error, hover, `:active`, focus, WCAG-AA contrast.
- **Copy:** no "Elevate / Seamless / Unleash / Delve" cliches, no fake-precise numbers, sentence case, zero em-dashes.

Everything below is what's **specific to auditing and repairing an existing codebase** — it does not repeat the above.

## Surface & texture (existing-render smells)
- Pure `#000` background → off-black / tinted dark (`#0a0a0a`, `#121212`, dark navy).
- Tint shadows to the background hue; no pure-black drop shadows on light backgrounds.
- Flat, textureless backgrounds → subtle noise / grain / micro-pattern. Even linear gradients → radial / mesh / noise.
- Inconsistent light direction across shadows → pick one source and audit all shadows to it.
- Mixed warm/cool grays → one gray family.
- Empty, flat, text-only sections → add real imagery (blurred/masked), an ambient gradient, or `https://picsum.photos/seed/{name}/1920/1080` placeholders.

## Alignment & spacing craft
- Cards forced to equal height by flex → allow variable height or masonry when content varies.
- CTAs at random heights in card groups → pin buttons to the card bottom so they form a clean line.
- Feature lists / prices starting at different Y across columns → align shared elements; fixed-height title/price blocks.
- Symmetric top/bottom section padding → adjust optically (bottom often needs slightly more).
- No overlap or depth → use negative margins to layer elements.
- Icons-in-text, play-buttons-in-circles → 1–2px optical nudges; mathematical centering isn't optical centering.
- Numbers in a proportional font → tabular figures (`font-variant-numeric: tabular-nums`) for data.
- Orphaned last-line words → `text-wrap: balance` / `pretty`.
- Missing whitespace → increase spacing; let it breathe.

## Layout mechanics
- `height: 100vh` full-screen sections → `min-height: 100dvh` (iOS Safari viewport bug).
- Complex flexbox `%` math (`w-[calc(33%-1rem)]`) → CSS Grid.
- No max-width container → constrain to ~1200–1440px with auto margins.
- Dashboards defaulting to a left sidebar → try top nav, a command menu, or a collapsible panel.

## Component swaps (replace the cliche)
- Generic card (border + shadow + white bg) → use only bg, only spacing, or `divide-y` / `border-t`; cards only when elevation means hierarchy.
- Always filled + ghost button → add text / tertiary styles to cut noise.
- Pill "New" / "Beta" badges → square badges, flags, or plain labels.
- Accordion FAQ → side-by-side list, searchable help, inline disclosure.
- 3-card carousel testimonials with dots → masonry wall, embedded posts, or one rotating quote.
- Pricing 3-tower → highlight the recommended tier with color/emphasis, not just height.
- Modals for everything → inline edit, slide-over panel, or expandable section.
- Avatar circles everywhere → squircles / rounded squares.
- Sun/moon theme toggle → dropdown, system preference, or settings integration.
- 4-column footer link farm → simplify to main paths + legally required links.

## Iconography
- Lucide / Feather exclusively → Phosphor, Heroicons, Tabler, or a custom set. One family per project.
- Cliche metaphors (rocket = launch, shield = security) → less obvious glyphs (bolt, fingerprint, spark, vault).
- Inconsistent stroke widths → standardize to one.
- Missing favicon → add a branded one.
- Stock "diverse team" photos → real photos, candid shots, or a consistent illustration style.

## Content realism (existing filler)
- `John Doe` / `Jane Smith` → diverse realistic names. `Acme Corp` / `Nexus` / `SmartFlow` → believable contextual brands.
- All blog dates identical → randomize. Same avatar reused for many users → unique assets each.
- Lorem Ipsum → real draft copy. Passive voice → active ("We couldn't save your changes"). "Oops!" errors → direct ("Connection failed. Please try again.").

## Interactivity gaps (existing code)
- Dead links to `#` → real destinations or visibly disabled.
- No current-page indicator in nav → style the active link.
- Instant anchor jumps → `scroll-behavior: smooth`.
- Animating `top` / `left` / `width` / `height` → `transform` / `opacity` (GPU-accelerated).

## Code quality
- Div soup → semantic `<nav>` / `<main>` / `<article>` / `<aside>` / `<section>`.
- Inline styles mixed with classes → move to the styling system.
- Hardcoded px widths → relative units + `max-width`.
- Missing / empty `alt` on meaningful images → describe the content.
- Arbitrary `z-index: 9999` → a clean z-index scale.
- Commented-out dead code → remove.
- Import hallucinations → verify every import exists in the dependency file.
- Missing `<title>`, `description`, `og:image`, social meta → add them.

## Strategic omissions (what AI forgets)
- No privacy / terms links in the footer. No "back" navigation (dead-end flows). No custom 404. No client-side form validation. No "skip to content" link. No cookie consent where required.

## Upgrade techniques (premium touches to apply)
- **Type:** variable-font weight/width animation on scroll/hover; outline-to-fill on entry; text-mask reveals over media.
- **Layout:** broken / asymmetric grid, whitespace maximization, parallax card stacks, split-screen opposite-direction scroll.
- **Motion:** inertia smooth-scroll, staggered entry (Y-translate + fade), spring physics over linear easing, scroll-driven mask / wipe / draw-on-SVG reveals.
- **Surface:** true glassmorphism (1px inner border + inner shadow, not just blur), cursor-reactive spotlight borders, a fixed grain/noise overlay, colored/tinted shadows.

---

_Workflow, fix-priority order, and rules live in the skill's [`SKILL.md`](../SKILL.md)._
