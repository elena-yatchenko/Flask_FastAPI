# Задание №9
# Создать страницу, на которой будет форма для ввода имени и электронной почты
# При отправке которой будет создан cookie файл с данными пользователя
# Также будет произведено перенаправление на страницу приветствия, где будет отображаться имя пользователя.
# На странице приветствия должна быть кнопка "Выйти"
# При нажатии на кнопку будет удален cookie файл с данными пользователя и произведено перенаправление на страницу
# ввода имени и электронной почты.

from flask import Flask, request, make_response, redirect, url_for, render_template

app = Flask(__name__)


@app.route("/")
def index():
    return redirect(url_for("submit"))


# @app.route("/<name>/")
# def hello(name):
#     context = {"title": "Приветствие", "name": name}
#     response = make_response(render_template("hello_page.html", **context))
#     response.set_cookie("username", context["name"])
#     return f"Hello, {name}"


@app.route("/submit", methods=["GET", "POST"])
def submit():
    if request.method == "POST":
        name = request.form.get("name")
        email = request.form.get("email")
        context = {"title": "Приветствие", "name": name, "email": email}
        response = make_response(render_template("hello_page.html", **context))
        response.set_cookie("username", [context["name"], context["email"]])
        return response
    return render_template("get_name.html")


# @app.route("/")
# def index():
#     context = {"title": "Главная", "name": "Елена"}
#     response = make_response(render_template("main.html", **context))
#     response.headers["new_head"] = "New value"
#     response.set_cookie("username", context["name"])
#     return response


if __name__ == "__main__":
    app.run(debug=True)
