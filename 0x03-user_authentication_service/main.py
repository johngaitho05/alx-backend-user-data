#!/usr/bin/env python3
""" Advanced Task Main Module """
import requests

BASE_URL = "http://localhost:5000"


def register_user(email: str, password: str) -> None:
    """ Register User """
    endpoint = f"{BASE_URL}/users"
    data = {"email": email, "password": password}
    response = requests.post(endpoint, data=data, timeout=5)
    assert response.status_code == 200
    # print("✔️ User registered successfully.")


def log_in_wrong_password(email: str, password: str) -> None:
    """ Log in Wrong Password """
    endpoint = f"{BASE_URL}/sessions"
    data = {"email": email, "password": password}
    response = requests.post(endpoint, data=data, timeout=5)
    assert response.status_code == 401
    # print("✔️ Log in with wrong password failed.")


def log_in(email: str, password: str) -> str:
    """ Log in """
    endpoint = f"{BASE_URL}/sessions"
    data = {"email": email, "password": password}
    response = requests.post(endpoint, data=data, timeout=5)
    assert response.status_code == 200
    # print("✔️ Log in successful.")
    return response.cookies.get("session_id")


def profile_unlogged() -> None:
    """ Profile Unlogged """
    response = requests.get(f"{BASE_URL}/profile", timeout=5)
    assert response.status_code == 403
    # if response.status_code == 403:
    #     print("✔️ Profile unlogged test successful.")
    # else:
    #     print("❌ Profile unlogged test failed.")


def profile_logged(session_id: str) -> None:
    """ Profile Logged """
    cookies = {"session_id": session_id}
    response = requests.get(f"{BASE_URL}/profile", cookies=cookies, timeout=5)
    assert response.status_code == 200
    data = response.json()
    assert data["email"] == EMAIL
    # print("✔️ Profile logged test successful.")


def log_out(session_id: str) -> None:
    """ Log out """
    endpoint = f"{BASE_URL}/sessions"
    cookies = {"session_id": session_id}
    response = requests.delete(endpoint, cookies=cookies, timeout=5)
    assert response.status_code == 200
    # print("✔️ Log out successful.")


def reset_password_token(email: str) -> str:
    """ Reset Password Token """
    endpoint = f"{BASE_URL}/reset_password"
    data = {"email": email}
    response = requests.post(endpoint, data=data, timeout=5)
    assert response.status_code == 200
    data = response.json()
    # print("✔️ Reset password token successful.")
    return data["reset_token"]


def update_password(email: str, reset_token: str, new_password: str) -> None:
    """ Update Password """
    endpoint = f"{BASE_URL}/reset_password"
    data = {"email": email, "reset_token": reset_token,
            "new_password": new_password}
    response = requests.put(endpoint, data=data, timeout=5)
    assert response.status_code == 200
    # print("✔️ Password updated successfully.")


EMAIL = "guillaume@holberton.io"
PASSWD = "b4l0u"
NEW_PASSWD = "t4rt1fl3tt3"


if __name__ == "__main__":

    register_user(EMAIL, PASSWD)
    log_in_wrong_password(EMAIL, NEW_PASSWD)
    profile_unlogged()
    session_id = log_in(EMAIL, PASSWD)
    profile_logged(session_id)
    log_out(session_id)
    reset_token = reset_password_token(EMAIL)
    update_password(EMAIL, reset_token, NEW_PASSWD)
    log_in(EMAIL, NEW_PASSWD)
