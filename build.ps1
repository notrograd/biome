Write-Host "Installing Biome..."

try {
    $prefix = "$env:USERPROFILE\AppData\Local\Biome"
    python -m pip install -e . --prefix $prefix *> $null 2>&1

    $binPath = "$prefix\Scripts"
    $currentPath = [Environment]::GetEnvironmentVariable("PATH", "User")

    if (-not ($currentPath -like "*$binPath*")) {
        [Environment]::SetEnvironmentVariable("PATH", "$currentPath;$binPath", "User")
        Write-Host "Added '$binPath' to your user PATH."
    }

    Write-Host "Done. Open a new shell and run 'biome help'."
}
catch {
    Write-Error "Installation failed: $_"
}
