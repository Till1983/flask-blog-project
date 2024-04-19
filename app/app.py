from flask import Flask, redirect, url_for, render_template
from . import blogposts #simple_pages

app = Flask(__name__)
app.config.from_object('app.config')

app.register_blueprint(blogposts.routes.blueprint)
#app.register_blueprint(simple_pages.routes.blueprint)