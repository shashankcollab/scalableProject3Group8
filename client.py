#!/usr/bin/env python3
 
from os import dup
import socket
import sys
import json
 
#_HOST = sys.argv[1]  if len(sys.argv) > 1 else None  # The server's hostname or IP address
PORT = 33000 # The port used by the server
msg = 'connect'


def run():
    available_hosts = []
    _HOST = sys.argv[1]  if len(sys.argv) > 1 else None
    while True:
        HOST = input("Please type the new peer or hit Enter to continue : \n") or _HOST
        while HOST is None:
            HOST = input("NO PEER SPECIFIED! Please type peer: \n") or _HOST
        print("Connected to the peer: ", HOST)
        msg = input("Please enter the key you registered with to send to sender: \n")
        try:
            with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
                # here i am just trying to see if i can read the avaialble hosts from the list
               # availableHosts= availableHost('hosts.csv').split(",")
                #HOSTS=[]
                #for i in availableHosts:
                 #   print('host is {}'.format(i))
                  #  HOSTS.append(i)
                s.connect((HOST, PORT))
                s.sendall(msg.encode())
                data = s.recv(1024).decode()
                if "_" in data:
                    live_data = data.split('_')[0]
                    available_hosts = data.split('_')[1]
                    print('available hosts are: {}'.format(available_hosts))
                    if data:
                        d = json.loads(live_data)
                        if "Enjoy" in d["Alert"]:
                            print('Great! \nSuggesiont from POD {} is {} Weather seems good with temperature {} humidity {}: '.format(HOST, d["Alert"],d["temperature"],d["humidity"]))
                        else:
                            print('Caution! \nSuggesiont from POD {} is {} because of weather condition temperature is {} humidity {}: '.format(HOST, d["Alert"],d["temperature"],d["humidity"]))


                        with open('temp_log_client.json', 'w') as f:
                            print ('Storing file..')
                            if not data:
                                break
                            f.write('\n')
                            f.write(live_data)
                            s.close()
                    else :
                        print('No data available at the moment at {}'.format(HOST))
                    print ('Succesfully recieved')
                else:
                    print('Incorrect key .. system is existing, please retry')
                    
        except Exception as e:
            print('An Exception occurred so searching for new peer...')
            peerFound = False
            available_hosts.remove(HOST)
            if len(available_hosts) > 0:
                
                for host in available_hosts:
                    # check if host is active
                    try:
                        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s: 
                            s.connect((HOST, PORT))
                            
                            HOST = host
                            peerFound = True
                            s.close()
                            break
                    except Exception as e:
                        
                        continue
            if not peerFound:
                print('No peer alive')    
                sys.exit(0)
        print('Peer found is {}'.format(HOST))

        data = input("Please hit enter to continue or type 'quit' if you want to close the connection: ") or "no"
        if data[0:1].lower() == "q" or data[0:4].lower() == "quit":
            sys.exit(0)
        _HOST = HOST

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
