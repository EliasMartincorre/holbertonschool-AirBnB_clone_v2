#!/usr/bin/python3
""" script that starts a Flask web application

- Routes:
/: display “Hello HBNB!”
/hbnb: display “HBNB”
/c/<text>: display “C ”, followed by the value of the text variable"""

from flask import Flask

app = Flask(__name__)


@app.route('/', strict_slashes=False)
def home():
    """ display string """
    return "Hello HBNB"


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """ Display string """
    return "HBNB"


@app.route("/c/<text>", strict_slashes=False)
def func(text):
    """ display c + text """
    text = text.replace('_', ' ')
    return f"c {text}"


@app.route("/python/", strict_slashes=False)
@app.route("/python/<text>", strict_slashes=False)
def ptyon(text='is_cool'):
    """ display  """
    text = text.replace('_', ' ')
    return f"Python {text}"


@app.route('/number/<int:n>', strict_slashes=False)
def number(n):
    return f"{n} is a number"


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
