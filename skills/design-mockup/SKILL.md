---
name: design-mockup
description: Generate design and concept mockup images from a text prompt (plus optional reference images) via the OpenRouter API using Google's Gemini image model. Project-agnostic — no forced brand look, so any style. Use when the user wants to create, generate, draw, or mock up a visual: concept art, character/model turnaround sheets, environment/level art, UI/HUD mockups, icons, logos, or style explorations — even phrased as "make a mockup", "concept art", "character sheet", or "show me what X could look like". Do NOT use for editing the user's existing project files, or for non-image tasks.
argument-hint: "[prompt] [output?]"
version: 1.0.0
license: MIT
---

# Design Mockup Generator

Generates images from a text prompt (+ optional reference images) using OpenRouter's Gemini image model. Neutral by default: the look comes entirely from your prompt — flat-shaded low-poly, painterly, photoreal, UI wireframe, whatever you ask.

## API key (one-time setup)
The script resolves the OpenRouter key in this order:
1. `OPENROUTER_API_KEY` environment variable (preferred).
2. `key.txt` in this skill folder (one line: the key). **`key.txt` is gitignored — never commit it.**

If neither exists, get a key at https://openrouter.ai/keys and set the env var or create `key.txt`. **Never read another project's `.env`** — keys are per-project. If a key was pasted into chat, suggest rotating it.

## Generate
Requires Python with the `openai` package (`python -m pip install openai -q` if it's missing).

```bash
python scripts/generate.py --prompt "<your prompt>" --output "<path/to/out.png>"
```
Options:
- `--ref <img1> <img2> ...` — reference image(s) for style / image-to-image (multimodal).
- `--model <id>` — override the model (default `google/gemini-3.1-flash-image-preview`).

It saves the PNG, writes a `<name>.prompt.txt` sidecar, and prints the path.

## After generating — review it
Read the image back (Read tool) and check: right subject, right style, no unwanted text/watermark, clear composition. If it's off, refine the prompt (add specificity, name a reference style, drop conflicting terms) and regenerate once.

## Prompt templates
Fill-in-the-blank prompts for the common mockup types (flat-shaded low-poly, Synty PBR, character model sheets, UI/HUD, environments, icons/logos) live in [`references/prompt-templates.md`](references/prompt-templates.md). Read it whenever the user wants one of those.

## Tips
- State the **style explicitly** — there is no default style, that's the point.
- Character sheets: ask for aligned front/side/back views, plain background, relaxed A-pose so the result is usable as a modeling reference.
- Explore 2–3 variants, then pick and refine. Image gen is non-deterministic.
