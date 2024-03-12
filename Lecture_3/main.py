from flask import Flask
from Lecture_3.models import db, User, Post, Comment

app = Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///mydatabase.db"
db.init_app(app)

"""➢Создание таблиц в базе данных

Остался финальный этап. Напишим функцию, которая создаст таблицы через
консольную команду. Заполняем основной файл проекта"""


@app.cli.command("init-db")
def init_db():
    db.create_all()
    print("OK")  # просто чтоб понять, что функция отработала


"""Из models импортировали все созданные классы таблиц. Без этого импорта
функция create_all может не увидеть какие таблицы необходимо создать (Т.е. явно 
в коде мы эти классы не используем, но использует функция для создания базы данных).
Далее создали функцию, которая будет вызвана командой в консоли:

# flask init-db

"""
"""🔥 Внимание! Если команда в консоли выдает ошибку, проверьте что у вас
есть wsgi.py файл в корневой директории проекта и он верно работает.

Например его код может быть таким:

from flask_lesson_3.app_01 import app

if __name__ == '__main__':
app.run(debug=True)
"""

"""Мы рассмотрели основные аспекты создания моделей в Flask-SQLAlchemy. Были
описаны классы моделей, поля моделей и создание связей между моделями.
"""
