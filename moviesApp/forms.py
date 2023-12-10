from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, TextAreaField
from wtforms.validators import InputRequired, Email, EqualTo

class CreateAccountForm(FlaskForm):
    """Create acct form"""

    name = StringField("Name", validators=[InputRequired(message="Name must be entered")])
    username = StringField("Username", validators=[InputRequired(message="Username must be entered")])
    email = StringField("Email", validators=[InputRequired(message="Email must be entered"), Email()])
    password = PasswordField("Create Password", validators=[InputRequired(message="Password must be entered")])
    confirm_pwd = PasswordField("Confirm Password", validators=[InputRequired(message="Please confirm password"), EqualTo('password', message='Password must match')])


class LoginForm(FlaskForm):
    """Login form"""

    username = StringField("Username", validators=[InputRequired(message="Username must be entered")])
    password = PasswordField("Password", validators=[InputRequired(message="Password must be entered")])


class ReviewForm(FlaskForm):
    """Lets user write their reviews"""

    review = TextAreaField("Review", validators=[InputRequired(message="Must write a review to submit!")])