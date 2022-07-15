import icmplib
import socket
import concurrent.futures as conc
import sys
import itertools

hostdict = {}
def findhosts(tar):
    localip = socket.gethostbyname(socket.gethostname())
    localrange = ".".join(localip.split(".")[:3])
    try:
        target = localrange + "." + str(tar)
        result = (icmplib.ping(target, count=4, interval=0.1, timeout=2))
        print(target, result.is_alive)
        if result.is_alive == True:
            return target
        else:
            return None
    except Exception as e:
        print(e)
def portcheck(host, port):
    open_ports = []
    print(port)
    with socket.socket(socket.AF_INET, type=socket.SOCK_STREAM) as s:
        try:
            target = (host, port)
            port_check = s.connect(target)
            open_ports.append(port)
        except Exception as e:
            print(e)
    curdict = {host : open_ports}
    hostdict.update(curdict)
if __name__ == "__main__":
    alive_hosts = []
    with conc.ThreadPoolExecutor() as executor:
        for result in executor.map(findhosts, range(1, 255)):
            if result is not None:
                alive_hosts.append(result)
    for i in alive_hosts:
        print(f"Host {i} is alive!")
        while True:
            response = input(f"Would you like to perform a port scan on {i}? Y/N ")
            if response == "Y" or response == "y":
                while True:
                    ports = input("What ports would you like to scan? 1 - Custom Range; 2 - Preset List; 3 - Single Port; 4 - All Ports ")
                    if ports == "1":
                        portrange1 = input("Please provide the first in the range. ")
                        portrange2 = input(f"First port is {portrange1}. Please provide the second number in the range. ")
                        print(f"Now scanning ports {portrange1} through {portrange2} on target {i}.")
                        with conc.ThreadPoolExecutor() as executor:
                            for result in executor.map(portcheck, itertools.repeat(i), range(portrange1, portrange2+1)):
                                break
                    elif ports == "2":
                        portrange = [21, 22, 25, 26, 53, 80, 88, 110, 135, 143, 389, 443, 445, 636, 993, 995, 2077, 2078, 2082, 2083, 2086, 2087, 2095, 2096, 3306, 3268, 3269]
                        print(f"Now scanning {i} with a pre-dertmined range of ports.")
                        with conc.ThreadPoolExecutor() as executor:
                            for result in executor.map(portcheck, itertools.repeat(i), portrange):
                                pass
                        break
                    elif ports == "3":
                        targport = input("Please provide a port.")
                        if targport > 65535 or targport <= 0:
                            print("Invalid selection. Please select a number between 1 and 65535.")
                            break
                        else:
                            print(f"Scanning {i} on port {targport}.")
                            portcheck(i, targport)
                            break
                    elif ports == "4":
                        print(f"Scanning {i} on every port.")
                        fullrange = []
                        for i in range(1, 65536):
                            fullrange.append(i)
                        with conc.ThreadPoolExecutor as executor:
                            for result in executor.map(portcheck, itertools.repeat(i), portrange):
                                pass
                        break
                    else:
                        print("Please pick from the available options.")
                        pass
                break
            elif response == "N" or response == "n":
                pass
                break
            else:
                print("That was not a valid option.")
    print(hostdict)
    sys.exit()