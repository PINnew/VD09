from app import db
from app import login_manager
from flask_login import UserMixin
from sqlalchemy import Column, Integer, String


# Создаём класс и колонки базы данных
class User(db.Model, UserMixin):
    id = Column(Integer, primary_key=True)
    username = Column(String(100), unique=True, nullable=False)
    password = Column(String(200), nullable=False)
    clicks = Column(Integer, default=0)

    def __repr__(self):
        return f'User {self.username} - clicks: {self.clicks}'

# Создаём декоратор и функцию
@login_manager.user_loader # Этот декоратор связывает функцию с flask_login, чтобы загружать пользователя по id
def load_user(user_id):
    return User.query.get(int(user_id))
