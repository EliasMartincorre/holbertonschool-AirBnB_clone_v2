#!/usr/bin/python3
""" first file of flask """

from flask import Flask
app = Flask(__name__)


@app.route('/', strict_slashe=False)
def home():
    """ first mensaje"""
    return "Hello HBNB!"


if __name__ == '__main__':
    # DEBUG is SET to TRUE. CHANGE FOR PROD
    app.run(host='0.0.0.0', port=5000, debug=True)
