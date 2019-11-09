import datetime
import os
import json
import socket    
from port_scanner import search
from ip2geotools.databases.noncommercial import DbIpCity


class TextColors:
    HEADER = '\033[95m'
    BLUE = '\033[94m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    RED = '\033[91m'
    END = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'


def displayASCII():
    print("  _____             __ _            _   ")
    print(" / ____|           / _(_)          | |  ")
    print("| |     ___  _ __ | |_ _ _ __   ___| |_ ")
    print("| |    / _ \| '_ \|  _| | '_ \ / _ \ __|")
    print("| |___| (_) | | | | | | | | | |  __/ |_ ")
    print(" \_____\___/|_| |_|_| |_|_| |_|\___|\__|\n")     
    print("--help or -h for menu")
    print("--quit or -q to exit\n")


def prettyListPrint(ugly_list, message):
    size = len(ugly_list)
    if size == 0:
        print(TextColors.RED + "[\n    Empty\n]\n" + TextColors.END)
        return
    print(TextColors.GREEN + "[ " + message + TextColors.END)
    for i in range(0, size, 3):
        print(TextColors.GREEN + ("    %s" % ugly_list[i]) + TextColors.END, end="")
        if i+1 < size:
            print(TextColors.GREEN + (" %s" % ugly_list[i+1]) + TextColors.END, end="")
        if i+2 < size:
            print(TextColors.GREEN + (" %s" % ugly_list[i+2]) + TextColors.END)
    print(TextColors.GREEN + "\n]\n" + TextColors.END)


def getMetaData(file):
    try:
        stats = os.stat(file)
        metadata = "File Size: " + str(stats.st_size) + " bytes\n"
        metadata += "File Modified: " + str(datetime.datetime.fromtimestamp(stats.st_mtime / 1000.0)) + "\n"
        metadata += "I-node: " + str(stats.st_ino) + "\n"
        metadata += "Device: " + str(stats.st_dev) + "\n"
        metadata += "Hardlinks: " + str(stats.st_nlink) + "\n"
        metadata += "User Id (uid): " + str(stats.st_uid) + "\n"
        metadata += "Group Id (gid): " + str(stats.st_gid) + "\n"
        metadata += "NOTE: On a Windows systems these values may not be accurate\n"
        print(metadata)
    except:
        print("ERROR: Failed to get information from", file)


def whoAmI():
    hostname = socket.gethostname()    
    ipaddr = socket.gethostbyname(hostname)    
    print("Your computer's name is:", hostname)    
    print("Your computer's IP address is:", ipaddr) 


def getIpAddressData(ipaddr):
    try:
        response = DbIpCity.get(ipaddr, api_key="free")
        data = "IP: " + response.ip_address + "\n"
        data += "City: " + response.city + "\n"
        data += "Country: " + response.country + "\n"
        data += "Region: " + response.region + "\n"
        data += "Latitude: " + str(response.latitude) + "\n"
        data += "Longitude: " + str(response.longitude) + "\n"
        print(data)
    except:
        print(TextColors.RED + "Could not fetch location for " + ipaddr + TextColors.END)


def whoisLookup(ipaddr, outfile=None):
    pass


def printHelpMenu():
    print(TextColors.GREEN + "\n---- Command List ----\n" + TextColors.END)

    print("scan")
    print("\n\t- Displays all open ports within the specified range on the provided IP address")
    print("\t-   Usage: scan IP_ADDRESS LOWER_PORT UPPER_PORT")
    print("\t- Example: scan 127.0.0.1 10000 25000\n")

    print("locate")
    print("\n\t- Finds the country where the given IP address is located")
    print("\t-   Usage: locate IP_ADDRESS")
    print("\t- Example: locate 127.0.0.1\n")

    print("whois")
    print("\n\t- Looks up IP address information from whois search tool")
    print("\t-   Usage: whois IP_ADDRESS")
    print("\t- Example: whois 127.0.0.1\n")

    print("whoami")
    print("\n\t- Retrieve IP address and name of your device")
    print("\t-   Usage: whoami\n")

    print("meta")
    print("\n\t- Displays meta data about a file")
    print("\t-   Usage: meta SOME_FILE")
    print("\t- Example: meta ./src/file.txt\n")
    

if __name__ == "__main__":

    displayASCII()
    while True:

        # Read in input from the user and split it
        command = str(input(TextColors.BLUE + "command$ " + TextColors.END)).strip()
        if command == "--help" or command == "-h":
            printHelpMenu()
            continue
        if command == "--quit" or command == "-q":
            print("\nGoodbye!")
            break
        tokens = command.split(" ")
        argc = len(tokens)

        # Scan available ports on a network
        if command.startswith("scan"):
            if argc == 4:
                results = search(tokens[1], tokens[2], tokens[3])
                prettyListPrint(results, "Open Ports Found")
            else:
                print("USAGE: scan IP_ADDRESS LOWER_PORT UPPER_PORT")
        
        # Get the location of the given IP address
        elif command.startswith("locate"):
            if argc == 2:
                getIpAddressData(tokens[1])
            else:
                print("USAGE: locate 127.0.0.1")
        
        # Get information from the whois tool about an IP address
        elif command.startswith("whois"):
            if argc == 2:
                whoisLookup(tokens[1], None)
            else:
                print("USAGE: whois 127.0.0.1")

        # Get information about your device
        elif command.startswith("whoami"):
            whoAmI()

        # Get meta data about a file
        elif command.startswith("meta"):
            if argc == 2:
                getMetaData(tokens[1], None)
            else:
                print("USAGE: meta file.txt")

        # Unrecognized command
        else:
            print("ERROR: Command not recognized")
