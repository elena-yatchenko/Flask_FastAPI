from flask_sqlalchemy import SQLAlchemy
db = SQLAlchemy()

"""Создание моделей
При работе с Flask-SQLAlchemy необходимо определить модели данных, которые
будут использоваться в приложении. Модель - это класс, который описывает
структуру таблицы в базе данных.

➢Определение классов моделей

Для определения модели необходимо создать класс, который наследует от класса
Model из библиотеки SQLAlchemy. Название класса должно соответствовать
названию таблицы в базе данных.
Наполняем кодом models.py
"""
# Пример:

from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

db = SQLAlchemy()

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True,
    nullable=False)
    email = db.Column(db.String(120), unique=True,
    nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    # строка posts см. ниже
    posts = db.relationship('Post', backref='author', lazy=True)

    def __repr__(self):
        return f'User({self.username}, {self.email})'
    
"""В этом примере определена модель User, которая имеет четыре поля: id, username,
email и created_at. Поле id является первичным ключом таблицы и автоматически
генерируется при добавлении записи в таблицу. Поля username и email являются
строками с ограничением на уникальность и обязательность заполнения. Поле
created_at содержит дату и время создания записи и автоматически заполняется
текущей датой и временем при добавлении записи."""

"""➢Описание полей моделей

Для описания полей модели используются классы-типы данных из библиотеки
SQLAlchemy. Существуют следующие типы данных:

● Integer — целое число
● String — строка
● Text — текстовое поле
● Boolean — булево значение
● DateTime — дата и время
● Float — число с плавающей точкой
● Decimal — десятичное число
● Enum — перечисление значений
● ForeignKey — внешний ключ к другой таблице"""

# Рассмотрим ещё один пример таблицы:

class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(80), nullable=False)
    content = db.Column(db.Text, nullable=False)
    author_id = db.Column(db.Integer, db.ForeignKey('user.id'),
    nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self):
        return f'Post({self.title}, {self.content})'
    
"""В этом примере определена модель Post, которая имеет пять полей: id, title, content,
author_id и created_at. Поля title и content являются строками и обязательны для
заполнения. Поле author_id является внешним ключом к таблице пользователей
(User) и ссылается на поле id этой таблицы. Поле created_at содержит дату и время
создания записи и автоматически заполняется текущей датой и временем при
добавлении записи.
"""
# К моделе пользователя добавим следующую строку:
# posts = db.relationship('Post', backref='author', lazy=True)
"""Так мы (а точнее наш код) понимаем какие посты принадлежат конкретному
пользователю.
"""
"""➢Создание связей между моделями

Для создания связей между моделями используется поле ForeignKey. Оно указывает
на поле первичного ключа связанной таблицы.
"""
class Comment(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.Text, nullable=False)
    post_id = db.Column(db.Integer, db.ForeignKey('post.id'),
    nullable=False)
    author_id = db.Column(db.Integer, db.ForeignKey('user.id'),
    nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self):
        return f'Comment({self.content})'

"""В этом примере определена модель Comment, которая имеет пять полей: id, content,
post_id, author_id и created_at. Поля content и post_id являются обязательными для
заполнения. Поле post_id является внешним ключом к таблице постов (Post) и
ссылается на поле id этой таблицы. Поле author_id является внешним ключом к
таблице пользователей (User) и ссылается на поле id этой таблицы. Поле created_at
содержит дату и время создания записи и автоматически заполняется текущей
датой и временем при добавлении записи.
"""
"""➢Создание таблиц в базе данных

Остался финальный этап. Напишим функцию, которая создаст таблицы через
консольную команду. Заполняем основной файл проекта (см. файл main.ru)"""