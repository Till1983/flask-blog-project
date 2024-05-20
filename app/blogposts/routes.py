from flask import Blueprint, render_template, request, redirect, url_for
from app.blogposts.models import Article, Topic
from flask_login import login_required, login_user, logout_user, current_user
from app.extensions.database import db, migrate


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
    if request.endpoint not in ['blogposts.posts', 'blogposts.view_post'] and not current_user.is_authenticated:
        return redirect(url_for('users.show_login_form'))


@blueprint.post('/create-post')
def post_create_post():
    title = request.form['title']
    content = request.form['blogpost']

    new_post = Article(author=current_user, title=title, content=content)
    db.session.add(new_post)
    db.session.commit()
    return redirect(url_for('blogposts.posts'))


@blueprint.route('/post/<int:post_id>')
def view_post(post_id):
    article = Article.query.get_or_404(post_id)
    return render_template('view-post.html', title=article.title, article=article)


@blueprint.route('/edit-post/<int:post_id>', methods=['GET', 'POST'])
@login_required
def edit_post(post_id):
    article = Article.query.get_or_404(post_id)
    if article.author != current_user:
        abort(403)
    if request.method == 'POST':
        article.title = request.form['title']
        article.content = request.form['content']
        db.session.commit()
        return redirect(url_for('blogposts.posts'))
    return render_template('edit-post.html', article=article)


@blueprint.route('/delete-post/<int:post_id>')
def delete_post(post_id):
    article = Article.query.get_or_404(post_id)
    if article.author != current_user:
        abort(403)
    db.session.delete(article)
    db.session.commit()
    return redirect(url_for('blogposts.posts'))


@blueprint.route('/run-seed-article')
def run_seed_article():
    if not Article.query.filter_by(title='First Blogpost').first():
        import app.scripts.seed
        return 'Article seed completed.'
    else:
        'No article to return.'