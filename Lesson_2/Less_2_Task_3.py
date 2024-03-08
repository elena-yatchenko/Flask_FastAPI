# Создать страницу, на которой будет форма для ввода логина и пароля, при нажатии на кнопку "Отправить"
# будет произведена проверка соответствия логина и пароля и переход на страницу приветствия пользователя или страницу с ошибкой.


from flask import Flask, request, render_template, url_for, abort, redirect
import logging

app = Flask(__name__)
logger = logging.getLogger(__name__)

LOGIN = "admin"
PASSWORD = "123"


@app.route("/<name>/")
def hello(name):
    return f"Hello, {name}"


@app.route("/", methods=["GET", "POST"])
def submit():
    if request.method == "POST":
        login = request.form.get("login")
        password = request.form.get("password")
        if login == LOGIN and password == PASSWORD:
            return redirect(url_for("hello", name=login))
        else:
            abort(404)
    return render_template("login.html")


@app.errorhandler(404)
def page_not_found(e):
    logger.warning(e)
    context = {"title": "Ошибка"}
    return render_template("404.html", **context), 404


if __name__ == "__main__":
    app.run(debug=True)
