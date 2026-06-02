#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Probe local runtimes useful for reproducing lab screenshots/artifacts."""
from __future__ import annotations

import importlib.util
import json
import shutil
import subprocess
import sys


PY_MODULES = [
    "playwright",
    "selenium",
    "flask",
    "django",
    "fastapi",
    "uvicorn",
    "pandas",
    "numpy",
    "matplotlib",
    "pytest",
    "jupyter",
    "notebook",
]

COMMANDS = [
    "python",
    "py",
    "node",
    "npm",
    "java",
    "javac",
    "mvn",
    "gradle",
    "mysql",
    "sqlite3",
    "git",
]


def command_version(command: str) -> str | None:
    path = shutil.which(command)
    if not path:
        return None
    for args in ([command, "--version"], [command, "-version"], [command, "-v"]):
        try:
            proc = subprocess.run(args, capture_output=True, text=True, timeout=5)
        except Exception:
            continue
        text = (proc.stdout or proc.stderr).strip().splitlines()
        if text:
            return text[0][:160]
    return path


def main() -> None:
    modules = {name: importlib.util.find_spec(name) is not None for name in PY_MODULES}
    commands = {name: command_version(name) for name in COMMANDS}
    result = {
        "python": sys.executable,
        "python_version": sys.version.split()[0],
        "python_modules": modules,
        "commands": commands,
        "screenshot_hints": [],
    }
    if modules.get("playwright") or modules.get("selenium"):
        result["screenshot_hints"].append("browser automation available")
    if modules.get("flask") or modules.get("fastapi") or modules.get("django"):
        result["screenshot_hints"].append("python web app runtime available")
    if commands.get("node") and commands.get("npm"):
        result["screenshot_hints"].append("node/npm web project runtime available")
    if commands.get("java") or commands.get("javac"):
        result["screenshot_hints"].append("java runtime/tooling available")
    print(json.dumps(result, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
