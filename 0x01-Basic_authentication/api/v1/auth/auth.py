#!/usr/bin/env python3
"""This module contains
user authentication code"""

from flask import request
from typing import List, TypeVar


class Auth:
    """The authentication class."""

    @staticmethod
    def slash_handler(path: str) -> str:
        """Return path equivalent with
        or without slash"""
        if path[-1] == '/':
            return path[:-1]
        return path + "/"

    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """Check whether path is exluded from authorization"""
        if path and excluded_paths:
            slash_alternative = self.slash_handler(path)
            if path in excluded_paths or slash_alternative in excluded_paths:
                return False
        return True

    def authorization_header(self, request=None) -> str:
        """Validate the request object"""
        if request and request.headers.get('Authorization'):
            return request.headers.get('Authorization')
        return None

    def current_user(self, request=None) -> TypeVar('User'):
        """A stub for the real documentation"""
        return None


class BasicAuth(Auth):
    """The basic authentication class"""
    pass
