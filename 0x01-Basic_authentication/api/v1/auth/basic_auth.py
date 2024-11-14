#!/usr/bin/env python3
"""This module contains
basic authentication class"""

from .auth import Auth


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
