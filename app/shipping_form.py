from flask_wtf import FlaskForm
from wtforms import SelectField, StringField,  BooleanField, SubmitField
from wtforms.validators import DataRequired
from map.map import map

class PackageForm(FlaskForm):
    sender = StringField("Sender", [DataRequired()])
    recipient = StringField("Recipient", [DataRequired()])
    origin = SelectField("Origin", [DataRequired()], choices=[(city, city) for city in map])
    destination = SelectField("Destination", [DataRequired()], choices=[(city, city) for city in map])
    express_shipping = BooleanField("Express Shipping", [DataRequired()])
    submit = SubmitField("Submit")
    cancel = SubmitField("Cancel")
