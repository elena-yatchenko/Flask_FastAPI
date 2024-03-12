# Задание №3
# Доработаем задача про студентов
# Создать базу данных для хранения информации о студентах и их оценках в
# учебном заведении.
# База данных должна содержать две таблицы: "Студенты" и "Оценки".
# В таблице "Студенты" должны быть следующие поля: id, имя, фамилия, группа
# и email.
# В таблице "Оценки" должны быть следующие поля: id, id студента, название
# предмета и оценка.
# Необходимо создать связь между таблицами "Студенты" и "Оценки".
# Написать функцию-обработчик, которая будет выводить список всех
# студентов с указанием их оценок.

from flask import Flask, redirect, render_template, url_for
from HW_model_3 import db, Student, Grade
from random import randint, sample

app = Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///db_grades.db"
db.init_app(app)


# создание БД
@app.cli.command("init-db")
def init_db():
    db.create_all()
    print("OK")


# заполнение БД тестовыми данными
@app.cli.command("fill-db")
def fill_tables():
    for i in range(1, 7):
        new_student = Student(
            name=f"student{i}",
            last_name=f"last_name{i}",
            group=randint(1, 5),
            email=f"email{i}@fr.az",
        )
        db.session.add(new_student)
    db.session.commit()
    print("Создана БД студентов")

    subjects = ["math", "chemistry", "english", "art", "physics", "literature"]

    for i in range(1, 7):
        subject = sample(subjects, 3)
        for j in range(3):
            new_grade = Grade(student_id=i, subject=subject[j], mark=randint(3, 6))
            db.session.add(new_grade)
    db.session.commit()
    print("Создана БД оценок")

    # for i in range(1, 21):
    #     new_grade = Grade(
    #         mark=randint(3, 6),
    #         subject=choice(subjects),
    #         student_id=randint(1, 7),
    #     )


# выведение данных на html страницу
@app.route("/")
def index():
    return redirect(url_for("show_data"))


@app.route("/books/")
def show_data():
    grades = Grade.query.all()
    students = Student.query.all()
    print(students)
    print(grades)
    context = {"grades": grades, "students": students, "title": "Данные студентов"}
    return render_template("data.html", **context)


if __name__ == "__main__":
    app.run(debug=True)
