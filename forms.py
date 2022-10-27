from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Email

#SignIn
class UserLoginForm(FlaskForm):
    first = StringField("First Name", validators = [DataRequired()])
    last = StringField("Last Name", validators = [DataRequired()])
    email = StringField("Email", validators = [DataRequired(), Email()])
    password = PasswordField("Password", validators = [DataRequired()])
    submit_button = SubmitField()

#SignUp
class UserSignInForm(FlaskForm):
    email = StringField("Email", validators = [DataRequired(), Email()])
    password = PasswordField("Password", validators = [DataRequired()])
    submit_button = SubmitField()