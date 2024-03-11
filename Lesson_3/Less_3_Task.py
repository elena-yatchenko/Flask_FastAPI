"""
https://sqlitebrowser.org/dl/
"""

# Создать базу данных для хранения информации о студентах университета.
# База данных должна содержать две таблицы: "Студенты" и "Факультеты".
# В таблице "Студенты" должны быть следующие поля: id, имя, фамилия, возраст, пол, группа и id факультета.
# В таблице "Факультеты" должны быть следующие поля: id и название факультета.
# Необходимо создать связь между таблицами "Студенты" и "Факультеты".
# Написать функцию-обработчик, которая будет выводить список всех студентов с указанием их факультета.


from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
import enum


db = SQLAlchemy()


class Gender(enum.Enum):
    male = "мужской"
    female = "женский"


class Student(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)
    surname = db.Column(db.String(120), nullable=False)
    age = db.Column(db.Integer, nullable=False)
    gender = db.Column(db.Enum(Gender), nullable=False)
    email = db.Column(db.String(120), nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    posts = db.relationship("Post", backref="author", lazy=True)

    def __repr__(self):
        return f"User({self.username}, {self.email})"


class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(80), nullable=False)
    content = db.Column(db.Text, nullable=False)
    author_id = db.Column(db.Integer, db.ForeignKey("user.id"), nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self):
        return f"Post({self.title}, {self.content})"


from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
import enum

db = SQLAlchemy()


class Gender(enum.Enum):
    male = "муж"
    female = "жен"


class Fags(db.Model):
    id_ = db.Column(db.Integer, primary_key=True)
    fag_name = db.Column(db.String(80), nullable=False)
    student = db.relationship("Student", backref=db.backref("fax"), lazy=True)

    def __repr__(self):
        return f"Fags({self.fag_name})"


class Students(db.Model):
    id_ = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)
    last_name = db.Column(db.String(120), nullable=False)
    age = db.Column(db.Integer, nullable=False)
    gender = db.Column(db.Enum(Gender), nullable=False)
    group = db.Column(db.Integer, nullable=False)
    fags_id = db.Column(db.Integer, db.ForeignKey("fax.id_"), nullable=False)

    def __repr__(self):
        return f"Student({self.name}, {self.last_name})"


from flask import Flask, render_template
from models import db, Students, Fags, Gender
from random import choice, randint


app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///app_01.db"
db.init_app(app)


@app.cli.command("init-db")
def init_db():
    db.create_all()
    print("OK")


@app.cli.command("add-user")
def add_user():
    for _ in range(1, 11):
        fag = Fags(fag_name=choice(["math", "hist", "lang"]))
        db.session.add(fag)
    db.session.commit()

    for i in range(1, 11):
        student = Students(
            name=f"name{i}",
            last_name=f"last_name{i}",
            age=i + 15,
            gender=choice([Gender.male, Gender.female]),
            group=choice([1, 2, 3]),
            fags_id=randint(1, 10),
        )
        db.session.add(student)
    db.session.commit()


from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
import enum

db = SQLAlchemy()


class Gender(enum.Enum):
    male = "муж"
    female = "жен"


class Fags(db.Model):
    id_ = db.Column(db.Integer, primary_key=True)
    fag_name = db.Column(db.String(80), nullable=False)
    student = db.relationship("Students", backref=db.backref("fags"), lazy=True)

    def __repr__(self):
        return f"Fags({self.fag_name})"


class Students(db.Model):
    id_ = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)
    last_name = db.Column(db.String(120), nullable=False)
    age = db.Column(db.Integer, nullable=False)
    gender = db.Column(db.Enum(Gender), nullable=False)
    group = db.Column(db.Integer, nullable=False)
    fags_id = db.Column(db.Integer, db.ForeignKey("fags.id_"), nullable=False)

    def __repr__(self):
        return f"Student({self.name}, {self.last_name})"


# students = db.session.query(Student)

<div class="row">
        {% for st in student %}
        <p>Имя : {{ st.name }}<br>
        Фамилия: {{ st.last_name }}<br>
        Возраст: {{st.age}}<br>
        Пол: {{st.gender}}<br>
        Группа: {{st.group}}<br>
        Id факультета: {{st.fags_id}}<br>
        </p>
        {% endfor %}
    </div>
    
    
    
    <div class="row">
        {% for st in student %}
        <p>Имя : {{ st.name }}<br>
        Фамилия: {{ st.last_name }}<br>
        Возраст: {{st.age}}<br>
        Пол: {{st.gender}}<br>
        Группа: {{st.group}}<br>
        Id факультета: {{st.fags.fag_name}}<br>
        </p>
        {% endfor %}
    </div>