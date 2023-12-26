from flask import Blueprint

auth_bp = Blueprint('auth', __name__)

# Importez les routes après avoir créé le blueprint pour éviter les erreurs circulaires
from app.api.auth.routes import *
