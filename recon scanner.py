import socket
import subprocess
import whois

def ip_scanner():
    ip = input("Enter IP address: ")
    try:
        output = subprocess.check_output(["ping", "-c", "1", ip])
        print(f"[+] Host {ip} is reachable")
    except:
        print(f"[-] Host {ip} is not reachable")

def port_scanner():
    target = input("Enter target IP: ")
    ports = input("Enter ports (space separated): ").split()

    for port in ports:
        s = socket.socket()
        s.settimeout(1)
        result = s.connect_ex((target, int(port)))
        if result == 0:
            print(f"[+] Port {port} is OPEN")
        else:
            print(f"[-] Port {port} is CLOSED")
        s.close()

def subdomain_checker():
    domain = input("Enter domain (example.com): ")
    subs = input("Enter subdomains (space separated): ").split()

    for sub in subs:
        try:
            host = f"{sub}.{domain}"
            socket.gethostbyname(host)
            print(f"[+] Found: {host}")
        except:
            pass

def whois_lookup():
    domain = input("Enter domain: ")
    info = whois.whois(domain)
    print(info)

def dns_lookup():
    domain = input("Enter domain: ")
    subprocess.call(["nslookup", domain])

def main():
    while True:
        print("""
        
1. IP Scanner
2. Port Scanner
3. Subdomain Checker
4. WHOIS Lookup
5. DNS Lookup
0. Exit
""")
        choice = input("Choose option: ")

        if choice == "1":
            ip_scanner()
        elif choice == "2":
            port_scanner()
        elif choice == "3":
            subdomain_checker()
        elif choice == "4":
            whois_lookup()
        elif choice == "5":
            dns_lookup()
        elif choice == "0":
            break
        else:
            print("Invalid choice")

if __name__ == "__main__":
    main()

