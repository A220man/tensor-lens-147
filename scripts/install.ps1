# install.ps1 - PowerShell installation script
# Fixed: em-dashes replaced with ASCII dashes for PowerShell 5.1 UTF-8 compatibility

# Install scripts to user profile
$ScriptsDir = Join-Path $env:USERPROFILE ".claude" "scripts"
if (-not (Test-Path $ScriptsDir)) {
    New-Item -ItemType Directory -Path $ScriptsDir -Force | Out-Null
}

# Copy hunt.ps1
$HuntSource = Join-Path "$PSScriptRoot" "hunt.ps1"
$HuntTarget = Join-Path $ScriptsDir "hunt.ps1"
if (Test-Path $HuntSource) {
    Copy-Item -Path $HuntSource -Destination $HuntTarget -Force
    Write-Host "Installed hunt.ps1 to $HuntTarget"
} else {
    Write-Host "WARNING: hunt.ps1 not found at $HuntSource"
}

# Copy install.ps1 (self-referential - this is the installer)
$InstallTarget = Join-Path $ScriptsDir "install.ps1"
if (Test-Path $HuntSource -and $HuntSource -ne $InstallTarget) {
    Copy-Item -Path $HuntSource -Destination $InstallTarget -Force
}

# Create default config
$ConfigDir = Join-Path $env:USERPROFILE ".claude"
if (-not (Test-Path $ConfigDir)) {
    New-Item -ItemType Directory -Path $ConfigDir -Force | Out-Null
}

Write-Host "install.ps1 complete. Run 'hunt <target>' to scaffold an engagement."
