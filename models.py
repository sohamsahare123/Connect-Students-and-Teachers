from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin

db = SQLAlchemy()

class User(UserMixin, db.Model):

    __tablename__ = 'users'

    '''CREATE TABLE users (id SERIAL PRIMARY KEY, email VARCHAR(60) UNIQUE NOT NULL, username VARCHAR(20) UNIQUE NOT NULL, password TEXT NOT NULL, position TEXT NOT NULL, branch TEXT NOT NULL, college_name TEXT NOT NULL, linkedin TEXT, github TEXT);'''

    id = db.Column(db.Integer, primary_key = True)
    email = db.Column(db.String(60), unique = True, nullable = False)
    username = db.Column(db.String(20), unique = True, nullable = False)
    password = db.Column(db.String(), nullable = False)
    position = db.Column(db.String(), nullable = False)
    branch = db.Column(db.String(), nullable = False)
    college_name = db.Column(db.String(), nullable = False)
    linkedin = db.Column(db.String(), nullable = True)
    github = db.Column(db.String(), nullable = True)

class Collab(UserMixin, db.Model):

    __tablename__ = "collab"

    '''CREATE TABLE collab (id SERIAL PRIMARY KEY, follower_id INT NOT NULL, follower_username TEXT NOT NULL, followed_id INT NOT NULL, followed_username TEXT NOT NULL,  response TEXT);'''
    
    id = db.Column(db.Integer, primary_key = True)
    follower_id = db.Column(db.Integer, nullable = False)
    follower_username = db.Column(db.String(), nullable = False)
    followed_id = db.Column(db.Integer, nullable = False)
    followed_username = db.Column(db.String(), nullable = False)
    response = db.Column(db.String(), nullable = False)

class AddProject(UserMixin, db.Model):

    __tablename__ = "addproject"

    '''CREATE TABLE addproject (id SERIAL PRIMARY KEY, title TEXT NOT NULL, description TEXT NOT NULL, link TEXT NOT NULL, date_time TEXT NOT NULL, userid INT NOT NULL, username TEXT NOT NULL);'''

    id = db.Column(db.Integer, primary_key = True)
    title = db.Column(db.String(), nullable = False)
    description = db.Column(db.String(), nullable = False)
    link = db.Column(db.String(), nullable = False)
    date_time = db.Column(db.String(), nullable = False)
    userid = db.Column(db.String(), nullable = False)
    username = db.Column(db.String(), nullable = False)

class ProjectComments(UserMixin, db.Model):

    __tablename__ = "projectcomments"

    '''CREATE TABLE projectcomments (id SERIAL PRIMARY KEY, comment TEXT NOT NULL, date_time TEXT NOT NULL, userid INT NOT NULL, username TEXT NOT NULL, projectid INT NOT NULL);'''

    id = db.Column(db.Integer, primary_key = True)
    comment = db.Column(db.String(), nullable = False)
    date_time = db.Column(db.String(), nullable = False)
    userid = db.Column(db.String(), nullable = False)
    username = db.Column(db.String(), nullable = False)
    projectid = db.Column(db.String(), nullable = False)

class AddAcademics(UserMixin, db.Model):

    __tablename__ = "addacademics"

    '''CREATE TABLE addacademics (id SERIAL PRIMARY KEY, title TEXT NOT NULL, description TEXT NOT NULL, link TEXT NOT NULL, date_time TEXT NOT NULL, userid INT NOT NULL, username TEXT NOT NULL);'''

    id = db.Column(db.Integer, primary_key = True)
    title = db.Column(db.String(), nullable = False)
    description = db.Column(db.String(), nullable = False)
    link = db.Column(db.String(), nullable = False)
    date_time = db.Column(db.String(), nullable = False)
    userid = db.Column(db.String(), nullable = False)
    username = db.Column(db.String(), nullable = False)

class AcademicComments(UserMixin, db.Model):

    __tablename__ = "academiccomments"

    '''CREATE TABLE academiccomments (id SERIAL PRIMARY KEY, comment TEXT NOT NULL, date_time TEXT NOT NULL, userid INT NOT NULL, username TEXT NOT NULL, projectid INT NOT NULL);'''

    id = db.Column(db.Integer, primary_key = True)
    comment = db.Column(db.String(), nullable = False)
    date_time = db.Column(db.String(), nullable = False)
    userid = db.Column(db.String(), nullable = False)
    username = db.Column(db.String(), nullable = False)
    projectid = db.Column(db.String(), nullable = False)

class AddIdeas(UserMixin, db.Model):

    __tablename__ = "addideas"

    '''CREATE TABLE addideas (id SERIAL PRIMARY KEY, title TEXT NOT NULL, description TEXT NOT NULL, link TEXT NOT NULL, date_time TEXT NOT NULL, userid INT NOT NULL, username TEXT NOT NULL);'''

    id = db.Column(db.Integer, primary_key = True)
    title = db.Column(db.String(), nullable = False)
    description = db.Column(db.String(), nullable = False)
    link = db.Column(db.String(), nullable = False)
    date_time = db.Column(db.String(), nullable = False)
    userid = db.Column(db.String(), nullable = False)
    username = db.Column(db.String(), nullable = False)


class IdeasComments(UserMixin, db.Model):

    __tablename__ = "ideascomments"

    '''CREATE TABLE ideascomments (id SERIAL PRIMARY KEY, comment TEXT NOT NULL, date_time TEXT NOT NULL, userid INT NOT NULL, username TEXT NOT NULL, projectid INT NOT NULL);'''

    id = db.Column(db.Integer, primary_key = True)
    comment = db.Column(db.String(), nullable = False)
    date_time = db.Column(db.String(), nullable = False)
    userid = db.Column(db.String(), nullable = False)
    username = db.Column(db.String(), nullable = False)
    projectid = db.Column(db.String(), nullable = False)