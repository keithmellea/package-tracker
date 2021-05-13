from flask_wtf import FlaskForm
from wtforms.fields import StringField, PasswordField, SubmitField, EmailField
from wtforms.validators import DataRequired

class LoginForm(FlaskForm):
    username = StringField('Username', [DataRequired()])
    password = PasswordField('Password', [DataRequired()])
    submit = SubmitField('Login')
