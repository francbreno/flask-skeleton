from flask import Flask
from flask_marshmallow import Marshmallow
from flask_sqlalchemy import SQLAlchemy
from flask_jwt import JWT

from config import create_config

db = SQLAlchemy()
ma = Marshmallow()

from .services.auth import authenticate, identity
from .api import create_api_bp

def create_app(config_name):
    app = Flask(__name__)

    config = create_config(config_name)
    app.config.from_object(config)

    db.init_app(app)
    ma.init_app(app)
    jwt = JWT(app, authenticate, identity) # cria /auth

    _initialize_blueprints(app)

    return app

def _initialize_blueprints(app):
    api_bp = create_api_bp()
    app.register_blueprint(api_bp, url_prefix='/api')