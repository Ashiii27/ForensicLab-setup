# ============================================================================
# DFIR Lab - Tool Verification Script
# ============================================================================
# Purpose: Verify all DFIR tools are installed correctly
# Author: Ashish Kumar
# Date: February 2026
# ============================================================================

[CmdletBinding()]
param(
    [Parameter(Mandatory=$false)]
    [switch]$Detailed,
    
    [Parameter(Mandatory=$false)]
    [switch]$ExportReport
)

# Banner
Write-Host @"
╔══════════════════════════════════════════════════════════════╗
║          DFIR Lab - Tool Verification Script                ║
║              Checking Installation Status...                ║
╚══════════════════════════════════════════════════════════════╝
"@ -ForegroundColor Cyan

# Initialize counters
$totalTools = 0
$installedTools = 0
$missingTools = 0

# Results array for export
$results = @()

# Tool definitions
$tools = @{
    "Core Forensic Tools" = @{
        "FTK Imager" = @{
            "Path" = "C:\Tools\FTK_Imager\FTK Imager.exe"
            "Description" = "Disk imaging and memory acquisition"
            "Critical" = $true
        }
        "KAPE" = @{
            "Path" = "C:\Tools\KAPE\kape.exe"
            "Description" = "Artifact collection and parsing"
            "Critical" = $true
        }
        "Autopsy" = @{
            "Path" = "C:\Program Files\Autopsy\bin\autopsy64.exe"
            "Description" = "Digital forensics platform"
            "Critical" = $false
        }
    }
    
    "Eric Zimmerman Tools" = @{
        "Timeline Explorer" = @{
            "Path" = "C:\Tools\ZimmermanTools\TimelineExplorer\TimelineExplorer.exe"
            "Description" = "Timeline analysis"
            "Critical" = $true
        }
        "Registry Explorer" = @{
            "Path" = "C:\Tools\ZimmermanTools\RegistryExplorer\RegistryExplorer.exe"
            "Description" = "Registry analysis"
            "Critical" = $true
        }
        "ShellBags Explorer" = @{
            "Path" = "C:\Tools\ZimmermanTools\ShellBagsExplorer\ShellBagsExplorer.exe"
            "Description" = "ShellBag analysis"
            "Critical" = $false
        }
        "PECmd" = @{
            "Path" = "C:\Tools\ZimmermanTools\PECmd.exe"
            "Description" = "Prefetch analysis"
            "Critical" = $true
        }
        "JLECmd" = @{
            "Path" = "C:\Tools\ZimmermanTools\JLECmd.exe"
            "Description" = "Jump list analysis"
            "Critical" = $true
        }
    }
    
    "Utilities" = @{
        "7-Zip" = @{
            "Path" = "C:\Program Files\7-Zip\7z.exe"
            "Description" = "File compression"
            "Critical" = $true
        }
        "Notepad++" = @{
            "Path" = "C:\Program Files\Notepad++\notepad++.exe"
            "Description" = "Advanced text editor"
            "Critical" = $true
        }
        "Visual Studio Code" = @{
            "Path" = "C:\Program Files\Microsoft VS Code\Code.exe"
            "Description" = "Code editor and IDE"
            "Critical" = $false
        }
        "Firefox" = @{
            "Path" = "C:\Program Files\Mozilla Firefox\firefox.exe"
            "Description" = "Web browser for investigations"
            "Critical" = $false
        }
    }
    
    "Sysinternals Suite" = @{
        "Process Explorer" = @{
            "Path" = "C:\Tools\Sysinternals\procexp64.exe"
            "Description" = "Process monitoring"
            "Critical" = $true
        }
        "Autoruns" = @{
            "Path" = "C:\Tools\Sysinternals\Autoruns64.exe"
            "Description" = "Startup program analysis"
            "Critical" = $true
        }
        "TCPView" = @{
            "Path" = "C:\Tools\Sysinternals\Tcpview.exe"
            "Description" = "Network connection monitoring"
            "Critical" = $false
        }
    }
    
    "Network Analysis" = @{
        "Wireshark" = @{
            "Path" = "C:\Program Files\Wireshark\Wireshark.exe"
            "Description" = "Network protocol analyzer"
            "Critical" = $false
        }
    }
}

# Function to check tool installation
function Test-ToolInstallation {
    param(
        [string]$ToolName,
        [string]$ToolPath,
        [string]$Description,
        [bool]$Critical
    )
    
    $totalTools++
    
    if (Test-Path $ToolPath) {
        $installedTools++
        $status = "✓ INSTALLED"
        $color = "Green"
        
        if ($Detailed) {
            $fileInfo = Get-Item $ToolPath
            $version = $fileInfo.VersionInfo.FileVersion
            if ($version) {
                $status = "$status (v$version)"
            }
        }
    }
    else {
        $missingTools++
        $status = "✗ NOT FOUND"
        $color = "Red"
    }
    
    $criticalText = if ($Critical) { "[CRITICAL]" } else { "" }
    
    Write-Host ("{0,-35} {1,-15} {2}" -f $ToolName, $criticalText, $status) -ForegroundColor $color
    
    if ($Detailed -and $Description) {
        Write-Host ("  └─ {0}" -f $Description) -ForegroundColor Gray
    }
    
    # Add to results
    $script:results += [PSCustomObject]@{
        ToolName = $ToolName
        Status = if (Test-Path $ToolPath) { "Installed" } else { "Missing" }
        Path = $ToolPath
        Critical = $Critical
        Description = $Description
    }
}

# Check each category
foreach ($category in $tools.Keys) {
    Write-Host "`n[$category]" -ForegroundColor Yellow
    Write-Host ("─" * 70) -ForegroundColor DarkGray
    
    foreach ($tool in $tools[$category].Keys) {
        $toolInfo = $tools[$category][$tool]
        Test-ToolInstallation -ToolName $tool `
                             -ToolPath $toolInfo.Path `
                             -Description $toolInfo.Description `
                             -Critical $toolInfo.Critical
    }
}

# Check WSL and Linux tools
Write-Host "`n[WSL & Linux Tools]" -ForegroundColor Yellow
Write-Host ("─" * 70) -ForegroundColor DarkGray

$wslInstalled = (wsl --list --quiet 2>$null) -ne $null
if ($wslInstalled) {
    Write-Host "WSL                                                ✓ INSTALLED" -ForegroundColor Green
    
    # Check specific Linux tools
    $linuxTools = @(
        @{Name="Volatility3"; Command="vol.py"; Critical=$true}
        @{Name="Plaso (log2timeline)"; Command="log2timeline.py"; Critical=$true}
        @{Name="Oletools"; Command="olevba"; Critical=$true}
        @{Name="Bulk Extractor"; Command="bulk_extractor"; Critical=$false}
    )
    
    foreach ($ltool in $linuxTools) {
        $checkCmd = "wsl which $($ltool.Command) 2>/dev/null"
        $result = Invoke-Expression $checkCmd
        
        if ($result) {
            Write-Host ("{0,-35} {1,-15} ✓ INSTALLED" -f $ltool.Name, $(if($ltool.Critical){"[CRITICAL]"}else{""})) -ForegroundColor Green
        }
        else {
            Write-Host ("{0,-35} {1,-15} ✗ NOT FOUND" -f $ltool.Name, $(if($ltool.Critical){"[CRITICAL]"}else{""})) -ForegroundColor Red
        }
    }
}
else {
    Write-Host "WSL                                                ✗ NOT FOUND" -ForegroundColor Red
}

# Summary
Write-Host "`n╔══════════════════════════════════════════════════════════════╗" -ForegroundColor Cyan
Write-Host "║                        SUMMARY                               ║" -ForegroundColor Cyan
Write-Host "╚══════════════════════════════════════════════════════════════╝" -ForegroundColor Cyan

$percentageInstalled = [math]::Round(($installedTools / $totalTools) * 100, 2)

Write-Host "`nTotal Tools Checked:    " -NoNewline
Write-Host $totalTools -ForegroundColor White
Write-Host "Tools Installed:        " -NoNewline
Write-Host $installedTools -ForegroundColor Green
Write-Host "Tools Missing:          " -NoNewline
Write-Host $missingTools -ForegroundColor Red
Write-Host "Installation Status:    " -NoNewline
Write-Host "$percentageInstalled%" -ForegroundColor $(if($percentageInstalled -ge 90){"Green"}elseif($percentageInstalled -ge 70){"Yellow"}else{"Red"})

# Recommendations
if ($missingTools -gt 0) {
    Write-Host "`n⚠ RECOMMENDATIONS:" -ForegroundColor Yellow
    Write-Host "  → Review installation steps in README.md"
    Write-Host "  → Install missing CRITICAL tools first"
    Write-Host "  → Run this script again after installation"
}
else {
    Write-Host "`n✓ All tools successfully installed! Lab is ready." -ForegroundColor Green
}

# Export report if requested
if ($ExportReport) {
    $reportPath = "C:\Reports\tool_verification_$(Get-Date -Format 'yyyyMMdd_HHmmss').csv"
    
    # Create Reports directory if it doesn't exist
    if (-not (Test-Path "C:\Reports")) {
        New-Item -ItemType Directory -Path "C:\Reports" -Force | Out-Null
    }
    
    $results | Export-Csv -Path $reportPath -NoTypeInformation
    Write-Host "`n📄 Report exported to: $reportPath" -ForegroundColor Cyan
}

Write-Host "`n" # Blank line for spacing

# Return exit code based on critical tools
$criticalMissing = ($results | Where-Object { $_.Critical -eq $true -and $_.Status -eq "Missing" }).Count
if ($criticalMissing -gt 0) {
    Write-Host "⚠ WARNING: $criticalMissing critical tool(s) missing!" -ForegroundColor Red
    exit 1
}
else {
    exit 0
}
