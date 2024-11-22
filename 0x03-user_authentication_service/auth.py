#!/usr/bin/env python3

"""
Implement method for password hashing
"""
from typing import AnyStr
import bcrypt


def _hash_password(password: str) -> AnyStr:
    """Encrypt a password using bcrypt"""

    byts = password.encode('utf-8')
    salt = bcrypt.gensalt()
    hashed_pw = bcrypt.hashpw(byts, salt)
    return hashed_pw
