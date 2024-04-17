#!/usr/bin/env python3
"""
Basic authentication module
"""
import base64
import binascii
import os.path
from typing import TypeVar
from models.user import User

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
        except (TypeError, binascii.Error, UnicodeDecodeError):
            return

    def extract_user_credentials(
            self, decoded_base64_authorization_header: str) -> (str, str):
        """Extracts user credentials from base64 authorization header"""
        if ((not decoded_base64_authorization_header
                or type(decoded_base64_authorization_header) is not str) or
                ":" not in decoded_base64_authorization_header):
            return None, None
        return tuple(decoded_base64_authorization_header.split(":", 1))

    def user_object_from_credentials(self, user_email: str,
                                     user_pwd: str) -> TypeVar('User'):
        """Returns user object from user credentials"""
        if user_email is None or type(user_email) is not str:
            return
        if user_pwd is None or type(user_pwd) is not str:
            return
        if not os.path.isfile('.db_User.json'):
            return
        users = User.search({'email': user_email})
        return next((user for user in users if
                     user.is_valid_password(user_pwd)), None)

    def current_user(self, request=None) -> TypeVar('User'):
        """Returns current user"""
        auth_header = self.authorization_header(request)
        if not auth_header:
            return
        base64_authorization_header = (
            self.extract_base64_authorization_header(auth_header))
        if not base64_authorization_header:
            return
        decoded_base64_authorization_header = (
            self.decode_base64_authorization_header(
                base64_authorization_header))
        if not decoded_base64_authorization_header:
            return
        username, password = (
            self.extract_user_credentials(decoded_base64_authorization_header))
        if username is None or password is None:
            return
        return self.user_object_from_credentials(username, password)
