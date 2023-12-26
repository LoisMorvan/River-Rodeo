from flask import jsonify
from app.api.auth import auth_bp  # Importez le blueprint auth_bp ici

@auth_bp.route('/register', methods=['POST'])
def register():
    # Ajoutez votre logique d'enregistrement d'utilisateur ici
    return jsonify({"message": "User registered successfully"})
