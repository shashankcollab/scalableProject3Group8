# scalableProject3Group8
Group8 TCD Scalable

#### This project is to showcase peer to peer networking of a given IoT devices. Automation steps include :
- Create virtual environment
- set environment
- deactivate environment
##### After the env is set and code is loaded.
- Pull the latest code
- run the script mentioned below
- deactivate environment

### To work on the project please run the following script with the mentioned arguments.
#### 1. 1st arg is for the environment creation, 
#### 2. 2nd arg is for the comment to add after commit,

#### If environment is not set

#### [Example: ./cmd.sh foldername outputfilename git_commit_comment set_envrionment_flag]
./cmd.sh true

#### If environment is already set
./cmd.sh 

### This will basically run a pyhon code to generate sensor data and store it in a file. and then it will start the server [sender]. Other peers can come and connect to it by providing the POD identifier and receive the live server data.
- Run dataprovider.py
- Run server.py

#### Client side:
- Client PODs can connect to any other POD to receive the sensor data.

### No separate libraries Required: