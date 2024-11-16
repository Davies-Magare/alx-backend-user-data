#!/usr/bin/env python3

"""
This module contains the session authentication
class
"""

from flask import request
from .auth import Auth


class SessionAuth(Auth):
    """Class to manage user sessions"""

    pass
