# Results deck workflow

## Classify slides

Use exactly one primary type per slide:

| Type | Purpose | Required visible fields |
|---|---|---|
| 封面 | Identify project and meeting | Title, presenter, date when supplied |
| 背景页 | Explain established public knowledge | One public question or model, sources |
| 研究问题 | State the current experimental question | Question, rationale, decision to be made |
| 结果页 | Present one evidence unit | 实验目的, 实验方法, 实验结果, 一句话结论 |
| 阶段总结 | Synthesize a result module | Supported findings, limitations |
| 未来计划 | Define next experiments | Priority, experiment, criterion, fallback |
| 备用页 | Answer a likely supervisor question | Question answered, supporting detail |
| 其他 | Administrative content | One clear communication job |

Write the selected type in notes as `【页面类型】<type>`.

## Create a result record

For every result unit, record internally:

| Field | Content |
|---|---|
| Purpose | Biological question and decision |
| Model | Species, cell/tissue, genotype, state |
| Design | Groups, controls, randomization/blinding when relevant |
| Conditions | Dose, time, temperature, buffer, oxygen, passage, instrument settings, or other decisive variables |
| Method | Assay and direct readout |
| Replication | Biological `n`, technical repeats, batch structure |
| Statistics | Unit of analysis, summary, test, multiple-testing rule |
| Result | Direct observation including negative data and uncertainty |
| Conclusion | One sentence at the supported evidence level |
| Boundary | What is not demonstrated |
| Next step | Discriminating experiment and decision criterion |

Do not create the result slide until required missing fields have passed through the consolidated checklist.

## Structure result modules

Use this sequence when evidence permits: research question → design and controls → primary result → orthogonal validation → module summary → immediate next experiment.

Combine design with the result slide when the method is familiar and conditions fit legibly. Split it into a dedicated design slide when the controls or sampling hierarchy determine interpretation.

## Calibrate conclusions

- Use `显示` for direct observation.
- Use `与……相关` or `伴随` for association.
- Use `支持……参与` when perturbation provides functional support.
- Require adequate perturbation, controls, temporal order, and preferably rescue or orthogonal evidence for causality.
- Use `提示` and state the missing confirmation for preliminary evidence.

Never promote a representative image, one batch, technical repeats, colocalization, pathway enrichment, or a marker change into a causal mechanism.

## Plan future experiments

After each result module, propose only experiments that answer a live uncertainty. Rank the final roadmap:

| Priority | Experiment | Decision criterion | Fallback |
|---|---|---|---|
| P0 | Resolve validity or essential control | What result permits interpretation | Alternative assay or redesign |
| P1 | Test the central working model | Result supporting or refuting it | Orthogonal perturbation/readout |
| P2 | Extend mechanism or generality | Replication across context | Narrow the claim or model scope |

State sample needs, controls, key conditions, readout, expected alternatives, and the decision enabled. Do not invent unavailable resources; mark cost, time, biosafety, model, or reagent constraints for user confirmation.

