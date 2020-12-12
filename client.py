#!/usr/bin/env python3
 
import socket
import sys
 
HOST = sys.argv[1]  # The server's hostname or IP address
PORT = 33000 # The port used by the server
msg = sys.argv[2]
while True:
    
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.connect((HOST, PORT))
            s.sendall(msg.encode())
            data = s.recv(1024)
        
        print('Received', repr(data))
    except Exception as e:
        print('No server alive dude')
        sys.exit(0)

    data = input("Please specify 'yes/no' if you want to close the connection: ")
    if data[0:3].lower() == "yes" or data[0:1].lower() == "y":
        sys.exit(0)

