# Задание №2
# Создать базу данных для хранения информации о книгах в библиотеке.
# База данных должна содержать две таблицы: "Книги" и "Авторы".
# В таблице "Книги" должны быть следующие поля: id, название, год издания,
# количество экземпляров и id автора.
# В таблице "Авторы" должны быть следующие поля: id, имя и фамилия.
# Необходимо создать связь между таблицами "Книги" и "Авторы".
# Написать функцию-обработчик, которая будет выводить список всех книг с
# указанием их авторов.

from flask import Flask, redirect, render_template, url_for
from HW_model_2 import db, Author, Book
from random import randint, randrange

app = Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///db_books.db"
db.init_app(app)


# создание БД
@app.cli.command("init-db")
def init_db():
    db.create_all()
    print("OK")


# заполнение БД тестовыми данными
@app.cli.command("fill-db")
def fill_tables():
    for i in range(1, 6):
        new_author = Author(author_name=f"Author{i}", author_lastname=f"Last_name{i}")
        db.session.add(new_author)
    db.session.commit()
    print("Создана БД авторов")

    for i in range(1, 11):
        new_book = Book(
            name=f"Book{i}",
            public_year=randint(1990, 2020),
            count=randrange(0, 5000, 100),
            author_id=randint(1, 5),
        )
        db.session.add(new_book)
    db.session.commit()
    print("Создана БД книг")


# выведение данных на html страницу
@app.route("/")
def index():
    return redirect(url_for("show_books"))


@app.route("/books/")
def show_books():
    data = Book.query.all()
    # data = db.session.query(Book)
    context = {"books": data, "title": "Книги"}
    return render_template("books.html", **context)


if __name__ == "__main__":
    app.run(debug=True)
