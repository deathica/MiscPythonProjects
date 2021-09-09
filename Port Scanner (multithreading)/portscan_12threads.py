# Programmer: Deathica
# Date: 8/17/2021
# Program: Port Scanner with multithreading for 12 threads.
import socket
import sys as sys
from time import sleep
from multiprocessing import Process, Pool, Array, Manager, Value
common = {21, 22, 23, 25, 53, 110, 135, 137, 138, 139, 443, 445, 1433, 1434}
openports = []
userin = ""
count = 0
global target
iterable = []
mancount = Value("i", 0)
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
def scanner(port, target, manopenports):
    location = (target, port)
    global mancount
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            result_of_check = s.connect(location)
            print("Port " + str(port) + " is open.")
            with mancount.get_lock():
                mancount.value += 1
            manopenports.append(port)
    except Exception as e:
        print("Port " + str(port) + " is closed.")
        print(e)
while __name__ == "__main__":
    manager = Manager()
    manopenports = manager.list()
    mancount = manager.Value("i", 0)
    userin = int(input("Please select an option:\n1. Scan commonly exposed ports. (21, 22, 23, 25, 53, 110, 135, 137, 138, 139, 443, 445, 1433, 1434)\n2. Scan all possible ports. (MIGHT TAKE AWHILE!)\n3. Scan target port.\n4. Exit\n"))
    if userin != 4:
        target = input("Please enter target ip in x.x.x.x format.\nIf you would like to enter a domain, enter domain.\n")
    elif userin == 4:
        break
    if target == "domain":
        domainname = input("Enter domain name here.\n")
        target = socket.gethostbyname(domainname)
    for i in range(1, 65536):
        iterable.append((i, target, manopenports))
    if userin == 1:
        print("Scanning commonly exposed ports, please wait...")
        for val in common:
            location = (target, val)
            try:
                with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
                    result_of_check = s.connect(location)
                    print("Port " + str(val) + " is open.")
                    count += 1
                    openports.append(val)
            except Exception as e:
                print("Port " + str(val) + " is closed.")
                print(e)
        print("Open port count:", count)
        print("Open ports:", openports)
        count == 0
        openports == []
    if userin == 2:
        print("Scanning every port.")
        with Pool(processes = 12) as pool:
            pool.starmap(scanner, iterable)
        print("Open port count =", mancount.value)
        print("Open ports:", manopenports)
        mancount == 0
        manopenports == []
    if userin == 3:
        targetport = int(input("Enter target port.\n"))
        print("Scanning port, please wait...")
        location = (target, targetport)
        result_of_check = s.connect_ex(location)
        if result_of_check == 0:
            print("Port " + str(targetport) + " is open.")
        else:
            print("Port " + str(targetport) + " is closed.")
            print(result_of_check)
        s.close()
    cont = int(input("Press 1 to scan more ports, or 2 to close the program.\n"))
    if cont == 2:
        break
if __name__ == "__main__":
    print("Shutting down, have a nice day.")
    sleep(2)
    sys.exit()