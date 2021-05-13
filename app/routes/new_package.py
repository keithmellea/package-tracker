from flask import Blueprint, render_template, redirect, url_for
from ..shipping_form import PackageForm

bp = Blueprint('new_package', __name__, url_prefix='/new_package')

@bp.route("/", methods=['GET', 'POST'])
def new_package():
    form = PackageForm()
    if form.validate_on_submit():
         return redirect(url_for("root.root"))
    return render_template('shipping_request.html', form=form)
