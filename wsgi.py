import socket
from flask import Flask

application = Flask(__name__)

@application.route("/")
def hello():
    print('hello you log watcher!')
    
    file_obj = open('/mnt/vanilla-logdir/cec-vanilla.log', 'a')
    timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    file_obj.write(timestamp + ' ' + socket.gethostname() + ' \n')
    file_obj.close()
    
    return "Hello CEC, Im JPM - 2! Greetings from "+socket.gethostname()+"\n"


if __name__ == "__main__":
    application.run()
