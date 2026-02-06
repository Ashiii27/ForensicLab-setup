# DFIR Command Cheat Sheet

Quick reference for common digital forensics and incident response commands.

---

## 🪟 Windows Forensics

### Event Log Analysis

```powershell
# Failed login attempts (Event ID 4625)
Get-WinEvent -FilterHashtable @{LogName='Security'; ID=4625} -MaxEvents 100 |
    Select-Object TimeCreated, Message |
    Export-Csv failed_logins.csv

# Successful logins (Event ID 4624)
Get-WinEvent -FilterHashtable @{LogName='Security'; ID=4624} -MaxEvents 100 |
    Select-Object TimeCreated, Message

# Account lockouts (Event ID 4740)
Get-WinEvent -FilterHashtable @{LogName='Security'; ID=4740}

# Process creation events (Event ID 4688)
Get-WinEvent -FilterHashtable @{LogName='Security'; ID=4688} -MaxEvents 100

# Service installation (Event ID 7045)
Get-WinEvent -FilterHashtable @{LogName='System'; ID=7045}

# Export all Security logs
wevtutil epl Security C:\Evidence\Security.evtx
```

### Registry Analysis

```powershell
# USB devices
Get-ItemProperty -Path "HKLM:\SYSTEM\CurrentControlSet\Enum\USBSTOR\*\*" |
    Select-Object FriendlyName, Mfg

# Recent documents
Get-ItemProperty -Path "HKCU:\Software\Microsoft\Windows\CurrentVersion\Explorer\RecentDocs"

# Run keys (Persistence)
Get-ItemProperty -Path "HKLM:\Software\Microsoft\Windows\CurrentVersion\Run"
Get-ItemProperty -Path "HKCU:\Software\Microsoft\Windows\CurrentVersion\Run"

# Installed programs
Get-ItemProperty -Path "HKLM:\Software\Microsoft\Windows\CurrentVersion\Uninstall\*" |
    Select-Object DisplayName, DisplayVersion, Publisher, InstallDate

# Network shares
Get-SmbShare
Get-SmbConnection
```

### Process & Network Analysis

```powershell
# Current processes
Get-Process | Select-Object Id, ProcessName, Path, Company | Export-Csv processes.csv

# Network connections
Get-NetTCPConnection | Select-Object LocalAddress, LocalPort, RemoteAddress, RemotePort, State, OwningProcess

# Services
Get-Service | Where-Object {$_.Status -eq "Running"} | Select-Object Name, DisplayName, StartType

# Scheduled tasks
Get-ScheduledTask | Where-Object {$_.State -eq "Ready"}

# Startup programs
Get-CimInstance Win32_StartupCommand | Select-Object Name, Command, Location, User
```

### File System Analysis

```powershell
# Recently modified files
Get-ChildItem -Path C:\ -Recurse -File |
    Where-Object {$_.LastWriteTime -gt (Get-Date).AddDays(-7)} |
    Select-Object FullName, LastWriteTime, Length

# Find executables
Get-ChildItem -Path C:\Users -Recurse -Include *.exe, *.dll -ErrorAction SilentlyContinue

# Calculate file hash
Get-FileHash -Path C:\suspicious.exe -Algorithm SHA256

# Alternate Data Streams
Get-Item -Path C:\file.txt -Stream *

# File signatures
Format-Hex -Path C:\suspicious.exe -Count 16
```

### User Account Analysis

```powershell
# Local users
Get-LocalUser | Select-Object Name, Enabled, LastLogon

# Local groups
Get-LocalGroup

# Group members
Get-LocalGroupMember -Group "Administrators"

# Current user sessions
query user

# Login history
Get-WinEvent -FilterHashtable @{LogName='Security'; ID=4624} |
    Where-Object {$_.Properties[5].Value -eq 2} |
    Select-Object TimeCreated, @{n='User';e={$_.Properties[5].Value}}
```

---

## 🐧 Linux Forensics (WSL/Ubuntu)

### Volatility 3 Commands

```bash
# Get system info
vol.py -f memory.raw windows.info

# List processes
vol.py -f memory.raw windows.pslist
vol.py -f memory.raw windows.pstree

# Network connections
vol.py -f memory.raw windows.netscan
vol.py -f memory.raw windows.netstat

# Command lines
vol.py -f memory.raw windows.cmdline

# DLLs loaded by process
vol.py -f memory.raw windows.dlllist --pid 1234

# Handles
vol.py -f memory.raw windows.handles --pid 1234

# File scan
vol.py -f memory.raw windows.filescan

# Registry hives
vol.py -f memory.raw windows.registry.hivelist

# Malware detection
vol.py -f memory.raw windows.malfind

# Driver scan
vol.py -f memory.raw windows.driverscan

# Export process to executable
vol.py -f memory.raw windows.pslist --pid 1234 --dump

# Export file from memory
vol.py -f memory.raw windows.dumpfiles --pid 1234
```

### Plaso (Timeline Analysis)

```bash
# Create timeline from disk image
log2timeline.py --storage-file timeline.plaso /mnt/evidence

# Create timeline from live system
sudo log2timeline.py --storage-file system.plaso /

# Create timeline from specific directory
log2timeline.py --storage-file logs.plaso /var/log

# Process timeline to CSV
psort.py -o l2tcsv -w timeline.csv timeline.plaso

# Filter by date
psort.py -o l2tcsv timeline.plaso "date > '2024-01-01 00:00:00' and date < '2024-01-31 23:59:59'"

# Filter by filename
psort.py -o l2tcsv timeline.plaso "filename contains 'malware'"

# Dynamic output with filters
psort.py -o dynamic timeline.plaso "date > '2024-01-01'"

# Get timeline info
pinfo.py timeline.plaso

# Export to Excel format
psort.py -o xlsx -w timeline.xlsx timeline.plaso
```

### Oletools (Document Analysis)

```bash
# Analyze Office document
olevba suspicious.docm

# Identify file type
oleid document.doc

# Extract macros
olevba -c document.xlsm

# Detect malicious indicators
olevba --decode document.pptm

# Analyze all files in directory
olevba -r /mnt/c/Evidence/

# JSON output
olevba --json document.doc > analysis.json
```

### File Carving & Analysis

```bash
# Bulk Extractor
bulk_extractor -o output_dir disk.dd

# Foremost (file carving)
foremost -i disk.dd -o carved_files

# Strings from binary
strings -a suspicious.exe > strings.txt
strings -el suspicious.exe > strings_unicode.txt

# Binwalk (firmware analysis)
binwalk suspicious.bin
binwalk -e firmware.bin  # Extract

# File type identification
file suspicious.bin
file -b suspicious.exe  # Brief output
```

### Disk Analysis (Sleuth Kit)

```bash
# List partitions
mmls disk.dd

# File system info
fsstat -o 2048 disk.dd

# List files and directories
fls -r -o 2048 disk.dd

# Extract file by inode
icat -o 2048 disk.dd 12345 > extracted_file

# File timeline
fls -r -m C: -o 2048 disk.dd > bodyfile
mactime -b bodyfile -d > timeline.csv

# Find deleted files
fls -r -d -o 2048 disk.dd
```

---

## 🔧 KAPE Commands

```powershell
# Collect common artifacts
.\kape.exe --tsource C: --tdest C:\Evidence\KAPE --target !SANS_Triage

# Collect specific target
.\kape.exe --tsource C: --tdest C:\Evidence\KAPE --target EventLogs

# List available targets
.\kape.exe --tlist

# Process collected data
.\kape.exe --msource C:\Evidence\KAPE --mdest C:\Evidence\Processed --module !EZParser

# Collect and process in one command
.\kape.exe --tsource C: --tdest C:\Evidence\KAPE --target !SANS_Triage --msource C:\Evidence\KAPE --mdest C:\Evidence\Processed --module !EZParser

# Create VHDX container
.\kape.exe --tsource C: --tdest C:\Evidence\KAPE --target !SANS_Triage --vhdx Case001

# Transfer over network
.\kape.exe --tsource C: --tdest \\server\share\evidence --target !SANS_Triage
```

---

## 📊 Eric Zimmerman Tools

### Registry Explorer (CLI - RECmd)

```powershell
# Parse registry hive
cd C:\Tools\ZimmermanTools
.\RECmd.exe -f C:\Windows\System32\config\SYSTEM --bn BatchExamples\SYSTEM.reb

# Export to CSV
.\RECmd.exe -f SYSTEM --bn SYSTEM.reb --csv C:\Reports
```

### Prefetch Parser (PECmd)

```powershell
# Parse single prefetch file
.\PECmd.exe -f C:\Windows\Prefetch\CALC.EXE-AB12CD34.pf

# Parse all prefetch
.\PECmd.exe -d C:\Windows\Prefetch --csv C:\Reports --csvf prefetch.csv

# HTML output
.\PECmd.exe -d C:\Windows\Prefetch --html C:\Reports
```

### Jump List Parser (JLECmd)

```powershell
# Parse jump lists
.\JLECmd.exe -d C:\Users\user\AppData\Roaming\Microsoft\Windows\Recent --csv C:\Reports

# Specific file
.\JLECmd.exe -f AutomaticDestinations\1234abcd.automaticDestinations-ms
```

### AmCache Parser

```powershell
# Parse AmCache
.\AmcacheParser.exe -f C:\Windows\AppCompat\Programs\Amcache.hve --csv C:\Reports

# Include unassociated entries
.\AmcacheParser.exe -f Amcache.hve -i --csv C:\Reports
```

### ShellBags Explorer (CLI - SBECmd)

```powershell
# Parse user shellbags
.\SBECmd.exe -d C:\Users\user\NTUSER.DAT --csv C:\Reports

# Live registry
.\SBECmd.exe -l --csv C:\Reports
```

---

## 🔍 Network Forensics

### Wireshark (tshark CLI)

```bash
# Capture live traffic
tshark -i eth0 -w capture.pcap

# Read pcap file
tshark -r capture.pcap

# Filter HTTP traffic
tshark -r capture.pcap -Y "http"

# Extract HTTP objects
tshark -r capture.pcap --export-objects http,./http_objects

# DNS queries
tshark -r capture.pcap -Y "dns.qry.name" -T fields -e dns.qry.name

# Statistics
tshark -r capture.pcap -q -z conv,ip
tshark -r capture.pcap -q -z http,tree
```

### Network Commands (Windows)

```powershell
# Current connections
netstat -ano

# Routing table
route print

# ARP cache
arp -a

# DNS cache
ipconfig /displaydns

# Clear DNS cache
ipconfig /flushdns

# Network configuration
ipconfig /all
```

---

## 🧪 Hash & Comparison

```powershell
# Windows - Calculate hashes
certutil -hashfile file.exe MD5
certutil -hashfile file.exe SHA256
Get-FileHash file.exe -Algorithm SHA256

# Linux - Calculate hashes
md5sum file
sha256sum file
sha1sum file

# Compare directories
# Windows
FC /B file1.exe file2.exe

# Linux
diff file1 file2
cmp file1 file2
```

---

## 📋 One-Liners

### Quick Triage

```powershell
# Windows - Quick system snapshot
Get-Process > processes.txt
Get-Service > services.txt
Get-NetTCPConnection > connections.txt
Get-ScheduledTask > tasks.txt
ipconfig /all > network.txt

# Create evidence collection
$date = Get-Date -Format "yyyyMMdd_HHmmss"
$folder = "C:\Triage_$date"
New-Item -ItemType Directory -Path $folder
Get-Process | Export-Csv "$folder\processes.csv"
Get-Service | Export-Csv "$folder\services.csv"
Get-NetTCPConnection | Export-Csv "$folder\connections.csv"
```

### Suspicious File Hunt

```powershell
# Files created in last 24 hours in suspicious locations
Get-ChildItem -Path C:\Windows\Temp,C:\Users\*\AppData\Local\Temp -Recurse -File |
    Where-Object {$_.CreationTime -gt (Get-Date).AddDays(-1)} |
    Select-Object FullName, CreationTime, Length
```

### Memory Acquisition

```powershell
# Using DumpIt (if available)
.\DumpIt.exe /O C:\Evidence\memory.raw

# Using PowerShell (on modern Windows)
# Note: Requires admin and specialized tools
```

---

## 🎯 Investigation Workflow

### 1. Preserve Evidence
```powershell
# Create case folder with timestamp
$case = "Case_$(Get-Date -Format 'yyyyMMdd_HHmmss')"
New-Item -ItemType Directory -Path "C:\Cases\$case"
Set-Location "C:\Cases\$case"
```

### 2. Collect Volatile Data
```powershell
# Network, processes, memory
Get-NetTCPConnection | Export-Csv volatile_network.csv
Get-Process | Export-Csv volatile_processes.csv
```

### 3. Collect Artifacts
```powershell
# KAPE collection
C:\Tools\KAPE\kape.exe --tsource C: --tdest "C:\Cases\$case\artifacts" --target !SANS_Triage
```

### 4. Timeline Creation
```bash
# In WSL
log2timeline.py --storage-file /mnt/c/Cases/$case/timeline.plaso /mnt/c
psort.py -o l2tcsv -w /mnt/c/Cases/$case/timeline.csv /mnt/c/Cases/$case/timeline.plaso
```

### 5. Analysis & Reporting
```powershell
# Open Timeline Explorer
C:\Tools\ZimmermanTools\TimelineExplorer\TimelineExplorer.exe "C:\Cases\$case\timeline.csv"
```

---

## 📚 Quick Reference Links

**Windows Event IDs:**
- 4624: Successful logon
- 4625: Failed logon
- 4634: Logoff
- 4688: Process created
- 4720: User account created
- 4740: Account locked out
- 7045: Service installed

**Registry Locations:**
- `HKLM\Software\Microsoft\Windows\CurrentVersion\Run` - Auto-start programs
- `HKLM\System\CurrentControlSet\Services` - Services
- `HKCU\Software\Microsoft\Windows\CurrentVersion\Explorer\RecentDocs` - Recent docs
- `HKLM\System\CurrentControlSet\Enum\USBSTOR` - USB devices

**Artifact Locations:**
- `C:\Windows\Prefetch\` - Prefetch files
- `C:\$MFT` - Master File Table
- `C:\Windows\System32\winevt\Logs\` - Event logs
- `C:\Windows\System32\config\` - Registry hives

---

**Save this cheat sheet and print it for quick reference during investigations! 📌**
