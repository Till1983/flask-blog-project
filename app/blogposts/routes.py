from flask import Blueprint, render_template
from app.blogposts.models import Article, Topic

blueprint = Blueprint('blogposts', __name__)

@blueprint.route('/posts')
def posts():
    articles = Article.query.all()
    return render_template("posts.html", title="Thoughts and Musings", articles=articles)

@blueprint.route('/posts/<int:post_id>')
def post(post_id):
    '''Returns post by id from "articles" dictionary and shows error page if the post does not exist'''
    post = articles.get(post_id)
    if post:
        return render_template("post.html", post=post)
    else:
        return render_template("error.html", title="Error")