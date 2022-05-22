from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField
from wtforms.validators import DataRequired, Email


class RegisterForm(FlaskForm):
    username = StringField('Enter Username', validators=[
        DataRequired("Name Required")])
    email = StringField('Enter Email', validators=[
                        DataRequired("Email Required"), ])
    password = PasswordField('Enter Password', validators=[
                             DataRequired("Password Required")])
    submit = SubmitField('submit')