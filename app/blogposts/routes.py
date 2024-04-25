from flask import Blueprint, render_template
from app.blogposts.models import Article, Topic

blueprint = Blueprint('blogposts', __name__)

@blueprint.route('/posts')
def posts():
    articles = Article.query.all()
    return render_template("posts.html", title="Thoughts and Musings", articles=articles)

@blueprint.route('/create-post')
def create_post():
    return render_template("create-post.html")