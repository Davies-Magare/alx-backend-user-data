#!/usr/bin/env python3
""" Module of session authentication
    views
"""
from flask import jsonify, abort, request
from api.v1.views import app_views
import os

@app_views.route(
    '/auth_session/login', 
    methods=['POST'],
    strict_slashes=False)
def session_auth():
    """Route for session authentication"""
    email = request.form.get('email')
    password = request.form.get('password')
    if not email:
        return jsonify({"error": "email missing"}), 400
    elif not password:
        return jsonify({"error": "password missing"}), 400
    from models.user import User
    user = User.search({"email": email})[0]
    if not user:
        return jsonify({"error": "no user found for this email"}), 404
    if not user.is_valid_password(password):
        return jsonify({"error": "wrong password"}), 401
    from api.v1.app import auth
    session_id = auth.create_session(user.id)
    ret_val = jsonify(user.to_json())
    ret_val.set_cookie(os.getenv('SESSION_NAME'), session_id)
    return ret_val



    
