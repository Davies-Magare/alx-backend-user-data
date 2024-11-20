#!/usr/bin/env python3
"""This module contains code a
database mapping User
"""

from sqlalchemy import (
    Integer,
    String,
    ForeignKey,
    Column
)

from sqlalchemy.orm import declarative_base

Base = declarative_base()


class User(Base):
    """The user table class mapping"""

    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    email = Column(String(250), nullable=False)
    hashed_password = Column(String(250), nullable=False)
    session_id = Column(String(250))
    reset_token = Column(String(250))
