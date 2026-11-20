# hunt.ps1 - PowerShell hunting script
# Fixed: em-dashes replaced with ASCII dashes for PowerShell 5.1 UTF-8 compatibility

function hunt {
    param(
        [string]$Target = ''
    )

    if ([string]::IsNullOrWhiteSpace($Target)) {
        Write-Host "Usage: hunt <target>"
        return 1
    }

    # Create engagement folder
    $EngagementDir = Join-Path $env:USERPROFILE "claude" "engagements" $Target
    if (-not (Test-Path $EngagementDir)) {
        New-Item -ItemType Directory -Path $EngagementDir -Force | Out-Null
    }

    # Scaffold findings README
    $ReadmePath = Join-Path $EngagementDir "findings/README.md"
    if (-not (Test-Path $ReadmePath)) {
        $null = New-Item -ItemType File -Path $ReadmePath -Force
        "# Findings" | Out-File -FilePath $ReadmePath -Encoding UTF8
        "Target: $Target" | Out-File -FilePath $ReadmePath -Append -Encoding UTF8
    }

    # Initialize findings log
    $FindingsPath = Join-Path $EngagementDir "findings.log"
    "# Engagement started: $Target" | Out-File -FilePath $FindingsPath -Encoding UTF8

    Write-Host "Engagement scaffolded for: $Target"
    return 0
}

# Alias for quick access
Set-Alias hk hunt
