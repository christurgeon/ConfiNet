import datetime
import os
from port_scanner import search

"""
Bandwidth Monitor - A small utility program that tracks how much data you have uploaded and downloaded 
from the net during the course of your current online session. See if you can find out what periods of 
the day you use more and less and generate a report or graph that shows it.
"""

class TextColors:
    HEADER = '\033[95m'
    BLUE = '\033[94m'
    GREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
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
    print("--help for menu")
    print("--quit to exit\n")


def getMetaData(file, outfile=None):
    output = ""
    try:
        stats = os.stat(file)
        output += "File Size: " + str(stats.st_size) + " bytes\n"
        output += "File Modified: " + str(datetime.datetime.fromtimestamp(stats.st_mtime / 1000.0)) + "\n"
        output += "I-node: " + str(stats.st_ino) + "\n"
        output += "Device: " + str(stats.st_dev) + "\n"
        output += "Hardlinks: " + str(stats.st_nlink) + "\n"
        output += "User Id (uid): " + str(stats.st_uid) + "\n"
        output += "Group Id (gid): " + str(stats.st_gid) + "\n"
        output += "NOTE: On a Windows systems these values may not be accurate\n"
        if outfile:
            output.write(output)
        else:
            print(output)
    except:
        print("ERROR: Failed to get information from", file)


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

    print("meta")
    print("\n\t- Displays meta data about a file")
    print("\t-   Usage: meta SOME_FILE")
    print("\t- Example: meta ./src/file.txt\n")

    print(TextColors.GREEN + "---- Optional Flags ----" + TextColors.END)
    print("\n-d")
    print("\n\t- Dumps the contents to a file")
    print("\t- Usage: -d file.txt\n")


if __name__ == "__main__":

    displayASCII()
    while True:

        command = str(input(TextColors.BLUE + "command$ " + TextColors.END))
        if command == "--help":
            printHelpMenu()
            continue
        if command == "--quit":
            print("\nGoodbye!")
            break

        tokens = command.split(" ")
        print(tokens, end="\n")

        if command.startswith("scan"):
            if len(tokens) == 4:
                search(tokens[1], tokens[2], tokens[3])
        elif command.startswith("locate"):
            continue
        elif command.startswith("whois"):
            continue
        elif command.startswith("meta"):
            getMetaData(tokens[1], None)
        else:
            print("ERROR: Command not recognized")