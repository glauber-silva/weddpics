import datetime

from http import HTTPStatus

from flask import request, make_response, jsonify
from app.database.models import User
from flask_restx import Resource, Namespace
from flask_jwt_extended import create_access_token

ns = Namespace("users", "See and manipulate information related to users")


@ns.route('/signup')
class Signup(Resource):

    @ns.response(code=201, description="Create an user in Weddpics Gallery")
    def post(self):
        """
        SignUp Weddpics
        :return:
        """
        body = request.json
        user = User(**body)
        user.hash_password()
        user.save()
        return make_response(user.to_json(), HTTPStatus.CREATED)


@ns.route('/login')
class Login(Resource):

    @ns.response(code=200, description="LogIn to Weddpics Gallery")
    def post(self):
        """
        LogIn to app
        :return:
        """
        body = request.json
        user = User.objects.get(email=body.get('email'))
        authorized = user.check_password(body.get('password'))
        if not authorized:
            return make_response(jsonify({'error': 'Email or password invalid'}), HTTPStatus.UNAUTHORIZED)

        expires = datetime.timedelta(days=1)
        access_token = create_access_token(identity=str(user.id), expires_delta=expires)
        return make_response(jsonify({'token': access_token}), HTTPStatus.OK)
