from flask_wtf import FlaskForm
from wtforms import SelectField, StringField,  BooleanField, SubmitField
from map.map import map

class PackageForm(FlaskForm):
    sender = StringField("Sender")
    recipient = StringField("Recipient")
    origin = SelectField("Origin", choices=[(city, city) for city in map])
    destination = SelectField("Destination", choices=[(city,city) for city in map])
    express_shipping = BooleanField("Express Shipping")
    submit = SubmitField("Submit")
    cancel = SubmitField("Cancel")
