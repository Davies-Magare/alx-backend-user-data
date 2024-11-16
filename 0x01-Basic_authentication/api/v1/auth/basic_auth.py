#!/usr/bin/env python3
"""This module contains
basic authentication class"""

from .auth import Auth
from models.user import User
import base64
from typing import TypeVar
from flask import request

class BasicAuth(Auth):
    """The basic authentication class"""

    def extract_base64_authorization_header(
            self, authorization_header: str) -> str:
        """Extract the Base64 part of the authorization header"""
        if authorization_header and isinstance(
                authorization_header,
                str) and authorization_header.split(' ')[0] == 'Basic':
            return authorization_header.split(' ')[1]
        return None

    def decode_base64_authorization_header(
            self, base64_authorization_header: str) -> str:
        """Decode a Base64 string"""

        if isinstance(base64_authorization_header, str):
            try:
                decoded_str = base64.b64decode(
                    base64_authorization_header,
                    validate=True).decode('utf-8')
            except Exception:
                decoded_str = None

            finally:
                return decoded_str
        return None

    def extract_user_credentials(
            self, decoded_base64_authorization_header: str) -> (str, str):
        """Extract email and password from decoded string"""
        decoded_str = decoded_base64_authorization_header
        if isinstance(decoded_str, str) and ':' in decoded_str:
            email_password = decoded_str.split(':')
            return email_password[0], email_password[1]
        return None, None

    def user_object_from_credentials(
            self,
            user_email: str,
            user_pwd: str) -> TypeVar('User'):

        """Given credentials retrieve user from database"""

        condition = (
            user_email and isinstance(user_email, str) and
            user_pwd and isinstance(user_pwd, str)
        )
        if not condition:
            return None
        try:
            results = User.search({"email": user_email})
        except KeyError:
            return None
        if results and len(results) > 0:
            user = results[0]
            if user.is_valid_password(user_pwd):
                return user
        return None


    def current_user(self, request=None) -> TypeVar('User'):
        """Retrieve current user"""
        user = None
        try:
            request_auth = self.authorization_header(request)
            auth_header = self.extract_base64_authorization_header(request_auth)
            decoded_header = self.decode_base64_authorization_header(auth_header)
            email_pass = self. extract_user_credentials(decoded_header)
            user = user_object_from_credentials(email_pass[0], email_pass[1])
        except Exception:
            pass
        return user
