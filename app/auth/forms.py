from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import DataRequired, Length, Email, EqualTo
from wtforms import ValidationError
from ..models import User


class LoginForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(),
                                             Length(1,64),
                                             Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember_me = BooleanField('Keep me logged in')
    submit = SubmitField('Log in')


class RegistrationForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(),
                                             Length(1, 64),
                                             Email()])
    username = StringField('Username', validators=[DataRequired(),
                                                   Length(1, 64)])
    password = PasswordField('Password', validators=[DataRequired(),
                                                     EqualTo('password2',
                                                             message='password \
                                                             must equal')])
    password2 = PasswordField('Confirm password', validators=[DataRequired()])
    submit = SubmitField('Register')

    def validate_email(self, field):
        if User.query.filter_by(email=field.data).first():
            raise ValidationError('Email already exists')

    def validate_username(self, field):
        if User.query.filter_by(username=field.data).first():
            raise ValidationError('Username already exists')
