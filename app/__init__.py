import os

from flask import Flask, Blueprint
from flask_mongoengine import MongoEngine
from flask_restx import Api
from app.config import DevelopmentConfig, TestingConfig, ProductionConfig
from app.api.health.viewer import ns as health

db = MongoEngine()
api = Api()


def create_app(deploy_env: str = os.getenv('FLASK_ENV', 'Development')) -> Flask:
    app = Flask(__name__)

    configuration = {
        'Development': DevelopmentConfig,
        'Testing': TestingConfig,
        'Production': ProductionConfig
    }[deploy_env]

    app.config.from_object(configuration)

    __configure_extensions(app)

    blueprint = Blueprint("login", __name__)
    app.register_blueprint(blueprint)
    api.add_namespace(health, "/health")

    return app


def __configure_extensions(app: Flask):
    db.init_app(app)
    api.init_app(app)

