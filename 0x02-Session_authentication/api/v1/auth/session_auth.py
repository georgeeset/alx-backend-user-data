#!/usr/bin/env python3
"""Session authentication module for the API.
"""
from uuid import uuid4
from flask import request
from .auth import Auth
from models.user import User


class SessionAuth(Auth):
    """Session authentication class.
    """
    user_id_by_session_id = {}

    def create_session(self, user_id: str = None) -> str:
        """Creates a session id.
        """
        if user_id is None:
            return None

        if type(user_id) is str:
            session_id = str(uuid4())
            self.user_id_by_session_id[session_id] = user_id
            return session_id
        return None

    def user_id_for_session_id(self, session_id: str = None) -> str:
        """Retrieves the user id associated with
        given session id.
        """
        if session_id is None:
            return None

        if type(session_id) is str:
            return self.user_id_by_session_id.get(session_id)
        return None

    def current_user(self, request=None) -> User:
        """Retrieves the user associated with the request.
        """
        user_id = self.user_id_for_session_id(self.session_cookie(request))
        return User.get(user_id)
