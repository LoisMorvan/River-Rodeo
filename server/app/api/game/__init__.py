from flask import Blueprint

game_bp = Blueprint('game', __name__)

# Importez les routes après avoir créé le blueprint pour éviter les erreurs circulaires
from app.api.game.routes import *
