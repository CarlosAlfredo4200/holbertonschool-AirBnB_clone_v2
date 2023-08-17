#!/usr/bin/python3
"""Inicialization of the Python Flask application"""
from flask import Flask

app = Flask(__name__)


'''Route root URL'''


@app.route('/', strict_slashes=False)
def hello_hbnb():

    return "Hello HBNB!"


'''Route for /hbnb'''


@app.route('/hbnb', strict_slashes=False)
def hbnb():

    return "HBNB"


'''Route for /hbnb'''


@app.route('/c/<text>', strict_slashes=False)
def c_text(text):
    text = text.replace('_', ' ')
    return f"C {text}"


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
