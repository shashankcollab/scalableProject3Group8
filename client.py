#!/usr/bin/env python3
 
import socket
import sys
import json

_HOST = sys.argv[1]  if len(sys.argv) > 1 else None  # The server's hostname or IP address
PORT = 33000 # The port used by the server
# msg = sys.argv[2]
while True:
    HOST = input("Please type the new peer or hit Enter to continue : \n") or _HOST
    while HOST is None:
        HOST = input("NO PEER SPECIFIED! Please type peer: \n") or _HOST
    print("Connected to the peer: ", HOST)
    msg = input("Please enter the msg you want to send: \n")
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.connect((HOST, PORT))
            s.sendall(msg.encode())
            data = s.recv(1024).decode()
            d = json.loads(data)
            if "Enjoy" in d["Alert"]:
                print('Great! Suggesiont from POD {} is {} Weather seems good with temperature {} humidity {}: '.format(HOST, d["Alert"],d["temperature"],d["humidity"]))
            else:
                print('Caution! Suggesiont from POD {} is {} because of weather condition temperature is {} humidity {}: '.format(HOST, d["Alert"],d["temperature"],d["humidity"]))


            with open('temp_log_client.json', 'w') as f:
                print ('Storing file..')
                if not data:
                    break
                f.write('\n')
                f.write(data)
                s.close()
            print ('Succesfully recieved')
    except Exception as e:
        print('No server alive dude{}'.format(e))
        sys.exit(0)

    data = input("Please specify 'yes/no' if you want to close the connection: ")
    if data[0:3].lower() == "yes" or data[0:1].lower() == "y":
        sys.exit(0)
    _HOST = HOST
    