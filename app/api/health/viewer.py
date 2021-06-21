from http import HTTPStatus

from flask import make_response, jsonify
from flask_restx import Resource, Namespace

ns = Namespace("health", "Retrieve health check information")


@ns.route("/", methods=["GET"])
class Health(Resource):
    @ns.response(code=200, description="General Check")
    def get(self):
        """
        Check API's heath status
        """
        return make_response(jsonify({"message": "Weddpics running"}), HTTPStatus.OK)


