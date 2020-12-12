#!/usr/bin/env python3
 
import socket
import sys
HOST = socket.gethostname()  # Standard loopback interface address (localhost)
PORT = 33000        # Port to listen on (non-privileged ports are > 1023)
while(True):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        try:
            s.bind((HOST, PORT))
            s.listen(5)
            while True:
                msgStr = input("Please enter a message or type 'yes' to close the connection:  ")
                if msgStr[0:1].lower() == "y" or msgStr[0:3].lower() == "yes":
                    sys.exit(0)
                print("{}{}".format(HOST,PORT))
                conn, addr = s.accept()
                with conn:
                    print('Connected by', addr)
                    while True:
                        data = conn.recv(1024)
                        data = data.decode()
                        print('Message sent by client: ', data)
                        if not data:
                            break
                        elif data == 'connect':
                            #msgStr = 'Hello From the Server {}'.format(HOST)
                            conn.sendall(msgStr.encode())
                        else:
                            conn.sendall(b'No available data')
                
        except KeyboardInterrupt as e:
            print('server is disconnecting')
            sys.exit(0)
