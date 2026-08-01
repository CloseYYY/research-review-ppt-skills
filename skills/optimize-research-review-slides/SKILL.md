---
name: optimize-research-review-slides
description: Optimize a draft scientific review or methods-summary PowerPoint into a rigorous, coherent, presentation-ready journal-club or lab-meeting deck, using an optional reference/template PPTX or one of four bundled white-background color templates. Use for Chinese or English life-science review slides that need literature supplementation, scientific rewriting, concise titles, evidence-aware figures, unified formatting, no-template palette selection, target-duration control, a main-talk plus backup-slide structure, speaker notes, terminology expansion, citations, domain-specific standards, and rendered visual QA. Use when the presentation mainly synthesizes published knowledge or methods; do not use as the primary workflow for a data-driven lab meeting centered on the user's new experimental results.
---

# Optimize Scientific Review Slides

Transform a draft review deck into a concise scientific narrative while preserving evidence boundaries and the supplied visual template.

## Route the task

1. Use this skill when published literature, mechanisms, methods, or field comparisons are the main content.
2. Do not force this workflow onto a results presentation whose main argument depends on the user's new data. State that a result-reporting workflow is more suitable.
3. In Codex, also use the `presentations:Presentations` skill for every PPTX operation. Use `imagegen` only for conceptual diagrams, never to fabricate experimental evidence. Use `humanizer-zh` when the requested language is Chinese and natural scientific phrasing is required.
4. For TRAE WORK or Workbuddy, read [compatibility.md](references/compatibility.md) before implementation.
5. Read [domain-extensions.md](references/domain-extensions.md) only for the life-science domains actually present in the deck.

## Establish the input contract

Prefer these inputs:

- draft `.pptx` containing the research scope and existing material;
- optional reference/template `.pptx` defining layout and visual style;
- topic, audience, target duration, language, desired depth, and whether backup slides are wanted;
- optional papers, PDFs, datasets, institutional logos, and author information.

Before optimizing, obtain the main-deck size constraint with one concise question unless the user already supplied it. Offer three routes: target presentation duration, target main-slide count, or agent-determined length. Treat backup slides as outside the main-slide count unless the user says otherwise. If the user delegates the decision, inspect the draft and choose both a target duration and main-slide range, then state the choice before editing.

If no reference/template PPTX is supplied, read [default-template.md](references/default-template.md) and ask the user to choose A clinical blue, B life teal, C editorial coral, D graphite indigo, or agent-determined palette. Recommend A and use A when the user delegates or does not answer. When both deck size and palette are missing, ask for both in one compact intake question rather than two separate interruptions.

If a template is supplied, treat it as the visual authority. If no template is supplied, treat the selected bundled template as the visual authority. Explicit user visual direction overrides the bundled default. If other essential scientific scope is ambiguous, ask at most one additional concise question; otherwise make conservative assumptions and proceed. Preserve source files and export a new PPTX unless the user explicitly requests in-place editing.

## Execute the workflow

### 1. Audit both decks

- Inspect every draft and template slide, including masters, layouts, placeholders, notes, figures, tables, fonts, colors, and page furniture.
- When no external template is supplied, load the selected asset from `assets/default-templates/` and inspect all eight source layouts before editing.
- Run `scripts/audit_pptx.py` on the draft before editing and on the final file with `--strict`.
- Identify reusable template layouts rather than recreating the style approximately.
- Record existing claims, missing links, duplicated material, weak figures, and unsupported conclusions.

### 2. Build a review narrative

- Read [review-deck-workflow.md](references/review-deck-workflow.md).
- Define one communication job for the deck and one takeaway per slide.
- Separate measurement targets, biological interpretations, and downstream responses.
- Prefer a progression of scope → conceptual model → method/evidence groups → published cases → comparison/selection → limitations → practical recommendation → summary.
- Keep review and method-summary decks concise. Add slides only when they materially improve understanding.
- Read [duration-and-backup.md](references/duration-and-backup.md). Allocate time before finalizing slide count, and separate the main talk from backup material.
- When the user specifies minutes, derive a main-slide range. When the user specifies pages, derive an estimated duration. When both are provided but conflict, prioritize duration and explain the necessary page adjustment.

### 3. Verify and supplement the science

- Search current primary literature and authoritative sources when claims, nomenclature, protocols, or images are not supplied or may have changed.
- Prefer original papers for experimental examples and official databases for names, structures, markers, and standards.
- Distinguish direct evidence, orthogonal validation, biological response markers, and inference.
- Do not upgrade association into mechanism or a stress marker into direct aggregation evidence.
- Put a `[Sources]` block in the notes of every slide containing externally sourced claims or assets.
- Apply the relevant evidence, figure, nomenclature, and control rules from [domain-extensions.md](references/domain-extensions.md).

### 4. Rewrite for scientific speech

- Read [scientific-language.md](references/scientific-language.md).
- Rewrite titles as short biological conclusions or questions, not article-like sentences.
- Use plain, precise Chinese or English. Remove promotional wording, vague attribution, filler transitions, and formulaic AI phrasing.
- Shorten before reducing font size.
- Define uncommon technical terms and abbreviations on the first slide where the talk track uses them: Chinese name + English full name + abbreviation. Repeat the expansion in that slide's speaker notes.
- Do not expand universally familiar terms requested by the user, such as Western blot or FACS.

### 5. Select and place visuals

- Use published figures for experimental cases. Preserve labels when legible, crop only to clarify the cited panel, and cite the original paper in notes.
- Use simple generated or sourced schematics for pathways, mechanisms, workflows, and molecular concepts. Label generated visuals as conceptual and not experimental.
- Never create synthetic microscopy, blots, spectra, or quantitative plots that could be mistaken for data.
- Use diagrams only when they explain a relationship better than prose.

### 6. Apply the template and typography

- Preserve the template's master/layout hierarchy, margins, title treatment, footer, and page numbering.
- When no external template exists, use the selected bundled template rather than inventing an unrelated style or falling back to a generic layout library. Replace all sample copy while preserving its layout system and palette.
- Use a white background and a consistent sans-serif font when no stronger template instruction exists. The bundled templates use Microsoft YaHei with a white canvas and palette-specific accent colors.
- Use 1.2–1.5 line spacing for multiline content. Default to 1.25 for body text and 1.2 for compact terminology/source footers.
- Maintain readable hierarchy, consistent left/right margins, and at least 16 pt body text unless the supplied template clearly uses another validated scale.
- Avoid dense card grids, decorative icons, and repeated UI-like panels.

### 7. Write speaker notes

- Give every slide a self-contained script that explains what to notice, how to interpret it, and the transition to the next slide.
- Target roughly 45–90 seconds per content slide unless the user specifies a total duration.
- Use this structure:

```text
【讲稿】
【建议时长】60秒
<natural spoken scientific explanation>

[Sources]
- <claim or asset source>
```

- Expand uncommon terms in the notes at first occurrence, even when a concise definition is also visible on the slide.
- For backup slides, add `【备用页】` before `【讲稿】`; do not include backup pages in the main-talk time budget.

### 8. Validate the deliverable

- Read [quality-checklist.md](references/quality-checklist.md).
- Render every slide and inspect every slide at full size; use a montage only for deck-level consistency.
- Fix clipping, overlaps, awkward wrapping, tiny figure labels, inconsistent titles, missing citations, and terminology footers that compete with page numbers.
- Confirm every slide has notes and every external figure or non-trivial claim is traceable.
- Run the platform's overflow test plus `python scripts/audit_pptx.py FINAL.pptx --strict --target-minutes N` or `--target-main-slides N`. Use both when both constraints are compatible. Add `--require-backup` when the user requested backup slides.

## Deliver

Return only the final `.pptx` and a concise summary of representative changes. Mention major external sources used. Do not deliver scratch renders, temporary crops, or planning files unless requested.

## Optional invocation patterns

Read [compatibility.md](references/compatibility.md) for portable prompts and tool fallbacks. Use [quality-checklist.md](references/quality-checklist.md) as the acceptance contract, not as slide content.
