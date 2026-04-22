#  Python Port Scanner
A command-line port scanner built in Python as a cybersecurity learning project.

## Features
- Scan any host or IP address
- Detects open ports across a custom port range
- Identifies common services (SSH, HTTP, FTP, etc.)
- Multi-threaded for fast scanning
- Saves results to a .txt report file

## Technologies Used
- Python 3
- socket — for network connections
- threading — for fast parallel scanning
- datetime — for tracking scan duration

## How to Run
1. Clone this repo
2. Open terminal in the project folder
3. Run: `python main.py`
4. Enter target host and port range when prompted

## Example Output
```
========================================
       Python Port Scanner v3.0
========================================
Enter target host: scanme.nmap.org
Enter start port: 1
Enter end port: 1000

Scanning scanme.nmap.org on ports 1 to 1000...

Port 22    is OPEN  -->  SSH
Port 80    is OPEN  -->  HTTP

Scan complete in 1.292 seconds
Open ports found: 2
Results saved to: scan_scanme.nmap.org_1-1000.txt
========================================
```

## Legal Notice
Only scan hosts you have permission to scan.
scanme.nmap.org is a free legal practice target provided by Nmap.

## Author
Ranjan Budhathoki
