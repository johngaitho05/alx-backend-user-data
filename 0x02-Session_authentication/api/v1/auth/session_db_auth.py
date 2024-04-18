#!/usr/bin/env python3
"""
Session authentication with expiration time
"""
import uuid
from datetime import timedelta, datetime
from typing import Optional

from models.user_session import UserSession

from .session_exp_auth import SessionExpAuth


class SessionDBAuth(SessionExpAuth):
    """Persistent Session Auth With Expiration Time"""

    def create_session(self, user_id=None) -> Optional[str]:
        """Creates new session"""
        if not user_id:
            return
        session_id = str(uuid.uuid4())
        session = UserSession(user_id=user_id, session_id=session_id)
        session.save()
        return session.id

    def user_id_for_session_id(self, session_id=None) -> Optional[str]:
        """Gets user id for given session_id"""
        if session_id is None:
            return
        session = UserSession.get(session_id)
        if not session:
            return
        if (session.created_at + timedelta(seconds=self.session_duration) <
                datetime.utcnow()):
            return
        return session.user_id

    def destroy_session(self, request=None) -> bool:
        """Destroys UserSession based on the session_id
         from the request cookie"""
        if request is None:
            return False
        session_id = self.session_cookie(request)
        if not session_id:
            return False
        session = UserSession.get(session_id)
        if not session:
            return False
        session.remove()
        return True
