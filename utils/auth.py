from flask import session


def get_current_user():
    if not session.get("logged_in"):
        return None
    return session.get("username")