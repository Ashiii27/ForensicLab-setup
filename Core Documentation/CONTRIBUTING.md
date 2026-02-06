# Contributing to DFIR Home Lab

First off, thank you for considering contributing to this project! 🎉

This document provides guidelines for contributing to the DFIR Home Lab project.

## 📋 Table of Contents

- [Code of Conduct](#code-of-conduct)
- [How Can I Contribute?](#how-can-i-contribute)
- [Reporting Bugs](#reporting-bugs)
- [Suggesting Enhancements](#suggesting-enhancements)
- [Pull Request Process](#pull-request-process)
- [Style Guidelines](#style-guidelines)

## 📜 Code of Conduct

### Our Pledge

We are committed to providing a welcoming and inclusive environment for everyone, regardless of:
- Experience level
- Gender identity and expression
- Sexual orientation
- Disability
- Personal appearance
- Body size
- Race
- Ethnicity
- Age
- Religion
- Nationality

### Our Standards

**Positive behavior includes:**
- Using welcoming and inclusive language
- Being respectful of differing viewpoints
- Gracefully accepting constructive criticism
- Focusing on what's best for the community
- Showing empathy towards others

**Unacceptable behavior includes:**
- Harassment of any kind
- Trolling or insulting comments
- Public or private harassment
- Publishing others' private information
- Other unethical or unprofessional conduct

## 🤝 How Can I Contribute?

### 1. Reporting Bugs

Before creating a bug report:
- ✅ Check existing issues to avoid duplicates
- ✅ Update to the latest version
- ✅ Verify the issue is reproducible

**When reporting bugs, include:**
- Clear, descriptive title
- Exact steps to reproduce
- Expected vs actual behavior
- Screenshots (if applicable)
- Environment details:
  - Host OS and version
  - VirtualBox version
  - Windows VM version
  - Tool versions
- Error messages or logs

**Example:**

```markdown
**Bug**: FTK Imager fails to capture memory

**Steps to Reproduce:**
1. Open FTK Imager as Administrator
2. File → Capture Memory
3. Click "Capture"

**Expected**: Memory capture starts
**Actual**: Error "Access Denied"

**Environment:**
- Host: Windows 11 Pro 23H2
- VirtualBox: 7.0.14
- Guest: Windows Server 2019
- FTK Imager: 4.7.1.2

**Error Log:**
[Paste error message here]
```

### 2. Suggesting Enhancements

Enhancement suggestions are welcome! Include:
- Clear, descriptive title
- Detailed explanation of the enhancement
- Why this enhancement would be useful
- Examples of how it would work
- Potential drawbacks or considerations

**Enhancement Categories:**
- 🛠 New tool additions
- 📝 Documentation improvements
- 🎓 New learning projects
- ⚡ Performance optimizations
- 🔧 Configuration improvements
- 🐛 Bug fixes

### 3. Contributing Code

**Types of contributions:**
- PowerShell scripts for automation
- Python scripts for analysis
- Documentation updates
- Tutorial additions
- Tool installation guides
- Troubleshooting solutions

### 4. Contributing Documentation

Documentation improvements are highly valued:
- Fix typos or grammar
- Clarify confusing sections
- Add missing steps
- Update outdated information
- Add screenshots or diagrams
- Translate to other languages

## 🔄 Pull Request Process

### Before Submitting

1. **Fork the repository**
2. **Create a feature branch:**
   ```bash
   git checkout -b feature/your-feature-name
   ```
3. **Make your changes**
4. **Test thoroughly** in a clean VM
5. **Update documentation** if needed
6. **Commit with clear messages:**
   ```bash
   git commit -m "Add: Volatility3 automation script"
   git commit -m "Fix: KAPE installation path issue"
   git commit -m "Docs: Update WSL installation steps"
   ```

### Commit Message Guidelines

Use conventional commits:
- `Add:` - New features, tools, or scripts
- `Fix:` - Bug fixes
- `Update:` - Updates to existing content
- `Docs:` - Documentation changes
- `Refactor:` - Code refactoring
- `Test:` - Adding or updating tests
- `Style:` - Formatting changes

**Examples:**
```
Add: Automated Plaso timeline generation script
Fix: VirtualBox Guest Additions mounting issue
Update: FTK Imager to version 4.8
Docs: Clarify WSL1 vs WSL2 requirements
```

### Submitting the Pull Request

1. **Push to your fork:**
   ```bash
   git push origin feature/your-feature-name
   ```

2. **Create Pull Request** with:
   - Clear title summarizing changes
   - Detailed description of what and why
   - Reference related issues: `Fixes #123`
   - Screenshots/output if applicable
   - Testing performed

3. **PR Template:**

   ```markdown
   ## Description
   Brief description of changes

   ## Type of Change
   - [ ] Bug fix
   - [ ] New feature
   - [ ] Documentation update
   - [ ] Performance improvement

   ## Testing
   - [ ] Tested on Windows Server 2019
   - [ ] Tested on Windows 10
   - [ ] Tested in clean VM
   - [ ] Documentation verified

   ## Screenshots
   (if applicable)

   ## Related Issues
   Fixes #(issue number)
   ```

### Review Process

- Maintainers will review within 3-5 business days
- Address feedback and requested changes
- Once approved, PR will be merged
- You'll be added to contributors list! 🎉

## 📝 Style Guidelines

### PowerShell Scripts

```powershell
# Use clear, descriptive names
function Get-ForensicArtifacts {
    [CmdletBinding()]
    param(
        [Parameter(Mandatory=$true)]
        [string]$TargetPath,
        
        [Parameter(Mandatory=$false)]
        [string]$OutputPath = "C:\Evidence"
    )
    
    # Add comments for complex logic
    try {
        # Implementation
    }
    catch {
        Write-Error "Error: $_"
    }
}

# Use approved verbs
# Use proper error handling
# Include help documentation
```

### Python Scripts

```python
#!/usr/bin/env python3
"""
Module docstring describing purpose
"""

import argparse
import logging

def main():
    """Main function with clear purpose"""
    parser = argparse.ArgumentParser(
        description='Clear description'
    )
    # Use argparse for CLI
    # Use logging instead of print
    # Follow PEP 8 style guide
    
if __name__ == "__main__":
    main()
```

### Documentation (Markdown)

- Use clear headers (H1-H4)
- Include code blocks with syntax highlighting
- Add emoji for visual organization 🎯
- Use tables for structured data
- Include examples and outputs
- Link to related resources

**Example:**

```markdown
### Installing Volatility3

1. **Update system packages:**
   ```bash
   sudo apt update && sudo apt upgrade -y
   ```

2. **Install Volatility3:**
   ```bash
   pip3 install volatility3
   ```

3. **Verify installation:**
   ```bash
   vol.py -h
   ```

**Expected output:**
```
Volatility 3 Framework 2.x.x
...
```
```

### File Naming Conventions

- Scripts: `lowercase_with_underscores.ps1`
- Documentation: `PascalCase.md`
- Configs: `lowercase-with-hyphens.conf`

**Examples:**
- `collect_event_logs.ps1`
- `InstallationGuide.md`
- `volatility-config.conf`

## 🧪 Testing Requirements

### For Scripts

- Test in clean VM snapshot
- Test with different Windows versions
- Handle errors gracefully
- Provide clear error messages
- Include usage examples

### For Documentation

- Follow existing format
- Verify all commands work
- Check all links are valid
- Proofread for typos
- Test on different markdown renderers

## 📦 Adding New Tools

When proposing a new tool:

1. **Justification:**
   - Why is this tool needed?
   - What gap does it fill?
   - Is it actively maintained?

2. **Requirements:**
   - Installation instructions
   - Dependencies
   - License compatibility
   - System requirements

3. **Documentation:**
   - Basic usage guide
   - Example use case
   - Integration with existing tools

## 🏆 Recognition

Contributors will be:
- Added to README contributors section
- Mentioned in release notes
- Credited in related documentation

## 📞 Questions?

- Open an issue with the `question` label
- Reach out to maintainers
- Join community discussions

## 🙏 Thank You!

Your contributions help make digital forensics education more accessible to everyone!

---

**Remember:** Quality over quantity. Small, well-tested contributions are better than large, untested ones.

Happy contributing! 🚀
