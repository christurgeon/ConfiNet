import threading # use this to concurrently search for open ports


def displayASCII():
    print("  _____             __ _            _   ")
    print(" / ____|           / _(_)          | |  ")
    print("| |     ___  _ __ | |_ _ _ __   ___| |_ ")
    print("| |    / _ \| '_ \|  _| | '_ \ / _ \ __|")
    print("| |___| (_) | | | | | | | | | |  __/ |_ ")
    print(" \_____\___/|_| |_|_| |_|_| |_|\___|\__|\n")     


if __name__ == "__main__":

    displayASCII()
    print("\n---- Command List ----\n")

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

    print("---- Optional Flags ----")
    print("\n-d")
    print("\n\t- Dumps the contents to a file")
    print("\t- Usage: -d file.txt")
    

    # -f means all that comes after it is a file path
    # Can enter text in a string "hello there"