#!/usr/bin/env python3
"""
Session authentication with expiration time
"""
import os
from datetime import datetime, timedelta
from typing import Optional

from .session_auth import SessionAuth


class SessionExpAuth(SessionAuth):
    """Session Auth With Expiration Time"""

    def __init__(self):
        """Constructor"""
        super().__init__()
        duration = os.getenv("SESSION_DURATION", '0')
        if not duration.isdigit():
            duration = '0'
        self.session_duration = int(duration)

    def create_session(self, user_id=None) -> Optional[str]:
        """Extends create_session of SessionAuth
        class to add expiration time"""
        session_id = super(SessionExpAuth, self).create_session(user_id)
        if not session_id:
            return
        SessionExpAuth.user_id_by_session_id[session_id] = \
            {'user_id': user_id, 'created_at': datetime.now()}
        return session_id

    def user_id_for_session_id(self, session_id=None) -> Optional[str]:
        """Extends user_id_for_session_id of SessionAuth"""
        if (session_id is None or session_id not in SessionExpAuth.
                user_id_by_session_id):
            return
        session_dict = SessionAuth.user_id_by_session_id[session_id]
        if self.session_duration <= 0:
            return session_dict['user_id']
        if 'created_at' not in session_dict:
            return
        if (session_dict['created_at']
                + timedelta(seconds=self.session_duration) < datetime.now()):
            return
        return session_dict['user_id']
