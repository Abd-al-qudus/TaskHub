from wtforms import (
    StringField,
    PasswordField,
    SubmitField
)

from flask_wtf import FlaskForm
from wtforms.validators import (InputRequired, Length, EqualTo, Email, Regexp)
from wtforms import ValidationError
from api.databases import UserDatabaseOperation

userDb = UserDatabaseOperation()
class login_form(FlaskForm):
    username = StringField(validators=[InputRequired(), Email(), Length(1, 64)])
    pwd = PasswordField(validators=[InputRequired(), Length(min=8, max=72)])
    username = StringField(validators=[InputRequired()])
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
    pwd = PasswordField(validators=[InputRequired(), Length(8, 72)])
    cpwd = PasswordField(
        validators=[
            InputRequired(),
            Length(8, 72),
            EqualTo("pwd", message="Passwords must match !"),
        ]
    )
    submit = SubmitField('Login')
