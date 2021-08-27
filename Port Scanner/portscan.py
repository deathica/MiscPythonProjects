# Programmer: Deathica
# Date: 8/17/2021
# Program: Port Scanner
import socket
import sys as sys
from time import sleep
common = {21, 22, 23, 25, 53, 443, 110, 135, 137, 138, 139, 1433, 1434}
global userin
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
while True:
    userin = int(input("Please select an option:\n1. Scan commonly exposed ports. (21, 22, 23, 25, 53, 443, 110, 135, 137, 138, 139, 1433, 1434)\n2. Scan all possible ports. (MIGHT TAKE AWHILE!)\n3. Scan target port.\n4. Exit\n"))
    if userin != 4:
        target = input("Please enter target ip in x.x.x.x format.\nIf you would like to enter a domain, enter domain.\n")
    elif userin == 4:
        break
    if target == "domain":
        domainname = input("Enter domain name here.\n")
        target = socket.gethostbyname(domainname)
    if userin == 1:
        print("Scanning commonly exposed ports, please wait...")
        for val in common:
            location = (target, val)
            result_of_check = s.connect_ex(location)
            if result_of_check == 0:
                print("Port " + str(val) + " is open.")
            else:
                print("Port " + str(val) + " is closed.")
            s.close
        sleep(1)
    if userin == 2:
        print("Scanning every port.")
        for i in range(1, 65536):
            location = (target, i)
            result_of_check = s.connect_ex(location)
            if result_of_check == 0:
                print("Port " + str(i) + " is open.")
            else:
                print("Port " + str(i) + " is closed.")
            s.close()
        sleep(1)
    if userin == 3:
        targetport = int(input("Enter target port.\n"))
        print("Scanning port, please wait...")
        location = (target, targetport)
        result_of_check = s.connect_ex(location)
        if result_of_check == 0:
            print("Port " + str(targetport) + " is open.")
        else:
            print("Port " + str(targetport) + " is closed.")
        s.close()
        sleep(1)
    cont = int(input("Press 1 to scan more ports, or 2 to close the program.\n"))
    if cont == 2:
        break
print("Shutting down, have a nice day.")
sleep(2)
sys.exit()
