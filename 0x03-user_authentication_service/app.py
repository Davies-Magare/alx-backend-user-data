#!/usr/bin/env python3

"""
Declare a minimal flask 
application
"""

from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/")
def hola_mundo():
    """Greet the world!"""
    return jsonify({"message": "Bienvenue"})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")
