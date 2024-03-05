# Создать базовый шаблон для всего сайта, содержащий общие элементы дизайна (шапка, меню, подвал), и дочерние шаблоны для каждой отдельной страницы.
# Например, создать страницу "О нас" и "Контакты", используя базовый шаблон.

from flask import Flask
from flask import render_template

app = Flask(__name__)


@app.route("/")
def base():
    return render_template("base1.html")


@app.route("/about/")
def about():
    context = {"title": "Главная", "content": "Здесь будет добавлена информация о нас"}
    return render_template("about.html", **context)


@app.route("/contacts/")
def contacts():
    cont = ["г. Баку", "+99455-505-66-66", "e-mail"]
    context = {"title": "Наши контакты", "content": cont}
    return render_template("contacts.html", **context)


if __name__ == "__main__":
    app.run()
