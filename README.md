🔐 Digital Forensics Workstation – Home Lab Setup

A hands-on Digital Forensics & Incident Response (DFIR) homelab built using a Windows Virtual Machine with Ubuntu Linux via WSL. This project demonstrates how to create a professional forensic workstation using industry-recognized open-source and free tools for learning real-world investigations.

This lab is intended for training and practice purposes in a home environment.

🎯 Objective

Build a dedicated forensic workstation capable of:

Windows artifact analysis

Remote login investigations

Memory & disk forensics

Timeline creation

Log analysis

Malware & document inspection

🧱 Lab Architecture

Host Machine

VirtualBox (Type-2 Hypervisor)

Windows Server 2019 / Windows 10 VM

WSL1 + Ubuntu 20.04

Windows + Linux forensic tool stack

📋 Agenda

Workstation Setup Instructions

Tools Installation

Environment Configuration

Next Steps

Alternative Options

Why a Forensic Workstation

🛠 Workstation Setup Instructions
1️⃣ Install Hypervisor

Download and install VirtualBox

2️⃣ Install Windows Guest VM

Supported ISOs:

Windows Server 2019 (Recommended)

Windows 10 Enterprise

VM Requirements:

100GB Disk (Dynamic)

4GB+ RAM

2+ CPUs

NAT Networking

Post-install:

Install Guest Additions

Enable clipboard & drag/drop

Create initial snapshot

3️⃣ Enable WSL1 + Ubuntu

⚠️ VirtualBox does NOT support WSL2.

Enable WSL:

Enable-WindowsOptionalFeature -Online -FeatureName Microsoft-Windows-Subsystem-Linux


Install Ubuntu 20.04 manually and ensure WSL1:

wsl --set-default-version 1


Reboot and finish Ubuntu setup.

4️⃣ Configure Windows Environment (Forensic Best Practices)

Set timezone to UTC

Enable hidden files & extensions

Create folders:

C:\Cases

C:\Tools

Configure Microsoft Defender:

Disable cloud protection

Exclude C:\Cases and C:\Tools

🔧 Forensic Tools Installation
🐧 Linux (WSL)
sudo apt update
sudo apt install python3-pip
pip3 install volatility3 capstone oletools
sudo add-apt-repository ppa:gift/stable
sudo apt install plaso-tools


Tools:

Volatility3

Log2Timeline (Plaso)

Oletools

🪟 Windows

Core Tools:

FTK Imager

KAPE

Notepad++

Visual Studio Code

7-Zip

Firefox

Excel

Purpose:

Disk & Memory Imaging

Artifact Collection

Log Parsing

Timeline Creation

Data Analysis

📸 Snapshot

Once setup is complete, take a snapshot — this becomes your clean forensic baseline for every investigation.

📚 Why a Forensic Workstation?

Digital investigations require handling multiple artifact types across operating systems. Having a pre-built forensic workstation allows rapid response and consistent analysis without tool conflicts.

🚀 Next Steps

Practice Windows artifact analysis

Simulate remote login attacks

Capture memory dumps

Create timelines with Plaso

Perform malware triage

Document investigations

⚠️ Disclaimer

This lab is for educational purposes only. Do not use these tools on systems you do not own or have permission to analyze.

👨‍💻 Author

Ashish Kumar
