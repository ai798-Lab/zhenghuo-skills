---
name: poster-line-illustrator
description: Generate raster, image-model poster-style illustrations from a theme using thin black continuous contour lines, large flat red/yellow accent shapes, tiny colored dots, and generous white or pale mint space. Use when the user provides poster or editorial references with expressive line-art figures and asks for a matching illustration, image-generation prompt, style guide, or test image; ignore all typography and readable text in the references unless text is explicitly requested. 中文触发词包括：海报线描插画、线描海报风格、手绘线条海报、红黄线描插画、极简线描人物插画、按那组三张海报风格画图、用那个红黄线条插画风格生成。
---

# Poster Line Illustrator

## Chinese Triggers

Use this skill when the user says phrases like:

- 海报线描插画
- 线描海报风格
- 手绘线条海报
- 红黄线描插画
- 极简线描人物插画
- 按那组三张海报风格画图
- 用那个红黄线条插画风格生成
- 用之前 OPC 那张图的风格生成

## Workflow

1. Read the user's theme, article section, or visual brief.
2. Read `references/style-dna.md`, `references/visual-grammar.md`, `references/theme-translation.md`, `references/prompt-template.md`, and `references/qa-checklist.md`.
3. Inspect `assets/examples/` for visual density, line behavior, accent scale, and composition. Ignore all readable text in those images.
4. Convert the theme into one surreal poster metaphor: one line-drawn figure or hand, one prop, and one flat accent shape.
5. Produce a raster illustration with the available image-generation model by default. Use the prompt template to constrain the model toward sparse poster line art.
6. Apply the QA checklist. If the result looks like a business infographic, UI, logo, or literal scene, reduce it back to a sparse poster illustration.

## Output Rules

- Default to a portrait poster canvas.
- Use no readable text unless the user explicitly asks for title or copy.
- Keep the illustration sparse: one dominant contour figure, one core prop, two large accent shapes maximum, and three to six tiny dots or short marks.
- Use image generation as the primary production method. Do not substitute SVG/HTML/CSS for the final image unless the user explicitly asks for vector/code output or the image model is unavailable.
- If the user requests Imagen 2.0 and an Imagen 2.0-capable tool is available, use that model. If not, use the available image generation tool and state the limitation plainly.

## Assets

Reference images live in `assets/examples/`:

- `poster-line-01.png`
- `poster-line-02.png`
- `poster-line-03.png`

Use them for line rhythm, color placement, and poster spacing. Do not copy their text, exact figures, exact layouts, or placeholder copy.
