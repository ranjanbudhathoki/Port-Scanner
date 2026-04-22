
#making port scanner

import socket  #Build-in python library for network connections
import threading  #this helps to run multiple things at the same time
import datetime


PORT_SERVICES = {
    21:   "FTP",
    22:   "SSH",
    23:   "Telnet",
    80:   "HTTP",
    110:  "POP3",
    143:  "IMAP",
    443:  "HTTPS",
    3306: "MySQL",
    3389: "RDP",
    8080: "HTTP-Alt"
}

#threading.lock() prevents two threads from writing results at the same time
lock = threading.Lock()

#List to store all the open ports found during the scan
open_ports = []
def scan_port(host, port):
    """
    Tries to connect to given ports and returns true if port is open
     else closed.
     It can run inside a thread
    """
    try:
        #creates a new socket using IPv4 and TCP
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        #It sets time to wait for a  response and move on if np answer
        sock.settimeout(1)

        #Tries to connecr host on the given port
        #connect_ex returns 0 if port is open, non zero if failed
        result = sock.connect_ex((host, port))

        sock.close()

        if result == 0:
            service = get_service(port)

            with lock:
                print(f"Port {port:<5} is OPEN  ----> {service}")
                open_ports.append(port)

    #if unexpected error occurs then treat as closed
    except:
        pass

def get_service(port):
    """
    Looks up the service name for a given port number.
    Returns the service name if known, else returns unknown

    """
    return PORT_SERVICES.get(port, "Unknown")

#----Main Program-----

print("=" * 40)
print("       Python Port Scanner v3.0")
print("=" * 40)

# Get target host — strip() removes accidental spaces the user might type
host = input("Enter target host: ").strip()

# Validate port input — keep asking until they type a valid number
try:
    start_port = int(input("Enter start port: "))
    end_port = int(input("Enter end port:   "))
except ValueError:
    print("Invalid port number. Please enter numbers only.")
    exit()

# Record the exact time the scan started
start_time = datetime.datetime.now()
print(f"\nScan started at: {start_time.strftime('%H:%M:%S')}")
print(f"Scanning {host} on ports {start_port} to {end_port}...\n")

# Create one thread per port
threads = []
for port in range(start_port, end_port + 1):
    # Each thread runs scan_port() with its own port number
    thread = threading.Thread(target=scan_port, args=(host, port))
    threads.append(thread)
    thread.start()

# Wait for ALL threads to finish before continuing
for thread in threads:
    thread.join()

# Record end time and calculate how long the scan took
end_time = datetime.datetime.now()
duration = end_time - start_time

# Print summary
print(f"\n{'=' * 40}")
print(f"Scan complete in {duration.seconds}.{duration.microseconds // 1000:03d} seconds")
print(f"Open ports found: {len(open_ports)}")
print(f"{'=' * 40}")

# Save results to a text file
filename = f"scan_{host}_{start_port}-{end_port}.txt"
with open(filename, "w") as f:
    f.write(f"Scan Report\n")
    f.write(f"{'=' * 40}\n")
    f.write(f"Target:     {host}\n")
    f.write(f"Port Range: {start_port} - {end_port}\n")
    f.write(f"Scanned at: {start_time.strftime('%Y-%m-%d %H:%M:%S')}\n")
    f.write(f"Duration:   {duration.seconds}.{duration.microseconds // 1000:03d} seconds\n")
    f.write(f"{'=' * 40}\n\n")
    if open_ports:
        for port in sorted(open_ports):
            f.write(f"Port {port:<5} OPEN  -->  {get_service(port)}\n")
    else:
        f.write("No open ports found.\n")
    f.write(f"\n{'=' * 40}\n")

print(f"Results saved to: {filename}")


