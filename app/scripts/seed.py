from app.app import create_app
from app.blogposts.models import Article, Topic
from app.users.models import Author
from app.extensions.database import db
from datetime import datetime

if __name__ == '__main__':
    app = create_app()
    app.app_context().push()

users = [
    {'name': 'John Doe', 'email': 'john.doe@email.com', 'password': 'mockpassword1'},
    {'name': 'Jane Doe', 'email': 'jane.doe@email.com', 'password': 'mockpassword2'},
    {'name': 'Alan Doe', 'email': 'alan.doe@email.com', 'password': 'mockpassword3'},
    {'name': 'Adam Doe', 'email': 'adam.doe@email.com', 'password': 'mockpassword4'},
    {'name': 'Lily Doe', 'email': 'lily.doe@email.com', 'password': 'mockpassword5'}
]


# Add the content of the 'users' and the 'blog_post' lists to the Author table.
# Since the id columns have been set to autoincrement, it is not necessary to include them here.
for user in users:
    entries = Author(
        name = user['name'],
        email = user['email'],
        password = user['password']
    )

    db.session.add(entries)

db.session.commit()


blog_post = [
    {'title': 'First Blogpost', 'content': 'This is the first blogpost', 'author_id': 1, 'date': datetime.utcnow()},
    {'title': 'Second Blogpost', 'content': 'This is the second blogpost', 'author_id': 4, 'date': datetime.utcnow()},
    {'title': 'First Blogpost', 'content': 'This is the third blogpost', 'author_id': 2, 'date': datetime.utcnow()}
]


for post in blog_post:
    entry = Article(
        title = post['title'],
        content = post['content'],
        author_id = post['author_id'],
        date = post['date']
    )

    db.session.add(entry)

db.session.commit()