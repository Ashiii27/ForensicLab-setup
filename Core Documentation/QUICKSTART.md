# 🚀 Quick Start Guide - DFIR Home Lab

**Welcome!** This guide will get you started with your DFIR Home Lab in under 30 minutes.

---

## ⚡ Fast Track Setup

### Step 1: Download Required Software (15 minutes)

**On your host machine:**

1. **VirtualBox** 
   - Download: https://www.virtualbox.org/wiki/Downloads
   - Install with Extension Pack

2. **Windows Server 2019 ISO** (or Windows 10)
   - Evaluation: https://www.microsoft.com/en-us/evalcenter/evaluate-windows-server-2019
   - Size: ~5GB

### Step 2: Create Virtual Machine (5 minutes)

1. **Open VirtualBox** → Click **New**

2. **Configure:**
   ```
   Name: DFIR-Workstation
   Type: Microsoft Windows
   Version: Windows 2019 (64-bit)
   RAM: 4096 MB
   Disk: 100 GB (Dynamic)
   ```

3. **Settings:**
   - System → Processor → 2 CPUs
   - Storage → Add Windows ISO to optical drive
   - Network → NAT

4. **Start VM** and install Windows

### Step 3: Essential Configuration (10 minutes)

**Inside the VM:**

1. **Install Guest Additions:**
   ```
   Devices → Insert Guest Additions CD
   Run installer → Reboot
   ```

2. **Enable WSL1:**
   ```powershell
   # Open PowerShell as Administrator
   Enable-WindowsOptionalFeature -Online -FeatureName Microsoft-Windows-Subsystem-Linux
   # Reboot when prompted
   
   # After reboot
   wsl --set-default-version 1
   ```

3. **Install Ubuntu 20.04:**
   - Open Microsoft Store
   - Search: "Ubuntu 20.04"
   - Install and launch
   - Create username and password

---

## 🛠️ Essential Tools (30 minutes)

### Windows Tools

**Create tool directories:**
```powershell
New-Item -ItemType Directory -Path "C:\Tools"
New-Item -ItemType Directory -Path "C:\Cases"
New-Item -ItemType Directory -Path "C:\Evidence"
```

**Install via WinGet (fastest method):**
```powershell
# Install WinGet if not present (Windows 10 1809+)
winget install -e --id 7zip.7zip
winget install -e --id Notepad++.Notepad++
winget install -e --id Microsoft.VisualStudioCode
winget install -e --id Mozilla.Firefox
winget install -e --id Python.Python.3.11
```

**Manual Downloads (if needed):**

1. **FTK Imager** (Memory/Disk Imaging)
   - https://www.exterro.com/ftk-imager
   - Extract to: `C:\Tools\FTK_Imager`

2. **KAPE** (Artifact Collection)
   - https://www.kroll.com/kape
   - Extract to: `C:\Tools\KAPE`

3. **Eric Zimmerman Tools** (Forensic Utilities)
   ```powershell
   cd C:\Tools
   Invoke-WebRequest "https://raw.githubusercontent.com/EricZimmerman/Get-ZimmermanTools/master/Get-ZimmermanTools.ps1" -OutFile "Get-ZimmermanTools.ps1"
   .\Get-ZimmermanTools.ps1 -Dest "C:\Tools\ZimmermanTools"
   ```

### Linux Tools (WSL)

**Open Ubuntu terminal:**

```bash
# Update system
sudo apt update && sudo apt upgrade -y

# Install Python and pip
sudo apt install -y python3 python3-pip

# Install Volatility3
pip3 install volatility3

# Install Plaso
sudo add-apt-repository -y ppa:gift/stable
sudo apt update
sudo apt install -y plaso-tools

# Install Oletools
pip3 install oletools

# Verify installations
vol.py -h
log2timeline.py --version
olevba --help
```

---

## ✅ Verification

**Run this script to verify your setup:**

```powershell
# Save as C:\Tools\quick_verify.ps1
$tools = @(
    "C:\Tools\FTK_Imager\FTK Imager.exe",
    "C:\Tools\KAPE\kape.exe",
    "C:\Tools\ZimmermanTools\TimelineExplorer\TimelineExplorer.exe",
    "C:\Program Files\7-Zip\7z.exe",
    "C:\Program Files\Notepad++\notepad++.exe"
)

Write-Host "`nVerifying tool installation..." -ForegroundColor Cyan

foreach ($tool in $tools) {
    $name = Split-Path $tool -Leaf
    if (Test-Path $tool) {
        Write-Host "✓ $name" -ForegroundColor Green
    } else {
        Write-Host "✗ $name - NOT FOUND" -ForegroundColor Red
    }
}

# Check WSL
if (wsl --list --quiet 2>$null) {
    Write-Host "✓ WSL Ubuntu" -ForegroundColor Green
} else {
    Write-Host "✗ WSL Ubuntu - NOT FOUND" -ForegroundColor Red
}

Write-Host "`nSetup verification complete!`n" -ForegroundColor Cyan
```

---

## 🎯 Your First Investigation

### Quick Win #1: Analyze Event Logs

```powershell
# Parse failed login attempts
Get-WinEvent -FilterHashtable @{LogName='Security'; ID=4625} -MaxEvents 50 |
    Select-Object TimeCreated, Message |
    Export-Csv C:\Reports\failed_logins.csv -NoTypeInformation

# View results
Import-Csv C:\Reports\failed_logins.csv | Format-Table -AutoSize
```

### Quick Win #2: List Running Processes

```powershell
# Using WMIC
wmic process get ProcessId,ParentProcessId,CommandLine,ExecutablePath /format:csv > C:\Reports\process_list.csv

# Open in Timeline Explorer
C:\Tools\ZimmermanTools\TimelineExplorer\TimelineExplorer.exe C:\Reports\process_list.csv
```

### Quick Win #3: Capture Memory

```
1. Open FTK Imager as Administrator
2. File → Capture Memory
3. Destination: C:\Evidence\memory_capture.mem
4. Check "Include pagefile"
5. Click "Capture"
```

---

## 📚 Next Steps

**Once you've completed the quick start:**

1. **Take a VM Snapshot** (VirtualBox → Machine → Take Snapshot)
   - Name: "Clean_Baseline"
   - This is your restore point

2. **Practice Scenarios:**
   - Install a program and analyze prefetch files
   - Create some files and build a timeline
   - Browse the web and extract browser history

3. **Read the Full README:**
   - Complete tool descriptions
   - Advanced configurations
   - Project ideas

4. **Join the Community:**
   - r/computerforensics
   - DFIR Discord servers
   - Follow @13Cubed on YouTube

---

## 🆘 Troubleshooting

**VM won't start?**
- Enable VT-x/AMD-V in BIOS
- Disable Hyper-V on Windows host: `bcdedit /set hypervisorlaunchtype off`

**WSL2 instead of WSL1?**
```powershell
wsl --set-default-version 1
wsl --set-version Ubuntu-20.04 1
```

**Tools blocked by Windows Defender?**
```powershell
Add-MpPreference -ExclusionPath "C:\Tools"
```

**Out of disk space?**
- Delete unused snapshots
- Clear downloads folder
- Expand VM disk in VirtualBox settings

---

## 💡 Pro Tips

1. **Always work from snapshots** - Never corrupt your baseline
2. **Document everything** - Create case notes in Notepad++
3. **Use UTC timezone** - Standardize your analysis
4. **Name files clearly** - Use timestamps: `evidence_20240206_143022.mem`
5. **Organize your cases** - One folder per investigation in `C:\Cases`

---

## 🎓 Learning Resources

**Beginner Friendly:**
- 13Cubed YouTube: https://youtube.com/@13Cubed
- SANS Posters: https://www.sans.org/posters/
- AboutDFIR: https://aboutdfir.com/

**Practice Datasets:**
- Digital Corpora: https://digitalcorpora.org/
- NIST CFReDS: https://cfreds.nist.gov/

**Certifications to Consider:**
- GCFE (GIAC Certified Forensic Examiner)
- EnCE (EnCase Certified Examiner)
- CHFI (Computer Hacking Forensic Investigator)

---

## ✨ You're Ready!

Your DFIR lab is now operational. Start with simple tasks and gradually tackle more complex investigations.

**Remember:** Every expert was once a beginner. Keep practicing!

---

**Need Help?**
- Check the main [README.md](README.md) for detailed documentation
- Review [CONTRIBUTING.md](CONTRIBUTING.md) to submit improvements
- Open an issue on GitHub for support

**Happy Investigating! 🔍**
