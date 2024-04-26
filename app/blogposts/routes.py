from flask import Blueprint, render_template, request, redirect, url_for, flash
from app.blogposts.models import Article, Topic
from flask_login import login_required, login_user, logout_user, current_user


blueprint = Blueprint('blogposts', __name__)


@blueprint.route('/posts')
def posts():
    articles = Article.query.all()
    return render_template("posts.html", title="Thoughts and Musings", articles=articles)


@blueprint.get('/create-post')
@login_required
def get_create_post():
    return render_template("create-post.html")


@blueprint.before_request
def check_login_status():
    if not current_user.is_authenticated:
        flash('You need to log in to create a blogpost!', "error")
        return redirect(url_for('users.show_login_form'))


@blueprint.post('/create-post')
def post_create_post():
    name = request.form.get['name']
    title = request.form.get['title']
    blogpost = request.form.get['blogpost']
    return render_template("create-post.html")