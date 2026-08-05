---
name: optimize-research-results-slides
description: Create or optimize confidential Chinese life-science lab-meeting PowerPoint decks centered on the user's experimental results. Use for existing PPTX files or raw experiment notes, figures, and outlines that must become a rigorous data-driven progress report with per-result-slide purpose, methods and key conditions, direct results, a one-sentence conclusion, future experiments, speaker notes, terminology expansion, white-background scientific styling, and rendered PPTX QA. Do not use as the primary workflow for literature-review decks; route background-only slides through the installed optimize-research-review-slides skill.
---

# Optimize Research Results Slides

Build a result-driven lab-meeting deck for a supervisor and research group. Preserve uncertainty, confidentiality, and the evidentiary boundary of every experiment.

## Enforce dependencies and confidentiality

1. Use `presentations:Presentations` for every PPTX read, edit, render, and export operation.
2. Confirm that `optimize-research-review-slides` is installed before working on background-knowledge slides. If it is unavailable, pause and give the user its installation instruction; do not copy or silently replace it.
3. For Chinese copy, use `Humanizer Zh` when installed. If it is unavailable, apply [scientific-language.md](references/scientific-language.md) completely.
4. Read [confidentiality.md](references/confidentiality.md) before inspecting user material. Never send unreleased experimental content or identifying derivatives to web search, image generation, external APIs, or unrelated agents.

## Establish the input contract

Accept either an existing `.pptx` or notes, figures, tables, and outlines. Also accept an optional white-background template, target duration or main-slide count, redaction instructions, and supporting public papers.

Preserve every source file and export a new PPTX. Treat a supplied template as authoritative only when it uses a white background and a consistent sans-serif type system; otherwise retain its useful hierarchy while normalizing those requirements. Default to Microsoft YaHei, white canvas, clinical blue `#1F4E79`, and 1.25 body line spacing.

If duration and page count are both absent, ask one concise question offering minutes, main-slide count, or agent judgment. Combine it with the missing-information checklist when practical.

## Audit, classify, and gate

1. Inspect every input slide, note, figure, table, master, layout, placeholder, comment, and external relationship locally.
2. Classify each slide as `封面`, `背景页`, `研究问题`, `结果页`, `阶段总结`, `未来计划`, `备用页`, or `其他`.
3. Read [results-deck-workflow.md](references/results-deck-workflow.md). Create an internal result record for every result slide or result unit.
4. Read [intake-checklist.md](references/intake-checklist.md). Send one consolidated, slide-indexed checklist containing every missing scientific field. Stop and wait for one consolidated reply. Treat `无`, `不适用`, `不清楚`, and `已隐藏` as valid answers.
5. Apply the response mapping exactly. Never infer a redacted name, image, value, or conclusion.

Do not reveal internal planning metadata on visible slides. Put machine-auditable page type markers in notes only.

## Build the result narrative

- Give every result slide one communication job and visibly include `实验目的`, `实验方法`, `实验结果`, and `一句话结论`.
- Include sample/model, groups and controls, critical conditions, readout, biological replicate count, and statistics wherever they determine interpretation.
- Choose a layout around the evidence: figure-left/text-right, figure-top/text-bottom, or dominant figure with a narrow explanation rail. Do not force four equal cards.
- Distinguish direct observation, association, functional support, and causal evidence. Preserve negative data, variability, batch effects, limitations, and missing controls.
- After each coherent result module, add a next-step recommendation tied to the evidence. End with a roadmap organized by priority, experiment, decision criterion, and fallback.
- Load only the relevant section of [domain-extensions.md](references/domain-extensions.md) and apply its controls and evidence rules.

## Handle background, visuals, and redactions

- Invoke `optimize-research-review-slides` only for background-knowledge slides. Search public information using generic public topics that cannot reveal the user's hypothesis, target, model, phenotype, or unpublished conclusion.
- Use published figures or authoritative databases for public background. Never generate or source microscopy, blots, flow plots, spectra, or quantitative plots that could be mistaken for user data.
- Preserve user aliases exactly. Use a restrained dashed placeholder labelled `待补：图片`, `待补：名称`, `待补：数值`, or `待补：结论` for hidden content. Use `待确认` for unknown content.
- Use white backgrounds, one sans-serif family, clinical-blue accents, and 1.2–1.5 line spacing for multiline text. Prefer 1.25 for body text. Shorten text before reducing font size.

## Write notes and terminology

Give every slide notes in this structure:

```text
【页面类型】结果页
【讲稿】
【建议时长】75秒
<natural spoken explanation>

【首次术语】中文名称（English full name，ABBR）

[Sources]
- 用户提供的未公开数据
```

Omit `【首次术语】` when none appears. On the first slide where an uncommon term is spoken, place `中文名称（English full name，ABBR）` in genuine blank space and repeat it naturally in notes. Do not expand Western blot, FACS, PCR, DNA, or RNA by default.

For result slides, explain the question, critical conditions, what the data show, the justified interpretation, the limitation, and the transition. Do not recite slide text. Mark user result slides as `用户提供的未公开数据`; do not add speculative external citations.

## Validate and deliver

1. Read [quality-checklist.md](references/quality-checklist.md).
2. Run `python scripts/audit_pptx.py DRAFT.pptx` before editing.
3. Render every final slide and inspect every slide at full size. Fix clipping, overlap, one-word wrapping, illegible labels, unresolved unintended placeholders, and visual imbalance.
4. Run the presentation overflow test and then:

```text
python scripts/audit_pptx.py FINAL.pptx --strict --require-white-background
```

Add `--target-minutes N`, `--target-main-slides N`, `--required-font "Microsoft YaHei"`, or `--strict-terms` when applicable.

5. Return only the verified `.pptx` and a concise summary. Do not deliver extracted data, temporary crops, renders, prompts, logs, or planning files.

