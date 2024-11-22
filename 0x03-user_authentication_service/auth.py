#!/usr/bin/env python3

"""
Implement method for password hashing
"""
from typing import AnyStr
import bcrypt
import uuid
from db import DB
from user import User
from sqlalchemy.orm.exc import NoResultFound


def _hash_password(password: str) -> AnyStr:
    """Encrypt a password using bcrypt"""

    byts = password.encode('utf-8')
    salt = bcrypt.gensalt()
    hashed_pw = bcrypt.hashpw(byts, salt)
    return hashed_pw


def _generate_uuid() -> str:
    """Generate a string uuid"""
    return str(uuid.uuid4())


class Auth:
    """Auth class to interact with the authentication database.
    """

    def __init__(self):
        """class constructor"""
        self._db = DB()

    def register_user(self, email: str, password: str) -> User:
        """Register user in database"""
        db = self._db
        if email and password:
            password = _hash_password(password)
            try:
                user = db.find_user_by(email=email)
                if user:
                    raise ValueError(f"User {email} already exists")
            except NoResultFound:
                user = db.add_user(email, password)
                return user
            except Exception as e:
                raise e

    def valid_login(self, email: str, password: str) -> bool:
        """Validate email and password"""

        ret_value = False
        db = self._db
        if email and password:
            password = password.encode('utf8')
            try:
                user = db.find_user_by(email=email)
                if bcrypt.checkpw(password, user.hashed_password):
                    ret_value = True
            except NoResultFound:
                pass
        return ret_value

    def create_session(self, email: str) -> str:
        """Generate new uuid based on session_id"""

        db = self._db
        try:
            user = db.find_user_by(email=email)
            # print("in crt_session: ", user.__dict__)
            user.session_id = _generate_uuid()
        except Exception:
            return None
        return user.session_id

    def get_user_from_session_id(self, session_id: str) -> User:
        """Retrieve the user based on session_id"""
        db = self._db
        if session_id is None:
            return None
        try:
            user = db.find_user_by(session_id=session_id)
        except NoResultFound:
            user = None
        return user

    def destroy_session(self, user_id: int) -> None:
        """Destroy the user session"""
        db = self._db
        try:
            db.update_user(user_id, session_id=None)
        except Exception as e:
            pass
