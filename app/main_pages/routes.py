from flask import Blueprint, render_template

blueprint = Blueprint('main_pages', __name__)

@blueprint.route("/")
@blueprint.route("/home")
@blueprint.route("/index")
def index():
    return render_template("index.html", title="Welcome")

@blueprint.route('/about')
def about():
    return render_template("about.html", title="About this blog")

@blueprint.route('/contact')
def contact():
    return render_template("contact.html", title="Contact me")