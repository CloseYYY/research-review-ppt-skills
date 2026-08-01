# Life-science domain extensions

Load only the sections relevant to the deck.

## Contents

1. Molecular and cell biology
2. Immunology and flow cytometry
3. Omics and bioinformatics
4. Structural biology and biophysics
5. Pharmacology and drug discovery
6. Neuroscience, pathology, and imaging
7. Cross-domain rules

## 1. Molecular and cell biology

### Evidence priorities

- Separate expression, localization, interaction, modification, activity, and phenotype.
- Require perturbation and rescue before presenting a protein as causally necessary and sufficient.
- Distinguish colocalization from direct interaction and compartment proximity from lumenal localization.
- Treat stress-response markers as responses unless structural or functional evidence identifies the initiating lesion.

### Preferred visuals

- simplified pathway or compartment schematic;
- representative microscopy with scale bar and channel labels;
- biochemical fractionation or interaction workflow;
- evidence-layer table linking assay to conclusion.

### Common controls

- loading and fraction-purity controls;
- tagged-protein expression and localization controls;
- knockdown/knockout efficiency and rescue expression;
- antibody specificity, secondary-only, and isotype controls when relevant;
- cell viability and stress induced by the assay itself.

### Common errors

- using mRNA abundance as a direct proxy for protein activity;
- interpreting co-immunoprecipitation as direct physical binding;
- equating puncta with aggregates without biochemical or conformational validation;
- showing a pathway diagram that implies causality not tested in the cited study.

## 2. Immunology and flow cytometry

### Evidence priorities

- Define species, tissue, stimulation, time point, and cell population before discussing phenotype.
- Distinguish frequency, absolute count, marker intensity, function, and lineage identity.
- State the gating hierarchy and exclusion gates for viability, doublets, and unwanted lineages.
- Treat marker combinations as operational definitions; acknowledge context-dependent expression.

### Preferred visuals

- compact gating tree or representative sequential plots;
- cytokine or functional-response comparison with biological replicates;
- tissue–cell–state hierarchy;
- marker table including positive, negative, and functional markers.

### Common controls

- fluorescence-minus-one controls where gating requires them;
- single-stain compensation controls and autofluorescence assessment;
- unstimulated, vehicle, positive stimulation, and viability controls;
- batch-bridging samples for longitudinal acquisition;
- biological replicate and donor/animal-level statistics.

### Common errors

- reporting only percentages when total cell numbers change;
- comparing median fluorescence intensity across batches without bridging or normalization;
- treating one activation marker as a complete functional state;
- omitting the parent population or gating denominator.

## 3. Omics and bioinformatics

### Evidence priorities

- State cohort, experimental unit, replicate structure, preprocessing, normalization, and statistical model.
- Distinguish exploratory discovery from confirmatory validation.
- Separate effect size from statistical significance and pathway enrichment from pathway activation.
- Identify whether analysis is bulk, single-cell, spatial, targeted, or untargeted.

### Preferred visuals

- analysis workflow with inputs, filters, and outputs;
- quality-control summary before biological interpretation;
- volcano or effect-size plot with thresholds defined;
- heatmap with sample annotation and scale meaning;
- enrichment plot with database, background universe, and multiple-testing method;
- single-cell embedding paired with quantitative composition or expression summaries.

### Common controls

- batch, library size, mapping/identification rate, missingness, and outlier assessment;
- false-discovery-rate correction;
- independent cohort or targeted assay validation;
- cell-composition or covariate adjustment when relevant;
- data and code accession for published cases.

### Common errors

- interpreting an embedding distance as a formal biological distance;
- using pathway enrichment alone as proof of pathway activity;
- showing only selected genes without the selection rule;
- treating technical replicates as independent biological replicates;
- omitting the denominator used for percentages or enrichment.

## 4. Structural biology and biophysics

### Evidence priorities

- Define sample purity, construct boundaries, oligomeric state, buffer, concentration, and temperature.
- Separate resolution, precision, model fit, conformational heterogeneity, and biological relevance.
- Pair structural observations with biochemical or functional validation when making mechanistic claims.
- Distinguish native complexes from assemblies promoted by purification or concentration.

### Preferred visuals

- structure overview plus one annotated interface or conformational change;
- method-specific validation metric such as map–model fit, class distribution, or residuals;
- orthogonal biophysical comparison of size, secondary structure, or binding;
- simple state-transition diagram grounded in measured conformations.

### Common controls

- monodispersity and aggregation assessment;
- concentration dependence and buffer sensitivity;
- negative controls for binding or assembly;
- replicate preparations and orthogonal methods;
- mutation or functional assay testing the proposed interface.

### Common errors

- interpreting a static structure as the only physiological state;
- hiding low-resolution or poorly supported regions;
- comparing structures without alignment and domain-boundary context;
- treating docking or prediction confidence as experimental validation.

## 5. Pharmacology and drug discovery

### Evidence priorities

- Separate biochemical potency, cellular potency, target engagement, selectivity, exposure, efficacy, and toxicity.
- State concentration, exposure time, vehicle, assay window, and biological system.
- Prefer concentration–response relationships and effect sizes over single-dose comparisons.
- Distinguish on-target mechanism from phenotypic correlation.

### Preferred visuals

- target–assay–cell–animal evidence funnel;
- concentration–response curve with replicate and fitting information;
- selectivity or off-target comparison;
- pharmacokinetic–pharmacodynamic relationship;
- efficacy and tolerability shown together when relevant.

### Common controls

- vehicle, inactive analog, positive control, and orthogonal chemistry;
- direct target-engagement assay;
- rescue or resistance mutation where feasible;
- cytotoxicity and assay-interference checks;
- exposure confirmation in the tested compartment.

### Common errors

- calling a compound selective from one comparator;
- equating cellular phenotype with target engagement;
- comparing half-maximal values from incompatible assay conditions;
- presenting animal efficacy without exposure or tolerability context.

## 6. Neuroscience, pathology, and imaging

### Evidence priorities

- Define anatomical region, cell type, disease stage, imaging modality, and sampling unit.
- Distinguish representative fields, section-level summaries, animal-level summaries, and longitudinal measurements.
- Separate structural pathology, molecular marker changes, circuit activity, and behavior.
- Account for spatial heterogeneity and blinded quantification.

### Preferred visuals

- anatomy overview followed by a clearly located region of interest;
- representative image paired with animal-level quantification;
- time course linking molecular, pathological, and behavioral stages;
- segmentation or image-analysis workflow with thresholds disclosed.

### Common controls

- scale bars, acquisition settings, background subtraction, and batch controls;
- blinded region selection and analysis;
- multiple animals with nested or mixed-effects statistics when fields are subsamples;
- antibody or tracer specificity;
- motion, bleaching, and phototoxicity controls for live imaging.

### Common errors

- treating fields of view as independent animals;
- choosing only visually dramatic regions;
- inferring neuronal activity from an indirect marker without temporal context;
- mixing human pathology stages or animal ages without explicit stratification.

## 7. Cross-domain rules

- Use the biological replicate as the statistical unit unless the cited design justifies otherwise.
- Show representative data and quantitative summaries together when possible.
- State normalization denominators, thresholds, and exclusion rules.
- Preserve uncertainty, negative results, and context dependence.
- Use official gene/protein nomenclature for the relevant species.
- Keep domain-specific details in backup slides when they interrupt the main review narrative but are likely to arise in questions.
