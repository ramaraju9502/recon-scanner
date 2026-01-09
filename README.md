# recon-scanner

ReconScanner – Network Reconnaissance Tool
📌 What is ReconScanner?

ReconScanner is a Python-based reconnaissance (information gathering) tool used in cybersecurity and ethical hacking.
It helps in collecting basic network and domain information about a target system.

Reconnaissance is the first phase of ethical hacking, where information is gathered before any attack or security testing.
----------------------------------------------------------------------------------------------------------------------------------------------------------------------

🎯 What is the Use of ReconScanner?

ReconScanner is used to:

Check whether a target IP is alive

Identify open and closed ports

Find valid subdomains

Get domain ownership details (WHOIS)

Perform DNS lookups

It is mainly useful for:

Cybersecurity students

Ethical hacking learning

Mini / academic projects

--------------------------------------------------------------------------------------------------------------------------------------------------------------------

🧩 Components of ReconScanner

ReconScanner consists of the following modules:

IP Scanner

Checks if a host is reachable using ping

Port Scanner

Scans user-specified ports using TCP sockets

Subdomain Checker

Finds valid subdomains using DNS resolution

WHOIS Lookup

Fetches domain registration details

DNS Lookup

Retrieves DNS records using nslookup

Main Menu

Menu-driven interface to access all features
----------------------------------------------------------------------------------------------------------------------------------------------------------------------
🛠 How ReconScanner is Made

Written in Python

Uses socket programming for port scanning

Uses system commands (ping, nslookup)

Uses WHOIS database lookup

Designed as a menu-driven CLI tool

Modular functions for each recon task
---------------------------------------------------------------------------------------------------------------------------------------------------------------------------
📚 Libraries Used

Library	Purpose

socket	Port scanning & DNS resolution

subprocess	Running system commands

whois	Fetching domain registration info
----------------------------------------------------------------------------------------------------------------------------------------------------------------------
📥 Installation in Kali Linux
Step 1: Update system
sudo apt update

Step 2: Install Python & pip
sudo apt install python3 python3-pip -y

Step 3: Install WHOIS Python library
pip3 install python-whois

Step 4: Clone the repository
git clone https://github.com/yourusername/ReconScanner.git

Step 5: Go to project directory
cd ReconScanner

Step 6: Run the tool
python3 reconscanner.py
--------------------------------------------------------------------------------------------------------------------------------------------------------------------
▶️ How to Use

After running the program, you will see:

======== ReconScanner ========
1. IP Scanner
2. Port Scanner
3. Subdomain Checker
4. WHOIS Lookup
5. DNS Lookup
0. Exit


Enter the option number

Provide required input (IP / domain / ports)

View output in terminal

This tool is creatd only for educational and ethical purposes.
Do not scan any system or domain without proper authorization.
The developer is not responsible for misuse
