# Prompt & Style Guide

Reference for the `image-gen` skill. Fill in the `{brackets}`. Keep the style words — they're what make each look land.

## Prompt structure

Write **one flowing natural-language paragraph** (modern models prefer prose over comma-keyword lists), ordering the elements:

1. **Subject** — who/what it is, key attributes, count, wardrobe/material, expression, pose/action. Front-load the most important subject in the first ~10 words.
2. **Style / medium** — photo vs render vs illustration + genre/era/artist vibe.
3. **Composition** — shot type & framing (close-up, wide, overhead, eye-level), subject placement, background/setting, depth.
4. **Lighting & color** — source/quality/direction (soft golden-hour, hard rim, studio softbox), mood, palette.
5. **Detail & tech** — fidelity + terms the models know: `85mm f/2.8`, `shot on medium-format film`, `shallow depth of field`, `8k`, `sharp focus` for photos; `octane render`, `PBR materials`, `ambient occlusion`, `global illumination` for 3D.
6. **Text** — put any words you want rendered in `"double quotes"` and state font/placement.
7. **Avoids** — phrase every exclusion as a **positive desired state** in plain language (`clean uncluttered background`, `empty sky`, `smooth skin`), never a negative-prompt list.

Set aspect ratio via `--aspect`, not the prompt text.

## General style presets

| Style | Prompt fragment |
|---|---|
| **Photorealistic** | a photorealistic photograph of {subject}, shot on a 50mm lens at f/1.8, natural soft daylight, true-to-life color, fine skin and surface texture, sharp focus, subtle film grain |
| **Cinematic** | a cinematic film still of {subject}, anamorphic widescreen framing, dramatic low-key lighting with warm rim light, teal-and-orange grade, shallow depth of field, atmospheric haze |
| **Editorial photo** | a high-fashion editorial photograph of {subject}, medium-format studio shot, controlled softbox key with clean rim light, seamless colored backdrop, glossy magazine finish |
| **3D render** | a polished 3D render of {subject}, Octane/Blender Cycles style, physically-based materials, soft global illumination with ambient occlusion, subtle subsurface scattering, studio HDRI reflections |
| **Flat vector** | a flat vector illustration of {subject}, bold geometric shapes, limited harmonious palette, clean crisp edges, no gradients or outlines, generous negative space |
| **Line art** | a clean black-and-white line-art drawing of {subject}, uniform confident ink strokes, no shading or fill, white background, minimal and elegant |
| **Watercolor** | a soft watercolor painting of {subject}, visible paper texture, loose wet-on-wet washes and gentle color bleeds, delicate pastel palette, hand-painted organic edges |
| **Anime** | an anime-style illustration of {subject}, clean cel shading, expressive large eyes, crisp lineart, vibrant saturated colors, detailed background |
| **Isometric** | a cute isometric illustration of {subject}, 45-degree isometric projection, tiny detailed diorama, soft ambient shadows, pastel palette, miniature-world look |
| **Product shot** | a professional product photograph of {subject}, centered on a seamless white studio background, soft even three-point lighting, gentle reflection, razor-sharp focus, e-commerce quality |
| **Logo / icon** | a minimal vector logo/icon of {subject}, simple memorable geometric mark, flat solid colors, perfect symmetry, high contrast, clean shapes on a plain background |
| **Pixel art** | a detailed pixel-art sprite of {subject}, crisp aligned pixels, limited retro palette, dithered shading, clean outlines, 16-bit game aesthetic |
| **Oil painting** | a classical oil painting of {subject}, visible impasto brushstrokes, rich layered pigments, warm chiaroscuro lighting, canvas texture, fine-art gallery feel |
| **Blueprint / technical** | a technical blueprint diagram of {subject}, precise white line drawing on deep blue background, orthographic views with measurement callouts, monospace labels |

## Game-art & UI templates

Detailed fill-in templates for game/app work. Always include a style block — there is no default style.

**Low-poly game art (flat-shaded — detail from lighting):**
> Low-poly 3D game [render/scene] of [SUBJECT], stylized [GENRE] art direction like Quaternius / Monument Valley. Faceted flat-shaded geometry, clean limited vertex-color palette, NO surface textures. Detail from lighting only: warm directional sun, soft ambient occlusion, gentle global illumination, crisp rim/edge highlights, subtle bloom. [CAMERA]. Cohesive, clean anti-aliased edges. No text, no UI, no watermark.

**Low-poly PBR (Synty-style — detail from textures):**
> Low-poly 3D game render of [SUBJECT] in Synty Studios style. Low-poly silhouettes with hand-painted / normal-mapped PBR surface detail, soft specular highlights, painterly stylized textures. Warm sun, ambient occlusion, rim light, gentle bloom. [CAMERA]. Richer surface detail while keeping low-poly geometry. No text, no UI, no watermark.

**Character model sheet (turnaround):**
> Character model sheet / turnaround reference for a 3D artist. [CHARACTER DESCRIPTION]. Show THREE aligned full-body views side by side on a plain neutral light-gray background: front, side, back — same height, relaxed A-pose. [PASTE A STYLE BLOCK ABOVE]. Consistent design across all three views. No text labels, no watermark.

**Environment / level concept:**
> [BIOME/LOCATION] concept art for a [GENRE] game, [STYLE]. Establishing wide shot, clear focal point [LANDMARK], readable layout for gameplay, [TIME OF DAY] lighting, depth with foreground / midground / background. No text, no UI.

**UI / HUD mockup:**
> Game UI/HUD mockup for a [GENRE] game, [ART STYLE] theme. Show [ELEMENTS: health bar, minimap, hotbar, inventory panel]. Clean layout, legible, [COLOR PALETTE], flat design, crisp. (Use as a visual target, then build it in-engine.)

## Tips

- **Aspect ratio via `--aspect`, not prompt words.** Common: `1:1` (avatars, icons, product), `16:9`/`21:9` (cinematic, banners), `9:16` (phone/story), `4:5` (social portrait), `3:2`/`4:3` (editorial/print). Gemini also supports extremes like `4:1` for panoramas.
- **No negative prompts.** These models largely ignore `negative prompt:` / long DO-NOT lists. Phrase avoids as positives: `clean empty background` not `no clutter`, `smooth flawless skin` not `no blemishes`, `sharp focus` not `not blurry`.
- **Control rendered text.** Wrap exact words in `"double quotes"` and state placement/font (`a bold sans-serif sign reading "OPEN" centered at the top`). One or two text elements at a time.
- **Attach a reference (`--ref`)** when you must preserve identity, brand, product, layout, or an exact style words can't pin down. The Gemini default blends up to ~14 refs. Skip refs for generic/novel scenes.
- **Iterate, don't re-roll.** If it's ~80% right, describe the single change (`make the jacket red`, `lower the horizon`, `add soft rim light`) so composition and identity stay stable.
- **Use vocabulary the models know.** Camera terms for photos (`85mm f/2.8`, `golden hour`, `three-point lighting`); render terms for 3D (`PBR materials`, `global illumination`, `ambient occlusion`, `octane render`). Strong, reliable style anchors.
- **One clear focal subject** beats many competing ones. Split complex multi-part images into separate generations or edits.
- **Watermarks:** don't rely on `no watermark`; positively specify `clean plain unbranded surface`. Note Gemini images carry an invisible SynthID watermark by design — a prompt can't remove it.
