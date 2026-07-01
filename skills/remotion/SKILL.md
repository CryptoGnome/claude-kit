---
name: remotion
description: Rules and gotchas for Remotion — programmatic video in React (render React components to MP4). Use when writing or editing Remotion compositions, <Composition>/<Sequence>/<Series>, useCurrentFrame/interpolate/spring/useVideoConfig, staticFile, @remotion/media <Video>/<Audio>/<OffthreadVideo>, @remotion/renderer, or `npx remotion` studio/still/render. Do NOT use for general React app UI, DOM state, or normal web animation — use react-best-practices for those.
version: 1.0.0
license: MIT
---

# remotion — video in React, rendered frame by frame

Remotion renders your React component once **per frame** (across parallel workers), then stitches the frames into video. Two React habits invert here: **time is a prop (the frame), not a side effect**, and **render must be deterministic**. (Distilled in our own way from the Remotion team's `remotion-best-practices`, MIT. For general React/hooks/state, use `react-best-practices`.)

## The rules

1. **One clock only.** Drive every animation off `useCurrentFrame()`. **Forbidden** (they don't render): CSS transitions/animations, Tailwind animation classes, `Date.now()`, `setTimeout`/`setInterval`, `requestAnimationFrame`.
2. **Determinism.** Output must be a pure function of `(frame, props, useVideoConfig())`. No unseeded randomness — use `random(seed)` from `remotion`, never `Math.random()`. Don't read wall-clock or external mutable state.
3. **`interpolate()` by default; `spring()` only for explicit physics/bounce.** Clamp when a value shouldn't run past its range: `interpolate(frame, [in, out], [from, to], { extrapolateLeft: "clamp", extrapolateRight: "clamp" })`. Custom curves via `easing: Easing.bezier(...)` — `Easing.out` for enters, `Easing.in` for exits.
4. **Read config, don't hardcode.** Pull `fps` / `durationInFrames` / `width` / `height` from `useVideoConfig()`. Express durations as seconds × fps (`2 * fps` = 2s), never a bare frame count that assumes an fps.
5. **Keep animation Studio-editable.** Put the `interpolate()` call **inline in the `style` prop**, and animate individual transform props (`scale`, `translate`, `rotate`) — not a composed `` transform: `scale(${x})` `` string. Inline + individual props = Remotion Studio can edit them.
6. **Time with components, not math.** `<Sequence from={f} durationInFrames={n}>` to delay/limit; child frames are **relative** to the sequence start. `layout="none"` for inline (default is `AbsoluteFill`). `<Series>` for back-to-back scenes.
7. **Assets.** Files go in `public/`, referenced via `staticFile("name.ext")` (remote URLs also fine). `<Img>` from `remotion`; `<Video>`/`<Audio>` from **`@remotion/media`** (the current package — older projects use core `<Audio>` / `<OffthreadVideo>`; watch the import path).
8. **Async data → `calculateMetadata`.** For anything you must `fetch` before rendering, use `calculateMetadata({ props, abortSignal })` on `<Composition>` to set duration/dimensions/props up front; pass `abortSignal` so stale Studio requests cancel; `Promise.all` for multiple sources. (`delayRender()`/`continueRender()` is the lower-level fallback for async work *inside* a component.)
9. **Workflow.** Scaffold only in an empty folder (`npx create-video@latest`). Preview with `npx remotion studio`. Cheap sanity check: `npx remotion still <id> --frame=N --scale=0.25` (frame is zero-based). Render via `npx remotion render` or `@remotion/renderer`.

## Effects & advanced
Reach in this order: plain HTML/CSS/SVG (filter/blend/mask) → a built-in effect from `@remotion/*` → a custom `createEffect()` → `<HtmlInCanvas onPaint>` as a last resort. Remotion has first-class support for captions/subtitles, audio visualization & silence detection, transitions, 3D (Three.js / R3F), Google/local fonts, GIFs, Lottie, MapLibre, trimming, and transparent video — look up the official docs when you hit one. For TTS voiceover or transcription, bring your own key (e.g. ElevenLabs / whisper) — never commit it.
