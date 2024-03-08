# Задание №6
# Создать страницу, на которой будет форма для ввода имени
# и возраста пользователя и кнопка "Отправить"
# При нажатии на кнопку будет произведена проверка
# возраста и переход на страницу с результатом или на
# страницу с ошибкой в случае некорректного возраста.

from flask import Flask, render_template, request, redirect, url_for, abort
import logging

app = Flask(__name__)
logger = logging.getLogger(__name__)


@app.route("/<name>/")
def hello(name):
    return f"Hello, {name}"


@app.route("/", methods=["POST", "GET"])
def operation():
    if request.method == "POST":
        name = request.form.get("name")
        age = int(request.form.get("age"))
        if age >= 18:
            return redirect(url_for("hello", name=name))
        else:
            abort(404)
    return render_template("age.html")


@app.errorhandler(404)
def page_not_found(e):
    logger.warning(e)
    return render_template("404.html", title="Ошибка"), 404


if __name__ == "__main__":
    app.run(debug=True)
