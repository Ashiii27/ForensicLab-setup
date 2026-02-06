<div align="center">

# 🛡️ Digital Forensics Workstation – DFIR Home Lab

<img src="https://readme-typing-svg.herokuapp.com?size=24&duration=3000&color=00F7FF&center=true&vCenter=true&width=600&lines=Digital+Forensics+Home+Lab;Windows+%2B+WSL+Ubuntu;DFIR+Training+Environment;SOC+%7C+Blue+Team+Practice" />

A professional **Digital Forensics & Incident Response (DFIR) Home Lab** built using  
**Windows VM + Ubuntu (WSL)** with industry-recognized forensic tools.

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Platform](https://img.shields.io/badge/Platform-Windows%20%7C%20Linux-blue)]()
[![Made with Love](https://img.shields.io/badge/Made%20with-❤️-red)]()

</div>

---

## 📌 Table of Contents

- [🎯 Objective](#-objective)
- [🧱 Lab Architecture](#-lab-architecture)
- [📋 Prerequisites](#-prerequisites)
- [🛠 Part 1: Hypervisor Setup](#-part-1-hypervisor-setup)
- [💻 Part 2: Windows VM Configuration](#-part-2-windows-vm-configuration)
- [🐧 Part 3: WSL & Ubuntu Setup](#-part-3-wsl--ubuntu-setup)
- [⚙️ Part 4: Environment Hardening](#️-part-4-environment-hardening)
- [🔧 Part 5: Tool Installation](#-part-5-tool-installation)
- [📸 Part 6: Baseline Snapshot](#-part-6-baseline-snapshot)
- [🚀 Part 7: Validation & Testing](#-part-7-validation--testing)
- [📚 Use Cases & Next Steps](#-use-cases--next-steps)
- [🔍 Troubleshooting](#-troubleshooting)
- [📖 Resources](#-resources)
- [⚠️ Disclaimer](#️-disclaimer)
- [👨‍💻 Author](#-author)

---

## 🎯 Objective

Build a **dedicated forensic workstation** capable of performing:

✅ **Windows Artifact Analysis** (Registry, Event Logs, Prefetch, etc.)  
✅ **Remote Login Investigations** (RDP, SSH, VPN sessions)  
✅ **Memory & Disk Forensics** (RAM dumps, disk images)  
✅ **Timeline Creation** (Super timeline analysis)  
✅ **Log Analysis** (Windows Event Logs, Sysmon, IIS)  
✅ **Malware & Document Inspection** (Static analysis, macro extraction)

---

## 🧱 Lab Architecture

```
┌─────────────────────────────────────────┐
│         Host Machine (Physical)         │
│      Windows/Linux/macOS + 16GB RAM     │
└──────────────────┬──────────────────────┘
                   │
        ┌──────────▼──────────┐
        │   VirtualBox 7.x    │
        │ (Type-2 Hypervisor) │
        └──────────┬──────────┘
                   │
        ┌──────────▼──────────────────────┐
        │  Windows Server 2019 / Win10    │
        │  100GB Disk | 4GB RAM | 2 CPU   │
        └──────────┬──────────────────────┘
                   │
        ┌──────────▼──────────┐
        │   WSL1 + Ubuntu     │
        │      20.04 LTS      │
        └──────────┬──────────┘
                   │
        ┌──────────▼──────────────────────┐
        │      DFIR Tool Stack            │
        │  Volatility | KAPE | FTK | ETC  │
        └─────────────────────────────────┘
```

---

## 📋 Prerequisites

### Hardware Requirements
| Component | Minimum | Recommended |
|-----------|---------|-------------|
| **RAM** | 8 GB | 16 GB+ |
| **Storage** | 150 GB free | 250 GB+ SSD |
| **CPU** | Dual-core | Quad-core with VT-x/AMD-V |
| **Network** | Internet connection for downloads | — |

### Software Requirements
- ✅ VirtualBox 7.0+ ([Download](https://www.virtualbox.org/wiki/Downloads))
- ✅ Windows Server 2019 ISO ([Evaluation](https://www.microsoft.com/en-us/evalcenter/evaluate-windows-server-2019)) **OR** Windows 10/11 Enterprise
- ✅ Ubuntu 20.04 LTS ([Download](https://releases.ubuntu.com/20.04/))

### Knowledge Requirements
- Basic understanding of Windows administration
- Familiarity with command line (PowerShell, Bash)
- General cybersecurity concepts

---

## 🛠 Part 1: Hypervisor Setup

### Step 1.1: Install VirtualBox

1. **Download VirtualBox:**
   - Visit: https://www.virtualbox.org/wiki/Downloads
   - Download version for your host OS (Windows/macOS/Linux)

2. **Install with Extension Pack:**
   ```bash
   # Windows: Run installer as Administrator
   # Linux example:
   sudo apt install virtualbox virtualbox-ext-pack
   ```

3. **Verify Installation:**
   - Open VirtualBox Manager
   - Check: `File → Preferences → Extensions` (Extension Pack should be listed)

### Step 1.2: Configure VirtualBox Defaults

```
File → Preferences → General:
  Default Machine Folder: C:\VirtualMachines (or custom path)

Network → NAT Networks:
  Click [+] → Create "NatNetwork"
  Network CIDR: 10.0.2.0/24
  Enable DHCP
```

---

## 💻 Part 2: Windows VM Configuration

### Step 2.1: Create Virtual Machine

1. **Launch VirtualBox** → Click **"New"**

2. **Basic Configuration:**
   ```
   Name: DFIR-Workstation
   Type: Microsoft Windows
   Version: Windows 2019 (64-bit) or Windows 10 (64-bit)
   ```

3. **Memory Allocation:**
   ```
   RAM: 4096 MB (4GB minimum)
   ```

4. **Hard Disk:**
   ```
   ☑ Create a virtual hard disk now
   Type: VDI (VirtualBox Disk Image)
   Storage: Dynamically allocated
   Size: 100 GB
   ```

5. **Click Create**

### Step 2.2: VM Settings Optimization

**Right-click VM → Settings:**

#### 🖥️ System Tab
```
Motherboard:
  Boot Order: Optical → Hard Disk
  ☑ Enable EFI (if using modern Windows ISO)
  
Processor:
  CPU: 2-4 cores
  ☑ Enable PAE/NX
```

#### 💾 Storage Tab
```
Controller: IDE
  ☐ Empty → Click disk icon → Choose Windows ISO

Controller: SATA
  ☑ Use Host I/O Cache
```

#### 🌐 Network Tab
```
Adapter 1:
  ☑ Enable Network Adapter
  Attached to: NAT
```

#### 📺 Display Tab
```
Video Memory: 128 MB
Graphics Controller: VMSVGA
☑ Enable 3D Acceleration
```

#### 🗂️ Shared Folders Tab
```
Click [+] icon:
  Folder Path: C:\Shared (create on host first)
  Folder Name: Shared
  ☑ Auto-mount
  ☑ Make Permanent
```

### Step 2.3: Install Windows

1. **Start the VM** (Click "Start")

2. **Windows Installation:**
   - Select: **Windows Server 2019 Standard (Desktop Experience)** or **Windows 10 Pro**
   - Installation Type: **Custom: Install Windows only**
   - Select unallocated space → Next
   - Wait for installation (15-30 minutes)

3. **Initial Setup:**
   ```
   Administrator Password: Create strong password
   Network: Select "Private Network"
   ```

4. **Windows Updates:**
   ```powershell
   # Run Windows Update
   Settings → Update & Security → Windows Update → Check for updates
   ```

### Step 2.4: Install Guest Additions

**Inside the VM:**

1. **VirtualBox Menu:** `Devices → Insert Guest Additions CD Image`

2. **Run Installer:**
   ```
   Open File Explorer → CD Drive (VirtualBox Guest Additions)
   Run: VBoxWindowsAdditions.exe
   Install with default options
   Reboot VM
   ```

3. **Enable Features:**
   ```
   Devices → Shared Clipboard → Bidirectional
   Devices → Drag and Drop → Bidirectional
   ```

---

## 🐧 Part 3: WSL & Ubuntu Setup

### Step 3.1: Enable WSL (Version 1)

⚠️ **Important:** VirtualBox only supports **WSL1** (not WSL2)

**Open PowerShell as Administrator:**

```powershell
# Enable WSL Feature
Enable-WindowsOptionalFeature -Online -FeatureName Microsoft-Windows-Subsystem-Linux

# Reboot when prompted
Restart-Computer
```

### Step 3.2: Set WSL Default Version

```powershell
# After reboot, open PowerShell as Admin again
wsl --set-default-version 1
```

### Step 3.3: Install Ubuntu 20.04

**Method 1: Microsoft Store (Easiest)**

1. Open **Microsoft Store**
2. Search: **"Ubuntu 20.04 LTS"**
3. Click **"Get"** → **"Install"**
4. Launch Ubuntu from Start Menu
5. Create UNIX user:
   ```
   Username: dfir
   Password: [create password]
   ```

**Method 2: Manual Installation**

```powershell
# Download Ubuntu 20.04 appx
Invoke-WebRequest -Uri https://aka.ms/wslubuntu2004 -OutFile Ubuntu2004.appx -UseBasicParsing

# Install
Add-AppxPackage .\Ubuntu2004.appx

# Launch
ubuntu2004.exe

# Create user
```

### Step 3.4: Verify WSL Installation

```bash
# Check WSL version
wsl --list --verbose

# Should show:
#   NAME            STATE           VERSION
# * Ubuntu-20.04    Running         1
```

---

## ⚙️ Part 4: Environment Hardening

### Step 4.1: Set Timezone to UTC

**Windows:**

```powershell
# Set to UTC
Set-TimeZone -Id "UTC"

# Verify
Get-TimeZone
```

**Ubuntu (WSL):**

```bash
sudo timedatectl set-timezone UTC
timedatectl
```

### Step 4.2: Configure File Explorer

**Show Hidden Files & Extensions:**

1. Open **File Explorer**
2. Click **"View"** tab
3. Check:
   - ☑ **File name extensions**
   - ☑ **Hidden items**

**Registry Method:**

```powershell
# Show hidden files
Set-ItemProperty -Path "HKCU:\Software\Microsoft\Windows\CurrentVersion\Explorer\Advanced" -Name "Hidden" -Value 1

# Show file extensions
Set-ItemProperty -Path "HKCU:\Software\Microsoft\Windows\CurrentVersion\Explorer\Advanced" -Name "HideFileExt" -Value 0

# Restart Explorer
Stop-Process -Name explorer -Force
```

### Step 4.3: Create Forensic Folder Structure

```powershell
# Create directories
New-Item -ItemType Directory -Path "C:\Cases"
New-Item -ItemType Directory -Path "C:\Tools"
New-Item -ItemType Directory -Path "C:\Evidence"
New-Item -ItemType Directory -Path "C:\Reports"

# Verify
Get-ChildItem C:\ | Where-Object { $_.PSIsContainer }
```

### Step 4.4: Configure Windows Defender

**Add Exclusions (Prevent tool blocking):**

```powershell
# Open PowerShell as Administrator

# Add folder exclusions
Add-MpPreference -ExclusionPath "C:\Cases"
Add-MpPreference -ExclusionPath "C:\Tools"
Add-MpPreference -ExclusionPath "C:\Evidence"

# Verify exclusions
Get-MpPreference | Select-Object -ExpandProperty ExclusionPath
```

**Disable Cloud Protection (Optional for lab):**

```
Windows Security → Virus & threat protection → 
  Manage settings → 
    Cloud-delivered protection: OFF
    Automatic sample submission: OFF
```

⚠️ **Note:** Only disable these in an isolated lab environment.

---

## 🔧 Part 5: Tool Installation

### 🐧 Part 5A: Linux Tools (WSL)

**Open Ubuntu terminal:**

```bash
# Update system
sudo apt update && sudo apt upgrade -y

# Install prerequisites
sudo apt install -y python3 python3-pip git build-essential
```

#### 1. Volatility 3 (Memory Forensics)

```bash
# Install Volatility3
pip3 install volatility3

# Install additional dependencies
pip3 install capstone yara-python pycryptodome

# Verify installation
vol.py -h

# Create alias for easier access
echo "alias vol='vol.py'" >> ~/.bashrc
source ~/.bashrc
```

**Test Volatility:**

```bash
# Download sample memory image (optional)
mkdir ~/samples
cd ~/samples
# Use your own memory dumps or download from:
# https://github.com/volatilityfoundation/volatility/wiki/Memory-Samples
```

#### 2. Plaso (Log2Timeline - Super Timeline)

```bash
# Add GIFT PPA
sudo add-apt-repository -y ppa:gift/stable
sudo apt update

# Install Plaso tools
sudo apt install -y plaso-tools

# Verify installation
log2timeline.py --version
psort.py --version
pinfo.py --version
```

**Test Plaso:**

```bash
# Create test timeline
log2timeline.py --storage-file test.plaso /var/log
psort.py -o dynamic -w test_timeline.csv test.plaso
```

#### 3. Oletools (Office Document Analysis)

```bash
# Install oletools
pip3 install -U oletools

# Verify installation
olevba --help
oleid --help
```

#### 4. Additional Useful Tools

```bash
# Bulk Extractor (Carving)
sudo apt install -y bulk-extractor

# Sleuth Kit (File system analysis)
sudo apt install -y sleuthkit

# Autopsy dependencies
sudo apt install -y testdisk

# Forensic utilities
sudo apt install -y foremost scalpel binwalk
```

### 🪟 Part 5B: Windows Tools

#### 1. FTK Imager (Disk Imaging & Memory Acquisition)

```powershell
# Download FTK Imager
Start-Process "https://www.exterro.com/ftk-imager"

# Manual Installation:
# 1. Download FTK Imager from Exterro
# 2. Install to C:\Tools\FTK_Imager
# 3. Run as Administrator for first time
```

**After Installation:**

```
Right-click FTK Imager → Properties → Compatibility:
  ☑ Run this program as an administrator
```

#### 2. KAPE (Kroll Artifact Parser and Extractor)

```powershell
# Download KAPE
cd C:\Tools
Start-Process "https://www.kroll.com/en/services/cyber-risk/incident-response-litigation-support/kroll-artifact-parser-extractor-kape"

# Extract to C:\Tools\KAPE
# No installation required - portable tool
```

**Initial Configuration:**

```powershell
cd C:\Tools\KAPE
# Run gkape.exe (GUI) or kape.exe (CLI)
# Update targets and modules on first run
```

#### 3. Eric Zimmerman Tools Suite

```powershell
# Download all tools
cd C:\Tools
New-Item -ItemType Directory -Path "C:\Tools\ZimmermanTools"

# Use Get-ZimmermanTools script
Invoke-WebRequest "https://raw.githubusercontent.com/EricZimmerman/Get-ZimmermanTools/master/Get-ZimmermanTools.ps1" -OutFile "Get-ZimmermanTools.ps1"

# Run script
.\Get-ZimmermanTools.ps1 -Dest "C:\Tools\ZimmermanTools"
```

**Key Tools Included:**
- Timeline Explorer
- Registry Explorer
- ShellBags Explorer
- AmcacheParser
- PECmd (Prefetch)
- JLECmd (Jump Lists)

#### 4. Visual Studio Code

```powershell
# Download and install VS Code
winget install -e --id Microsoft.VisualStudioCode

# Or download from: https://code.visualstudio.com/
```

**Recommended Extensions:**

```
- Hex Editor
- Rainbow CSV
- Python
- PowerShell
```

#### 5. Notepad++

```powershell
# Install via winget
winget install -e --id Notepad++.Notepad++

# Or download from: https://notepad-plus-plus.org/
```

#### 6. 7-Zip

```powershell
# Install 7-Zip
winget install -e --id 7zip.7zip

# Or download from: https://www.7-zip.org/
```

#### 7. Firefox (Browser for investigations)

```powershell
# Install Firefox
winget install -e --id Mozilla.Firefox
```

#### 8. Sysinternals Suite

```powershell
# Download entire suite
cd C:\Tools
New-Item -ItemType Directory -Path "C:\Tools\Sysinternals"

# Download
Invoke-WebRequest "https://download.sysinternals.com/files/SysinternalsSuite.zip" -OutFile "Sysinternals.zip"

# Extract
Expand-Archive -Path "Sysinternals.zip" -DestinationPath "C:\Tools\Sysinternals"

# Add to PATH
[Environment]::SetEnvironmentVariable("Path", $env:Path + ";C:\Tools\Sysinternals", [EnvironmentVariableTarget]::Machine)
```

#### 9. Wireshark (Network Analysis)

```powershell
# Install Wireshark
winget install -e --id WiresharkFoundation.Wireshark
```

#### 10. Python (for scripts)

```powershell
# Install Python 3.11
winget install -e --id Python.Python.3.11

# Verify installation
python --version

# Install forensic libraries
pip install pefile yara-python volatility3
```

### 📋 Tool Installation Verification

**Create verification script:**

```powershell
# Save as C:\Tools\verify_tools.ps1

$tools = @{
    "FTK Imager" = "C:\Tools\FTK_Imager\FTK Imager.exe"
    "KAPE" = "C:\Tools\KAPE\kape.exe"
    "Timeline Explorer" = "C:\Tools\ZimmermanTools\TimelineExplorer\TimelineExplorer.exe"
    "7-Zip" = "C:\Program Files\7-Zip\7z.exe"
    "VS Code" = "C:\Program Files\Microsoft VS Code\Code.exe"
}

foreach ($tool in $tools.GetEnumerator()) {
    if (Test-Path $tool.Value) {
        Write-Host "✓ $($tool.Key) - INSTALLED" -ForegroundColor Green
    } else {
        Write-Host "✗ $($tool.Key) - NOT FOUND" -ForegroundColor Red
    }
}
```

**Run verification:**

```powershell
.\verify_tools.ps1
```

---

## 📸 Part 6: Baseline Snapshot

### Step 6.1: Clean Up VM

```powershell
# Clear temporary files
Remove-Item -Path "$env:TEMP\*" -Recurse -Force -ErrorAction SilentlyContinue

# Clear browser caches (if applicable)
# Clear download folder
Remove-Item -Path "$env:USERPROFILE\Downloads\*" -Recurse -Force

# Empty Recycle Bin
Clear-RecycleBin -Force -ErrorAction SilentlyContinue
```

### Step 6.2: Defragment (Optional)

```powershell
# Optimize system drive
Optimize-Volume -DriveLetter C -Defrag -Verbose
```

### Step 6.3: Shut Down VM Cleanly

```powershell
# Shut down
Stop-Computer
```

### Step 6.4: Create Snapshot

**In VirtualBox Manager:**

1. Select **DFIR-Workstation** VM
2. Click **☰ Menu** → **Snapshots**
3. Click **"Take"** snapshot button
4. Name: **"Clean_Baseline_DFIR_Lab"**
5. Description: 
   ```
   Clean installation with all tools installed
   Date: [Current Date]
   Windows + WSL + All DFIR Tools
   ```
6. Click **OK**

### Step 6.5: Verify Snapshot

```
Snapshots tab should show:
  └─ Clean_Baseline_DFIR_Lab (Current State)
```

**To restore snapshot later:**
- Right-click snapshot → **"Restore Snapshot"**

---

## 🚀 Part 7: Validation & Testing

### Test 1: Memory Acquisition

```powershell
# Using FTK Imager
# 1. Launch FTK Imager as Administrator
# 2. File → Capture Memory
# 3. Destination: C:\Evidence\memory_test.mem
# 4. ☑ Include pagefile
# 5. Click Capture
```

### Test 2: Artifact Collection with KAPE

```powershell
cd C:\Tools\KAPE

# Collect Windows event logs
.\kape.exe --tsource C: --tdest C:\Evidence\KAPE_Output --target EventLogs --vhdx TestCollection
```

### Test 3: Timeline Creation

**In WSL Ubuntu:**

```bash
# Create super timeline of C drive
sudo log2timeline.py --storage-file C_drive.plaso /mnt/c/Windows/System32/winevt/Logs

# Process timeline
psort.py -o l2tcsv -w timeline_output.csv C_drive.plaso

# View first 20 entries
head -20 timeline_output.csv
```

### Test 4: Registry Analysis

```powershell
# Using Registry Explorer (Zimmerman Tools)
cd C:\Tools\ZimmermanTools

# Launch Registry Explorer
.\RegistryExplorer\RegistryExplorer.exe

# Load: C:\Windows\System32\config\SYSTEM
```

---

## 📚 Use Cases & Next Steps

### Beginner Projects

1. **Windows Event Log Analysis**
   ```powershell
   # Parse Security logs for failed logons
   Get-WinEvent -FilterHashtable @{LogName='Security'; ID=4625} | 
       Select-Object TimeCreated, Message | 
       Export-Csv C:\Reports\failed_logons.csv
   ```

2. **Prefetch Analysis**
   ```powershell
   # Parse prefetch files
   cd C:\Tools\ZimmermanTools
   .\PECmd.exe -d C:\Windows\Prefetch --csv C:\Reports --csvf prefetch_analysis.csv
   ```

3. **USB Device History**
   ```powershell
   # Check USBSTOR registry
   Get-ItemProperty -Path "HKLM:\SYSTEM\CurrentControlSet\Enum\USBSTOR\*\*" | 
       Select-Object FriendlyName, Mfg
   ```

### Intermediate Projects

4. **Memory Analysis with Volatility**
   ```bash
   # In WSL
   vol.py -f /mnt/c/Evidence/memory_dump.mem windows.info
   vol.py -f /mnt/c/Evidence/memory_dump.mem windows.pslist
   vol.py -f /mnt/c/Evidence/memory_dump.mem windows.netscan
   ```

5. **Super Timeline Analysis**
   ```bash
   # Create timeline from disk image
   log2timeline.py --storage-file case001.plaso evidence.dd
   
   # Filter for specific date range
   psort.py -o l2tcsv case001.plaso "date > '2024-01-01 00:00:00'"
   ```

6. **Malicious Macro Detection**
   ```bash
   # Analyze Office document
   olevba suspicious_document.docm
   oleid suspicious_document.docm
   ```

### Advanced Projects

7. **Full Disk Forensic Analysis**
   - Acquire disk image with FTK Imager
   - Mount with Arsenal Image Mounter
   - Parse with Autopsy
   - Timeline with Plaso
   - Report findings

8. **Ransomware Incident Response**
   - Memory dump analysis
   - File system timeline
   - Network connection analysis
   - IOC extraction
   - Lateral movement detection

9. **Insider Threat Investigation**
   - Browser history forensics
   - File access auditing
   - USB device tracking
   - Email analysis
   - Data exfiltration detection

### 🎓 Learning Resources

**Online Courses:**
- SANS FOR500: Windows Forensic Analysis
- TCM Security: Practical Windows Forensics
- 13Cubed YouTube Channel (Highly Recommended)

**Practice Datasets:**
- Digital Corpora: https://digitalcorpora.org/
- NIST CFReDS: https://cfreds.nist.gov/
- AboutDFIR: https://aboutdfir.com/

**Communities:**
- r/computerforensics
- DFIR Discord servers
- ForensicFocus forums

---

## 🔍 Troubleshooting

### Issue: WSL2 vs WSL1 Confusion

**Error:** "Please enable the Virtual Machine Platform Windows feature"

**Solution:**
```powershell
# Force WSL1
wsl --set-default-version 1

# Convert existing distro to WSL1
wsl --set-version Ubuntu-20.04 1
```

### Issue: VirtualBox VM Won't Start

**Error:** "VT-x is not available" or "AMD-V is not available"

**Solution:**
1. Reboot host computer
2. Enter BIOS/UEFI (F2/DEL during boot)
3. Enable: **Intel VT-x** or **AMD-V**
4. Enable: **Intel VT-d** or **AMD IOMMU**
5. Save and reboot

### Issue: Tools Being Blocked by Defender

**Solution:**
```powershell
# Re-add exclusions
Add-MpPreference -ExclusionPath "C:\Tools"
Add-MpPreference -ExclusionExtension ".exe"

# Verify
Get-MpPreference | Select-Object ExclusionPath
```

### Issue: Shared Folders Not Mounting

**Solution:**
1. Verify Guest Additions installed
2. Check VirtualBox Settings → Shared Folders
3. Inside VM:
   ```powershell
   # Mount manually
   net use Z: \\vboxsvr\Shared
   ```

### Issue: Ubuntu Fails to Install

**Solution:**
```powershell
# Reset WSL
wsl --unregister Ubuntu-20.04

# Reinstall from Store or manually
```

### Issue: Plaso Installation Fails

**Solution:**
```bash
# Remove and re-add repository
sudo add-apt-repository --remove ppa:gift/stable
sudo add-apt-repository ppa:gift/stable
sudo apt update
sudo apt install plaso-tools -y
```

---

## 📖 Resources

### Official Documentation
- [Volatility 3 Docs](https://volatility3.readthedocs.io/)
- [KAPE Documentation](https://ericzimmerman.github.io/KapeDocs/)
- [Plaso Wiki](https://plaso.readthedocs.io/)
- [Eric Zimmerman Tools](https://ericzimmerman.github.io/)

### DFIR Blogs
- [13Cubed](https://www.13cubed.com/)
- [SANS DFIR](https://www.sans.org/blog/category/digital-forensics/)
- [AboutDFIR](https://aboutdfir.com/)

### Tools & Downloads
- [FTK Imager](https://www.exterro.com/ftk-imager)
- [KAPE](https://www.kroll.com/kape)
- [Sysinternals](https://docs.microsoft.com/en-us/sysinternals/)

---

## ⚠️ Disclaimer

⚠️ **LEGAL AND ETHICAL USE ONLY**

This lab is designed for:
- ✅ Educational purposes
- ✅ Authorized security research
- ✅ Professional training
- ✅ Personal skill development

**DO NOT:**
- ❌ Analyze systems without explicit authorization
- ❌ Use tools for unauthorized access
- ❌ Violate any laws or regulations
- ❌ Perform forensics on production systems without approval

**You are responsible for complying with:**
- Computer Fraud and Abuse Act (CFAA)
- Local and international laws
- Organizational policies
- Professional ethics

**The author assumes NO liability for misuse of this lab.**

---

<div align="center">

## 👨‍💻 Author

**Ashish Kumar**  
*Cybersecurity | DFIR | SOC Enthusiast*

[![LinkedIn](https://img.shields.io/badge/LinkedIn-Connect-blue?style=flat&logo=linkedin)](https://www.linkedin.com/in/ashish-kumar)
[![GitHub](https://img.shields.io/badge/GitHub-Follow-black?style=flat&logo=github)](https://github.com/ashishkumar)
[![Email](https://img.shields.io/badge/Email-Contact-red?style=flat&logo=gmail)](mailto:contact@example.com)

---

### 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

### ⭐ Support This Project

If you found this lab useful, please consider:
- ⭐ Starring this repository
- 🔄 Sharing with colleagues
- 💬 Providing feedback via Issues
- 🤝 Contributing improvements

---

**Last Updated:** February 2026  
**Version:** 1.0.0

</div>
