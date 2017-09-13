import sys
import os

from flask import Flask

application = Flask(__name__)

@application.route("/")
def hello():

    ret = "Hello World !!1!<br>"
    ret += "<p>sys.path = " + str(sys.path) + "</p>\n"
    ret += "<p>os.getcwd() = " + str(os.getcwd()) + "</p>\n"
    ret += "<p>Environment:<br>"

    for name in os.environ:
        ret += name + " = " + os.environ[name] + "<br>\n"

    return ret

if __name__ == "__main__":
    application.run()
