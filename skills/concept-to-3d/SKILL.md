---
name: concept-to-3d
description: >-
  Turn a 2D character/monster/prop concept into a game-ready 3D model (.glb) inside a
  Godot project, using Blender (via the blender-mcp server) + Rodin/Hyper3D image-to-3D.
  Use whenever the user wants to convert concept art into 3D, generate a 3D character or
  creature or prop from an image or description, get an AI-generated model into Blender or
  Godot, or build out game art assets. Triggers on "make this 3D", "concept to model",
  "generate a 3D character/monster", "get this into the game as 3D", "image to 3D".
version: 1.0.0
license: MIT
---

# Concept → 3D → Godot pipeline

Convert a concept image into a clean, game-ready `.glb` in a Godot project.

## Prerequisites (check first)
- **Blender open** with the **blender-mcp** server connected (panel shows "Running on port 9876").
  Verify with `get_scene_info`.
- **Rodin/Hyper3D enabled** — check `get_hyper3d_status`. **The mode decides whether an upload is needed:**
  - **`MAIN_SITE` (incl. the free-trial key) → image-to-3D reads LOCAL file paths. No upload. PREFERRED — fully automatable.**
  - **`FAL_AI` → image-to-3D needs PUBLIC image URLs → you must upload the images first.** The auto-mode
    safety classifier BLOCKS the agent from uploading local files to outside hosts (anti-exfiltration), and a
    skill cannot bypass that (it inspects the command, not the caller). So in fal mode the user must either
    run the upload themselves or add a permission rule. **Prefer MAIN_SITE/local mode to avoid all of this.**

## Steps

### 1. Get a Rodin-optimized turnaround
Use the `design-mockup` skill (text-only so nothing is sent out) to make a 3-view turnaround built for
reconstruction — NOT a beauty shot:
> Three full-body views (FRONT, LEFT SIDE, BACK) of the SAME character, side by side on a plain flat
> light-gray background. Relaxed A-pose, arms slightly away from the torso, full body head-to-toe, all
> three the same height. Flat even neutral studio lighting, minimal shadows, consistent design. No text.

### 2. Crop into separate views (in Blender — no shell, no upload)
```python
import bpy, numpy as np, os
src = r"<turnaround.png>"; outdir = r"<project>/concept/views"; os.makedirs(outdir, exist_ok=True)
img = bpy.data.images.load(src); w, h = img.size
arr = np.array(img.pixels[:], dtype=np.float32).reshape(h, w, 4); third = w // 3
for i, n in enumerate(["front", "side", "back"]):
    x0 = i*third; x1 = w if i == 2 else (i+1)*third
    sub = arr[:, x0:x1, :].copy()
    o = bpy.data.images.new(n, sub.shape[1], sub.shape[0], alpha=True)
    o.pixels = sub.ravel().tolist(); o.filepath_raw = os.path.join(outdir, n+".png"); o.file_format='PNG'; o.save()
    bpy.data.images.remove(o)
bpy.data.images.remove(img)
```

### 3. Generate with Rodin
- **MAIN_SITE/local:** `generate_hyper3d_model_via_images(input_image_paths=[front, side, back])`
- **FAL_AI:** needs `input_image_urls=[...]` → requires uploads (see prereqs).
- Then `poll_rodin_job_status(request_id=...)` until `COMPLETED`, then `import_generated_asset(name, request_id=...)`.

### 4. Make it game-ready (in Blender)
Rodin output is Y-up, centered, ~20k tris with a baked PBR texture. Fix via mesh-data ops (reliable over MCP;
`bpy.ops.*_apply` is flaky over the socket):
```python
import bpy, math, mathutils
ob = bpy.data.objects["<Name>"]; ob.rotation_euler = (0,0,0)
ob.data.transform(mathutils.Matrix.Rotation(math.radians(90), 4, 'X'))      # Y-up -> Z-up (stand it up)
mz = min(v.co.z for v in ob.data.vertices)
ob.data.transform(mathutils.Matrix.Translation((0,0,-mz)))                   # feet to z=0
# decimate to game-poly via depsgraph (reliable):
m = ob.modifiers.new("Dec","DECIMATE"); m.ratio = 0.2
deg = bpy.context.evaluated_depsgraph_get()
newmesh = bpy.data.meshes.new_from_object(ob.evaluated_get(deg))
old = ob.data; ob.modifiers.clear(); ob.data = newmesh; bpy.data.meshes.remove(old)
# export:
bpy.ops.object.select_all(action='DESELECT'); ob.select_set(True); bpy.context.view_layer.objects.active = ob
bpy.ops.export_scene.gltf(filepath=r"<project>/assets/.../model.glb", export_format='GLB', use_selection=True)
```
(Optional: replace the baked texture with flat palette materials for a cohesive low-poly look.)

### 5. Into Godot
- `.glb` imports natively → a scene with `MeshInstance3D` (+ `Skeleton3D`/`AnimationPlayer` if rigged).
- Instance it under the player/mob scene in place of the placeholder mesh; keep the collision shape.
- Rigged characters: drive an `AnimationTree` (idle/run/attack) from the synced state.
- Verify: `Godot --headless --path <project> --import` (exit 0 + a `.glb.import` file = success).

## The upload guardrail — how to actually automate
A skill does NOT make uploads work. The only real fixes:
1. **Best — local mode:** in the BlenderMCP panel click **Set Free Trial API Key** (or use a personal Rodin
   key) so Rodin is `MAIN_SITE`. Then step 3 uses local paths and the whole pipeline runs with zero prompts.
2. **Keep fal:** the user adds a permission rule to `.claude/settings.local.json` allowing the upload command,
   then runs it / lets the agent run it. This keeps an exfiltration path open and is fiddlier — prefer #1.
