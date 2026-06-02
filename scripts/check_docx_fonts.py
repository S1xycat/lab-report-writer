#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Check generated DOCX runs for missing East Asian font settings."""
from __future__ import annotations

import argparse
import json
import re
import zipfile
from collections import Counter
from pathlib import Path
from xml.etree import ElementTree as ET


NS = {
    "w": "http://schemas.openxmlformats.org/wordprocessingml/2006/main",
}
CHINESE_RE = re.compile(r"[\u3400-\u9fff]")


def attr(element: ET.Element | None, name: str) -> str | None:
    if element is None:
        return None
    return element.attrib.get(f"{{{NS['w']}}}{name}")


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("docx")
    parser.add_argument("--json", action="store_true")
    args = parser.parse_args()

    path = Path(args.docx)
    with zipfile.ZipFile(path) as zf:
        root = ET.fromstring(zf.read("word/document.xml"))

    total_chinese_runs = 0
    missing_east_asia: list[str] = []
    east_asia_fonts: Counter[str] = Counter()
    ascii_fonts: Counter[str] = Counter()

    for run in root.findall(".//w:r", NS):
        text = "".join(node.text or "" for node in run.findall(".//w:t", NS))
        if not text or not CHINESE_RE.search(text):
            continue
        total_chinese_runs += 1
        r_fonts = run.find("./w:rPr/w:rFonts", NS)
        east_asia = attr(r_fonts, "eastAsia")
        ascii_font = attr(r_fonts, "ascii")
        if east_asia:
            east_asia_fonts[east_asia] += 1
        else:
            missing_east_asia.append(text[:80])
        if ascii_font:
            ascii_fonts[ascii_font] += 1

    result = {
        "docx": str(path),
        "chinese_runs": total_chinese_runs,
        "missing_east_asia_count": len(missing_east_asia),
        "east_asia_fonts": dict(east_asia_fonts),
        "ascii_fonts": dict(ascii_fonts),
        "examples_missing_east_asia": missing_east_asia[:10],
        "revision_recommended": bool(missing_east_asia) or len(east_asia_fonts) > 3,
    }

    if args.json:
        print(json.dumps(result, ensure_ascii=False, indent=2))
    else:
        for key, value in result.items():
            print(f"{key}: {value}")


if __name__ == "__main__":
    main()
