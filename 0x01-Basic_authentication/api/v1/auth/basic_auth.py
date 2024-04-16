#!/usr/bin/env python3
"""
Basic authentication module
"""
from .auth import Auth


class BasicAuth(Auth):
    """Basic Auth class"""

    def extract_base64_authorization_header(self,
                                            authorization_header: str) -> str:
        """Return decoded base64 authorization header"""
        if (not authorization_header or type(authorization_header) is not str
                or not authorization_header.startswith('Basic ')):
            return
        return authorization_header.split("Basic ")[1]
