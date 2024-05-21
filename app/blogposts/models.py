from app.extensions.database import db
from datetime import datetime

class Article(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    title = db.Column(db.String(255))
    content = db.Column(db.String(100000))
    author_id = db.Column(db.Integer, db.ForeignKey('author.id', name='article_author'))
    date = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)