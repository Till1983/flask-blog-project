from flask import Flask, redirect, url_for, render_template

app = Flask(__name__)
app.config.from_object('app.config')

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

@app.route('/posts')
def posts():
    return render_template("posts.html", title="My Thoughts and Musings")

@app.route('/posts/<int:post_id>')
def post(post_id):
    '''Returns post by id from "articles" dictionary and shows error page if the post does not exist'''
    post = articles.get(post_id)
    if post:
        return render_template("post.html", post=post)
    else:
        return render_template("error.html", title="Error")


