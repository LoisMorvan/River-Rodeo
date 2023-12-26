from flask import jsonify

from . import user_bp

from flask import Blueprint, jsonify, request
from app.api.user.models import User, db

user_bp = Blueprint('user', __name__)

@user_bp.route('/register', methods=['POST'])
def register():
    data = request.get_json()

    username = data.get('username')
    email = data.get('email')
    password = data.get('password')  # Assurez-vous de hasher le mot de passe avant le stockage en production

    new_user = User(username=username, email=email, password=password)

    db.session.add(new_user)
    db.session.commit()

    return jsonify({"message": "User registered successfully"})
