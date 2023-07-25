import os
import time

x = input("please input target ip or domain:   ")
y = input("would you like to perform nikto scans?   ")
z = input("would you like to perform dirbuster scan?   ")


def nmapscan():
    os.system("nmap " + x + " > F_scan_nmap_scan")
    os.system("cat F_scan_nmap_scan")
    time.sleep(2)
    print("            ")
    print("performing second scan...")
    print("            ")
    os.system("sudo nmap -p- " + x + " > allports_scan")
    time.sleep(5)
    os.system("cat allports_scan | grep open | cut -d \"/\" -f1 | tr '\\n' ',' > ports")
    time.sleep(2)
    print("            ")
    print("performing third scan...")
    print("            ")
    os.system("sudo nmap -v -p $(cat ports) " + x + " -A > detailed_scan")
    os.system("cat detailed_scan")


nmapscan()
