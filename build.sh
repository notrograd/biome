#!/usr/bin/bash

echo "Installing Biome..."

python3 src/setup.py > /dev/null 2>&1

echo "Done. Run biome help to see a list of available commands."
