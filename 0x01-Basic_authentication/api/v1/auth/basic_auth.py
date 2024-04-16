#!/usr/bin/env python3
"""
Basic authentication module
"""
import base64
import binascii

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

    def decode_base64_authorization_header(
            self, base64_authorization_header: str) -> str:
        """Decodes base64 authorization header"""
        if (not base64_authorization_header or
                type(base64_authorization_header) is not str):
            return
        try:
            return (base64.b64decode(base64_authorization_header)
                    .decode('utf-8'))
        except (TypeError, binascii.Error):
            return

    def extract_user_credentials(
            self, decoded_base64_authorization_header: str) -> (str, str):
        """Extracts user credentials from base64 authorization header"""
        if ((not decoded_base64_authorization_header
                or type(decoded_base64_authorization_header) is not str) or
                ":" not in decoded_base64_authorization_header):
            return None, None
        return tuple(decoded_base64_authorization_header.split(":"))
