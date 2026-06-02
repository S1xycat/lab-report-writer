#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Roughly compare two DOCX lab reports for over-similarity."""
from __future__ import annotations

import argparse
import json
import re
import zipfile
from collections import Counter
from difflib import SequenceMatcher
from pathlib import Path
from xml.etree import ElementTree as ET


NS = {"w": "http://schemas.openxmlformats.org/wordprocessingml/2006/main"}


def read_docx_xml(path: Path, name: str) -> ET.Element | None:
    try:
        with zipfile.ZipFile(path) as zf:
            return ET.fromstring(zf.read(name))
    except Exception:
        return None


def extract_text(path: Path) -> str:
    root = read_docx_xml(path, "word/document.xml")
    if root is None:
        return ""
    paragraphs: list[str] = []
    for para in root.findall(".//w:p", NS):
        parts = [node.text or "" for node in para.findall(".//w:t", NS)]
        text = "".join(parts).strip()
        if text:
            paragraphs.append(text)
    return "\n".join(paragraphs)


def count_elements(path: Path) -> dict[str, int]:
    root = read_docx_xml(path, "word/document.xml")
    if root is None:
        return {"tables": 0, "images": 0}
    tables = len(root.findall(".//w:tbl", NS))
    images = len(root.findall(".//{http://schemas.openxmlformats.org/drawingml/2006/main}blip"))
    return {"tables": tables, "images": images}


def normalize(text: str) -> str:
    text = re.sub(r"\s+", " ", text)
    text = re.sub(r"[，。；：、,.?:;!！“”\"'（）()\[\]【】]", " ", text)
    return re.sub(r"\s+", " ", text).strip().lower()


def lines(text: str) -> list[str]:
    return [normalize(line) for line in text.splitlines() if len(normalize(line)) >= 12]


def ngrams(text: str, size: int = 18) -> Counter[str]:
    cleaned = normalize(text)
    if len(cleaned) <= size:
        return Counter()
    return Counter(cleaned[i : i + size] for i in range(0, len(cleaned) - size + 1))


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("sample_docx")
    parser.add_argument("generated_docx")
    parser.add_argument("--json", action="store_true")
    args = parser.parse_args()

    sample = Path(args.sample_docx)
    generated = Path(args.generated_docx)
    sample_text = extract_text(sample)
    generated_text = extract_text(generated)
    sample_lines = set(lines(sample_text))
    generated_lines = set(lines(generated_text))
    shared_lines = sorted(sample_lines & generated_lines, key=len, reverse=True)

    sample_ngrams = ngrams(sample_text)
    generated_ngrams = ngrams(generated_text)
    shared_ngrams = sum((sample_ngrams & generated_ngrams).values())
    total_ngrams = max(1, min(sum(sample_ngrams.values()), sum(generated_ngrams.values())))

    sequence_ratio = SequenceMatcher(None, normalize(sample_text), normalize(generated_text)).ratio()
    line_ratio = len(shared_lines) / max(1, min(len(sample_lines), len(generated_lines)))
    ngram_ratio = shared_ngrams / total_ngrams
    elements_sample = count_elements(sample)
    elements_generated = count_elements(generated)
    matching_counts = elements_sample == elements_generated

    revise = sequence_ratio >= 0.45 or line_ratio >= 0.25 or ngram_ratio >= 0.35
    result = {
        "sample": str(sample),
        "generated": str(generated),
        "sequence_ratio": round(sequence_ratio, 3),
        "shared_line_ratio": round(line_ratio, 3),
        "shared_ngram_ratio": round(ngram_ratio, 3),
        "shared_distinctive_lines": shared_lines[:10],
        "sample_counts": elements_sample,
        "generated_counts": elements_generated,
        "matching_table_image_counts": matching_counts,
        "revision_recommended": revise,
    }

    if args.json:
        print(json.dumps(result, ensure_ascii=False, indent=2))
    else:
        for key, value in result.items():
            print(f"{key}: {value}")


if __name__ == "__main__":
    main()
