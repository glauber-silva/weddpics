import os

from flask import url_for
from flask_restx import Api as _Api
from jsonschema import FormatChecker

v = os.popen('git log | head -n 1')
commit = v.read().replace("commit ", "")[:7]


class PatchedApi(_Api):
    @property
    def specs_url(self):
        return url_for(self.endpoint('specs'))


api = PatchedApi(version='0.1#{}'.format(commit),
                 default='',
                 doc='/docs',
                 title='Wedding photo gallery',
                 description='Provide a photo gallery platform',
                 format_checker=FormatChecker())