# Programmer: Deathica
# Date: 12/11/2023
# Program: Port Scanner tool.
from colorama import Fore, Back
from multiprocessing import Pool, Manager
import os
import socket
import sys as sys
import pyfiglet

txt = (Fore.GREEN + Back.BLACK)
common = [21, 22, 23, 25, 53, 80, 110, 135, 137, 138, 139, 443, 445, 1433, 1434, 3389]
userin = ""
target = ""
iterable = []
banner = pyfiglet.figlet_format("Port Scanner", font = "banner3")
subbanner = pyfiglet.figlet_format("By: Deathica", font = "mini")

def scanner(target, port, Global):
    location = (target, port)
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.connect(location)
            print("Port " + str(port) + " is open.")
            Global.count += 1
            Global.list = Global.list + str(port) + " "
    except Exception as e:
        print(port, "is closed.")

if __name__ == "__main__":
    os.system("cls")
    print(txt)
    print(banner)
    print(subbanner)

while __name__ == "__main__":
    man = Manager()
    Global = man.Namespace()
    Global.count = 0
    Global.list = ""
    userin = int(input("Please select an option:\n1. Scan commonly exposed ports.\n2. Scan all possible ports.\n3. Scan target port or ports.\n4. Exit\n"))
    if userin == 1 or userin == 2 or userin == 3:
        target = input("Please enter target ip in x.x.x.x format.\nIf you would like to enter a domain, enter domain.\n")
    elif userin == 4:
        break
    elif userin != 1 or userin != 2 or userin != 3 or userin != 4:
        print("Error. Provided input not one of the available options.")
        continue
    if target == "domain":
        domainname = input("Enter domain name here.\n")
        target = socket.gethostbyname(domainname)
    if userin == 1:
        print("Scanning commonly exposed ports, please wait...")
        count = 0
        for i in common:
            common[count] = [target, i, Global]
            count += 1
        with Pool() as pool:
            pool.starmap(scanner, common)
            print("Total open ports:", Global.count)
            print("Open ports:", Global.list)
    if userin == 2:
        if iterable.length() < 65535:
            for i in range(1, 65536):
                iterable.append(target, i, Global)
        print("Scanning every port.")
        with Pool() as pool:
            pool.starmap(scanner, iterable)
            print("Total open ports:", Global.count)
            print("Open ports:", Global.list)
    if userin == 3:
        targetports = input("Enter target port or ports with spaces between each port.\n")
        targetports = targetports.split(" ")
        print(targetports)
        if len(targetports) == 1:
            print("Scanning port, please wait...")
            location = (target, int(targetports[0]))
            try:
                with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
                    s.connect(location)
                    print("Port " + str(targetports[0]) + " is open.")
            except Exception as e:
                print("Port " + str(targetports[0]) + " is closed.")
        else:
            print("Scanning ports, please wait...")
            count = 0
            for i in targetports:
                targetports[count] = [target, int(i), Global]
                count += 1
            with Pool() as pool:
                pool.starmap(scanner, targetports)
                print("Total open ports:", Global.count)
                print("Open ports:", Global.list)
    try:
        cont = int(input("Press 1 to scan more ports, or 2 to close the program.\n"))
        if cont == 2:
            break
    except Exception as e:
        print(e)

if __name__ == "__main__":
    print("Shutting down, have a nice day.")
    print(Fore.WHITE, Back.BLACK)
    sys.exit()
