#!/usr/bin/env python3
""" Module for session auth views
"""
import os

from api.v1.views import app_views
from flask import request, jsonify, abort
from models.user import User


@app_views.route('/auth_session/login', methods=['POST'], strict_slashes=False)
def session_auth() -> str:
    """ POST /api/v1/status
      - handles all routes for the Session authentication
    """
    email = request.form.get('email')
    password = request.form.get('password')
    if email is None:
        return jsonify({'error': 'email missing'}), 400
    if password is None:
        return jsonify({'error': 'password missing'}), 400
    users = User.search({'email': email})
    if not users:
        return jsonify({'error': "no user found for this email"}), 404
    user = next((
        user for user in users if user.is_valid_password(password)), None)
    if not user:
        return jsonify({'error': 'wrong password'}), 401
    from api.v1.app import auth
    session_id = auth.create_session(user.id)
    session_name = os.environ.get('SESSION_NAME')
    res = jsonify(user.to_json())
    res.set_cookie(session_name, session_id)
    return res, 200


@app_views.route('/auth_session/logout', methods=['DELETE'],
                 strict_slashes=False)
def logout() -> str:
    """Logs out the user by deleting the session"""
    from api.v1.app import auth
    if not auth.destroy_session(request):
        return abort(404)
    return jsonify({}), 200
