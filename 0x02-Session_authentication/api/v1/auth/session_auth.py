#!/usr/bin/env python3

"""
This module contains the session authentication
class
"""

from flask import request
from .auth import Auth
import uuid


class SessionAuth(Auth):
    """Class to manage user sessions"""

    user_id_by_session_id = {}

    def create_session(self, user_id: str = None) -> str:
        """Create a Session ID for a user_id"""

        if not user_id or not isinstance(user_id, str):
            return None
        session_id = str(uuid.uuid4())
        SessionAuth.user_id_by_session_id[session_id] = user_id
        return session_id
