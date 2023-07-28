import os
import time

def main ():
    x = input ("please input target ip or domain:   ")
    z = input ("would you like to perform dirbuster scan? (y/n)   ")
    y = input ("would you like to perform nikto scans? (y/n)   ")

    nmapscan (x)
    gob (x, z)
    nikto (x, y)

def nmapscan (x):
    os.system ("nmap " + x + " > F_nmap_scan")
    os.system ("cat F_nmap_scan")
    
    time.sleep (2)
    
    print ("            ")
    print ("performing second scan...")
    print ("            ")
    os.system ("sudo nmap -p- " + x + " > second_allports_scan")
    os.system ("cat second_allports_scan")
    time.sleep (5)
    
    os.system ("cat second_allports_scan | grep open | cut -d \"/\" -f1 | tr '\\n' ',' > ports")
    
    time.sleep (2)
    
    print ("            ")
    print ("performing third scan...")
    print ("            ")
    os.system ("sudo nmap -v -p $(cat ports) " + x + " -A > third_Aggresive_scan")
    os.system ("cat third_scan")

def nikto (x, y):
    if y.lower () in ["y", "yes", "Yes", "YES" ""]:
        os.system ("nikto -h" + " " + x + " " + "> nikto_scan")
        time.sleep (60)
        os.kill ()
    else:
        print ("skipping nikto scan...")

def gob (x, y):
    if y.lower () in ["y", "yes", "Yes", "YES", ""]:
        os.system ("gobuster dir -u" + " " + x + " " + "-w /usr/share/wordlists/dirb/common.txt -t 4 --delay 1s -o gob_scan")
    else:
        print ("skipping gobuster scan...")

if __name__ == "__main__":
    main ()
