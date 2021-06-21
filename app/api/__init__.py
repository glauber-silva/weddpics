import os

from flask import url_for, Blueprint
from flask_restx import Api
from app.api.health.viewer import ns as health
from app.api.photos.viewer import ns as photos

v = os.popen('git log | head -n 1')
commit = v.read().replace("commit ", "")[:7]

api_bp = Blueprint('api', __name__, url_prefix='/api')

api = Api(api_bp, version='0.1#{}'.format(commit), title='Wedding photo gallery',
          description='Provide a photo gallery platform', doc='/docs')

api.add_namespace(health)
api.add_namespace(photos)
