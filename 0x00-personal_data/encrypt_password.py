#!/usr/bin/env python3
"""
User passwords should NEVER be stored in plain text in a database.

Implement a hash_password function that expects one string argument name
password and returns a salted, hashed password, which is a byte string.

Use the bcrypt package to perform the hashing (with hashpw).
"""
import bcrypt


def hash_password(password: str) -> bytes:
    """
    Hashes a password using bcrypt with salt.

    Args:
    password (str): The password to be hashed.

    Returns:
    bytes: The salted, hashed password.
    """
    # Generate a salt and hash the password using bcrypt
    salt = bcrypt.gensalt()
    hashed_password = bcrypt.hashpw(password.encode('utf-8'), salt)
    return hashed_password


def is_valid(hashed_password: bytes, password: str) -> bool:
    """
    Validates whether the provided password matches the hashed password.

    Args:
    hashed_password (bytes): The hashed password.
    password (str): The password to be validated.

    Returns:
    bool: True if the password matches the hashed password, False otherwise.
    """
    # Verify if the provided password matches the hashed password
    return bcrypt.checkpw(password.encode('utf-8'), hashed_password)
