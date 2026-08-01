# Bundled default templates

Use this reference only when the user does not supply a reference/template PPTX.

## Selection rule

Ask once:

> 没有检测到参考模板。请选择默认配色：A 临床蓝（推荐、最通用）、B 生命青绿（柔和、偏细胞与转化）、C 编辑珊瑚（观点鲜明、偏科学媒体风格）、D 石墨靛蓝（克制、偏数据与方法）；也可以由我自动决定。

If duration or page count is also missing, combine both choices in the same intake question. Use A when the user delegates, does not answer, or gives no usable preference. Use B for a clearly cell-biology, immunology, aging, or translational tone only when that context makes it a better fit. Use C when the user explicitly wants an editorial or science-media feeling. Use D for method comparisons, structural work, or data-heavy technical reviews when a restrained tone is preferred.

An explicit user palette, brand direction, or institutional standard overrides these defaults. A supplied reference/template PPTX always overrides the bundled templates.

## Assets

| Option | Name | Template asset | Primary accent | Supporting accent |
|---|---|---|---|---|
| A | Clinical blue / 临床蓝 | `assets/default-templates/clinical-blue.pptx` | `#1769AA` | `#73A9D0` |
| B | Life teal / 生命青绿 | `assets/default-templates/life-teal.pptx` | `#007C7A` | `#7CC8B8` |
| C | Editorial coral / 编辑珊瑚 | `assets/default-templates/editorial-coral.pptx` | `#D95D45` | `#EAA28F` |
| D | Graphite indigo / 石墨靛蓝 | `assets/default-templates/graphite-indigo.pptx` | `#4B55A5` | `#9299D0` |

Use `assets/default-templates/palette-preview.png` when the platform can show a local preview and the user would benefit from seeing the four options.

## Shared visual system

- Canvas: 16:9, white background.
- Typeface: Microsoft YaHei for Chinese; use a metrically compatible sans-serif fallback when unavailable.
- Minimum hierarchy: deck title 50 pt, slide title 35 pt, intermediate heading 24 pt, body 16 pt.
- Body line spacing: 1.25 by default; allow 1.2–1.5 according to density.
- Margins: approximately 72 px on a 1280 × 720 canvas, with equal left and right margins.
- Structure: flat scientific composition, limited containers, no decorative icon grids or dashboard-like panels.
- Footer: quiet gray metadata and page numbering; never let terminology or citation text compete with the footer.

## Layout inventory

Each template contains eight editable source slides:

1. minimal cover;
2. section divider;
3. concept or scope overview;
4. published figure plus interpretation;
5. method comparison;
6. workflow or evidence chain;
7. conclusion and next step;
8. backup page.

Inspect all eight slides, duplicate only the layouts required by the narrative, and replace every sample title, label, figure placeholder, footer, author field, and example statement. Do not deliver template sample copy. Preserve the selected deck's spacing, title treatment, palette, and page furniture while varying slide silhouettes according to content.
