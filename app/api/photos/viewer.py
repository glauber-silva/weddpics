from http import HTTPStatus
import logging

import bson
from flask import make_response, jsonify, request
from flask_restx import Resource, Namespace
from flask_jwt_extended import jwt_required, get_jwt_identity

from app.database.models import Photo, User
from app.helpers.s3 import s3_upload_file

ns = Namespace("photos", description="See and manipulate information related to wedding photos")


@ns.route('/')
class PhotosApi(Resource):

    @ns.response(code=200, description="Return a list of photos")
    def get(self):
        """
        Return a list of Photos
        """
        photos = Photo.objects.all()
        return make_response(jsonify(photos), HTTPStatus.OK)

    @ns.doc("post_photo")
    @ns.response(code=201, description="Create photo")
    @jwt_required()
    def post(self):
        """ Insert a photo"""
        file = request.files['file']
        user_id = get_jwt_identity()
        user = User.objects.get(id=bson.objectid.ObjectId(user_id))
        image_url = s3_upload_file(file)
        photo = Photo(added_by=user, description=request.form['description'], image_url=image_url)
        photo.save()
        user.update(push__photos=photo)
        user.save()
        return make_response(jsonify({"message": "Image included"}),
                             HTTPStatus.CREATED)


@ns.route('/<photo_id>')
@ns.param('photo_id', 'The photo identifier')
class PhotoApi(Resource):

    @ns.doc('get_photo')
    @ns.response(code=200, description="Return a photo")
    @jwt_required()
    def get(self, photo_id):
        """
        Retrieves a photo with the entered id
        :param photo_id:
        :return:
        """
        photo = Photo.objects.get(id=photo_id)
        return make_response(jsonify(photo), HTTPStatus.OK)

    @ns.doc('update_photo')
    @ns.response(code=201, description="Update photo information")
    @jwt_required()
    def put(self, photo_id):
        """
        Edit a photo with the entered id
        :param photo_id:
        :return:
        """
        body = request.json
        Photo.objects.get(id=photo_id).update(**body)
        return make_response(jsonify({'message': 'updated'}), HTTPStatus.CREATED)

    @ns.doc('delete_photo')
    @ns.response(code=200, description="Delete a photo")
    @jwt_required()
    def delete(self, photo_id):
        """
        Delete a photo with the entered id
        :param photo_id:
        :return:
        """
        Photo.objects.get(id=photo_id).delete()
        return make_response(jsonify({'message': 'Deleted'}), HTTPStatus.OK)
