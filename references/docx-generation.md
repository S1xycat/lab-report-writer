# DOCX Chinese Generation

Use this reference before generating any DOCX that contains Chinese text.

## Font Rule

For Chinese DOCX output, never rely only on `run.font.name`. In Word, Chinese fonts use the `w:eastAsia` attribute. Every run that contains report text must set all relevant font slots:

- `w:ascii`
- `w:hAnsi`
- `w:eastAsia`
- `w:cs`

Use a helper and call it for every run, including headings, table cells, captions, headers, footers, text boxes when accessible, and code blocks.

```python
from docx.oxml.ns import qn
from docx.shared import Pt


def set_run_font(run, name="宋体", size=10.5, bold=None):
    run.font.name = name
    run.font.size = Pt(size)
    if bold is not None:
        run.bold = bold
    r_fonts = run._element.rPr.rFonts
    r_fonts.set(qn("w:ascii"), name)
    r_fonts.set(qn("w:hAnsi"), name)
    r_fonts.set(qn("w:eastAsia"), name)
    r_fonts.set(qn("w:cs"), name)
```

If `run._element.rPr` or `rFonts` is absent, create or access it before setting attributes:

```python
r_pr = run._element.get_or_add_rPr()
r_fonts = r_pr.get_or_add_rFonts()
```

## Recommended Font System

- Cover title / first-level headings: `黑体`, bold if appropriate.
- Body text: `宋体`.
- Table text: `宋体`.
- Figure and table captions: `宋体`.
- Code: `Consolas` for ASCII code; use `宋体` or a mixed-font helper if Chinese comments appear.
- Common body size: 10.5 pt or the template's existing body size.

When a template is provided, inspect its styles and match the visible size/layout, but still set `w:eastAsia` explicitly on generated runs.

## Common Traps

- `document.styles["Normal"].font.name = "宋体"` does not reliably fix every generated run.
- `add_run()` may not inherit East Asian font settings from the paragraph style.
- Table cell paragraphs and runs need the same explicit font handling.
- Reusing sample/template styles can still produce mixed fonts if newly added runs lack `w:eastAsia`.
- Setting only paragraph style is not enough for runs created after the style change.

## Validation

After generating the DOCX, run:

```powershell
python scripts/check_docx_fonts.py path\to\report.docx
```

If missing East Asian fonts or unexpected font families are reported, fix the generator and regenerate the report instead of manually patching only a few paragraphs.
