---
name: photo-abstract-editorial
description: Create a clean editorial artwork that preserves an uploaded photograph at its original pixel dimensions and pairs it with an equally sized, photo-derived abstract memory panel and poetic English title. Use when asked to transform a photo into an abstract editorial diptych, photo-plus-abstraction composition, visual memory panel, or minimalist archival poster without redrawing or stylizing the source photo. Stack landscape photos above the panel; place square or portrait photos to its left.
---

# Photo Abstract Editorial

Create one finished image from one uploaded photograph. Keep the photograph pixel-faithful; derive the adjacent abstract panel only from the photograph's observed spatial, tonal, and color relationships.

## Workflow

1. Inspect the photograph internally and record its displayed pixel dimensions as `W × H` after honoring EXIF orientation. Identify three to six decisive spatial facts: subject relationships, scale, axes, direction, intervals, overlap, depth, rhythm, light, color roles, and negative space.
2. Keep the photo as an exact `W × H` section. Never scale, crop, redraw, extend, replace, retouch, filter, or otherwise alter its visible pixels.
3. Reconstruct the retained relationships as a sparse abstract motif—not a thumbnail, trace, illustration, vector icon, or style transfer. Prefer relationships over silhouettes and preserve only the minimum recognition cues needed for distinctive subjects.
4. Create the complete abstract panel at exactly `W × H` pixels, including its untextured, uniform ivory background, motif, and title. If the image generator cannot emit the exact pixel dimensions, use the closest supported canvas with the same orientation, then proportionally fit and pad only the abstract panel to `W × H`; never resize or crop the photo, and never stretch or crop the panel artwork.
5. Join the two equal-sized sections by orientation: when `W > H`, place the photo above the panel to produce `W × 2H`; otherwise (`W <= H`, including square images), place the photo left of the panel to produce `2W × H`. Join them directly with no gap, frame, shadow, collage, tape, or mockup effect.
6. Use one primary mark family and no more than two supporting families. Extract a muted palette solely from the photo; use generous whitespace and avoid invented decorative elements, colors, symbols, and symmetry.
7. Create one original English title of two to five words, grounded in visible facts. Place it only on the abstract panel in a restrained editorial serif face. Add a short subtitle only when it adds meaning.
8. Use [scripts/compose_editorial.py](scripts/compose_editorial.py) for deterministic sizing and joining. Confirm that the panel is `W × H` and that the final PNG is `W × 2H` or `2W × H` as required.
9. Return only the completed composition. Do not add commentary, analysis, title options, labels, dates, logos, or watermarks.

## Guardrails

- Treat the uploaded photo as the sole content source.
- Preserve the photo at its original displayed pixel dimensions and make the complete abstract panel exactly the same width and height.
- Treat `W > H` as landscape; treat `W <= H` as non-landscape, so square photos use the right-side panel layout.
- Keep the panel background flat, continuous, and neutral ivory; exclude gradients, paper texture, grain, glow, shadows, vignettes, stains, collage artifacts, and scan effects.
- Make every abstract mark traceable to a visual fact in the source photo.
- Preserve people as irregular continuous short vertical marks or gently tapered blocks, never illustrated heads, limbs, faces, or clothing.
- Preserve landmark architecture with at most one to three identity cues; omit architectural surface detail.

## Reference Prompt

Read the appropriate full prompt before producing the image:

- Chinese: [references/photo-abstract-editorial-prompt.zh-CN.md](references/photo-abstract-editorial-prompt.zh-CN.md)
- English: [references/photo-abstract-editorial-prompt.en.md](references/photo-abstract-editorial-prompt.en.md)

Use [assets/examples](assets/examples) as visual input examples only. Do not reuse their subject matter, colors, or composition unless the user supplies that exact image.
