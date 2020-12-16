# scalableProject3Group8
Scalable Project Group8 TCD

## Installation Guide:

Checkout the code from the Repo: git clone https://github.com/shashankcollab/scalableProject3Group8.git

### If you do not have access to the repo please email to shrivass@tcd.ie

#### This project is to showcase peer to peer networking of given IoT devices. Automation steps include :
- Create virtual environment
- set environment
- deactivate environment
##### After the env is set and code is loaded.
- Pull the latest code
- run the script mentioned below
- once done, exit the script
- deactivate environment

### To work on the project please run the following script with the mentioned arguments.
#### 1. 1st arg is for the environment creation, 
#### 2. 2nd arg is for the comment to add after commit,

#### If environment is not set


#### [Example: ./runme.sh foldername outputfilename git_commit_comment set_envrionment_flag]
./runme.sh true

## Program Running Guide:

#### If environment is already set
./runme.sh 

### This will basically run a pyhon code to generate sensor data and store it in a file. and then it will start the server [sender]. Other peers can come and connect to it by providing the POD identifier and receive the live server data.
- Run dataprovider.py
- Run server.py

#### Client side:
- Client PODs can connect to any other POD to receive the sensor data.

### API details: User will see the list of APIs availble by hitting one of the pods
- Sample URL: curl -v http://rasp-030.berry.scss.tcd.ie:33002/

To see the availble POD please use /pods

To register and get the key please use /register

### /pods provides the list of pods available to connect

### /register provides registers the pod and let them connect to that pod. It also provides a sample command to request for connection.

- client.py {pod-name} {key}
example client.py rasp-030

- If you are registered to any other pod, please specify that in the next question.
- after that provide the key when asked to connect to system and get the data.

### To kill all the processes of this app, use :
- sh killme.sh
