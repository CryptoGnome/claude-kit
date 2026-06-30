#!/usr/bin/env python
"""design-mockup: generate images via OpenRouter + Gemini ("nano banana").

Project-agnostic. No forced style suffix.

Usage:
  python generate.py --prompt "..." --output out.png [--ref a.png b.png] [--model ID]

Key resolution order: OPENROUTER_API_KEY env var, then key.txt next to this script
or in the skill root. Never reads other projects' files.
"""
import os
import re
import sys
import base64
import argparse
from openai import OpenAI

DEFAULT_MODEL = "google/gemini-3.1-flash-image-preview"


def resolve_key():
    k = os.environ.get("OPENROUTER_API_KEY")
    if k:
        return k.strip()
    here = os.path.dirname(os.path.abspath(__file__))
    for cand in (os.path.join(here, "key.txt"), os.path.join(here, "..", "key.txt")):
        if os.path.exists(cand):
            with open(cand, "r", encoding="utf-8") as f:
                return f.read().strip()
    return None


def encode_image(path):
    with open(path, "rb") as f:
        return base64.b64encode(f.read()).decode("utf-8")


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--prompt", required=True)
    ap.add_argument("--output", default="mockup.png")
    ap.add_argument("--ref", nargs="*", default=[])
    ap.add_argument("--model", default=DEFAULT_MODEL)
    args = ap.parse_args()

    key = resolve_key()
    if not key:
        sys.exit("ERROR: no API key. Set OPENROUTER_API_KEY or create key.txt in the skill folder.")

    client = OpenAI(base_url="https://openrouter.ai/api/v1", api_key=key)

    if args.ref:
        content = []
        for p in args.ref:
            ext = p.rsplit(".", 1)[-1].lower()
            mime = "image/png" if ext == "png" else "image/jpeg"
            content.append({"type": "image_url",
                            "image_url": {"url": f"data:{mime};base64,{encode_image(p)}"}})
        content.append({"type": "text", "text": args.prompt})
        messages = [{"role": "user", "content": content}]
    else:
        messages = [{"role": "user", "content": args.prompt}]

    resp = client.chat.completions.create(
        model=args.model, messages=messages, extra_body={"modalities": ["image", "text"]})
    msg = resp.choices[0].message
    images = getattr(msg, "images", None)
    if not images:
        sys.exit("No image returned. Response: " + str(resp)[:500])

    out = args.output if args.output.endswith(".png") else args.output + ".png"
    d = os.path.dirname(os.path.abspath(out))
    if d:
        os.makedirs(d, exist_ok=True)
    url = images[0]["image_url"]["url"]
    data = re.sub(r"^data:image/[^;]+;base64,", "", url)
    with open(out, "wb") as f:
        f.write(base64.b64decode(data))
    with open(os.path.splitext(out)[0] + ".prompt.txt", "w", encoding="utf-8") as f:
        f.write("Prompt: " + args.prompt + "\nModel: " + args.model + "\n")
    print("Saved:", out)


if __name__ == "__main__":
    main()
