from flask import Blueprint, render_template

blueprint = Blueprint('blogposts', __name__)

@blueprint.route('/posts')
def posts():
    return render_template("posts.html", title="My Thoughts and Musings")

@blueprint.route('/posts/<int:post_id>')
def post(post_id):
    '''Returns post by id from "articles" dictionary and shows error page if the post does not exist'''
    post = articles.get(post_id)
    if post:
        return render_template("post.html", post=post)
    else:
        return render_template("error.html", title="Error")