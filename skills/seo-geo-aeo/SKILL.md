---
name: seo-geo-aeo
description: Audit a site for search readiness across SEO (traditional + technical), AEO (answer engines / featured snippets), and GEO (getting cited by AI answer engines like ChatGPT / Perplexity / Google AI Overviews, incl. AI-crawler access). Emits a scored, checklist-based markdown report with concrete fixes. Use when the user asks for an SEO / GEO / AEO audit, AI-search readiness, technical-SEO/crawlability review, schema / structured-data review, featured-snippet optimization, or "why isn't my site ranking / getting cited". Do NOT use for writing or editing site copy (use marketing-copy), or for metrics WebFetch can't measure — keyword volume, backlinks, rank (need Semrush/Ahrefs) and Core Web Vitals timing (need PageSpeed).
version: 1.1.0
license: MIT
---

# seo-geo-aeo — search & AI-answer readiness audit

Audit a page/site across three layers — **SEO** (rank in search), **AEO** (win featured snippets & answer boxes), **GEO** (get cited by AI answer engines) — and emit a scored markdown report with concrete fixes. (Distilled and **rebuilt** in our own way from SNLabat/SEO-GEO-AEO-Skill — safe-audited as pure markdown, then deepened with current technical-SEO and GEO practice. Zero-dependency, WebFetch-only, outputs markdown.)

## How to run
1. **Confirm scope first.** *Quick* = homepage + up to ~6 high-signal pages. *Full* = all meaningful pages (skip Privacy/Terms/login/thank-you and archive pages past page 2). Priority order: About → Services → Case Studies → Blog → Contact → FAQ → product pages.
2. **WebFetch the pages** (HTML, `robots.txt`, `sitemap.xml`). Audit the **whole scope before flagging anything "missing"** — a tag that lives on another page isn't missing.
3. Score each layer **1–10** (1–3 critical · 4–5 below average · 6–7 decent · 8–9 strong · 10 exemplary) and list fixes by impact.
4. **Be honest about limits.** WebFetch can't measure Core Web Vitals timing (**LCP / INP / CLS**), backlinks, keyword volume, or rank — say so and point to PageSpeed / Search Console / Semrush / Ahrefs. Never fabricate those numbers.

## SEO checklist (on-page)
- **Title:** present, unique, **50–60 chars**, primary keyword, not duplicated across pages.
- **Meta description:** present, **150–160 chars**, includes a CTA.
- **Headings:** exactly **one H1**; logical H2/H3; no stuffing.
- **Search intent match:** the page *format* fits the query type — informational → guide, commercial → comparison, transactional → product/pricing. A mismatch caps ranking no matter how good the copy.
- **Links / images:** descriptive internal anchor text; a clear internal-linking path to the page; descriptive image `alt`; modern formats + explicit dimensions.
- **Social:** Open Graph + Twitter Card (`og:title`, `og:description`, `og:image`).
- **Content:** **500+ words** standard pages, **1500+** pillar/cornerstone; visible publish/update dates; scannable (subheads, short paras, bullets).
- **Structured data:** JSON-LD present and syntactically valid (see `references/schema-snippets.md`).

## Technical SEO (crawl & index)
- **Indexability:** no accidental `noindex`; `canonical` points at the right URL (no canonical↔noindex conflict); the page is in the XML sitemap and not blocked by `robots.txt`.
- **robots.txt + sitemap.xml valid:** the sitemap lists only real `200` URLs (no 404 / redirect / noindex entries), under 50k URLs / 50MB.
- **Status codes:** permanent moves are **301** (not 302); no redirect chains or loops; no soft-404s.
- **One canonical host + scheme** (https), consistent trailing-slash; HSTS; no mixed content.
- **Mobile-first:** responsive, `viewport` set, adequate tap targets, no intrusive interstitials.
- **i18n:** `hreflang` reciprocal + self-referencing, with an `x-default`.

## AEO checklist (answer engines / snippets)
- **Answer-first paragraph of 40–60 words** directly under a **question-phrased H2/H3**.
- An explicit **definition sentence** ("X is…") for the core topic.
- Snippet-eligible formats: **numbered steps, bulleted lists, comparison tables**.
- Schema: **FAQPage**, **HowTo**, **SpeakableSpecification**.
- Conversational phrasing; cover long-tail who/what/when/where/why/how; target "People Also Ask"; local NAP + **LocalBusiness** schema if applicable.

## GEO checklist (get cited by AI answer engines)
- **E-E-A-T:** named authors with visible credentials; a substantive About page; accessible contact; trust signals (testimonials, awards, certs, press).
- **Extractable facts:** specific stats/data worth citing; the core claim stated clearly and **early**; cites external authoritative sources; original data / POV.
- **Entity clarity:** brand/person named consistently; **Organization** schema with `name`, `logo`, `url`, `sameAs` (social profiles); consistent facts across the web (LLMs cite what's corroborated).
- **AI-crawler access (decide per bot in `robots.txt`):** `GPTBot` / `OAI-SearchBot` (OpenAI), `ClaudeBot` / `anthropic-ai` (Anthropic), `PerplexityBot`, `Google-Extended` (Google AI), `CCBot` (Common Crawl). Blocking a bot removes you from that engine's answers — allow the ones you want to be cited by.
- **`llms.txt`** at the site root: a markdown map of your key pages/docs for LLMs (emerging convention, cheap to add).
- **Be in Bing:** ChatGPT search and Copilot draw from Bing's index — submit to Bing Webmaster Tools and use **IndexNow** for instant (re)indexing.
- **Technical:** HTTPS; clean crawlability (avoid JS-only rendering of key content — many AI crawlers don't execute JS); freshness.
- **AI-friendly schema:** **Author**, **Dataset**, **ClaimReview** where relevant.

Copy-paste JSON-LD templates are in [`references/schema-snippets.md`](references/schema-snippets.md).

## Output
A markdown report: a one-line verdict + the three 1–10 scores, then per layer the failing checks as `issue → fix` ordered by impact, ending with a "needs external tools" section (Core Web Vitals, backlinks, rank). Nothing is installed and nothing is sent anywhere — WebFetch reads the audited site, that's it.
