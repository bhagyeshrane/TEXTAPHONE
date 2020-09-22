from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import InputRequired, Length, EqualTo

class RegistrationForm(FlaskForm):
    """ Registration Form"""

    username = StringField('username_label', validators=[InputRequired(message="Username Required"), Length(min=4, max=25, message="Username must be between 4 and 25 characters")])

    password = PasswordField('password_label',validators=[InputRequired(message="Password Required"), Length(min=8, max=25, message="Username must be between 4 and 25 characters")])
    confirm_pwd = PasswordField('confirm_pwd_label',validators=[InputRequired(message="Password Required"), EqualTo('password', message="Password must match!") ])

    submit_button = SubmitField('Create')

