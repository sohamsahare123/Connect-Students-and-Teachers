from flask import Flask, render_template, redirect, url_for, flash, request
from flask_login import LoginManager, login_user, current_user, logout_user, login_required

from passlib.hash import pbkdf2_sha256
from datetime import datetime

import os, math, random

from forms import *
from models import *
from mailing import *

app = Flask(__name__)

app.secret_key = "\xce\xd6\xb9\x89\xe4|\x01\xc0\x8e\xf5E\x8f\x94F\xdd\xa3\xe4\x8c^W\xfe\xef\x86Y/\x14\xfe\xf4\x9d\xc6" #os.environ.get('SECRET')

app.config['SQLALCHEMY_DATABASE_URI'] = "postgres://prajwaldubey@vhackathon:Prajwal@123@vhackathon.postgres.database.azure.com:5432/vhackathon" #os.environ.get('DATABASE_URL')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

"""psql --host=vhackathon.postgres.database.azure.com --port=5432 --username=prajwaldubey@vhackathon --dbname=vhackathon"""

EMAIL_ADDRESS = "soham.sahare@vit.edu.in" #os.environ.get('EMAIL_ADDRESS')
EMAIL_PASSWORD = "Naz22291" #os.environ.get('EMAIL_PASSWORD')

db = SQLAlchemy(app)

login = LoginManager(app)
login.init_app(app)

@app.errorhandler(404) 
def not_found(e): 
  
    return "404 {}".format("HELLO")

@login.user_loader
def load_user(id):
    
    return User.query.get(int(id))

@app.route("/", methods = ['GET', 'POST'])
def main():

    return "Landing"

@app.route("/signup", methods = ['GET', 'POST'])
def signup():

    signup = SignUp()

    if signup.validate_on_submit():
        
        email = signup.email.data
        username = signup.username.data
        password = signup.password.data
        position = signup.position.data

        hashed_password = pbkdf2_sha256.hash(password)

        user = User(email = email, username = username, password = hashed_password, position = position)
        db.session.add(user)
        db.session.commit() 

        flash("Registered Successfully!!", 'success')

        # return "{} {} {} {}".format(email, username, password, position)
        return redirect(url_for('login'))

    return render_template('signup.html', form = signup)

@app.route("/login", methods = ['GET', 'POST'])
def login():

    login = LogIn()

    if login.validate_on_submit():

        user = login.username.data

        user_object = User.query.filter_by(username = user).first()
        login_user(user_object)

        flash("Login Successfull!!", 'success')
        return redirect(url_for('projects'))

    return render_template("login.html", form = login)

@app.route("/logout", methods = ['GET', 'POST'])
def logout():

    if not current_user.is_authenticated:

        flash("Please Login!!", 'danger')
        return redirect(url_for('login'))

    logout_user()
    flash("Logged out successfully!!", 'success')

    return "LOGGED OUT"
    return render_template("main.html")

@app.route("/projects", methods = ['GET', 'POST'])
#@login_required
def projects():

    add_posts = AddProjectPost()

    userid = current_user.get_id()
    user = User.query.filter_by(id = userid).first()
    user_name = user.username
    status = "1"

    posts = AddProject.query.all()

    if not current_user.is_authenticated:

        flash("Please Login!!", 'danger')
        status = "0"
        return render_template("projects.html", username = "username", add_project_form = add_posts, status = status, posts = posts)

    return render_template("projects.html", username = user_name, add_project_form = add_posts, status = status, posts = posts)

@app.route("/addproject", methods = ["POST"])
def addproject():

    if not current_user.is_authenticated:

        flash("Please Login!!", 'danger')
        return redirect(url_for('login'))

    add_posts = AddProjectPost()

    if add_posts.validate_on_submit():

        title = add_posts.title.data
        description = add_posts.description.data
        link = add_posts.link.data

        now = datetime.now()

        date = str(now.strftime("%d/%m/%Y"))
        time = str(now.strftime("%H:%M"))

        date_time = "{} {}".format(date, time)

        userid = current_user.get_id()
        user = User.query.filter_by(id = userid).first()
        username = user.username

        post = AddProject(title = title, description = description, link = link, date_time = date_time, userid = userid, username = username)
        db.session.add(post)
        db.session.commit() 

        return "{} {} {} {}".format(title, description, link, date_time)

@app.route("/forgotpassword", methods = ["GET", "POST"])
def forgotpassword():

    forgot_password = ForgetPassword()
    login = LogIn()

    if forgot_password.validate_on_submit():

        email = forgot_password.email.data
        TO = email
        
        user_email = User.query.filter_by(email = email).first()
        if (user_email):

            user = User.query.filter_by(email = email).first()

            username = user.username

            string = '0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
            password = "" 
            length = len(string) 
            for i in range(10):  
                password += string[math.floor(random.random() * length)] 

            hashed_password = pbkdf2_sha256.hash(password)

            db.session.query(User).filter(User.email == email).update({User.password: hashed_password}, synchronize_session=False)
            db.session.commit()

            send_mail_password_forgot(TO, EMAIL_ADDRESS, EMAIL_PASSWORD, username, password)

            flash("Temporary Password has been sent to your registered email", "success")

            return render_template("login.html", form = login)
        else:
            flash("This email is not registered", "danger")
            return render_template("forgotpassword.html", form = forgot_password)

    return render_template("forgotpassword.html", form = forgot_password)

if __name__ == "__main__":

    app.run(debug = True)