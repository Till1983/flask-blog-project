from flask import Flask, redirect, url_for, render_template
from . import blogposts, users

app = Flask(__name__)
app.config.from_object('app.config')

app.register_blueprint(blogposts.routes.blueprint)
app.register_blueprint(users.routes.blueprint)

@app.route("/")
@app.route("/home")
@app.route("/index")
def index():
    return render_template("index.html", title="Welcome")

@app.route('/about')
def about():
    return render_template("about.html", title="About this blog")

@app.route('/contact')
def contact():
    return render_template("contact.html", title="Contact me")