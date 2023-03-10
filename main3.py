""" how to run flask application on script ? (instead of long CLI command)"""

from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello():
    return "hello world"

if __name__== "__main__":
    app.run(host="localhost", port=8000, debug=True)