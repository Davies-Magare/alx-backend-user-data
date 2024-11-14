"""This module contains
user authentication code"""

from flask import request
from typing import List, TypeVar


class Auth:
    """The authentication class."""

    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """A stub for the real documentation"""
        return False

    def authorization_header(self, request=None) -> str:
        """A stub for the real documentation"""
        return None

    def current_user(self, request=None) -> TypeVar('User'):
        """A stub for the real documentation"""
        return None
