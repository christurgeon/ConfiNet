import os
import socket
import threading
from multiprocessing import Pool

MAXPORT = 65535

def searchHelper(args):
    print("Creating thread ", threading.get_ident(), "...", sep="")
    (ipaddr, start_port, end_port) = args
    open_ports = []
    for port in range(int(start_port), int(end_port)):
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        result = sock.connect_ex( (ipaddr, port) )
        if result == 0:
            open_ports.append(port)
        sock.close()
    return open_ports


def search(ipaddr, start_port, end_port):

    # Validate input 
    try:
        start_port = int(start_port)
        end_port = int(end_port)
    except:
        print("ERROR: Invalid port numbers entered")

    if start_port < 0 or end_port < 0:
        return list()
    if start_port > MAXPORT or end_port > MAXPORT:
        return list()
    if end_port < start_port:
        temp = start_port
        start_port = end_port
        end_port = temp

    # Create threads to look for open ports
    number_of_processors = os.cpu_count()
    diff = end_port - start_port
    list_of_args = []
    if diff < number_of_processors:
        results = searchHelper( (ipaddr, start_port, end_port) )
        return results
    else:
        base = diff // number_of_processors
        extra = diff % number_of_processors
        i = start_port

        # Start threads that have one extra port to scan
        for j in range(extra):
            list_of_args.append( (ipaddr, i, i+base+1) )
            i += base + 1

        # Start threads that have the default port to scan
        for j in range(7-extra):
            list_of_args.append( (ipaddr, i, i+base) )
            i += base

        # Account for the upper bound port 
        list_of_args.append( (ipaddr, i, i+base) )

        # Use thread pool to manage threads
        print("Preparing to search", diff, "ports using", number_of_processors, "processors at IP address", ipaddr)
        thread_pool = Pool(number_of_processors)
        results = thread_pool.map(searchHelper, list_of_args)
        return [x for y in results for x in y if x]        
        
