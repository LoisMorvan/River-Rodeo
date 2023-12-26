from flask import Flask, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
from flask_migrate import Migrate



# instantiate the app
app = Flask(__name__)
app.config.from_pyfile('config.py')  # Assurez-vous que le fichier de configuration est correct

# enable CORS
CORS(app, resources={r'/*': {'origins': '*'}})

db = SQLAlchemy(app)
migrate = Migrate(app, db)


from app.api import auth, game, user # Importez après avoir défini app pour éviter des erreurs circulaires


app.register_blueprint(auth.auth_bp, url_prefix='/api/auth')
app.register_blueprint(game.game_bp, url_prefix='/api/game')
app.register_blueprint(user.user_bp, url_prefix='/api/user')
