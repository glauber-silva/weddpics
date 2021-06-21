from datetime import datetime

from flask_mongoengine import Document
from mongoengine import StringField, BooleanField, DateTimeField


class Photo(Document):
    meta = {'collection': 'photo'}
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
