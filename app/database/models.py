from datetime import datetime

from flask_mongoengine import Document
from mongoengine import StringField, BooleanField, DateTimeField, EmailField
from flask_bcrypt import generate_password_hash, check_password_hash


# TODO Think about a Model Base class to add created and updated fields

class User(Document):
    meta = {'collection': 'users'}
    name = StringField(required=True)
    surname = StringField()
    email = EmailField(required=True, unique=True)
    password = StringField(required=True, min_length=6)
    is_staff = StringField(default=False, blank=True, null=True)
    created = DateTimeField()
    updated = DateTimeField()

    def save(self, *args, **kwargs):
        if not self.created:
            self.created = datetime.now()
        self.updated = datetime.now()
        return super(User, self).save(*args, **kwargs)

    def update(self, *args, **kwargs):
        self.updated = datetime.now()
        return super(User, self).save(*args, **kwargs)

    def hash_password(self):
        self.password = generate_password_hash(self.password).decode('utf8')

    def check_password(self, password):
        return check_password_hash(self.password, password)


class Photo(Document):
    meta = {'collection': 'photos'}
    owner = StringField(required=True)
    description = StringField(max_length=200, blank=True, null=True)
    image_url = StringField(blank=True, null=False)
    approved = BooleanField(default=False, blank=True, null=True)
    created = DateTimeField()
    updated = DateTimeField()

    def save(self, *args, **kwargs):
        if not self.created:
            self.created = datetime.now()
        self.updated = datetime.now()
        return super(Photo, self).save(*args, **kwargs)

    def update(self, *args, **kwargs):
        self.updated = datetime.now()
        return super(Photo, self).save(*args, **kwargs)
