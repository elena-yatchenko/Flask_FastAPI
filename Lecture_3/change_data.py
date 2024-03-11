"""Работа с данными
После определения моделей в Flask-SQLAlchemy можно начать работу с данными в
базе данных. Давайте рассмотрим основные методы для создания, изменения и
удаления записей, а также получения данных из базы данных и их фильтрацию.
"""
# ➢Создание записей

"""Для создания новой записи в базе данных необходимо создать объект модели и
добавить его в сессию базы данных. После этого нужно вызвать метод commit() для
сохранения изменений.
"""
from flask import Flask
from Lecture_3.models import db, User, Post, Comment

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///mydatabase.db'
db.init_app(app)

@app.cli.command("add-john")
def add_user():
    user = User(username='john', email='john@example.com')
    db.session.add(user)
    db.session.commit()
    print('John add in DB!')

"""В этом примере создается новый объект модели User с именем пользователя "john"
и электронной почтой "john@example.com". Затем объект добавляется в сессию
базы данных и сохраняется с помощью метода commit().
Как вы уже догадались для выполнения функции необходимо выполнить в консоли
команду 

# flask add-john
"""
# ➢Изменение записей

"""Для изменения существующей записи нужно получить ее из базы данных, изменить
нужные поля и вызвать метод commit()"""

@app.cli.command("edit-john")
def edit_user():
    user = User.query.filter_by(username='john').first()
    user.email = 'new_email@example.com'
    db.session.commit()
    print('Edit John mail in DB!')

"""В этом примере получаем объект модели User по имени пользователя "john",
изменяем его электронную почту на "new_email@example.com" и сохраняем
изменения с помощью метода commit().
"""

"""🔥 Внимание! Если бы база данных позволяла хранить несколько
пользователей с одинаковыми username, в переменную user попал бы один
пользователь благодаря методу first().
"""

# ➢Удаление записей
"""Для удаления записи нужно получить ее из базы данных, вызвать метод delete() и
затем вызвать метод commit().
"""

@app.cli.command("del-john")
def del_user():
    user = User.query.filter_by(username='john').first()
    db.session.delete(user)
    db.session.commit()
    print('Delete John from DB!')