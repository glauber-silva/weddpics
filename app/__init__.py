import os

from flask import Flask
from flask_bcrypt import Bcrypt
from flask_mongoengine import MongoEngine
from werkzeug.middleware.proxy_fix import ProxyFix
from flask_jwt_extended import JWTManager

from app.api import api
from app.api import api_bp
from app.config import DevelopmentConfig, TestingConfig, ProductionConfig
from app.api.health.viewer import ns as health
from app.api.photos.viewer import ns as photos
from flask_cors import CORS

db = MongoEngine()
bcrypt = Bcrypt()
jwt = JWTManager()
cors = CORS()


def create_app(deploy_env: str = os.getenv('FLASK_ENV', 'Development')) -> Flask:
    app = Flask(__name__)
    app.wsgi_app = ProxyFix(app.wsgi_app)
    configuration = {
        'Development': DevelopmentConfig,
        'Testing': TestingConfig,
        'Production': ProductionConfig
    }[deploy_env]

    app.config.from_object(configuration)

    __configure_extensions(app)

    app.register_blueprint(api_bp)
    return app


def __configure_extensions(app: Flask):
    db.init_app(app)
    bcrypt.init_app(app)
    jwt.init_app(app)
    cors.init_app(app)
