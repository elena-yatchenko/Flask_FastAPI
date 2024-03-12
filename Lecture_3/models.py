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
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    # строка posts см. ниже.
    # posts = db.relationship('Post', backref='author', lazy=True)
    # лучше использовать вариант backref=db.backref('author')
    """lazy=True - не сразу все данные таблицы подтягиваются, экономит память"""
    posts = db.relationship("Post", backref=db.backref("author"), lazy=True)

    # по функции repr смотреть инфо чуть ниже
    def __repr__(self):
        return f"User({self.username}, {self.email})"


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

# Использование типа данных Enum (посм. доп.инфо):

"""
Модуль enum в Python. Это стандартный модуль, который предоставляет инструменты для создания перечислений в Python. 
С его помощью можно легко определить классы перечислений и работать с ними.
Проще говоря, перечисления – это концепция или тип данных, а модуль enum – это конкретный 
инструмент в Python для работы с этим типом данных.

Создание перечислений в Python
Для создания перечисления в Python, необходимо определить класс, наследующий enum.Enum. 
Элементы этого класса определяются как атрибуты класса, и каждому из них присваивается уникальное значение. 

Вот пример создания перечисления:

#  enum_create.py
import enum

class BugStatus(enum.Enum):

    new = 7
    incomplete = 6
    invalid = 5
    wont_fix = 4
    in_progress = 3
    fix_committed = 2
    fix_released = 1

print('\nMember name: {}'.format(BugStatus.wont_fix.name)) 
print('Member value: {}'.format(BugStatus.wont_fix.value))
При запуске этого кода вы увидите следующее:

$ python3 enum_create.py

Member name: wont_fix
Member value: 4
Каждый атрибут в Enum автоматически становится экземпляром перечисления при определении класса. 
Эти экземпляры имеют два основных атрибута:

name, который содержит имя элемента;
value, который содержит его значение.
Нужно учитывать, что значения элементов перечисления могут быть любого типа, будь то целые числа, 
строки или даже кортежи. Если не требуется конкретное значение для элемента, 
можно использовать помощник auto(), который автоматически присвоит следующее доступное значение.
"""
"""
См. Пример из Lesson_3, task_1
import enum

class Gender(enum.Enum):
    male = "муж"
    female = "жен"
    
gender = db.Column(db.Enum(Gender), nullable=False)

Пример обращения к типу данных Enum для заполнения таблиц и т.п.

gender=choice([Gender.male, Gender.female]) - в ячейках таблицы будет male/female

Выведение значения атрибута (напр., на стр. html)

Пол: {{ st.gender.value }}<br>
"""
# Рассмотрим ещё один пример таблицы:


# 'id' - по идее зарезервированное слово, лучше не использовать. Можно 'id_', например
class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(80), nullable=False)
    content = db.Column(db.Text, nullable=False)
    author_id = db.Column(db.Integer, db.ForeignKey("user.id"), nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self):
        return f"Post({self.title}, {self.content})"


"""В этом примере определена модель Post, которая имеет пять полей: id, title, content,
author_id и created_at. Поля title и content являются строками и обязательны для
заполнения. Поле author_id является внешним ключом к таблице пользователей
(User) и ссылается на поле id этой таблицы. Поле created_at содержит дату и время
создания записи и автоматически заполняется текущей датой и временем при
добавлении записи.
"""
# К модели пользователя добавим следующую строку:
# posts = db.relationship('Post', backref='author', lazy=True)
"""Так мы (а точнее наш код) понимаем какие посты принадлежат конкретному
пользователю. 

!!!! Как работает перекрестная ссылка, смотреть подробнее в задаче 1 Lesson 3 
(Факультет: {{ st.fac_reference.faculty_name}})
Например, получаем данные статьи: post.title, post.content, post.author_id и т.п. (через точечную нотацию, обращаясь 
к свойствам экземпляра своего же классаб т.е. той же таблицы БД). 
Но если хотим  получить email автора статьи (это уже даныне другой таблицы, связанной. То обратимся через обратную 
ссылку backref, т.е. post.author.email)
"""
"""➢Создание связей между моделями

Для создания связей между моделями используется поле ForeignKey. Оно указывает
на поле первичного ключа связанной таблицы.
"""


class Comment(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.Text, nullable=False)
    post_id = db.Column(db.Integer, db.ForeignKey("post.id"), nullable=False)
    author_id = db.Column(db.Integer, db.ForeignKey("user.id"), nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self):
        return f"Comment({self.content})"


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

"""!!! __repr__()
Функция repr() вернет строку, содержащую печатаемое формальное представление объекта.

Для многих типов функция возвращает строку, которая при передаче в eval() может произвести объект с тем же значением, что и исходный. В других случаях представление является строкой, обрамлённой угловыми скобками (< и >), содержащей название типа и некую дополнительную информацию, часто название объекта и его адрес в памяти.

Чтобы определить значение, возвращаемое функцией для пользовательского типа следует реализовать для этого типа специализированный метод __repr__.

Примеры получения описания объекта.
class Person:
    name = 'Mike'

x = Person()
print(repr(x))
# <__main__.Person object at 0x7f0c483edbe0>


# Определим метод __repr__
class Person:
    name = 'Mike'

    def __repr__(self):
        return repr(self.name)


x = Person()
print(repr(x))
# 'Mike'
"""
