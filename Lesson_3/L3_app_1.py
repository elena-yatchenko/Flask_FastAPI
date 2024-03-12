# Создать базу данных для хранения информации о студентах университета.
# База данных должна содержать две таблицы: "Студенты" и "Факультеты".
# В таблице "Студенты" должны быть следующие поля: id, имя, фамилия, возраст, пол, группа и id факультета.
# В таблице "Факультеты" должны быть следующие поля: id и название факультета.
# Необходимо создать связь между таблицами "Студенты" и "Факультеты".
# Написать функцию-обработчик, которая будет выводить список всех студентов с указанием их факультета.

from flask import Flask, redirect, render_template, url_for
from L3_model_1 import db, Student, Faculty, Gender
from random import choice

app = Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///database_1.db"
db.init_app(app)


# создание БД
@app.cli.command("init-db")
def init_db():
    db.create_all()
    print("OK")


# заполнение БД тестовыми данными
@app.cli.command("fill-db")
def fill_tables():
    faculties = ["math", "chemistry", "english", "art", "physics", "literature"]
    for faculty in faculties:
        new_faculty = Faculty(faculty_name=faculty)
        db.session.add(new_faculty)
    db.session.commit()
    print("Заполнены факультеты")

    for i in range(1, 7):
        new_student = Student(
            name=f"student{i}",
            last_name=f"last_name{i}",
            age=i + 16,
            gender=choice([Gender.male, Gender.female]),
            group=i,
            faculty_id=choice(range(1, 7)),
        )
        db.session.add(new_student)
    db.session.commit()
    print("Заполнены студенты")


# выведение данных на html страницу
@app.route("/")
def index():
    return redirect(url_for("show_students"))


@app.route("/students/")
def show_students():
    # data = Student.query.all()
    data = db.session.query(Student)
    context = {"students": data, "title": "Студенты"}
    print(data)
    return render_template("students.html", **context)


if __name__ == "__main__":
    app.run(debug=True)
