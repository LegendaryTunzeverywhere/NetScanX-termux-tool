import requests
import os
from colorama import Fore
import sys
from art import *
import ipaddress
import socket

if os.name == 'posix':
   os.system('clear')
else:
   print(Fore.YELLOW+"\n[!] Unable to run NetScanX on this platform...\n"+Fore.WHITE)
   exit(0)

def banner():
    print(text2art("NetScanX"))
    print(Fore.RED+"[+] Owner: https://x.com/legendarytunzeverywhere\n"+Fore.WHITE)
    print(Fore.BLUE+"A security tool that looks up open ports and vulnerabilities...\n"+Fore.WHITE)
banner()

def get_help():
    print(Fore.YELLOW+"[!] python netscanx.py -t <ip address>\n"+Fore.WHITE)

if len(sys.argv) == 3:
   pass
else:
   get_help()
   exit(0)

if sys.argv[1] != '-t':
   get_help()
   exit(0)

if sys.argv[2] == "":
   get_help()
   exit()

def validate_ip(ip_str):
    try:
        ip_obj = ipaddress.ip_address(ip_str)
        return True
    except ValueError:
        return False

if validate_ip(sys.argv[2]) == True:
   pass
else:
   get_help()
   exit(0)

ip_addr = sys.argv[2]

try:
    data = requests.get("https://internetdb.shodan.io/{}".format(ip_addr)).json()
except requests.exceptions.ConnectionError:
    print(Fore.YELLOW+"[!] Error: requests.exceptions.ConnectionError...\n"+Fore.WHITE)
    exit(0)
 
ip = data.get('ip', '')
ports = data.get('ports', [])
vulns = data.get('vulns', [])

print(Fore.YELLOW+"IP ADDRESS - {}".format(ip_addr),Fore.WHITE)

print(Fore.BLUE+"\n-[OPEN PORTS]-\n"+Fore.WHITE)
for port in ports:
    service_name = socket.getservbyport(port)
    print(port, " - ", service_name)
print()

if len(vulns) == 0:
   print(Fore.BLUE+"-[VULNERABILITY STATUS]-\n"+Fore.WHITE)
   print(Fore.GREEN+"- Not Vulnerable\n"+Fore.WHITE)
else:
   print(Fore.BLUE+"-[VULNERABILITY STATUS]-\n"+Fore.WHITE)
   print(Fore.RED+"- Vulnerable"+Fore.WHITE)
   print(Fore.BLUE+"\n-[FOUND CVES]-\n"+Fore.WHITE)
   for v in vulns:
       print("https://www.cve.org/CVERecord?id="+v)

print()
exit()
