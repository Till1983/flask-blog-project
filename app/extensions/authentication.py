from flask_login import LoginManager
from app.users.models import Author

login_manager = LoginManager()

@login_manager.user_loader
def load_user(id):
  return Author.query.get(id)