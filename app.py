from flask import Flask
import socket
app = Flask(__name__)

@app.route("/")
def home():
    return "Hello, World!"
    
if __name__ == "__main__":
     app.run( host=socket.gethostname() ,port=33033,debug=True)
