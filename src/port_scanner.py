import socket
import threading
from threading import Lock, Thread

MAXPORT = 65535
mutex = Lock()

def searchHelper(ipaddr, start_port, end_port, open_ports):

    print("Creating thread ", threading.get_ident(), "...", sep="")

    for port in range(int(start_port), int(end_port)):
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        result = sock.connect_ex( (ipaddr, port) )
        if result == 0:
            mutex.acquire()
            open_ports.append(port)
            mutex.release()
        sock.close()


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
    open_ports = []
    diff = end_port - start_port
    if diff < 8:
        searchHelper(ipaddr, start_port, end_port, open_ports)
    else:
        base = diff / 8
        extra = diff % 8
        i = start_port
        thread_pool = []

        # Start threads that have one extra port to scan
        for i in range(extra):
            t = Thread(target=searchHelper, args=(ipaddr, i, i+base+1, open_ports)).start()
            thread_pool.append(t)
            i += base + 1

        # Start threads that have the default port to scan
        for i in range(7-extra):
            t = Thread(target=searchHelper, args=(ipaddr, i, i+base, open_ports)).start()
            thread_pool.append(t)
            i += base

        # Account for the upper bound port 
        t = Thread(target=searchHelper, args=(ipaddr, i, i+base+1, open_ports)).start()
        thread_pool.append(t)

        # Join the threads
        print(thread_pool)
        for thread in thread_pool:
            thread.join()
    return open_ports


