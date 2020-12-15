from flask import Flask
import socket
import client as c
import uuid
app = Flask(__name__)

@app.route("/")
def home():
    return f'<h1>Hello, New POD!</h1> </br>Welcome to Group 8 Project. <br/><br/>These are available APIs <br/><br/> <ul><li>To see the availble POD please use <b>/pods</b> <br/><br/></li><li>To register and get the key please use <b>/register</b></li></ul>'

@app.route("/pods")
def pods():
    availableHosts= c.availableHost('hosts.csv').split(",")
    avlhost= print_ul(availableHosts)
    return f'There are following PODs available to connect <br/><ul>{avlhost}</ul>'

@app.route("/register")
def register():
    newkeyval=newkey()
    f = open("ourkey.csv", "a")
    f.write(f"{newkeyval},")
    f.close()
    return f'Here is your key: {newkeyval}'

@app.route("/showconnectionstring")
def showconnectionstring():
    availableHosts= c.availableHost('hosts.csv').split(",")
    avlhost= print_ul(availableHosts)
    return f'python3 client.py {avlhost} {availableHosts}'

def print_ul(elements):
    output='<ul>'
    for s in elements:
        ul = "<li>" + s + "</li>"
        output=output+ul
    output=output+'</ul>'
    return output

def newkey(string_length=6):
    #gives you the key to use as registration
    random = str(uuid.uuid4()) 
    random = random.upper() 
    random = random.replace("-","")
    return random[0:string_length] # Return the random string.

if __name__ == "__main__":
     app.run( host=socket.gethostname() ,port=33002,debug=False)