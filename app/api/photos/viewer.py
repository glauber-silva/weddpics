from http import HTTPStatus

from flask import make_response, jsonify, request
from flask_restx import Resource, Namespace

from app.database.models import Photo

ns = Namespace("photos", description="See and manipulate information related to wedding photos")


@ns.route('/')
class PhotosList(Resource):

    @ns.response(code=200, description="Return a list of photos")
    def get(self):
        """
        Return a list of Photos
        """
        photos = Photo.objects().to_json()
        return make_response(photos, HTTPStatus.OK)

    @ns.response(code=201, description="Create photo")
    def post(self):
        """ Insert a list of photos"""
        body = request.json
        photos = Photo(**body).save()
        photos.to_json()
        return make_response(photos, HTTPStatus.CREATED)


@ns.route('/<photo_id>')
@ns.param('photo_id', 'The photo identifier')
class Photo(Resource):

    @ns.doc('get_photo')
    @ns.response(code=200, description="Return a photos")
    def get(self, photo_id):
        """
        Retrieves a photo with the entered id
        :param photo_id:
        :return:
        """
        photo = Photo.objects.get(id=photo_id)
        return make_response(photo.to_json(), HTTPStatus.OK)

    @ns.doc('update_photo')
    @ns.response(code=201, description="Update photo information")
    def put(self, photo_id):
        """
        Edit a photo with the entered id
        :param photo_id:
        :return:
        """
        body = request.json
        photo = Photo.objects.get(id=photo_id).update(**body)
        return make_response(photo.to_json(), HTTPStatus.CREATED)

    @ns.doc('delete_photo')
    @ns.response(code=200, description="Delete a photo")
    def delete(self, photo_id):
        """
        Delete a photo with the entered id
        :param photo_id:
        :return:
        """
        Photo.objects.get(id=photo_id).delete()
        return make_response(jsonify({'message': 'Deleted'}), HTTPStatus.OK)
