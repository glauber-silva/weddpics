from flask import Blueprint

bp_common = Blueprint('common', __name__, url_prefix='')


@bp_common.route('/', methods=['GET'])
def index():
    return "Weddpics API"