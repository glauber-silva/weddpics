from flask_mongoengine import Document
from mongoengine import StringField, BooleanField, DateTimeField


class Photo(Document):
    meta = {'collection': 'photo'}
    owner = StringField(required=True)
    description = StringField(max_length=200, blank=True, null=True)
    image_url = StringField(blank=True, null=False)
    approved = BooleanField(default=False, blank=True, null=True)
    created = DateTimeField(auto_now_add=True)
    updated = DateTimeField(auto_now=True)
