#!/usr/bin/python3
""" take a argument of request and post them."""
# Import Flask
from flask import Flask

# Create an instance of Flask
app = Flask(__name__)

# Define routes
@app.route('/', strict_slashes=False)
def hello():
    """ display saludo """
    return 'Hello HBNB!'

@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """ Display "HBNB" """
    return 'HBNB'

@app.route('/c/<text>', strict_slashes=False)
def c(text):
    """ Display "C " followed by the value of the text variable"""
    text = text.replace('_', ' ')
    return 'C {}'.format(text)

# Run the app on 0.0.0.0, port 5000
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
