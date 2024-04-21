from flask import Blueprint, render_template
from .models import Author

blueprint = Blueprint('users', __name__)

@blueprint.route('/register', methods=['GET', 'POST'])
def create_account():
    return render_template('register.html', title="Create Your Account Here")

@blueprint.route('/login', methods=['GET', 'POST'])
def login():
    return render_template('login.html', title="Login")