from http import HTTPStatus

from flask import make_response, jsonify, request
from flask_restx import Resource, Namespace

from app.database.models import Photo

ns = Namespace("photos", description="See and manipulate information related to wedding photos")


@ns.route('/')
class PhotosList(Resource):

    @ns.response(code=200, description="Return a list of photos")
    def get(self):
        photos = Photo.objects().to_json()
        return make_response(photos, HTTPStatus.OK)

    @ns.response(code=201, description="Create photos")
    def post(self):
        """ Insert a list of photos"""
        body = request.json
        photo = Photo(**body).save()
        photo_id = photo.id
        return make_response(jsonify({'id': str(photo_id)}), HTTPStatus.CREATED)


@ns.route('/<photo_id>')
@ns.param('photo_id', 'The photo identifier')
class Photo(Resource):

    @ns.doc('get_cat')
    @ns.response(code=200, description="Return a photos")
    def get(self, photo_id):
        photo = Photo.objects.get(id=photo_id).to_json()
        return make_response(photo, HTTPStatus.OK)

