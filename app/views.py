from flask import render_template, session, redirect, request, flash, url_for, send_file
from app import app, db
from models import User
import datetime
import flask_login
import csv
from flask_login import login_required, logout_user

login_manager = flask_login.LoginManager()
login_manager.init_app(app)



@login_manager.user_loader
def load_user(userid):
    return User.query.get(userid)

@app.route('/')
@app.route('/index', methods=['GET', 'POST'])
def index():
    return render_template("index.html")