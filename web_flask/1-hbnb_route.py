#!/usr/bin/python3
""" creation of minimal flask aplication"""
# Import Flask
from flask import Flask

# Create an instance of Flask
app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello():
    """ Display "Hello HBNB!" """
    return 'Hello HBNB!'


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """ Display "HBNB"""
    return 'HBNB'


# Run the app on 0.0.0.0, port 5000
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
