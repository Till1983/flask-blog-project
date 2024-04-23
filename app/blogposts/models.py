from app.extensions.database import db
from datetime import datetime

class Article(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    title = db.Column(db.String(50))
    content = db.Column(db.String(10000))
    topic_id = db.Column(db.Integer, db.ForeignKey('topic.id', name='article_topic'))
    author_id = db.Column(db.Integer, db.ForeignKey('author.id', name='article_author'))
    date = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    topics = db.relationship('Topic', secondary='article_topic', backref='articles', lazy=True)

class Topic(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(80))

# Define association table for the many-to-many relationship between Article and Topic
article_topic = db.Table('article_topic',
    db.Column('article_id', db.Integer, db.ForeignKey('article.id'), primary_key=True),
    db.Column('topic_id', db.Integer, db.ForeignKey('topic.id'), primary_key=True)
)