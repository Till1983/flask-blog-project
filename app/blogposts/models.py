from app.extensions.database import db
from datetime import datetime

class Article(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.String)
    topic_id = db.Column(db.Integer, db.ForeignKey('topic.id'))
    author_id = db.Column(db.Integer, db.ForeignKey('author.id'))
    date = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    topics = db.relationship('Topic', backref='author', lazy=True)

class Topic(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80))
    article_id = db.Column(db.Integer, db.ForeignKey('article.id'))