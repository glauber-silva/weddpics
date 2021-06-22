from http import HTTPStatus

from flask import request, make_response, jsonify
from app.database.models import User
from flask_restx import Resource, Namespace

ns = Namespace("users", "See and manipulate information related to users")


@ns.route('/signup')
class Signup(Resource):

    @ns.response(code=201, description="Create an user in Weddpics Gallery")
    def post(self):
        body = request.json
        user = User(**body)
        user.hash_password()
        user.save()
        return make_response(user.to_json(), HTTPStatus.CREATED)
