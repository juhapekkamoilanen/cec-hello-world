import socket
from flask import Flask

application = Flask(__name__)

@application.route("/")
def hello():
    
    return "Hello CEC, Im JPM! Greetings from "+socket.gethostname()+"\n"


if __name__ == "__main__":
    application.run()
