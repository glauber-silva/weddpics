from .db import db


class Photo(db.Document):
    description = db.CharField('description', max_length=200, blank=True, null=True)
    is_approved = db.BooleanField('is approved', default=False, blank=True, null=True)
    created_at = db.DateTimeField('created at', auto_now_add=True)
    updated_at = db.DateTimeField('updated at', auto_now=True)