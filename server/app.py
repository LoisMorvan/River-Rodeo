from flask import Flask, jsonify
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.sql import func
from dotenv import load_dotenv
import os

# Load environment variables
load_dotenv()

# instantiate the app
app = Flask(__name__)
app.config.from_object(__name__)

# enable CORS
CORS(app, resources={r'/*': {'origins': '*'}})


# Load configuration based on environment
environment = os.environ.get('FLASK_ENV')

if environment == 'development':
    app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DEV_DATABASE_URI')
else:
    app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('PROD_DATABASE_URI')

app.config['ENV'] = environment
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)


# sanity check route
@app.route('/ping', methods=['GET'])
def ping_pong():
    return jsonify('pong!')

# Table User


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    userName = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(80), unique=True, nullable=False)
    password = db.Column(db.String(80), nullable=False)
    created_at = db.Column(db.DateTime(timezone=True),
                           server_default=func.now())

    def __repr__(self):
        return f'<User {self.userName}>'


# Create all class define here
with app.app_context():
    db.create_all()


if __name__ == '__main__':
    app.run()
