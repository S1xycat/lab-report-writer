# Differentiation

Use this reference when generating multiple reports or creating a new report from a finished sample.

Default stance: a finished sample report is a quality reference, not a source draft. The new report should satisfy the same assignment while having its own evidence backbone, data, organization choices, and analysis path.

## Sample Firewall

When a finished sample is provided:

- Read it once for required coverage and teacher expectations.
- Extract only a compact style/coverage profile.
- Close the sample mentally before drafting the new report.
- Draft from the task book, template, related files, generated data, and the difference plan.
- Use the official template, not the sample report, as the formatting authority when both exist.

## Preserve

- Required template structure.
- Required experiment objectives.
- Correct domain concepts.
- Valid formulas and methods.
- Real user-provided data unless the user asks for variants.
- School-required cover layout, headings, and submission rules from the template/task book.

## Vary

- Evidence backbone: selected examples, test cases, trials, screenshots, datasets, or scenario framing.
- Section wording and sentence order.
- Example inputs and test cases.
- Table row ordering when order is not required.
- Table grouping, table titles, and figure placement when the template does not dictate them.
- Analysis angle.
- Conclusion emphasis.
- Chart captions.
- Simulated data values within plausible ranges.
- Screenshot placeholders and figure captions.
- Paragraph length, transition style, and discussion order.

## Do Not Copy

- Sample report personal information.
- Sample report exact paragraphs.
- Sample report unique data unless user says it is shared source data.
- Screenshots from a sample report unless user says they are reusable.
- Sample report table order, chart order, example sequence, or conclusion structure when they are not required by the task/template.
- Sample report distinctive formatting choices when a separate template is provided.

## Single-Report Strategy

Even for one generated report, define a short variant profile:

- Report stance: process-oriented, result-oriented, error-analysis-oriented, application-oriented, or comparison-oriented.
- Data profile: normal-case-heavy, boundary-case-heavy, noisy-but-stable, improved-after-adjustment, or mixed.
- Evidence choices: different cases, screenshots, charts, or logs from the sample.
- Analysis emphasis: correctness, stability, efficiency, usability, limitations, or improvement.
- Conclusion emphasis: what was verified, what issue was found, or what improvement was achieved.

Use this profile before writing. The finished report should not look like the sample with synonyms swapped in.

## Multi-Version Strategy

For each version, define a short variant profile:

- Variant name or letter.
- Writing style: concise, detailed, process-oriented, analysis-oriented.
- Evidence mode.
- Data profile: low-noise, medium-noise, edge-case-heavy, normal-case-heavy.
- Result emphasis: accuracy, efficiency, stability, error analysis, usability.

Then vary:

- Experimental data or test cases.
- Observed result tables.
- Error analysis.
- Conclusion wording.
- Figure captions and table names.

Keep all variants internally consistent.

## Similarity Reduction Checklist

Before delivery, compare against the sample report or previous variants:

- Opening purpose paragraph is rewritten.
- Tables are not identical unless required by the task.
- Analysis contains different phrasing and emphasis.
- Conclusions mention different observations.
- Simulated data uses different but plausible values.
- File names and required section titles follow template but content differs.
- Non-required section ordering, table order, figure placement, and example sequence differ where practical.
- If DOCX samples are available, run `scripts/compare_docx_similarity.py` and revise when it recommends revision.
