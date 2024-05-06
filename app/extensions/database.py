from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

db = SQLAlchemy()
migrate = Migrate()

class CRUDMixin():
    # Taken from https://codecookies.xyz/flask-tutorial/v1/crud#update
    def save(self):
        db.session.add(self)
        db.session.commit()
        return self
