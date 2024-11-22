#!/usr/bin/env python3
"""
Main file
"""
from auth import Auth

email = 'bo@bob.com'
password = 'MyPwdOfBob'
auth = Auth()

user = auth.register_user(email, password)
print(user.__dict__)
session = auth.create_session(email)
print('session: ', session)
user = auth.get_user_from_session_id(session)
print('userfromsess: ', user.__dict__)
user = auth.get_user_from_session_id(session)
auth.destroy_session(user.id)
user = auth.get_user_from_session_id(session)
if not user:
    print("Gotcha")
