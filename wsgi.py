import socket
from datetime import datetime
from flask import Flask

application = Flask(__name__)

@application.route("/")
def hello():
    print('hello you log watcher!')
    timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    foo="0"
    
    try:
        foo="1"
        file_obj = open('/mnt/cec-vanilla.log', 'a')
        file_obj.write(timestamp + ' ' + socket.gethostname() + ' \n')
        file_obj.close()
        
        file_obj2 = open('/mnt/cec-vanilla.log', 'r')
        foo=file_obj2.read()
        print(foo)
        file_obj2.close()
    except:
        foo="error"
    
    return "<pre>Hello CEC, Im version 1 - " + foo + "! Greetings from "+socket.gethostname()+"\n"+timestamp+"\n</pre>"


if __name__ == "__main__":
    application.run()
