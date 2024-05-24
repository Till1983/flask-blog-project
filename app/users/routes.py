from flask import Blueprint, render_template, request, redirect, url_for, flash
from flask_login import login_user, logout_user, login_required, current_user
from .models import Author
from app.extensions.database import db
from werkzeug.security import generate_password_hash, check_password_hash

blueprint = Blueprint('users', __name__)

@blueprint.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        password = request.form['psw']
        repeat_password = request.form['rpsw']

        if password != repeat_password:
            return render_template('register.html', title="Create Your Account Here", error="Passwords do not match!")

        hashed_password = generate_password_hash(password)
        new_user = Author(name=name, email=email, password=hashed_password)
        db.session.add(new_user)
        db.session.commit()
        message = "You have successfully created your account!"
        return render_template('login.html', title="Login", message=message)

    return render_template('register.html', title="Create Your Account Here")

@blueprint.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['psw']
        user = Author.query.filter_by(email=email).first()

        if user and check_password_hash(user.password, password):
            login_user(user)
            return redirect(url_for('users.login_success'))
        else:
            error = "Incorrect email or password. Please try again." if user else "User not found. Please check for typos."
            return render_template('login.html', title="Login", error=error)

    return render_template('login.html', title="Login")

@blueprint.route('/welcome')
def login_success():
    return render_template('success.html', title="Welcome!")

@blueprint.route('/logout')
@login_required
def logout():
    logout_user()
    return render_template('logout.html', title="Until next time!", message="You are now logged out")
"""
@blueprint.route('/run-seed-user')
def run_seed_user():
    if not Author.query.filter_by(name="John Doe").first():
        import app.scripts.seed
        return 'User seed completed'
    else:
        return 'User already exists'
"""