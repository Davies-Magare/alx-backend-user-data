#!/usr/bin/env python3

"""
Declare a minimal flask
application
"""

from auth import Auth
from flask import (
    Flask,
    jsonify,
    request
)

app = Flask(__name__)

AUTH = Auth()


@app.route("/")
def hola_mundo():
    """Greet the world!"""
    return jsonify({"message": "Bienvenue"})


@app.route("/users", methods=['POST'])
def register_user():
    """Register a user in the database"""

    email = request.form.get('email')
    password = request.form.get('password')
    if email and password:
        try:
            user = AUTH.register_user(email, password)
            return jsonify({"email": f"{email}", "message": "user_created"}), 200
        except ValueError:
            return jsonify({"message": "email already registered"}), 400


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")
