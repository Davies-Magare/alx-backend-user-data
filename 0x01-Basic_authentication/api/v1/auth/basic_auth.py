#!/usr/bin/env python3
"""This module contains
basic authentication class"""

from .auth import Auth
import base64


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
