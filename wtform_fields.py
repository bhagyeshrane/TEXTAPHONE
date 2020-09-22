from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import InputRequired, Length, EqualTo, ValidationError
from models import User
from passlib.hash import pbkdf2_sha256


def invalid_credentials(form, field):
    """Username and password checker """

    username_entered = form.username.data
    password_entered = field.data

    #check credentials are valid
    user_object = User.query.filter_by(username=username_entered).first()
    if user_object is None:
        raise ValidationError("Username and password is incorrect")
    elif not pbkdf2_sha256.verify(password_entered, user_object.password):
        raise ValidationError("Username and password is incorrect")


class RegistrationForm(FlaskForm):
    """ Registration Form """

    username = StringField('username_label', validators=[InputRequired(message="Username Required"), Length(min=4, max=25, message="Username must be between 4 and 25 characters")])

    password = PasswordField('password_label',validators=[InputRequired(message="Password Required"), Length(min=8, max=25, message="Username must be between 4 and 25 characters")])
    confirm_pwd = PasswordField('confirm_pwd_label',validators=[InputRequired(message="Password Required"), EqualTo('password', message="Password must match!") ])

    submit_button = SubmitField('Sign up')


    def validate_username(self, username):
        user_object = User.query.filter_by(username=username.data).first()
        if user_object:
            raise ValidationError("Username already exist. Please use another username.")

class LoginForm(FlaskForm):
    """ Login Form """

    username = StringField('username_label', validators=[InputRequired(message="Username Required")])
    password = StringField('password_label', validators=[InputRequired(message="Password Required"),invalid_credentials])
    submit_button = SubmitField('Sign in')
