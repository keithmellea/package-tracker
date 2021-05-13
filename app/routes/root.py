from flask import Blueprint, render_template

bp = Blueprint('root', __name__, url_prefix='')

@bp.route('/', methods=['GET'])
def root():
    return 'here'
