from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_cors import CORS


app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///aardvark.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

CORS_ORIGINS = ['http://localhost:3000']
CORS_METHODS = ['GET', 'POST', 'PUT', 'DELETE']
CORS_ALLOWED_HEADERS = ['Content-Type']

db = SQLAlchemy()

Migrate(app, db)

db.init_app(app)