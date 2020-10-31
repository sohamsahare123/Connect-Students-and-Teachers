from flask_wtf import FlaskForm

from wtforms import StringField, PasswordField, SubmitField, RadioField, SelectField
from wtforms.fields.html5 import EmailField
from wtforms.validators import InputRequired, Length, EqualTo, ValidationError

from models import *

from passlib.hash import pbkdf2_sha256

def invalid(form, field):

    username = form.username.data
    password = field.data
    
    user_data = User.query.filter_by(username = username).first()
        
    if user_data is None:
        raise ValidationError("Username or password is incorrect")

    elif not pbkdf2_sha256.verify(password, user_data.password):
        raise ValidationError("Username or password is incorrect")

def validate_email(form, field):

        user_object = User.query.filter_by(username = form.email.data).first()
        
        if user_object:
            raise ValidationError("Email already exists")

def validate_username(form, username):

        user_object = User.query.filter_by(username = form.username.data).first()
        if user_object:
            raise ValidationError("Username already exists")

class SignUp(FlaskForm): # Signup

    email = EmailField("email", validators = [InputRequired("Email Required"), validate_email])
    username = StringField("username", validators = [InputRequired("Username Required"), validate_username, Length(min = 5, max = 20, message = "Username must be between 5 to 20 characters")])
    password = PasswordField("password", validators = [InputRequired("Password Required"), Length(min = 5, max = 20, message = "Password must be between 5 to 20 characters")])
    confirm_password = PasswordField("confirm_password", validators = [InputRequired("Password Required"), EqualTo("password", message = "Password must match")])
    position = RadioField("position", choices = [("teacher", "Teacher"), ("student", "Student")])
    branch = SelectField("branch", choices = [('biomedical', 'Biomedical'),('computer engineering','Computer Engineering'),('electrical', 'Electrical'), ('electronics', 'Electronics'), ('electronics and telecommunication', 'Electronics and Telecommunication'),('information technology','Information Technology'),('other','Other')])
    
    college_name = StringField("college_name", validators = [InputRequired("College Name Required")])

    submit = SubmitField("Submit")

class LogIn(FlaskForm): # Login
    
    username = StringField("username_label", validators = [InputRequired("Username Required")])
    password = PasswordField("password_label", validators = [InputRequired("Password Required"), invalid])

    submit = SubmitField("Submit")

class ForgetPassword(FlaskForm):
    email = EmailField("email", validators = [InputRequired("Email Required"), validate_email])
    
    submit = SubmitField("Submit")

class AddProjectPost(FlaskForm): 

    title = StringField("title", validators = [InputRequired("Title Required")])
    description = StringField("description", validators = [InputRequired("Description Required")])
    link = StringField("link", validators = [InputRequired("Link Required")])

    submit = SubmitField('Add')

# class AddProjectComments(FlaskForm):

#     comment = StringField("comment", validators = [InputRequired("Comment Required")])
#     project_id = StringField("project_id", validators = [InputRequired("project_id Required")])

#     submit = SubmitField('Add')