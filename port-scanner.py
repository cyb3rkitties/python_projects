import socket
import termcolor

def scan(targets, ports):

    print(f"\nStarting to scan target {targets}")
    for port in range(1, ports):
        scan_port(targets, port)

def scan_port(ipaddress, port):
    try:
        sock = socket.socket()
        sock.connect((ipaddress, port))
        print(f"[+] Port {port} Open")
        sock.close()
    except:
        pass

targets = input("Enter target IP addresses to be scanned, separated by a space: ")
ports = int(input("Enter number of port to be scanned: "))

if " " in targets:
    print(termcolor.colored(("Scanning multiple targets"), 'magenta'))

    for ip_add in targets.split(" "):
        scan(ip_add, ports)

else:
    scan(targets, ports)