---
name: image-gen
description: Generate any kind of image from a text prompt (and optional reference images) via OpenRouter — pick from several image models, with built-in prompt/style help. Use when the user wants to create, generate, draw, make, or design an image, picture, illustration, render, logo, icon, mockup, or concept — phrased as "make an image", "generate a picture of…", "draw me…", "create a logo/icon", or "I need a visual for…". Do NOT use for editing the user's existing project files or for reading/analyzing an existing image.
argument-hint: "[prompt] [output?]"
version: 1.0.0
license: MIT
---

# image-gen — generate any image via OpenRouter

One general image generator: describe what you want, optionally pick a model, get a PNG. No forced style — the look comes entirely from your prompt.

## API key (one-time setup)
Resolved in order: (1) `OPENROUTER_API_KEY` env var (preferred), (2) `key.txt` in this skill folder (one line: the key). **`key.txt` is gitignored — never commit it.** Get a key at https://openrouter.ai/keys. Never read another project's `.env` — keys are per-project. If a key was pasted into chat, suggest rotating it.

## Generate
Stdlib Python only — **no `pip install` needed**.
```bash
python scripts/generate.py --prompt "<your prompt>" --output "out.png"
```
Options:
- `--model <id>` — pick a model (see menu). Default `google/gemini-3.1-flash-image-preview`.
- `--ref <img> ...` — reference image(s) for identity/brand/style or image-to-image (works best with the Gemini default, which blends up to ~14 refs).
- `--aspect <ratio>` — e.g. `16:9`, `1:1`, `9:16` (for the FLUX/Seedream/Grok models).
- `--api {auto|chat|images}` — endpoint override; `auto` picks correctly per model.

Saves the PNG + a `<name>.prompt.txt` sidecar and prints the path.

## Model menu (verified June 2026)
**Default engine — Gemini / GPT (fast, simple, supports `--ref` image-to-image):**

| Model | Use it for |
|---|---|
| `google/gemini-3.1-flash-image-preview` *(default)* | Best general pick — Pro-level quality at Flash speed/cost |
| `google/gemini-3-pro-image-preview` | Highest Google fidelity + best in-image text (slower/pricier) |
| `google/gemini-2.5-flash-image` | Cheaper, widely-tested fallback |
| `openai/gpt-5-image-mini` | Strong instruction-following + reliable rendered text |

**Alternative engines — add `--api images` (different providers/looks):**

| Model | Use it for |
|---|---|
| `black-forest-labs/flux.2-pro` | Top FLUX quality/editing, up to ~4MP |
| `black-forest-labs/flux.2-klein-4b` | Fastest/cheapest FLUX for bulk work |
| `bytedance-seed/seedream-4.5` | Varied styles, strong photoreal |
| `x-ai/grok-imagine-image-quality` | xAI photoreal alternative |

Browse the always-current list at **https://openrouter.ai/collections/image-models**. Any model from there works; use `--api images` if it isn't a Gemini/GPT image model. (`-preview` slugs get promoted to stable GA slugs over time — reconfirm on the model page if one stops resolving.)

## Prompt & style help
Write **one flowing sentence** (not a keyword pile), front-loading the subject:
> **[subject]** + key details → **[style / medium]** → **[composition / shot]** → **[lighting / color]** → **[detail; camera or render terms]**.

Quick style starters (full set + game-art/UI templates in [`references/prompt-guide.md`](references/prompt-guide.md)):
- **Photoreal:** "…photorealistic, shot on a 50mm lens at f/1.8, soft daylight, sharp focus"
- **Cinematic:** "…cinematic film still, anamorphic, dramatic low-key rim light, teal-and-orange grade"
- **3D render:** "…polished 3D render, Octane style, PBR materials, soft global illumination"
- **Flat vector:** "…flat vector illustration, bold geometric shapes, limited palette, no gradients"
- **Logo / icon:** "…minimal vector logo, simple geometric mark, flat colors, plain background"

Key tips: phrase **avoids as positives** ("clean empty background", not "no clutter") — these models ignore negative-prompt syntax. Put words you want rendered in `"double quotes"`. Set aspect ratio via `--aspect`, not the prompt. Iterate with one specific change instead of re-rolling.

## After generating — review it
Read the image back (Read tool) and check: right subject, right style, no unwanted text/watermark, clean composition. If it's off, change one thing and regenerate once.
