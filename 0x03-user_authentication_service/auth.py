#!/usr/bin/env python3

"""
Implement method for password hashing
"""
from typing import AnyStr
import bcrypt
from db import DB
from user import User
from sqlalchemy.orm.exc import NoResultFound
def _hash_password(password: str) -> AnyStr:
    """Encrypt a password using bcrypt"""

    byts = password.encode('utf-8')
    salt = bcrypt.gensalt()
    hashed_pw = bcrypt.hashpw(byts, salt)
    return hashed_pw

class Auth:
    """Auth class to interact with the authentication database.
    """

    def __init__(self):
        """class constructor"""
        self._db = DB()

    def register_user(self, email:str, password:str) -> User:
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

    
