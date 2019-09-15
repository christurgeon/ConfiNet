import socket

MAXPORT = 65535


"""
add multithreading to the port search to make it much quicker
...
...
might need mutex locks for the add process
"""

def search(ip_addr, start_port, end_port):

    # Validate input 
    try:
        start_port = int(start_port)
        end_port = int(end_port)
    except:
        print("ERROR: Invalid port numbers entered")
    if start_port < 0 or end_port < 0:
        return -1
    if start_port > MAXPORT or end_port > MAXPORT:
        return -1
    if end_port < start_port:
        temp = start_port
        start_port = end_port
        end_port = temp

    # Check for open ports and add them to a list
    open_ports = []
    for port in range(start_port, end_port + 1):
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        result = sock.connect_ex( (ip_addr, port) )
        if result == 0:
            open_ports.append(port)
        sock.close()
    
    return open_ports

