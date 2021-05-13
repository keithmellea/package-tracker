from flask import Blueprint, render_template, redirect
from flask.helpers import url_for
from ..models import Package, User
from flask_login import current_user, login_user, logout_user

bp = Blueprint('root', __name__, url_prefix='')

@bp.route('/', methods=['GET'])
def root():
    if current_user.is_authenticated:
        # refactor for current_user later
        packages = Package.query.all()
        return render_template("package_status.html", packages=packages)
    form = LoginForm()
    if form.validate_on_submit():
        username = form.username.data
        user = User.query.filter(User.username==username).first()
        if not user or not user.check_password(form.password.data):
            return redirect(url_for(".root"))
        packages = Package.query.filter(Package.sender_id==user.id).all()
        return redirect(url_for('.root')) #user fail login
    return render_template("login.html")
