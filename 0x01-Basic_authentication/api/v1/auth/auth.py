#!/usr/bin/env python3
"""
Request Authorization Template
"""
import re
from typing import List, TypeVar

from flask import request as flask_request


class Auth:
    """Auth class"""

    def __init__(self):
        """Initialization"""
        pass

    def matches(self, s1, s2) -> bool:
        """Checks if two strings are equal"""
        pattern = re.compile(s1)
        return bool(pattern.match(s2))

    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """Checks whether authentication is for a given path"""
        if not path:
            return True
        if not excluded_paths:
            return True
        return not any([self.matches(p.rstrip('/'), path.rstrip('/')) for p
                        in excluded_paths])

    def authorization_header(self, request: flask_request = None) -> str:
        """Returns the value of the authorization header of a request"""
        if not request or 'Authorization' not in request.headers:
            return
        return request.headers['Authorization']

    def current_user(self, request: flask_request = None) -> TypeVar('User'):
        """Returns the current user."""
        return
