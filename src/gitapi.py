# Copyright (c), 2025, Biome Build System.
# All source code in the Biome Build System is licensed under the BSD-2 Clause.
#
# gitapi.py
# Git compatibility API.
#
# author: notrograd
# version: 0.1.0
# date: 5-19-25

import git
import yml
import subprocess as sp
from pathlib import Path

try:
    dpath = Path(yml.Read("biome.project.source.dirs")[0])
except Exception as e:
    print(f"[biome] warning: failed to read source dirs: {e}")
    dpath = Path("pkg")

dpath.mkdir(parents=True, exist_ok=True)

try:
    manager = yml.Read("biome.manager")
except Exception:
    manager = None

try:
    dependencies = yml.Read("biome.dependencies")
except Exception:
    dependencies = []

try:
    repositories = yml.Read("biome.repositories")
except Exception:
    repositories = []

def pkg():
    if repositories:
        for repo in repositories:
            name = Path(repo).stem
            dest = dpath / name
            try:
                print(f"[biome] cloning {repo} -> {dest}")
                git.Repo.clone_from(f"https://{repo}", dest)
            except Exception as e:
                print(f"[biome] fatal: failed to clone {repo}: {e}")
        return

    if manager and dependencies:
        for dep in dependencies:
            com = f"{manager} {dep}"
            print(f"[biome] RUN: {com}")
            try:
                sp.run(com.split(), check=True)
            except Exception as e:
                print(f"[biome] failed to run: {com}: {e}")
        return

    print("[biome] no repositories or dependencies to process. Exit.")
