# Standard Input Folder

When the user provides a folder path, first check whether it uses this standard layout:

- `实验任务书`: assignment instructions, lab manuals, requirements.
- `实验所需文件`: code, datasets, projects, SQL, models, exported logs, required assets.
- `实验报告模板`: blank or partially filled report templates.
- `成品实验报告`: finished examples used only for structure, detail level, and style.
- `实验相关课件`: slides, textbook chapters, lecture notes, reference material.
- `实验原始数据.md`: raw measured data, copied result tables, logs, notes.
- `个人信息.md`: cover-page fields.
- `评分标准.md`: rubric, checklist, scoring rules.
- `输出文件要求.md`: format, naming rules, destination folder, version count.
- `目标写作风格.md`: tone, length, similarity target, special wording preference.

## Reading Rules

- Treat this folder as the primary input manifest.
- Read non-empty files and non-empty role folders.
- Skip empty `.md` files and empty folders silently.
- Do not ask the user to fill blank optional files.
- If `实验原始数据.md` is empty and there are no raw data files under `实验所需文件`, generate plausible simulated data by default.
- If screenshots are required, inspect `实验所需文件`, `实验任务书`, and `成品实验报告` before using placeholders. For software/computing screenshots, run `scripts/probe_runtime.py` and attempt a minimal reproduction path when practical. Empty screenshot inputs do not automatically mean placeholder; runnable files may be enough to generate screenshots.
- If `实验报告模板` contains multiple templates, choose the most specific one for the requested experiment; otherwise ask one concise question only if the choice changes the output materially.
- If `成品实验报告` contains examples, use them for structure and density only. Do not copy their data, screenshots, personal details, or distinctive wording.
- If `输出文件要求.md` is empty, default to DOCX in the user's requested or nearby output folder.

## Suggested Folder Check

Run:

```powershell
$env:PYTHONUTF8='1'; python scripts/inspect_inputs.py "<folder>"
```

Use the resulting role summary to decide which files to read first.
