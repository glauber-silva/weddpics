from flask_mongoengine import Document
from mongoengine import StringField, BooleanField, DateTimeField


class Photo(Document):
    owner = StringField(required=True)
    description = StringField(max_length=200, blank=True, null=True)
    image_url = StringField(blank=True, null=False)
    approved = BooleanField(default=False, blank=True, null=True)
    created = DateTimeField(auto_now_add=True)
    updated = DateTimeField(auto_now=True)

    # owner = models.ForeignKey('users.User', verbose_name='owner', related_name='photos', on_delete=models.CASCADE)
    # description = models.CharField('description', max_length=200, blank=True, null=True)
    # photo_url = models.CharField('photo url', blank=True, null=True, max_length=300)
    # is_approved = models.BooleanField('is approved', default=False, blank=True, null=True)
    # created_at = models.DateTimeField('created at', auto_now_add=True)
    # updated_at = models.DateTimeField('updated at', auto_now=True)
