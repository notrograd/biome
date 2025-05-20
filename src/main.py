# Copyright (c), 2025, Biome Build System.
# All source code in the Biome Build System is licensed under the BSD-2 Clause.
#
# main.py
# Main file. Command line arguments, groups everything together. About as much as you'd expect.
#
# author: notrograd
# version: 0.1.0
# date: 5-19-25

import sys
from gitapi import pkg

def main():
    if len(sys.argv) < 2:
        print("Usage: biome <command>")
        return

    cmd = sys.argv[1]

    if cmd == "help":
        print("biome build    - Clone / install dependencies")
        print("biome help     - Show this help message")
    elif cmd == "build":
        pkg()
    else:
        print(f"Unknown command: {cmd}")

