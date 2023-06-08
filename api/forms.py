from wtforms import (
    StringField,
    PasswordField,
    SubmitField
)

from flask_wtf import FlaskForm
from wtforms.validators import InputRequired, Length, EqualTo, Email, Regexp ,Optional
from flask_login import current_user
from wtforms import ValidationError,validators
from api.databases import UserDatabaseOperation

userDb = UserDatabaseOperation()
class login_form(FlaskForm):
    username = StringField(validators=[InputRequired(), Email(), Length(1, 64)])
    pwd = PasswordField(validators=[InputRequired(), Length(min=8, max=72)])
    # Placeholder labels to enable form rendering
    username = StringField(
        validators=[InputRequired()]
    )
    submit = SubmitField('Login')


class register_form(FlaskForm):
    username = StringField(
        validators=[
            InputRequired(),
            Length(3, 20, message="Please provide a valid name"),
            Regexp(
                "^[A-Za-z][A-Za-z0-9_.]*$",
                0,
                "Usernames must have only letters, " "numbers, dots or underscores",
            ),
        ]
    )
    email = StringField(validators=[InputRequired(), Email(), Length(1, 64)])
    pwd = PasswordField(validators=[InputRequired(), Length(8, 72)])
    cpwd = PasswordField(
        validators=[
            InputRequired(),
            Length(8, 72),
            EqualTo("pwd", message="Passwords must match !"),
        ]
    )
    submit = SubmitField('Login')


    def validate_email(self, email):
        if userDb.get_user(usrname=email.data):
            raise ValidationError("Email already registered!")

    def validate_uname(self, username):
        if userDb.get_user(username=username.data):
                raise ValidationError("Username already taken!")