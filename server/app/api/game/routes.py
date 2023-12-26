from flask import jsonify

from . import game_bp

@game_bp.route('/register', methods=['POST'])
def register():
    # Ajoutez votre logique d'enregistrement d'utilisateur ici
    return jsonify({"message": "User registered successfully"})