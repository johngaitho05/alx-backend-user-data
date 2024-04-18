#!/usr/bin/env python3
"""
Session authentication module
"""
import os
import uuid

from .auth import Auth


class SessionAuth(Auth):
    """Basic Auth class"""

    user_id_by_session_id = {}

    def create_session(self, user_id: str = None) -> str:
        """Creates a session id for the given user id"""
        if user_id is None or type(user_id) is not str:
            return
        session_id = str(uuid.uuid4())
        SessionAuth.user_id_by_session_id[session_id] = user_id
        return session_id

    def user_id_for_session_id(self, session_id: str = None) -> str:
        """Gets a session id for the given user id"""
        if session_id is None or type(session_id) is not str:
            return
        return SessionAuth.user_id_by_session_id.get(session_id)
