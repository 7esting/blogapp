from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, PasswordField, BooleanField, \
    SubmitField
from wtforms.validators import ValidationError, DataRequired, Email, EqualTo, \
    Length
from app.models import User


class LoginForm(FlaskForm):
    # [This field is required.] is from validators=[DataRequired()]
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password&nbsp;&nbsp;&nbsp;&nbsp;<a href="/reset_password_request">Forgot password?</a>',
                                validators=[DataRequired()])
    remember_me = BooleanField('Remember me')
    submit = SubmitField('Sign In')


class RegistrationForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    password2 = PasswordField(
        'Repeat Password', validators=[DataRequired(), EqualTo('password')]
    )
    submit = SubmitField('Register')


    def validate_username(self, username):
        user = User.query.filter_by(username=username.data).first()
        if user is not None:
            raise ValidationError('Username already exists, choose another.')


    def validate_email(self, email):
        user = User.query.filter_by(email=email.data).first()
        if user is not None:
            raise ValidationError('Email already exists, use different email.')


class EditProfileForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired()]) 
    about_me = TextAreaField('About me', validators=[Length(min=0, max=140)])
    submit = SubmitField('Submit')

    # def __init__(self, original_username, *args, **kwargs):
    #     super(EditProfileForm, self).__init__(*args, **kwargs)
    #     self.original_username = original_username

    # Constructor
    def __init__(self, original_username, original_email, *args, **kwargs):
        super(EditProfileForm, self).__init__(*args, **kwargs)
        self.original_username = original_username
        self.original_email = original_email


    def validate_username(self, username):
        if username.data != self.original_username:
            user = User.query.filter_by(username=self.username.data).first()
            if user is not None:
                raise ValidationError('Please use a different username.')

    # New def
    def validate_email(self, email):
        if email.data != self.original_email:
            email = User.query.filter_by(email=self.email.data).first()
            if email is not None:
                raise ValidationError('Please use a different email.')


class PostForm(FlaskForm):
    post = TextAreaField('Leave a comment',
        validators=[DataRequired(), Length(min=1, max=140)])
    submit = SubmitField('Submit')


class ResetPasswordRequestForm(FlaskForm):
    email = StringField('Enter your email address', validators=[DataRequired(), Email()])
    submit = SubmitField('Send password reset email')


class ResetPasswordForm(FlaskForm):
    password = PasswordField('Password', validators=[DataRequired()])
    password2 = PasswordField(
        'Repeat Password', validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Reset Password')

    