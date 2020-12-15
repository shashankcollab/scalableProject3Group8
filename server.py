#!/usr/bin/env python3
 
import socket
import sys
import dataprovider as dpr
import csv
import threading 
HOST = socket.gethostname()  # Standard loopback interface address (localhost)
PORT = 33000        # Port to listen on (non-privileged ports are > 1023)


def broadcast_peers(connections, peers):
    for connection in connections:
        peer = '_Peers currently in the network:_{}'.format(peers)
        print(f'peers in the network: {peer}')
        try:
            filename = 'temp_log.json'
            f = open(filename, 'rb')
            for line in (f.readlines() [-1:]): 
                msgStr=line
            #print('Hello From the Server {} is with data {}'.format(msgStr,data))
            byteStr = msgStr + peer.encode()
            print(byteStr)
            connection.sendall(byteStr)
        except Exception as e:
            pass

def run():
    connections = []
    peers = []
    while(True):
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            try:
                s.bind((HOST, PORT))
                s.listen(5)
                msgStr='connect'
                while True:
                    # if msgStr[0:1].lower() == "c" or msgStr[0:3].lower() == "close":
                    #     sys.exit(0)
                    if msgStr[0:1].lower() != "q" or msgStr[0:4].lower() != "quit":
                        print("------------ Server is running! ------------")
                        print("Waiting for connection in Host {} on Port {}".format(HOST,PORT))
                        conn, addr = s.accept()
                        if conn not in connections:
                            connections.append(conn)
                        if addr not in peers:
                            peers.append(addr)
                        print('Connected peers are: {}/n{}'.format( addr, conn))

                        #checkpeers(conn,addr)
                        try:
                            with conn:
                                    print('Connected by', addr)
                                    while True:
                                        data = conn.recv(1024)
                                        data = data.decode()
                                        print('Message sent by client: ', data)
                                        if not data:
                                            break
                                        elif checkconnect(data):
                                            c_thread = threading.Thread(target=broadcast_peers, args = (connections, peers))
                                            c_thread.daemon = True
                                            c_thread.start()
                                        else:
                                            conn.sendall(b'No available data')
                        except KeyboardInterrupt as e:
                            print('server is disconnecting')
                            sys.exit(0)
                        except Exception as e:
                            print(e)
                            sys.exit(0)
                        #msgStr = input("Please hit enter to send communuication to receivers \nOr type 'quit' to close the connection:  ")
                        #if msgStr[0:1].lower() == "q" or msgStr[0:4].lower() == "quit":
                            #print('closing connection')
                            #sys.exit(0)
                    else:
                        print('closing connection')
                        sys.exit(0)

            except KeyboardInterrupt as e:
                print('server is disconnecting')
                sys.exit(0)

def checkpeers(conn, addr):
    if conn not in connections:
        connections.append(conn)
    if addr not in peers:
        peers.append(addr)
    print('Connected peers are: {}/n{}'.format( addr, conn))
    #return connections, peers

def checkconnect(data):
    status=False
    csv_file = csv.reader(open('ourkey.csv', "r"), delimiter=",")
    for row in csv_file:
        if data in row:
            status= True
    return status

if __name__ == '__main__':
    run()
