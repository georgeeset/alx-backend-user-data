#!/usr/bin/env python3
"""
A simple flask app
"""

from flask import Flask, jsonify
from auth import Auth


app = Flask(__name__)
AUTH = Auth()
strict_slashes=False

@app.route("/", methods=["GET"])
def index() -> str:
    """To return a JSON payload of the form
    """
    return jsonify({"message": "Bienvenue"})


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")