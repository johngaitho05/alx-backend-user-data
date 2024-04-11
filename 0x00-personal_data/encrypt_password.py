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
