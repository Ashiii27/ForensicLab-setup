# DFIR Lab Scripts

This directory contains automation scripts for your DFIR lab.

## 📁 Contents

### 1. `verify_tools.ps1`

**Purpose:** Verify all DFIR tools are installed correctly

**Usage:**
```powershell
# Basic verification
.\verify_tools.ps1

# Detailed output with version info
.\verify_tools.ps1 -Detailed

# Export results to CSV
.\verify_tools.ps1 -ExportReport

# Both detailed and export
.\verify_tools.ps1 -Detailed -ExportReport
```

**Features:**
- Checks all Windows and Linux forensic tools
- Identifies critical vs optional tools
- Color-coded output
- Generates CSV report
- Returns exit code based on critical tools

**Example Output:**
```
[Core Forensic Tools]
──────────────────────────────────────────────────────────────────────
FTK Imager                         [CRITICAL]      ✓ INSTALLED
KAPE                               [CRITICAL]      ✓ INSTALLED
Autopsy                                            ✗ NOT FOUND

SUMMARY
─────────────────────────────
Total Tools Checked:    25
Tools Installed:        22
Tools Missing:          3
Installation Status:    88%
```

---

### 2. `analyze_memory.py`

**Purpose:** Automated Volatility3 memory analysis

**Usage:**
```bash
# Basic analysis (fast - core plugins only)
python3 analyze_memory.py -f memory.raw -o output_dir

# Full analysis (includes malware detection - slower)
python3 analyze_memory.py -f memory.raw -o output_dir --full

# Export as CSV instead of text
python3 analyze_memory.py -f memory.raw -o output_dir --format csv

# Skip report generation
python3 analyze_memory.py -f memory.raw -o output_dir --no-report
```

**Features:**
- Runs common Volatility3 plugins automatically
- Saves results to organized output directory
- Generates summary report
- Supports multiple output formats (text, CSV, JSON)
- Color-coded progress indicators
- Timeout handling for hung plugins

**Plugins Run (Basic Analysis):**
- `windows.info` - System information
- `windows.pslist` - Process list
- `windows.pstree` - Process tree
- `windows.cmdline` - Command line arguments
- `windows.netscan` - Network connections
- `windows.filescan` - File objects
- And more...

**Additional Plugins (Full Analysis):**
- `windows.malfind` - Malware detection
- `windows.ldrmodules` - Module analysis
- `windows.ssdt` - System Service Descriptor Table
- `windows.driverscan` - Driver analysis
- And more...

**Example Output:**
```
╔══════════════════════════════════════════════════════════════╗
║        DFIR Lab - Automated Memory Analysis Tool            ║
║                  Powered by Volatility3                     ║
╚══════════════════════════════════════════════════════════════╝

Memory Dump Information:
  File: memory.raw
  Size: 2048.50 MB
  Created: 2024-02-06 14:30:22

Starting analysis of memory.raw...
Output directory: /output

[*] Running windows.info... ✓ Complete
[*] Running windows.pslist... ✓ Complete
[*] Running windows.netscan... ✓ Complete
...

Analysis Summary:
  Successful: 15
  Failed: 0
  Total: 15

✓ Analysis complete! Results saved to: /output
```

---

## 🚀 Getting Started

### Installation

**Windows (PowerShell):**
```powershell
# No installation needed - scripts are standalone
# Just ensure execution policy allows scripts
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
```

**Linux/WSL (Python):**
```bash
# Ensure Python 3 is installed
python3 --version

# Install Volatility3 if not already installed
pip3 install volatility3

# Make script executable
chmod +x analyze_memory.py
```

### Quick Test

**Test PowerShell script:**
```powershell
cd C:\Tools\scripts
.\verify_tools.ps1 -Detailed
```

**Test Python script:**
```bash
# In WSL Ubuntu
cd /mnt/c/Tools/scripts
python3 analyze_memory.py --help
```

---

## 📝 Creating Your Own Scripts

### Script Template (PowerShell)

```powershell
# ============================================================================
# Script Name
# ============================================================================
# Purpose: What this script does
# Author: Your Name
# Date: Date
# ============================================================================

[CmdletBinding()]
param(
    [Parameter(Mandatory=$true)]
    [string]$RequiredParam,
    
    [Parameter(Mandatory=$false)]
    [switch]$OptionalSwitch
)

# Your code here
Write-Host "Script output" -ForegroundColor Green
```

### Script Template (Python)

```python
#!/usr/bin/env python3
"""
Script description
"""

import argparse

def main():
    parser = argparse.ArgumentParser(description='Script description')
    parser.add_argument('-f', '--file', required=True, help='Input file')
    args = parser.parse_args()
    
    # Your code here
    print("Script output")

if __name__ == '__main__':
    main()
```

---

## 🛠️ Common Use Cases

### 1. Pre-Investigation Checklist
```powershell
# Verify all tools before starting case
.\verify_tools.ps1 -Detailed -ExportReport

# Review the report
Import-Csv C:\Reports\tool_verification_*.csv | Format-Table
```

### 2. Automated Memory Triage
```bash
# Quick triage of suspicious system
python3 analyze_memory.py -f /mnt/c/Evidence/suspect.mem -o /mnt/c/Cases/case001/memory

# Review key findings
cat /mnt/c/Cases/case001/memory/analysis_report.txt
cat /mnt/c/Cases/case001/memory/windows.netscan.txt
cat /mnt/c/Cases/case001/memory/windows.malfind.txt
```

### 3. Scheduled Tool Verification
```powershell
# Add to scheduled task to verify tools daily
$action = New-ScheduledTaskAction -Execute "PowerShell.exe" -Argument "-File C:\Tools\scripts\verify_tools.ps1 -ExportReport"
$trigger = New-ScheduledTaskTrigger -Daily -At 9am
Register-ScheduledTask -Action $action -Trigger $trigger -TaskName "DFIR_ToolCheck" -Description "Daily DFIR tool verification"
```

---

## 🔧 Troubleshooting

### PowerShell Script Won't Run

**Error:** "Execution policy prevents script"

**Solution:**
```powershell
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
```

### Python Script: Module Not Found

**Error:** `ModuleNotFoundError: No module named 'volatility3'`

**Solution:**
```bash
pip3 install volatility3 --break-system-packages
```

### Script Path Issues

**Use absolute paths when in doubt:**
```powershell
# Instead of: .\script.ps1
C:\Tools\scripts\verify_tools.ps1

# Instead of: python3 script.py
python3 C:\Tools\scripts\analyze_memory.py
```

---

## 📚 Additional Resources

**Learn PowerShell:**
- Microsoft Learn: https://learn.microsoft.com/powershell/
- PowerShell Gallery: https://www.powershellgallery.com/

**Learn Python for DFIR:**
- Automating OSINT: https://github.com/Te-k/harpoon
- DFIR Python Libraries: https://github.com/python-forensics

**Volatility Documentation:**
- Official Docs: https://volatility3.readthedocs.io/
- Command Reference: https://github.com/volatilityfoundation/volatility3

---

## 🤝 Contributing

Have a useful script? Consider contributing!

1. Follow the coding standards above
2. Add comprehensive comments
3. Include usage examples
4. Test in clean VM
5. Submit pull request

See [CONTRIBUTING.md](../CONTRIBUTING.md) for details.

---

## 📄 License

All scripts in this directory are licensed under the MIT License.

See [LICENSE](../LICENSE) for full text.

---

**Happy Automating! 🚀**
