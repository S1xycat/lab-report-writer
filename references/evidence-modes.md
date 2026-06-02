# Evidence Modes

Use real user-provided data when present. If real data is absent, generate plausible simulated data by default; use local reproduction or public sources only when helpful for calibration, context, formulas, or screenshots.

## Mode 1: User-Provided Real Data

Use when raw data, logs, screenshots, code output, measurements, or result tables are provided.

Rules:

- Preserve original values.
- Clean formatting but do not silently change results.
- If values are inconsistent, flag the inconsistency before final delivery.

## Mode 2: Agent Local Reproduction

Use when the experiment can be run locally and doing so helps calibrate results, understand the process, or create screenshots/artifacts:

- Programming experiments.
- Software testing.
- Database experiments.
- Data analysis.
- Algorithm experiments.
- Simulation experiments.
- Web or automation experiments.

Actions:

- Build or run the experiment.
- Save logs, screenshots, generated data, and commands.
- Use generated artifacts as report evidence or calibration material.
- Mention in the final response or sidecar notes that data came from local reproduction when useful.
- Do not label values inside the finished report body as locally reproduced unless requested.

## Mode 3: Public Sources

Use when local reproduction is impractical but public data or authoritative references help calibrate values, formulas, or background.

Actions:

- Browse or inspect official/public sources when current or precise source attribution matters.
- Cite sources in the final response or sidecar notes.
- Include citations in the report only when the task, template, or user asks for them.
- Do not invent citations.

Use for:

- Public datasets.
- Standard algorithm examples.
- Public benchmark results.
- Official tool documentation.

## Mode 4: Simulated Data

Use when real user-provided data is absent. This is the default missing-data mode.

Rules:

- Generate plausible data according to experiment principles.
- Include realistic noise, units, and rounding.
- Avoid perfect linearity unless the experiment is theoretical.
- Avoid contradictions between raw data, charts, and conclusions.
- Preserve provenance outside the report body: simulated data should not be described as the user's personal measurements.
- In the finished report body, present generated values as normal result tables and analysis. Do not insert labels such as `模拟数据`, `示例数据`, `推断数据`, or `公开来源数据` by default.
- Avoid explicit personal claims such as `本人实测` unless the user provided actual measured data.

Optional outside-report wording:

- `报告正文已按普通实验数据呈现；数据生成方式已在工作说明中记录。`
- `报告中未额外标注数据来源标签，如需可另附生成依据说明。`

## Mode 5: Placeholders

Use when evidence is required but unavailable and should not be simulated.

Common placeholders:

- `【此处插入实验运行截图】`
- `【此处填写实测数据】`
- `【此处补充实验设备照片】`
- `【此处填写姓名/学号/班级】`

Default screenshot behavior:

- Do not ask for process screenshots or videos.
- For software/computing screenshots, run `scripts/probe_runtime.py` and attempt a minimal reproduction path when practical.
- Insert placeholders only if screenshots are required and cannot be locally reproduced after the reproduction check.
