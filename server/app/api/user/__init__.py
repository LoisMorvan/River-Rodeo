from flask import Blueprint

user_bp = Blueprint('user', __name__)

# Importez les routes après avoir créé le blueprint pour éviter les erreurs circulaires
from app.api.user.routes import *
