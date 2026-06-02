# Workflow

## 1. Input Inventory

Classify files into these roles:

- Standard input folder: role-named folders/files such as `实验任务书`, `实验所需文件`, `实验报告模板`, `成品实验报告`, `实验相关课件`, `实验原始数据.md`, `个人信息.md`, `评分标准.md`, `输出文件要求.md`, and `目标写作风格.md`.
- Task book: assignment instructions, experiment requirements, lab manual.
- Related files: code, datasets, project folders, SQL, models, exported logs, course files.
- Template: empty or partially filled report format.
- Sample report: finished report used for structure and detail level.
- Raw data: CSV, Excel, logs, result tables, screenshots, measurements.
- Course materials: slides, textbook chapters, PDFs.
- Rubric: scoring standard or checklist.

For a standard input folder:

- Read non-empty role folders and non-empty `.md` files.
- Skip empty role folders and zero-byte `.md` files without asking.
- Treat `实验原始数据.md` as optional. If it is empty and no raw data files are present, generate simulated data by default.

If no task book exists, infer the experiment topic from filenames and ask one concise question if the goal is still unclear.

## 2. Requirement Extraction

Extract:

- Experiment title.
- Objectives.
- Required principles or background.
- Required tools, files, or datasets.
- Required procedure.
- Required outputs: tables, figures, screenshots, formulas, answers, logs, code snippets.
- Required analysis and conclusion.
- Submission format and naming.

Build a section checklist before writing.

## 3. Template Extraction

When a template is provided:

- Preserve cover fields and heading order.
- Preserve table style where practical.
- Preserve page margins, font family, and heading hierarchy if detectable.
- Keep placeholders for unknown personal fields.

When no template is provided, use a standard structure:

1. Cover
2. Experiment Purpose
3. Experiment Principle
4. Experiment Environment or Materials
5. Experiment Procedure
6. Experiment Results
7. Analysis
8. Conclusion
9. Appendix if needed

Do not require detailed environment information from the user. Infer generic environment when needed.

## 4. Sample Report Use

Use a finished sample report to learn:

- Section order.
- Expected detail level.
- Table and figure placement.
- Tone.
- Common conclusion style.

Treat the sample as a weak reference, not a draft to rewrite. If a separate report template exists, the template controls formatting and the sample controls only expected completeness.

Before drafting from a sample, write a difference plan:

- New evidence backbone: what data, cases, screenshots, or examples will be different.
- New analysis angle: what result pattern or problem focus will be emphasized.
- New structure choices: where table order, subsection grouping, or figure placement can differ without violating the task/template.
- New conclusion path: which observations will support the conclusion.

Do not reuse sample wording, data, screenshots, personal details, table order, paragraph sequence, or distinctive layout choices unless the user explicitly says to reuse them.

## 5. Evidence Plan

Before drafting, decide for each required result:

- Real user data available.
- Simulated data needed because real user data is absent.
- Local reproduction or public sources useful for calibration, formulas, or screenshots.
- Screenshot can be produced from existing images, runnable files, generated outputs, or a minimal equivalent local reproduction.
- Placeholder needed.

Keep the final report internally consistent: tables, analysis, and conclusion must agree.

For screenshot requirements, read `screenshot-reproduction.md` and complete the reproduction check before placing any screenshot placeholder.

For software/computing experiments, run `scripts/probe_runtime.py` before deciding that an environment cannot be built. If usable tooling exists, attempt a minimal reproduction path.

## 6. Report Generation

Generate report content in this order:

1. Cover and metadata.
2. Purpose and principle.
3. Method/procedure.
4. Results, tables, figures, generated screenshots, or screenshot placeholders only when reproduction is not practical.
5. Analysis tied to results.
6. Conclusion tied to purpose and observed outcomes.
7. References or appendix when needed.

Use concise student-style language unless the user requests a formal technical tone.

For Chinese DOCX output, read `docx-generation.md` and apply explicit East Asian font settings to every generated run.

## 7. Delivery

Return:

- Output path.
- Evidence mode used, noted outside the report body unless the user requests otherwise.
- Missing placeholders.
- Validation summary.
