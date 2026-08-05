# Confidentiality and data handling

## Treat all experimental content as confidential

Assume every user-provided result, conclusion, image, table, gene or target name, alias mapping, sample identifier, filename, note, and slide element is unpublished unless the user explicitly marks it public.

## Keep confidential work local

- Inspect and transform user materials only with local workspace tools.
- Do not place user content in web queries, image-generation prompts, external APIs, public URLs, telemetry-oriented tools, or unrelated tasks.
- Do not use a confidential hypothesis, target, model, phenotype, condition combination, or distinctive alias to formulate a public query.
- Do not ask another agent to inspect confidential material. Forward-test this skill only with synthetic fixtures.
- Store intermediates in the task-local temporary directory. Deliver only the requested PPTX; remove temporary exports when the platform permits safe cleanup.

## Separate public background research

Public research is allowed only for a generic topic that cannot identify the user's unreleased work. Use original papers and authoritative databases. Record public sources in notes. Never upload a user figure for reverse-image search or ask an external model to interpret it.

If a background topic cannot be generalized safely, do not browse. Use user-provided sources or ask for a public formulation.

## Prevent accidental disclosure

- Preserve aliases and redactions exactly; never reconstruct hidden identities.
- Remove comments, hidden review text, external local/network links, embedded files, and unused confidential media from the final copy when not required.
- Avoid filenames or full local paths in visible slides and notes.
- Do not expose prompts, checklist responses, extracted OCR, source inventories, or temporary render paths.
- Preserve the original file and export a new file. Never overwrite the source by default.

## Handle visuals and provenance

Do not generate synthetic experimental evidence. Generated conceptual diagrams may be used only for generic public biology, must be labelled conceptual, and must not include confidential entities, conditions, or conclusions.

Use this entry for user result slides:

```text
[Sources]
- 用户提供的未公开数据
```

Use ordinary citations for public background. Never cite a public paper as the source of the user's experimental observation.
