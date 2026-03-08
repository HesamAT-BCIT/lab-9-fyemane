import os
from functools import wraps

from flask import request, jsonify
from firebase_admin import auth