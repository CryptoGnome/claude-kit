#!/usr/bin/env python
"""image-gen: generate images via OpenRouter. Stdlib only (no pip install).

Two OpenRouter paths, auto-selected by model:
  - chat/completions + modalities  -> Google Gemini + OpenAI GPT image models
  - /api/v1/images                 -> FLUX.2, Seedream, Grok Imagine, etc.

Key resolution: OPENROUTER_API_KEY env var, then key.txt in this folder or the skill root.
Never reads other projects' files.
"""
import os
import re
import sys
import json
import base64
import argparse
import urllib.request
import urllib.error

BASE = "https://openrouter.ai/api/v1"
DEFAULT_MODEL = "google/gemini-3.1-flash-image-preview"


def resolve_key():
    k = os.environ.get("OPENROUTER_API_KEY")
    if k:
        return k.strip()
    here = os.path.dirname(os.path.abspath(__file__))
    for cand in (os.path.join(here, "key.txt"), os.path.join(here, "..", "key.txt")):
        if os.path.exists(cand):
            with open(cand, encoding="utf-8") as f:
                return f.read().strip()
    return None


def pick_api(model, override):
    if override != "auto":
        return override
    m = model.lower()
    if ("gemini" in m and "image" in m) or (m.startswith("openai/") and "image" in m):
        return "chat"
    return "images"


def data_url(path):
    ext = path.rsplit(".", 1)[-1].lower()
    mime = "image/png" if ext == "png" else "image/jpeg"
    with open(path, "rb") as f:
        return "data:%s;base64,%s" % (mime, base64.b64encode(f.read()).decode())


def post(path, key, body):
    req = urllib.request.Request(
        BASE + path, data=json.dumps(body).encode(),
        headers={"Authorization": "Bearer " + key, "Content-Type": "application/json"})
    try:
        with urllib.request.urlopen(req, timeout=180) as r:
            return json.load(r)
    except urllib.error.HTTPError as e:
        sys.exit("OpenRouter HTTP %s: %s" % (e.code, e.read().decode()[:500]))


def fetch(url):
    with urllib.request.urlopen(url, timeout=120) as r:
        return r.read()


def gen_chat(key, model, prompt, refs):
    if refs:
        content = [{"type": "image_url", "image_url": {"url": data_url(p)}} for p in refs]
        content.append({"type": "text", "text": prompt})
    else:
        content = prompt
    resp = post("/chat/completions", key,
                {"model": model,
                 "messages": [{"role": "user", "content": content}],
                 "modalities": ["image", "text"]})
    msg = resp["choices"][0]["message"]
    imgs = msg.get("images")
    if not imgs:
        sys.exit("No image returned: " + json.dumps(resp)[:500])
    url = imgs[0]["image_url"]["url"]
    return base64.b64decode(re.sub(r"^data:image/[^;]+;base64,", "", url))


def gen_images(key, model, prompt, aspect, refs):
    body = {"model": model, "prompt": prompt, "n": 1}
    if aspect:
        body["aspect_ratio"] = aspect
    if refs:
        body["input_references"] = [data_url(p) for p in refs]
    resp = post("/images", key, body)
    data = resp.get("data")
    if not data:
        sys.exit("No image returned: " + json.dumps(resp)[:500])
    item = data[0]
    if item.get("b64_json"):
        return base64.b64decode(item["b64_json"])
    if item.get("url"):
        return fetch(item["url"])
    sys.exit("No image data in response: " + json.dumps(resp)[:500])


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--prompt", required=True)
    ap.add_argument("--output", default="image.png")
    ap.add_argument("--model", default=DEFAULT_MODEL)
    ap.add_argument("--ref", nargs="*", default=[])
    ap.add_argument("--aspect", default=None, help="e.g. 16:9 (images-API models)")
    ap.add_argument("--api", choices=["auto", "chat", "images"], default="auto")
    a = ap.parse_args()

    key = resolve_key()
    if not key:
        sys.exit("ERROR: no API key. Set OPENROUTER_API_KEY or create key.txt in the skill folder.")

    api = pick_api(a.model, a.api)
    if api == "chat":
        png = gen_chat(key, a.model, a.prompt, a.ref)
    else:
        png = gen_images(key, a.model, a.prompt, a.aspect, a.ref)

    out = a.output if a.output.endswith(".png") else a.output + ".png"
    d = os.path.dirname(os.path.abspath(out))
    if d:
        os.makedirs(d, exist_ok=True)
    with open(out, "wb") as f:
        f.write(png)
    with open(os.path.splitext(out)[0] + ".prompt.txt", "w", encoding="utf-8") as f:
        f.write("Prompt: %s\nModel: %s\nAPI: %s\n" % (a.prompt, a.model, api))
    print("Saved: %s (%s api, %s)" % (out, api, a.model))


if __name__ == "__main__":
    main()
