# Cross-platform compatibility

The scientific workflow is portable. File-editing capabilities differ by platform, so preserve the acceptance criteria even when implementation tools change.

## Codex

Invoke `$optimize-research-review-slides` with the draft and optional template PPTX. Also load the installed presentation skill. Use the required Codex presentation runtime for import, editing, rendering, and PPTX export.

Portable invocation:

```text
Use $optimize-research-review-slides to optimize the attached scientific review PPTX. Before editing, ask whether I want to control the main deck by presentation duration, main-slide count, or let the agent decide; backup slides do not count toward the main-slide total. Then follow the attached template, apply the relevant life-science domain rules, add timed speaker notes and sources, render every slide, and return a verified PPTX.
```

## TRAE WORK

Add this skill folder to the project or agent-readable rules directory. In the task prompt, instruct the agent to read `SKILL.md` first and then only the referenced files required for the task. If native PPTX editing is unavailable, use a compatible JavaScript PowerPoint library or LibreOffice conversion pipeline, but preserve the source/template and render the final deck for visual review.

## Workbuddy

Attach or mount this folder with the task materials. Ask the agent to treat `SKILL.md` as the governing workflow. Map its available document, browser, image, and execution tools to the same stages: inspect → research → edit → notes/sources → render → validate.

## Tool-neutral fallback prompt

```text
Read optimize-research-review-slides/SKILL.md and follow it as the governing workflow. Inputs are DRAFT.pptx and TEMPLATE.pptx. First ask whether the main deck should be controlled by TARGET_MINUTES, TARGET_MAIN_SLIDES, or agent judgment. Backup pages do not count toward the main-slide total. Then create the main talk and backup section, apply the relevant life-science domain rules, preserve the original files, add timed per-slide notes and sources, and do not finish until all slides have been rendered and inspected.
```

## Portability requirements

- Do not depend on Codex-only citation directives inside the generated PPTX.
- Keep citations as ordinary text in speaker notes.
- Use standard PPTX features and embedded raster images.
- Use common sans-serif fonts or fonts explicitly supplied by the user.
- Keep the audit script standard-library-only so it can run in most Python 3 environments.
- If a platform cannot preserve notes, disclose that limitation before delivery rather than silently omitting them.
