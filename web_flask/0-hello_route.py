#!/usr/bin/python3
""" first file of flask """
# import Flask
from flask import Flask
# create an instance of Flask
app = Flask(__name__)


@app.route('/', strict_slashe=False)
def home():
    """ first mensaje """
    return "Hello HBNB!"


# Run the app on 0.0.0.0, port 5000
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
