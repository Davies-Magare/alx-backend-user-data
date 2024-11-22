#!/usr/bin/env python3

"""
Declare a minimal flask
application
"""

from auth import Auth
from flask import (
    Flask,
    jsonify,
    request,
    abort
)
# from db import DB
# from sqlalchemy.orm.exc import NoResultFound

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
            return jsonify({"email": f"{email}", "message": "user created"})
        except ValueError:
            return jsonify({"message": "email already registered"}), 400


@app.route("/sessions", methods=['POST'])
def login():
    """Login the user based on their credentials"""

    email = request.form.get('email')
    password = request.form.get('password')
    login = AUTH.valid_login(email, password)
    if not login:
        abort(401)
    session_id = AUTH.create_session(email)
    response = jsonify({"email": email, "message": "logged in"})
    response.set_cookie("session_id", session_id)
    return response


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000", debug=True)
