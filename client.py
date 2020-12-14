#!/usr/bin/env python3
 
from os import dup
import socket
import sys
import json
 
HOST = sys.argv[1]  # The server's hostname or IP address
PORT = 33000 # The port used by the server
msg = 'connect'

def run():
    while True:
        
        try:
            with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
                # here i am just trying to see if i can read the avaialble hosts from the list
                availableHosts= availableHost('hosts.csv').split(",")
                HOSTS=[]
                for i in availableHosts:
                    print('host is {}'.format(i))
                    HOSTS.append(i)
                s.connect((HOST, PORT))
                s.sendall(msg.encode())
                data = s.recv(1024).decode()
                if data:
                    d = json.loads(data)
                    if "Enjoy" in d["Alert"]:
                        print('Great! \nSuggesiont from POD {} is {} Weather seems good with temperature {} humidity {}: '.format(HOST, d["Alert"],d["temperature"],d["humidity"]))
                    else:
                        print('Caution! \nSuggesiont from POD {} is {} because of weather condition temperature is {} humidity {}: '.format(HOST, d["Alert"],d["temperature"],d["humidity"]))


                    with open('temp_log_client.json', 'w') as f:
                        print ('Storing file..')
                        if not data:
                            break
                        f.write('\n')
                        f.write(data)
                        s.close()
                else :
                    print('No data available at the moment at {}'.format(HOST))
                print ('Succesfully recieved')
        except Exception as e:
            print('No server alive {}'.format(e))
            sys.exit(0)

        data = input("Please hit enter to continue or type 'quit' if you want to close the connection: ") or "no"
        if data[0:1].lower() == "q" or data[0:4].lower() == "quit":
            sys.exit(0)

def availableHost(filename):
    f = open(filename, 'rb')
    hostslist=''
    for line in (f.readlines() [-1:]):
        hostslist=hostslist+line.decode()
    return hostslist

def updateavailableHost(filename, host, action):
    f = open(filename, 'rb')
    hostslist=''
    for line in (f.readlines() [-1:]):
        hostslist=hostslist+line.decode()
    if action=='r':
        print('dosomething')
    elif action=='a':
        print('dosomething')
    return hostslist

if __name__ == '__main__':
    run()
