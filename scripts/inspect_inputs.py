#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Summarize possible lab-report input files in a folder."""
from __future__ import annotations

import argparse
from pathlib import Path


STANDARD_NAMES = {
    "实验任务书": "task",
    "实验所需文件": "related-files",
    "实验报告模板": "template",
    "成品实验报告": "sample",
    "实验相关课件": "course",
    "实验原始数据.md": "data",
    "个人信息.md": "personal-info",
    "评分标准.md": "rubric",
    "输出文件要求.md": "output-requirements",
    "目标写作风格.md": "writing-style",
}


ROLE_HINTS = {
    "output-requirements": ["输出", "命名", "文件格式", "destination", "format"],
    "personal-info": ["个人信息", "姓名", "学号", "班级"],
    "writing-style": ["写作风格", "语气", "style", "tone"],
    "task": ["任务", "实验指导", "assignment", "instruction", "manual"],
    "template": ["模板", "template", "空白", "报告格式"],
    "sample": ["成品", "样例", "范文", "sample", "finished"],
    "rubric": ["评分", "rubric", "标准"],
    "data": ["原始数据", "data", "数据", "result", "结果", "log", "日志"],
    "course": ["课件", "教材", "ppt", "chapter", "lecture"],
}


def guess_role(path: Path) -> str:
    if path.name in STANDARD_NAMES:
        return STANDARD_NAMES[path.name]
    for part in path.parts:
        if part in STANDARD_NAMES:
            return STANDARD_NAMES[part]
    name = path.name.lower()
    hits = []
    for role, keys in ROLE_HINTS.items():
        if any(key.lower() in name for key in keys):
            hits.append(role)
    if hits:
        return ",".join(hits)
    if path.suffix.lower() in {".csv", ".xlsx", ".xls", ".json", ".log", ".txt"}:
        return "data/notes"
    if path.suffix.lower() in {".docx", ".doc", ".pdf"}:
        return "document"
    if path.suffix.lower() in {".py", ".java", ".cpp", ".c", ".js", ".html", ".sql"}:
        return "related-code"
    if path.suffix.lower() in {".png", ".jpg", ".jpeg", ".bmp"}:
        return "image"
    return "related-file"


def is_empty_file(path: Path) -> bool:
    try:
        return path.stat().st_size == 0
    except FileNotFoundError:
        return True


def non_cache_files(root: Path) -> list[Path]:
    return [
        p for p in root.rglob("*")
        if p.is_file() and "__pycache__" not in p.parts
    ]


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("folder", help="Folder containing lab-report inputs")
    parser.add_argument("--max", type=int, default=200, help="Maximum files to list")
    args = parser.parse_args()

    root = Path(args.folder)
    if not root.exists():
        raise SystemExit(f"Folder not found: {root}")

    files = non_cache_files(root)
    dirs = [
        p for p in root.iterdir()
        if p.is_dir() and "__pycache__" not in p.parts
    ]
    print(f"Root: {root}")
    print(f"Files: {len(files)}")
    if dirs:
        print("Top-level folders:")
        for directory in dirs:
            child_files = non_cache_files(directory)
            status = "empty" if not child_files else f"{len(child_files)} file(s)"
            print(f"- {guess_role(directory)}\t{status}\t{directory.name}")
    print()
    for idx, path in enumerate(files[: args.max], 1):
        try:
            size = path.stat().st_size
        except FileNotFoundError:
            continue
        rel = path.relative_to(root)
        status = "empty-skip" if is_empty_file(path) else "read"
        print(f"{idx:03d}\t{guess_role(path)}\t{path.suffix or '(none)'}\t{size}\t{status}\t{rel}")
    if len(files) > args.max:
        print(f"... omitted {len(files) - args.max} files")


if __name__ == "__main__":
    main()
