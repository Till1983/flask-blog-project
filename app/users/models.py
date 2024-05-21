from app.extensions.database import db, CRUDMixin
from flask_login import UserMixin

class Author(db.Model, CRUDMixin, UserMixin):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(255))
    email = db.Column(db.String(255), unique=True)
    password = db.Column(db.String(255), unique=True)
    articles = db.relationship('Article', backref='author', lazy=True)