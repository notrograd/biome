Write-Host "Installing Biome..."

try {
    # Run python silently, redirecting stdout and stderr to null
    & python src\setup.py *> $null 2>&1
    Write-Host "Done. Run biome help to see a list of available commands."
}
catch {
    Write-Error "Installation failed: $_"
}
