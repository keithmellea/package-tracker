from flask import Blueprint, render_template

bp = Blueprint('new_package', __name__, url_prefix='/new_package')

@bp.route("/new_package", methods=['GET', 'POST'])
def new_package():
    form = PackageForm()
    return render_template('shipping_request.html', form = form)
