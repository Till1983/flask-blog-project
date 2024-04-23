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
    {'name': 'Adam Doe', 'email': 'adam.doe@email.com', 'password': 'mockpassword4'}
]

# Add the content of the 'users' list to the Author table.
# Since the id column has been set to autoincrement, it is not necessary to include it here.
for user in users:
    entries = Author(
        name = user['name'],
        email = user['email'],
        password = user['password']
    )

    db.session.add(entries)

db.session.commit()