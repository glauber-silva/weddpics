from http import HTTPStatus

from flask import make_response, jsonify
from flask_restx import Resource

from app.api import api


ns = api.namespace("health", description="Retrieve healthcheck information")


@ns.route("/", methods=["GET"])
class Health(Resource):
    @ns.response(code=200, description="General Check")
    def get(self):
        """
        Check API's heath status
        """
        return make_response(jsonify({"message": "Weddpics running"}), HTTPStatus.OK)


