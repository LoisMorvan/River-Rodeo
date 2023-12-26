from flask import Blueprint

# Créez les blueprints ici pour éviter les erreurs circulaires
auth_bp = Blueprint('auth', __name__)
game_bp = Blueprint('game', __name__)
user_bp = Blueprint('user', __name__)

# Enable CORS
from flask_cors import CORS
CORS(auth_bp, resources={r'/*': {'origins': '*'}})
CORS(game_bp, resources={r'/*': {'origins': '*'}})
CORS(user_bp, resources={r'/*': {'origins': '*'}})

# Importez les routes après avoir créé les blueprints pour éviter les erreurs circulaires
from app.api.auth.routes import *
from app.api.game.routes import *
from app.api.user.routes import *
