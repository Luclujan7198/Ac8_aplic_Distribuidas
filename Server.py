from flask import Flask
from flask import jsonify

App = Flask(__name__)

if __name__ == "__main__":
    App.run(port=80, debug=False)