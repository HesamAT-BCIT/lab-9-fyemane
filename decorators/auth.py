import os
from functools import wraps

from flask import request, jsonify
from firebase_admin import auth

def require_api_key(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        expected_key = os.environ.get("SENSOR_API_KEY")

        if not expected_key:
            return jsonify({"error": "API key not configured on server"}), 500

        provided_key = request.headers.get("X-API-Key")

        if not provided_key:
            return jsonify({"error": "Missing X-API-Key header"}), 401

        if provided_key != expected_key:
            return jsonify({"error": "Unauthorized"}), 401

        return f(*args, **kwargs)

    return decorated_function