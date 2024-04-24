from flask import Blueprint, render_template, request, redirect, url_for, session, flash
#from flask_login import login_user, logout_user, login_required
from .models import Author
from app.extensions.database import db, migrate
from werkzeug.security import generate_password_hash, check_password_hash

blueprint = Blueprint('users', __name__)

@blueprint.route('/register', methods=['GET', 'POST'])
def create_account():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        password = request.form['psw']
        repeat_password = request.form['rpsw']

        # checks if password and repeat_password match
        if password != repeat_password:
            return render_template('register.html', title="Create Your Account Here", error="Password do not match!")

        # hashing the password
        hashed_password = generate_password_hash(password)

        # adding new user to the database
        new_user = Author(name=name, email=email, password=hashed_password)
        db.session.add(new_user)
        db.session.commit()

        return redirect(url_for('users.login'))

    return render_template('register.html', title="Create Your Account Here")

@blueprint.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['psw']
        user = Author.query.filter_by(email=email).first()

        if user:
            if check_password_hash(user.password, password):
                return redirect(url_for('main_pages.index'))
            else:
                return render_template('login.html', title="Login", error="Incorrect email or password. Please try again.")

        return render_template('login.html', title="Login", error="User not found. Please check for typos.")

    return render_template('login.html', title="Login")