#!/usr/bin/env python3

"""Declare a class to manage
database operations
"""
from sqlalchemy import create_engine
from sqlalchemy.orm.exc import NoResultFound
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm.session import Session
from typing import Dict
from user import Base, User


class DB:
    """Class to manage database operations
    """

    def __init__(self) -> None:
        """Initialize a new DB instance
        """
        self._engine = create_engine("sqlite:///a.db", echo=False)
        Base.metadata.drop_all(self._engine)
        Base.metadata.create_all(self._engine)
        self.__session = None

    @property
    def _session(self) -> Session:
        """Memoized session object
        """
        if self.__session is None:
            DBSession = sessionmaker(bind=self._engine)
            self.__session = DBSession()
        return self.__session

    def add_user(self, email: str, hashed_password: str) -> User:
        """Save user to the database
        """
        # valid_args = isinstance(email, str) and isinstance(
        # hashed_password, str)
        # if valid_args:
        user = User(email=email,
                    hashed_password=hashed_password)
        self._session.add(user)
        self._session.commit()
        return user

    def find_user_by(self, **kwargs: Dict[str, str]) -> User:
        """Retrieve user from the database"""
        session = self._session
        # validate kwargs dict
        try:
            user = session.query(User).filter_by(**kwargs).one()
        except Exception as e:
            raise e
        if user is None:
            raise NoResultFound
        return user

    def update_user(self, user_id: str, **kwargs: Dict[str, str]) -> None:
        """
        Args:
            user_id
                The user id
            kwargs
               dictionary: the attribute to be updated and the
                    value to update it to.
        Return:
            None
        """
        session = self.__session
        try:
            user = session.query(User).filter_by(id=user_id).first()
            print(user.__dict__)
            if user:
                for key, value in kwargs.items():
                    if hasattr(user, key):
                        setattr(user, key, value)
                    else:
                        raise ValueError
                session.add(user)
                session.commit()
        except Exception as e:
            raise ValueError
        return None
