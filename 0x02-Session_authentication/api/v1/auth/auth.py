#!/usr/bin/env python3
"""
Request Authorization Template
"""
import os
import re
from typing import List, TypeVar

from flask import request as flask_request


class Auth:
    """Auth class"""

    def __init__(self):
        """Initialization"""
        pass

    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """Checks whether authentication is for a given path"""
        if not path:
            return True
        if not excluded_paths:
            return True
        path = path.rstrip('/')
        for excl_path in excluded_paths:
            excl_path = excl_path.rstrip('/')
            if excl_path.endswith('*'):
                if path.startswith(excl_path[:-1]):
                    return False
            elif excl_path == path:
                return False
        return True

    def authorization_header(self, request: flask_request = None) -> str:
        """Returns the value of the authorization header of a request"""
        if not request or 'Authorization' not in request.headers:
            return
        return request.headers['Authorization']

    def current_user(self, request: flask_request = None) -> TypeVar('User'):
        """Returns the current user."""
        return

    def session_cookie(self, request=None):
        """Gets a session cookie"""
        if request is None:
            return
        session_name = os.environ.get('SESSION_NAME')
        return request.cookies.get(session_name)
