# Copyright (c), 2025, Biome Build System.
# All source code in the Biome Build System is licensed under the BSD-2 Clause.
#
# yml.py
# YAML parsing.
#
# author: notrograd
# version: 0.1.0
# date: 5-19-25

import yaml
from pathlib import Path

CONFIG_PATH = Path("biome.yml")

def load_yaml():
    if not CONFIG_PATH.exists():
        raise FileNotFoundError(f"{CONFIG_PATH} does not exist")
    with CONFIG_PATH.open("r", encoding="utf-8") as file:
        return yaml.safe_load(file)

def Read(key: str):
    config = load_yaml()
    keys = key.split(".")
    current = config
    for k in keys:
        if isinstance(current, dict) and k in current:
            current = current[k]
        else:
            raise KeyError(f"Key '{key}' not found in biome.yml")
    return current
