from app.extensions.database import db

class Author(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80))
    email = db.Column(db.String(80), unique=True)
    password = db.Column(db.String(80), unique=True)
    #article_id = db.Column(db.Integer, db.ForeignKey('article.id'))
    articles = db.relationship('Author', backref='article', lazy=True)