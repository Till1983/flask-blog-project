from flask import Flask, redirect, url_for, render_template
from . import blogposts, users, main_pages

def create_app():
    app = Flask(__name__)
    app.config.from_object('app.config')
    register_blueprints(app)
    return app

def register_blueprints(app: Flask):
    app.register_blueprint(blogposts.routes.blueprint)
    app.register_blueprint(users.routes.blueprint)
    app.register_blueprint(main_pages.routes.blueprint)