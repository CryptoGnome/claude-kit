---
name: frontend-design
description: Frontend-design guardrails for building NEW frontend UI (landing pages, portfolios, marketing sites) that doesn't look AI-templated. Infers the right direction from the brief, sets variance/motion/density dials, and enforces countable anti-slop rules. Use when building or designing a new landing page, hero, portfolio, or marketing site, or when the user wants UI that "looks less generic / less AI / more designed". Do NOT use for dashboards or data-dense product UI; to upgrade an EXISTING site use redesign-existing-projects instead.
version: 1.0.0
license: MIT
---

# frontend-design — build UI that isn't templated

For **new** landing pages, portfolios, and marketing sites. Every rule here is contextual — read the brief first, then pull only what fits. (Distilled in our own way from the anti-slop ideas in [Leonxlnx/taste-skill](https://github.com/Leonxlnx/taste-skill), MIT.)

## 0. Read the brief before touching code
Infer: **page kind** (SaaS / consumer / agency / portfolio / editorial), **vibe words** the user used, **references** they named, **audience** (the audience picks the aesthetic, not your taste), and any **existing brand assets**. Then state a one-line **Design Read** before generating:
> "Reading this as: \<page kind> for \<audience>, \<vibe> language, leaning \<design system / aesthetic>."

If the read genuinely forks, ask **one** question. If you can infer it, don't ask — declare and proceed.

## 1. Three dials (baseline 8 / 6 / 4)
- **DESIGN_VARIANCE** (1 symmetry → 10 chaos): **8**
- **MOTION_INTENSITY** (1 static → 10 cinematic): **6**
- **VISUAL_DENSITY** (1 airy → 10 packed): **4**

Adjust from the read: minimalist/Linear → ~5/3/2 · premium consumer → ~7/6/3 · agency/Awwwards → ~9/8/3 · trust-first/public-sector → ~3/2/5.

## 2. Use real design systems, honestly
If the brief reads enterprise / Material / Carbon / Fluent / Primer / public-sector / shadcn / Tailwind — install and use the **official** package; don't hand-recreate its CSS or import its tokens then override 90%. **One system per project.** For pure aesthetics (glass, bento, brutalist, editorial) there's no official package — build native CSS + Tailwind and label borrowed inspiration honestly.

## 3. Anti-default banlist (the AI tells)
- **Fonts:** not `Inter` / `Roboto` / system as default. Reach for Geist, Outfit, Cabinet Grotesk, Satoshi. Serif is **very discouraged** as default — only if the brand names one or it's genuinely editorial/heritage. Emphasize with italic/bold of the *same* family; never inject a stray serif word into a sans headline. Don't default to Fraunces / Instrument Serif.
- **Color:** max **1 accent**, saturation < 80%. No AI-purple/blue glow gradients as default. No default premium-consumer beige+brass+espresso palette — rotate a different family each project.
- **Layout:** no centered-hero-over-mesh, no three equal feature cards, no glassmorphism on everything.

## 4. Countable rules (a reviewer can literally count these)
- **Eyebrows** (small uppercase tracking labels above headers): max **ceil(sectionCount / 3)**. If a section has one, the next two don't.
- **Zigzag** image+text splits: max **2 in a row**; the 3rd is a fail — break with a different layout family.
- **Hero:** ≤ **4 text elements** (eyebrow OR brand strip / headline ≤ 2 lines / subtext ≤ 20 words / 1 primary + ≤ 1 secondary CTA). Trust strips, taglines, pricing teasers move *below* the hero, which fits the first viewport.
- **One accent, one corner-radius scale, one page theme** — locked across the whole page. No blue CTA on a warm-grey page; no light section sandwiched in a dark page.
- **No duplicate-intent CTAs** ("Get in touch" + "Contact us" + "Let's talk" → pick one label).
- **Nav** renders on one line at desktop, ≤ 80px tall.

## 5. The em-dash ban (signature rule)
No em-dash (—) anywhere in visible copy. It's the #1 LLM tell. Use a period, a comma, or restructure. One visible em-dash = pre-flight fail.

## 6. Real images, full states
- Landing pages are visual products. If an image-gen tool exists (e.g. the [`image-gen`](../image-gen/SKILL.md) skill), use it for hero/section assets; else use `https://picsum.photos/seed/<desc>/<w>/<h>`. No div-based fake screenshots, no hand-rolled decorative SVGs as default. Even minimalist sites need 2–3 real images.
- Ship full interactive cycles: loading (skeletons, not spinners), empty, error, hover, and `:active` tactile feedback. Verify button/text and form contrast (WCAG AA).

## 7. Copy tells
Plain, specific language. Ban "Elevate / Seamless / Unleash / Next-Gen / Delve / In the world of…". No fake-precise invented numbers. No exclamation-mark success messages. Sentence case headers, not Title Case.

## Pre-flight (if any fails, you're not done)
1. Stated a one-line Design Read. 2. Dials set from the brief. 3. Official design system used where the brief called for one. 4. Banned fonts/palettes avoided. 5. Eyebrow / zigzag / hero / CTA-intent counts pass. 6. One accent + one radius + one theme. 7. Zero em-dashes in visible copy. 8. Real images, not fake-screenshot divs. 9. Loading/empty/error states + contrast checked. 10. Copy has no AI cliches or fake-precise numbers.
