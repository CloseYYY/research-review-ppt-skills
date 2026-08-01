# Duration control and backup slides

## Ask for the governing constraint

Before restructuring the deck, ask one compact question unless the user already supplied a constraint:

```text
本次主汇报希望按哪种方式控制篇幅：目标时长、主汇报页数，还是由我根据内容自动决定？备用页默认不计入主汇报页数。
```

If the interface supports choices, offer:

1. target duration in minutes;
2. target number of main slides;
3. agent decides after auditing the draft.

Do not ask the user to provide both minutes and pages. If the user provides both and they conflict, make duration the primary constraint because rehearsal time is the harder limit. Explain the adjusted main-slide range before editing.

When the agent decides, consider the number of distinct evidence units, figure complexity, audience familiarity, available template layouts, and the likely lab-meeting slot. State the chosen duration and main-slide range so the user can correct it while work continues.

## Plan from minutes, not from existing slide count

Set the main-talk time budget before deciding what stays in the main deck. Exclude title, acknowledgements, and backup pages only when they require negligible speaking time.

Use these starting ranges, then adjust for figure complexity and audience familiarity:

| Target time | Main content slides | Typical backup slides |
|---|---:|---:|
| 8–10 min | 7–10 | 2–4 |
| 12–15 min | 10–14 | 3–6 |
| 18–20 min | 14–18 | 4–8 |
| 25–30 min | 18–24 | 5–10 |

Do not use one-slide-per-minute mechanically. A dense published figure may need 90–120 seconds; a scope or transition slide may need 20–40 seconds.

## Allocate time by narrative role

A useful default for a concise review is:

- context and scope: 10–15%;
- concepts and evidence map: 15–20%;
- core methods, mechanisms, or evidence: 40–50%;
- published cases and comparison: 15–20%;
- recommendation, limitations, and summary: 10–15%.

Protect the final recommendation and summary. When over time, remove duplicated background or move technical depth to backup slides before cutting the synthesis.

## Add timing metadata to notes

Use an explicit per-slide target:

```text
【讲稿】
【建议时长】75秒
<script>

[Sources]
- <source>
```

Estimate speaking time after writing the actual script. Scientific Chinese is commonly planned at roughly 220–260 Chinese characters per minute; scientific English is commonly planned at roughly 120–145 words per minute. Slow down for equations, complex figures, unfamiliar nomenclature, and audience interaction.

Run:

```text
python scripts/audit_pptx.py FINAL.pptx --strict --target-minutes 15
```

For a page-count constraint, run:

```text
python scripts/audit_pptx.py FINAL.pptx --strict --target-main-slides 14
```

The main-slide count excludes pages marked `【备用页】` or `[Backup]`.

Treat the script estimate as a planning signal, not a substitute for rehearsal. Revise any slide whose script exceeds 120 seconds unless it is deliberately the central evidence slide.

## Build “main talk + backup” mode

Keep the main talk independently understandable. Append backup slides only after the main summary.

Recommended structure:

1. Main summary or take-home slide
2. “备用页 / Backup” divider
3. Backup slides grouped by likely question

Mark every backup slide in notes:

```text
【备用页】
【讲稿】
【建议时长】60秒
<answer to the anticipated question>

[Sources]
- <source>
```

The audit script excludes these pages from the main-talk duration.

## Choose useful backup content

Prefer backup slides that answer predictable questions:

- complete experimental workflow or protocol conditions;
- controls, gating strategy, normalization, or statistical assumptions;
- full uncropped literature figure corresponding to a main-slide panel;
- alternative mechanisms or conflicting evidence;
- method-selection detail and troubleshooting;
- reagent, marker, probe, or database definitions;
- additional disease models, cell types, or boundary conditions;
- reference list or figure-source index.

Do not use backup slides as a dumping ground. Each page should answer one likely question and remain presentation-ready.

## Format backup slides

- Reuse the same template and typography.
- Add a small, consistent “备用 / Backup” label without changing the main visual identity.
- Preserve full citations and speaker notes.
- Use appendix numbering such as A1, A2 when the editing system supports it reliably; otherwise retain continuous numbering and a visible backup label.
- Do not reference a backup page as required evidence for a main-slide conclusion.

## Validate duration and backup mode

- The total suggested time of main slides is within ±20% of the target before rehearsal.
- No main slide exceeds two minutes without a deliberate reason.
- Backup pages are excluded from the main duration estimate.
- Every backup page has a clear anticipated question, notes, and sources.
- The main summary appears before the backup divider.
