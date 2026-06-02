# Screenshot Reproduction

When a report requires screenshots, do not immediately leave placeholders. First decide whether a screenshot can be produced from provided materials and local runtimes. Do not reject software/computing screenshots as "environment too complex" without a runtime probe.

## Mandatory Runtime Probe

For software, web, database, algorithm, UI, notebook, or testing experiments, run:

```powershell
python scripts/probe_runtime.py
```

Use the result before deciding what can be reproduced. If Playwright/Selenium/Flask/Node/Java/database tooling is available, attempt a minimal runnable path before using placeholders.

Examples of minimal paths:

- Flask/FastAPI/Django or static HTML: start a local app/page and screenshot it with browser automation.
- Selenium/Playwright tests: run or adapt the test to capture pass/fail screenshots.
- Python scripts/notebooks: generate chart/table/terminal output and screenshot/export it.
- Java/web projects: check for existing build files or simple runnable entry points before giving up.
- Database labs: run SQL in an available local database or render result tables as screenshot-like outputs.

## Check Order

1. Existing images: search related folders for `.png`, `.jpg`, `.jpeg`, `.bmp`, `.gif`, `.webp`.
2. Local runtime availability: run `scripts/probe_runtime.py` and inspect available Python modules and commands.
3. Runnable web/UI files: look for `index.html`, Flask/Django/FastAPI apps, React/Vue/Vite projects, Java web projects, Selenium/Playwright tests, or browser automation scripts.
4. Runnable scripts/notebooks: look for `.py`, `.ipynb`, `.java`, `.cpp`, `.c`, `.js`, `.sql`, shell scripts, or build files that generate visible outputs.
5. Generated outputs: logs, reports, charts, CSV/Excel outputs, console output that can be rendered into screenshot-like figures.
6. Sample report screenshots: use only to understand what kind of screenshot is expected. Do not reuse sample screenshots unless the user explicitly says they are reusable.

## Reproduce When Practical

- Prefer running the provided project or test suite in a temporary/local working directory.
- For web or UI experiments, start the app when practical and capture screenshots with browser automation or system screenshot tools.
- For simple UI assignments, create a minimal equivalent app from the task requirements and provided code, then screenshot that app when the original project is absent or incomplete.
- For algorithm/data experiments, generate charts, tables, terminal outputs, or notebook outputs and screenshot/export them.
- Timebox dependency setup, but make a concrete attempt when the probe shows likely available tooling. A small Flask/static HTML/Playwright path should be attempted before placeholder fallback.
- Save generated screenshots in a clear artifacts folder near the generated report.

## Use Placeholders Only When

- The required screenshot is a physical classroom, hardware, chemistry, biology, instrument, or field-process image that cannot be reproduced.
- Required software cannot run after reasonable dependency/file inspection and the screenshot cannot be approximated from provided materials.
- Runtime probing found no practical path, or a concrete minimal reproduction attempt failed.
- The screenshot would require private credentials, paid services, remote systems, or unavailable devices.
- The user explicitly asked to leave placeholders.

## Final Response

Mention which screenshots were generated and which placeholders remain. Keep this explanation outside the report body unless the user asks for a work log.
