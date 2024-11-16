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

    def user_id_for_session_id(self, session_id: str = None) -> str:
        """Retrieve a user Id based on a Session ID"""
        if not session_id or not isinstance(session_id, str):
            return None
        user_id = SessionAuth.user_id_by_session_id.get(session_id)
        return user_id
