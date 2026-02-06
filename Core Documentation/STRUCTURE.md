# 📁 Repository Structure

This document outlines the complete structure of the DFIR Home Lab repository and explains the purpose of each file and directory.

---

## 📂 Directory Tree

```
DFIR-Home-Lab/
│
├── README.md                           # Main documentation
├── LICENSE                             # MIT License
├── CONTRIBUTING.md                     # Contribution guidelines
├── QUICKSTART.md                       # Fast setup guide
├── .gitignore                          # Git ignore rules
│
├── scripts/                            # Automation scripts
│   ├── README.md                       # Scripts documentation
│   ├── verify_tools.ps1               # PowerShell tool verification
│   └── analyze_memory.py              # Python memory analysis
│
└── resources/                          # Reference materials
    ├── CHEATSHEET.md                  # Command reference
    └── Case_Template.md               # Investigation template
```

---

## 📄 File Descriptions

### Root Level Files

#### README.md
**Purpose:** Main repository documentation
**Contains:**
- Complete setup instructions (7-part guide)
- Tool installation procedures
- Hardware/software requirements
- Troubleshooting section
- Learning resources

**When to use:** Start here for complete lab setup

---

#### QUICKSTART.md
**Purpose:** Fast-track setup guide
**Contains:**
- 30-minute setup process
- Essential tools only
- Quick verification steps
- First investigation examples

**When to use:** When you want to get started quickly

---

#### LICENSE
**Purpose:** Legal terms for repository use
**Contains:**
- MIT License text
- Usage permissions
- Liability disclaimers

**When to use:** Check before using or distributing

---

#### CONTRIBUTING.md
**Purpose:** Guidelines for contributors
**Contains:**
- Code of conduct
- Contribution process
- Pull request guidelines
- Coding standards
- Testing requirements

**When to use:** Before submitting contributions

---

#### .gitignore
**Purpose:** Exclude unnecessary files from Git
**Contains:**
- Virtual machine files (*.vdi, *.vmdk)
- Evidence files (*.mem, *.dd, *.E01)
- Temporary files
- Build artifacts

**When to use:** Automatically used by Git

---

### 📁 scripts/

#### verify_tools.ps1
**Type:** PowerShell Script
**Purpose:** Verify DFIR tool installation

**Features:**
- Checks 25+ tools
- Identifies critical vs optional
- Color-coded output
- CSV report generation

**Usage:**
```powershell
.\verify_tools.ps1 -Detailed -ExportReport
```

**When to use:**
- After initial setup
- Before starting investigations
- During system maintenance

---

#### analyze_memory.py
**Type:** Python Script
**Purpose:** Automate Volatility3 memory analysis

**Features:**
- Runs 15+ Volatility plugins
- Basic and full analysis modes
- Multiple output formats (text, CSV, JSON)
- Generates summary report

**Usage:**
```bash
python3 analyze_memory.py -f memory.raw -o output_dir --full
```

**When to use:**
- Memory dump analysis
- Malware triage
- Incident response

---

#### scripts/README.md
**Purpose:** Scripts documentation
**Contains:**
- Detailed usage instructions
- Example commands
- Troubleshooting tips
- Script templates

**When to use:** Reference for script usage

---

### 📁 resources/

#### CHEATSHEET.md
**Type:** Reference Document
**Purpose:** Quick command reference

**Sections:**
- Windows forensics commands
- Linux/WSL commands
- Volatility3 syntax
- Plaso timeline creation
- Registry analysis
- Network forensics
- One-liners for common tasks

**When to use:**
- During active investigations
- When you need quick syntax
- Learning new commands

**Print recommendation:** Yes - keep as desktop reference

---

#### Case_Template.md
**Type:** Documentation Template
**Purpose:** Standardized investigation documentation

**Sections:**
- Case information
- Evidence collection
- Chain of custody
- Analysis findings
- IOC documentation
- MITRE ATT&CK mapping
- Remediation actions
- Lessons learned

**When to use:**
- Start of every investigation
- To maintain consistency
- For legal documentation

**How to use:**
1. Copy template to `C:\Cases\[CASE-ID]\`
2. Fill in as investigation progresses
3. Export to PDF when complete

---

## 🎯 Usage Workflows

### Initial Setup Workflow

```
1. Read README.md (Part 1-7)
   ↓
2. Install VirtualBox
   ↓
3. Create Windows VM
   ↓
4. Install WSL + Ubuntu
   ↓
5. Run verify_tools.ps1
   ↓
6. Take VM snapshot
   ✓ Ready for investigations
```

### Investigation Workflow

```
1. Copy Case_Template.md to case folder
   ↓
2. Collect evidence (FTK Imager, KAPE)
   ↓
3. Run analyze_memory.py (if memory dump)
   ↓
4. Reference CHEATSHEET.md for commands
   ↓
5. Document findings in case template
   ↓
6. Generate reports
   ✓ Case complete
```

### Maintenance Workflow

```
1. Monthly: Run verify_tools.ps1
   ↓
2. Update tools (Zimmerman tools, etc.)
   ↓
3. Run verify_tools.ps1 again
   ↓
4. Take new snapshot
   ✓ System maintained
```

---

## 📋 File Usage Matrix

| File | Beginner | Intermediate | Advanced | Frequency |
|------|----------|--------------|----------|-----------|
| README.md | ✓✓✓ | ✓✓ | ✓ | Once (setup) |
| QUICKSTART.md | ✓✓✓ | ✓ | - | Once (setup) |
| CONTRIBUTING.md | ✓ | ✓✓ | ✓✓✓ | As needed |
| verify_tools.ps1 | ✓✓✓ | ✓✓✓ | ✓✓✓ | Weekly/Monthly |
| analyze_memory.py | ✓✓ | ✓✓✓ | ✓✓✓ | Per case |
| CHEATSHEET.md | ✓✓✓ | ✓✓✓ | ✓✓ | Daily |
| Case_Template.md | ✓✓ | ✓✓✓ | ✓✓✓ | Per case |

**Legend:**
- ✓✓✓ Essential
- ✓✓ Recommended
- ✓ Optional
- `-` Not applicable

---

## 🔄 Version Control Best Practices

### What to Commit

✅ **DO commit:**
- All documentation (*.md files)
- Scripts (*.ps1, *.py)
- Configuration templates
- .gitignore file
- README files

❌ **DON'T commit:**
- Virtual machine files
- Evidence files
- Memory dumps
- Case files
- Personal notes
- Tool binaries

### Recommended .gitignore

Already included in repository root. Key exclusions:
- `*.vdi`, `*.vmdk` (VM disk files)
- `*.mem`, `*.raw` (Memory dumps)
- `*.dd`, `*.E01` (Disk images)
- `Evidence/`, `Cases/` (directories)

---

## 📊 File Maintenance Schedule

| File | Update Frequency | Reason |
|------|------------------|---------|
| README.md | Quarterly | New tools, updated procedures |
| CHEATSHEET.md | Monthly | New commands, updated syntax |
| verify_tools.ps1 | Quarterly | New tools added to lab |
| analyze_memory.py | As needed | New Volatility plugins |
| Case_Template.md | Annually | Process improvements |

---

## 🎓 Learning Path by File

### Week 1: Setup
1. Read QUICKSTART.md
2. Follow README.md (Parts 1-4)
3. Run verify_tools.ps1

### Week 2: Basic Skills
1. Study CHEATSHEET.md (Windows section)
2. Practice commands from cheatsheet
3. Complete "Your First Investigation" from QUICKSTART.md

### Week 3: Memory Forensics
1. Read analyze_memory.py documentation
2. Capture test memory dump
3. Run automated analysis
4. Study CHEATSHEET.md (Volatility section)

### Week 4: Case Management
1. Review Case_Template.md
2. Create practice case
3. Document findings
4. Generate reports

### Ongoing: Skill Development
- Reference CHEATSHEET.md daily
- Update Case_Template.md with lessons learned
- Contribute improvements (see CONTRIBUTING.md)

---

## 🔗 Cross-References

### README.md References
- Links to QUICKSTART.md for fast setup
- References CONTRIBUTING.md for improvements
- Points to scripts/ for automation
- Mentions resources/ for reference materials

### QUICKSTART.md References
- Simplified version of README.md setup
- Links to full README.md for details
- References verify_tools.ps1 for validation

### Scripts References
- analyze_memory.py uses commands from CHEATSHEET.md
- verify_tools.ps1 checks tools listed in README.md
- Scripts README.md provides context for both

### Resources References
- CHEATSHEET.md complements README.md
- Case_Template.md implements workflows from README.md
- Both support actual investigation work

---

## 💾 Backup Recommendations

### Critical Files (Backup Priority 1)
- Case_Template.md (with your customizations)
- verify_tools.ps1 (if modified)
- analyze_memory.py (if modified)
- Any custom scripts you create

### Important Files (Backup Priority 2)
- README.md (with your notes)
- CHEATSHEET.md (with your additions)
- CONTRIBUTING.md

### Standard Files (Version-Controlled)
- LICENSE
- .gitignore
- Default templates

**Recommendation:** Keep all customizations in Git or cloud backup

---

## 📝 Customization Guide

### Files You Should Customize

1. **Case_Template.md**
   - Add your organization's logo/header
   - Modify report structure
   - Add custom sections
   - Update approval workflow

2. **verify_tools.ps1**
   - Add organization-specific tools
   - Modify tool paths
   - Add custom checks

3. **CHEATSHEET.md**
   - Add frequently used commands
   - Document your workflows
   - Add organization-specific IOCs

### Files to Keep Standard

- LICENSE (legal document)
- .gitignore (functional configuration)
- README.md (general documentation)

---

## 🎯 Quick Reference: Which File When?

| Scenario | Use This File |
|----------|---------------|
| "I'm setting up for the first time" | QUICKSTART.md or README.md |
| "I need to verify my tools work" | verify_tools.ps1 |
| "I have a memory dump to analyze" | analyze_memory.py |
| "What's the command for...?" | CHEATSHEET.md |
| "I'm starting a new investigation" | Case_Template.md |
| "I want to contribute" | CONTRIBUTING.md |
| "Can I use this for commercial work?" | LICENSE |

---

## 🆘 Troubleshooting by File

| Issue | Relevant File | Section |
|-------|---------------|---------|
| VM won't start | README.md | Troubleshooting |
| Tool not found | verify_tools.ps1 | Run to identify |
| WSL problems | README.md | Part 3: WSL Setup |
| Volatility errors | CHEATSHEET.md | Volatility Commands |
| Memory analysis slow | analyze_memory.py | Use basic mode |
| Don't know how to document | Case_Template.md | Follow template |

---

## ✅ Repository Health Checklist

Run this quarterly to maintain repository quality:

- [ ] All links in README.md work
- [ ] verify_tools.ps1 includes all current tools
- [ ] CHEATSHEET.md syntax is current
- [ ] Case_Template.md reflects current workflow
- [ ] .gitignore excludes all evidence types
- [ ] All scripts have updated dates
- [ ] Documentation reflects latest tool versions
- [ ] CONTRIBUTING.md reflects current process

---

**This structure is designed to be:**
- ✅ Beginner-friendly
- ✅ Professionally organized
- ✅ Easy to maintain
- ✅ Scalable for growth

**Last Updated:** February 2026
