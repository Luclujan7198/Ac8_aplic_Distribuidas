from flask import Flask
from flask import jsonify

App = Flask(__name__)

from models.Response import Response
from ErrorHandler import *
from Routes import *

if __name__ == "__main__":
    App.run(port=80, debug=False)