#!/usr/bin/env bash

echo "Installing Biome..."

prefix="$HOME/.local"
python3 -m pip install -e . --prefix "$prefix" > /dev/null 2>&1

binpath="$prefix/bin"

if ! grep -q "$binpath" <<< "$PATH"; then
    echo "export PATH=\"\$PATH:$binpath\"" >> "$HOME/.bashrc"
    echo "Added $binpath to PATH in .bashrc"
fi

echo "Done. Restart your shell and run 'biome help'."
