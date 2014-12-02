from flask import render_template, session, redirect, request, flash, url_for, send_file
from app import app, db
from models import User
from forms import NewMentor
import datetime
import flask_login
import csv
from flask_login import login_required, logout_user

login_manager = flask_login.LoginManager()
login_manager.init_app(app)



@login_manager.user_loader
def load_user(id_no):
    return User.query.get(id_no)

@app.route('/')
@app.route('/index', methods=['GET', 'POST'])
def index():
    return render_template("index.html")

@app.route('/add_user', methods=['GET', 'POST'])
def add_user():
    form = NewMentor()
    if form.validate_on_submit():
        first_name = form.first_name.data
        last_name = form.last_name.data
        email = form.email.data
        phone_no = form.phone_no.data
        password = form.password.data
        title = form.title.data
        ocu = form.ocu.data
        specialisations = form.specialisations.data
        cv = form.cv.data
        mentor = form.mentor.data
        coffee = form.coffee.data
        phone_chat = form.phone_chat.data
        email_chat = form.email_chat.data
        id_no = len(User.query.all()) + 1
        user = User(password=password, first_name=first_name, last_name=last_name, email=email, phone_no=phone_no, title=title, ocu=ocu, specialisations=specialisations,
                    cv=cv, mentor=mentor, coffee=coffee, phone_chat=phone_chat, email_chat=email_chat, id_no=id_no)
        db.session.add(user)
        db.session.commit()
        print form.errors
        return redirect('/index')
    print form.errors
    return render_template("add_user.html", form=form)

@app.route('/list_users', methods=['GET'])
def list_users():
    users = User.query.all()
    user_list = []
    for user in users:
        user_stats = [user.first_name, user.last_name, user.rank, user.role, user.coffee,
                      user.mentor, user.phone_no, user.email_chat]
        user_list.append(user_stats)
    return render_template("list_users.html", user_list=user_list)