import requests
from flask import request, jsonify, render_template, session, redirect, url_for
from firebase_admin import auth
from firebase import db
from config import Config
from . import auth_bp
