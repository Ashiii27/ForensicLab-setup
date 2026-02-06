# Case Template - [CASE ID]

**Status:** 🔴 Open | 🟡 In Progress | 🟢 Closed

---

## 📋 Case Information

| Field | Details |
|-------|---------|
| **Case ID** | CASE-2024-001 |
| **Case Name** | [Brief description] |
| **Date Opened** | YYYY-MM-DD HH:MM UTC |
| **Investigator** | [Your Name] |
| **Priority** | 🔴 High / 🟡 Medium / 🟢 Low |
| **Type** | Malware / Data Breach / Insider Threat / Other |

---

## 🎯 Incident Summary

### Initial Report
[Brief description of the incident as initially reported]

### Scope
- **Affected Systems:** [List systems]
- **Affected Users:** [List users]
- **Time Frame:** [Start] to [End]
- **Data at Risk:** [Description]

### Incident Timeline
| Time (UTC) | Event | Source |
|------------|-------|--------|
| 2024-02-06 14:30 | Initial alert received | SIEM |
| 2024-02-06 14:45 | Investigation started | SOC Analyst |
|  |  |  |

---

## 🔍 Evidence Collection

### Chain of Custody

| Evidence ID | Description | Source | Collected By | Date/Time | Hash (SHA256) |
|-------------|-------------|--------|--------------|-----------|---------------|
| E001 | Memory dump | WORKSTATION-01 | Analyst | 2024-02-06 15:00 | abc123... |
| E002 | Disk image | WORKSTATION-01 | Analyst | 2024-02-06 15:30 | def456... |
| E003 | Event logs | DC-01 | Analyst | 2024-02-06 16:00 | ghi789... |

### Evidence Location
```
C:\Cases\CASE-2024-001\
├── Evidence\
│   ├── E001_memory.raw
│   ├── E002_disk.E01
│   └── E003_eventlogs.zip
├── Analysis\
├── Reports\
└── Timeline\
```

---

## 🛠️ Tools Used

- [x] FTK Imager (Memory/Disk acquisition)
- [x] KAPE (Artifact collection)
- [ ] Volatility3 (Memory analysis)
- [ ] Timeline Explorer
- [ ] Wireshark
- [ ] Other: __________

---

## 📊 Analysis & Findings

### Initial Observations
[What was immediately noticed?]

### Detailed Analysis

#### 1. Memory Analysis
**Tool Used:** Volatility3
**Evidence ID:** E001

**Key Findings:**
- [ ] Suspicious processes identified
- [ ] Unusual network connections found
- [ ] Malicious DLLs detected
- [ ] Code injection identified

**Commands Run:**
```bash
vol.py -f E001_memory.raw windows.pslist
vol.py -f E001_memory.raw windows.netscan
vol.py -f E001_memory.raw windows.malfind
```

**Results:**
[Paste or summarize key outputs]

---

#### 2. Disk Forensics
**Tool Used:** [Tool name]
**Evidence ID:** E002

**Key Findings:**
- [ ] Malware files located
- [ ] Deleted files recovered
- [ ] Timeline anomalies
- [ ] Data exfiltration evidence

**File System Timeline:**
- Created: [Details]
- Modified: [Details]
- Accessed: [Details]

---

#### 3. Log Analysis
**Tool Used:** Windows Event Viewer / KAPE
**Evidence ID:** E003

**Key Events:**
| Event ID | Count | Description | Significance |
|----------|-------|-------------|--------------|
| 4624 | 45 | Successful logons | Check for unusual account/time |
| 4625 | 12 | Failed logons | Possible brute force |
| 4688 | 234 | Process creation | Check for suspicious processes |
| 7045 | 2 | Service installed | Possible persistence |

**Suspicious Activity:**
[Detail any anomalies]

---

#### 4. Network Analysis
**Tool Used:** [Tool name]
**Evidence ID:** [ID]

**External Connections:**
| IP Address | Port | Domain | Country | Reputation |
|------------|------|--------|---------|------------|
| 192.168.1.100 | 443 | example.com | US | Clean |
| 185.XX.XX.XX | 8080 | suspicious.ru | RU | 🔴 Malicious |

**C2 Communication:**
[Details of any command and control activity]

---

#### 5. Malware Analysis
**File Identified:** [malware.exe]
**Hash:** [SHA256]

**Static Analysis:**
- File Type: [PE32, DLL, etc.]
- Compile Time: [Date]
- Strings: [Notable strings]
- Imports: [Notable API calls]

**Dynamic Analysis:**
- Behavior: [Network, file, registry activity]
- IOCs: [List indicators]

**VirusTotal:** [XX/XX detections]

---

## 🎯 Indicators of Compromise (IOCs)

### File Hashes
```
SHA256:
- abc123def456... (malware.exe)
- 789ghi012jkl... (dropper.dll)

MD5:
- 1234567890abcdef...
```

### IP Addresses
```
185.XX.XX.XX (C2 Server)
203.XX.XX.XX (Scanning source)
```

### Domains
```
malicious-domain[.]com
evil-c2[.]ru
```

### File Paths
```
C:\Users\user\AppData\Local\Temp\malware.exe
C:\Windows\Temp\dropper.dll
```

### Registry Keys
```
HKLM\Software\Microsoft\Windows\CurrentVersion\Run\Malware
```

### Mutexes
```
Global\MalwareMutex123
```

---

## 🔐 Attack Reconstruction

### Attack Flow
```
1. [Initial Access] - Phishing email with malicious attachment
   ↓
2. [Execution] - User opens document, macro runs
   ↓
3. [Persistence] - Registry Run key created
   ↓
4. [Privilege Escalation] - Exploited vulnerability
   ↓
5. [Defense Evasion] - Disabled Windows Defender
   ↓
6. [Credential Access] - Dumped LSASS memory
   ↓
7. [Discovery] - Network reconnaissance
   ↓
8. [Lateral Movement] - Used stolen credentials
   ↓
9. [Collection] - Gathered sensitive files
   ↓
10. [Exfiltration] - Uploaded to external server
```

### MITRE ATT&CK Mapping
| Tactic | Technique | Sub-Technique | Observed |
|--------|-----------|---------------|----------|
| Initial Access | T1566 | Phishing | ✓ |
| Execution | T1204 | User Execution | ✓ |
| Persistence | T1547 | Registry Run Keys | ✓ |
| Privilege Escalation | T1068 | Exploitation | ✓ |
| Defense Evasion | T1562 | Disable Security Tools | ✓ |
| Credential Access | T1003 | LSASS Memory | ✓ |
| Discovery | T1046 | Network Scan | ✓ |
| Lateral Movement | T1021 | Remote Services | ✓ |
| Collection | T1005 | Local Data | ✓ |
| Exfiltration | T1041 | C2 Channel | ✓ |

---

## 📝 Conclusions

### Summary
[High-level summary of what happened]

### Root Cause
[Why did this incident occur?]

### Impact Assessment
- **Systems Affected:** [Number and list]
- **Data Compromised:** [Description and classification]
- **Business Impact:** [Description]
- **Estimated Cost:** [If applicable]

### Attribution (if applicable)
- **Actor:** [Unknown / APT group / Individual]
- **Motivation:** [Financial / Espionage / Hacktivism]
- **Confidence:** [Low / Medium / High]

---

## ✅ Remediation Actions

### Immediate Actions Taken
- [x] Isolated affected systems
- [x] Disabled compromised accounts
- [x] Blocked malicious IPs/domains
- [x] Removed malware
- [ ] Other: __________

### Short-term Recommendations (0-30 days)
1. Reset all passwords for affected accounts
2. Apply security patches to vulnerable systems
3. Update antivirus signatures
4. Review and update firewall rules
5. Implement additional monitoring

### Long-term Recommendations (30+ days)
1. Security awareness training for all users
2. Implement multi-factor authentication
3. Deploy EDR solution
4. Conduct penetration testing
5. Review and update incident response plan

---

## 📄 Documentation

### Reports Generated
- [ ] Executive Summary
- [ ] Technical Report
- [ ] Timeline Analysis
- [ ] IOC List
- [ ] Lessons Learned

### Files Attached
```
C:\Cases\CASE-2024-001\Reports\
├── Executive_Summary.docx
├── Technical_Report.pdf
├── Timeline.csv
├── IOC_List.csv
└── Screenshots\
```

---

## 🔄 Follow-up Actions

| Action | Assigned To | Due Date | Status |
|--------|-------------|----------|--------|
| Patch vulnerable systems | IT Admin | 2024-02-13 | 🟡 In Progress |
| User security training | HR | 2024-02-20 | 🔴 Not Started |
| Update IDS signatures | Security Ops | 2024-02-08 | 🟢 Complete |
|  |  |  |  |

---

## 📚 Lessons Learned

### What Went Well
1. [Item]
2. [Item]

### What Could Be Improved
1. [Item]
2. [Item]

### Action Items for Process Improvement
1. [Item]
2. [Item]

---

## ✍️ Sign-off

**Investigated By:**
- Name: [Your Name]
- Date: [Date]
- Signature: __________

**Reviewed By:**
- Name: [Supervisor]
- Date: [Date]
- Signature: __________

**Approved By:**
- Name: [Manager]
- Date: [Date]
- Signature: __________

---

## 📎 Appendices

### Appendix A: Full Timeline
[Link to detailed timeline CSV]

### Appendix B: Evidence Hashes
[Link to hash verification document]

### Appendix C: Tool Outputs
[Links to raw tool outputs]

### Appendix D: Screenshots
[Directory of screenshots]

---

**Case Status:** [Open/Closed]
**Last Updated:** YYYY-MM-DD HH:MM UTC
**Next Review:** YYYY-MM-DD

---

*This case template follows DFIR best practices and can be customized for your organization's needs.*
