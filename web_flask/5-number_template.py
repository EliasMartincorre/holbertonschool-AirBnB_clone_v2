#!/usr/bin/python3
""" script that starts a Flask web application
"""
from flask import Flask, render_template, url_for

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
    return f"python {text}"


@app.route('/number/<int:n>', strict_slashes=False)
def number(n):
    return f"{n} is a number"


@app.route("/number_template/<int:n>", strict_slashes=False)
def funcion(n):
    return render_template('5-number.html', n=n)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
