#!/usr/bin/env python3
"""
Request Authorization Template
"""
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
        return path.rstrip('/') not in [p.rstrip('/') for p in excluded_paths]

    def authorization_header(self, request: flask_request = None) -> str:
        """Returns the authorization header of a request"""
        return

    def current_user(self, request: flask_request = None) -> TypeVar('User'):
        """Returns the current user."""
        return
