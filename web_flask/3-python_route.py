#!/usr/bin/python3
"""
This script Starts a Flask web application.
"""

from flask import Flask

app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello_hbnb():
    """ this func Displays 'Hello HBNB!' """
    return 'Hello HBNB!'


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """ this func Displays HBNB """
    return 'HBNB'


@app.route('/c/<text>', strict_slashes=False)
def display_C(text):
    """ this func displays C + some text """
    return 'C {}'.format(text.replace('_', ' '))


@app.route('/python/<text>', strict_slashes=False)
def display_python(text='is cool'):
    """ this func displays python + some text """
    return 'Python {}'.format(text.replace('_', ' '))


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
