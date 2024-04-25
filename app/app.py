from flask import Flask, redirect, url_for, render_template
from . import blogposts, users, main_pages
from app.extensions.database import db, migrate
from app.extensions.authentication import login_manager
from os import environ

def create_app():
    app = Flask(__name__)
    app.config.from_object('app.config')
    app.secret_key = environ.get('SECRET_KEY')
    register_extensions(app)
    register_blueprints(app)
    login_manager.init_app(app)
    return app

def register_blueprints(app: Flask):
    app.register_blueprint(blogposts.routes.blueprint)
    app.register_blueprint(users.routes.blueprint)
    app.register_blueprint(main_pages.routes.blueprint)

def register_extensions(app: Flask):
    db.init_app(app)
    migrate.init_app(app, db, compare_type=True)