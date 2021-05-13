from flask import Blueprint, render_template
from ..models import Package

bp = Blueprint('root', __name__, url_prefix='')

@bp.route('/', methods=['GET'])
def root():
    packages = Package.query.all()
    return render_template("package_status.html", packages=packages)
