PROJECT: Suspicious IP Detection Tool

This project is split into two parts:
1. PowerShell script that collects the current network connections
2. Python script that checks the remote IPs against AbuseIPDB

HOW TO RUN:

1. Open PowerShell as Administrator
2. Run:
       ./collect_connections.ps1
   This creates connections.csv with all the active network connections.

3. Open ipchecker.py and add your AbuseIPDB API key.

4. Run the Python script:
       python ipchecker.py

5. The final output appears in analysis_report.json
