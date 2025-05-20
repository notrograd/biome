#!/usr/bin/env bash

echo "Installing Biome..."

if [ -f ".venv/bin/activate" ]; then
    source .venv/bin/activate
fi

python3 -m pip install -e . > /dev/null 2>&1

echo "Done. Run 'biome help' to see a list of available commands."
