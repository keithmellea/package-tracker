from flask import Blueprint, render_template, redirect, url_for
from ..shipping_form import PackageForm
from ..models import Package, db


bp = Blueprint('new_package', __name__, url_prefix='/new_package')

@bp.route("/", methods=['GET', 'POST'])
def new_package():
    form = PackageForm()
    if form.validate_on_submit():
        data = form.data
        new_package = Package(sender=data["sender"],
                              recipient=data["recipient"],
                              origin=data["origin"],
                              destination=data["destination"],
                              location=data["origin"])
        db.session.add(new_package)

        Package.advance_all_locations()
        return redirect(url_for("root.root"))
    return render_template('shipping_request.html', form=form)
