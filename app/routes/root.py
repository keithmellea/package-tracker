from flask import Blueprint, render_template, redirect
from ..models import Package
from flask_login import current_user, login_user, logout_user

bp = Blueprint('root', __name__, url_prefix='')

@bp.route('/', methods=['GET'])
def root():
    if current_user.is_authenticated:
        # refactor for current_user later
        packages = Package.query.all() 
        return render_template("package_status.html", packages=packages)
    form = LoginForm()