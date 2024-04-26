from flask import Blueprint, render_template, request, redirect, url_for, session, flash
from flask_login import login_user, logout_user, login_required, current_user, UserMixin
from .models import Author
from app.extensions.database import db, migrate
from werkzeug.security import generate_password_hash, check_password_hash


blueprint = Blueprint('users', __name__)


@blueprint.get('/register')
def show_registration_form():
    return render_template('register.html', title="Create Your Account Here")


@blueprint.post('/register')
def create_account():
    name = request.form['name']
    email = request.form['email']
    password = request.form['psw']
    repeat_password = request.form['rpsw']

    if password != repeat_password:
        return render_template('register.html', title="Create Your Account Here", error="Password do not match!")

    hashed_password = generate_password_hash(password)
    new_user = Author(name=name, email=email, password=hashed_password)
    db.session.add(new_user)
    db.session.commit()
    message = "You have successfully created your account!"
    return render_template('login.html', title="Login", message=message)


@blueprint.get('/login')
def show_login_form():
    return render_template('login.html', title="Login")


@blueprint.post('/login')
def login():
    email = request.form['email']
    password = request.form['psw']
    user = Author.query.filter_by(email=email).first()

    if user:
        if check_password_hash(user.password, password):
            login_user(user)
            message="You are now logged in!"
            return render_template('index.html', title="Login", message=message)
        else:
            return render_template('login.html', title="Login", error="Incorrect email or password. Please try again.")

    return render_template('login.html', title="Login", error="User not found. Please check for typos.")


@blueprint.get('/logout')
def logout():
    logout_user()
    return render_template('index.html', title="Until next time!")