Write-Host "Installing Biome..."

try {
    python -m pip install -e . *> $null 2>&1
    Write-Host "Done. Run 'biome help' to see a list of available commands."
}
catch {
    Write-Error "Installation failed: $_"
}
