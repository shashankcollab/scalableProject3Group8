
#!/usr/bin/env python3

import socket
import threading 
import sys
HOST = socket.gethostname()  # Standard loopback interface address (localhost)
PORT = 33000        # Port to listen on (non-privileged ports are > 1023)
connections = []
peers = []

def broadcast_peers(peers):
    for connection in connections:
        peers = 'Peers currently in the network: {}'.format(peers)
        connection.send(peers.encode())
while(True):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        try:
            s.bind((HOST, PORT))
            s.listen(5)
            while True:
                msgStr = input("Please enter a message or type 'yes' to close the connection:  ")
                if msgStr[0:1].lower() == "y" or msgStr[0:3].lower() == "yes":
                    sys.exit(0)
                else:
                    print("{}{}".format(HOST,PORT))
                    conn, addr = s.accept()
                    connections.append(conn)
                    peers.append(addr)
                    print('Connected peers are: ', peers)
                    c_thread = threading.Thread(target=broadcast_peers, args = (peers))
                    c_thread.daemon = True
                    c_thread.start()

                    with conn:
                        print('Connected by', addr)
                        while True:
                            data = conn.recv(1024)
                            data = data.decode()

                            print('Message sent by peer: ', data)
                            if not data:
                                break
                            elif data == 'connect':
                                #msgStr = 'Hello From the Server {}'.format(HOST)
                                conn.send(msgStr.encode())
                            else:
                                conn.send(b'No available data')

        except KeyboardInterrupt as e:
            print('server is disconnecting')
            sys.exit(0)

