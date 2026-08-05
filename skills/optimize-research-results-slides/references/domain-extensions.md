# Life-science result extensions

Load only the sections relevant to the user's experiments.

## Molecular and cell biology

- Separate abundance, localization, interaction, modification, activity, and phenotype.
- Require loading, fraction-purity, antibody-specificity, knockdown/knockout efficiency, rescue-expression, and viability controls as applicable.
- Do not equate mRNA with protein activity, colocalization with direct interaction, co-IP with direct binding, or puncta with aggregates.
- Report species, cell line, passage/state, construct, dose, exposure time, collection time, lysis/fractionation conditions, and normalization when decisive.

## Immunology and flow cytometry

- State species, tissue, stimulation, time point, parent population, gating hierarchy, exclusion gates, and denominator.
- Distinguish frequency, absolute count, marker intensity, lineage identity, and function.
- Check single-stain compensation, fluorescence-minus-one, viability, doublet exclusion, unstimulated/vehicle, positive stimulation, and batch bridging as relevant.
- Do not report fields, wells, or technical repeats as independent animals or donors.

## Omics and bioinformatics

- State cohort, experimental unit, biological replicates, preprocessing, normalization, covariates, batch handling, statistical model, and multiple-testing correction.
- Separate exploratory discovery from confirmatory validation, effect size from significance, and enrichment from pathway activation.
- For single-cell or spatial work, report filtering, sample-level replication, integration, annotation basis, composition testing, and independent validation.
- Do not interpret embedding distance as a formal biological distance or technical replicates as biological replicates.

## Imaging, neuroscience, and pathology

- State anatomical region, cell type, disease stage, acquisition settings, scale, field/section/animal hierarchy, segmentation, threshold, and blinding.
- Pair representative images with biological-unit quantification.
- Check scale bars, background subtraction, batch controls, antibody/tracer specificity, motion, bleaching, and phototoxicity as relevant.
- Do not select only dramatic fields or treat fields as independent animals.

## Structural biology and biophysics

- State construct boundaries, purity, oligomeric state, buffer, concentration, temperature, replicate preparation, and validation metric.
- Separate resolution, precision, model fit, conformational heterogeneity, and biological relevance.
- Pair structural claims with biochemical or functional tests when claiming mechanism.
- Do not treat docking or prediction confidence as experimental validation.

## Pharmacology and drug discovery

- Separate biochemical potency, cellular potency, target engagement, selectivity, exposure, efficacy, and toxicity.
- State compound identity or alias, vehicle, concentration, exposure time, assay window, model, replicate structure, and curve-fitting method.
- Prefer concentration–response evidence over a single dose. Check inactive analog, orthogonal chemistry, target engagement, rescue/resistance, cytotoxicity, and assay interference where feasible.
- Do not infer on-target action from phenotype alone.

## Cross-domain statistical rules

- Use the biological replicate as the statistical unit unless the design justifies otherwise.
- Distinguish biological and technical replication explicitly.
- State denominator, normalization, exclusions, missing-data handling, test, sidedness when relevant, and uncertainty interval.
- Preserve exact `n`; do not replace it with the number of images, wells, cells, or technical runs.
- Show negative and inconsistent results when they affect the conclusion.

