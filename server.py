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
                msgStr = input("Please enter the message to send to receivers \nOr type 'close' to close the connection:  ")
                if msgStr[0:1].lower() == "c" or msgStr[0:3].lower() == "close":
                    sys.exit(0)
                else:
                    print("{}{}".format(HOST,PORT))
                    conn, addr = s.accept()
                    try:
                        with conn:
                                print('Connected by', addr)
                                while True:
                                    data = conn.recv(1024)
                                    data = data.decode()
                                    print('Message sent by client: ', data)
                                    if not data:
                                        break
                                    elif data == 'connect':
                                        filename = 'temp_log.json'
                                        f = open(filename, 'rb')
                                        msgStr=''
                                        for line in (f.readlines() [-1:]): 
                                            msgStr=line
                                        print('Hello From the Server {} is with data {}'.format(msgStr,data))
                                        conn.sendall(msgStr)
                                    else:
                                        conn.sendall(b'No available data')
                    except Exception as e:
                        print(e)
                        sys.exit(0)
                
        except KeyboardInterrupt as e:
            print('server is disconnecting')
            sys.exit(0)
