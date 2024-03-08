# Создать страницу, на которой будет кнопка "Нажми меня", при нажатии на которую будет переход на другую страницу
# с приветствием пользователя по имени.

from flask import Flask, render_template, request, url_for, redirect

app = Flask(__name__)


@app.route("/<name>/")
def hello(name):
    return f"Hello, {name}!"


@app.route("/", methods=["GET", "POST"])
def get_name():
    if request.method == "POST":
        name = request.form.get("name")
        return redirect(url_for("hello", name=name))
    return render_template("get_name.html")


if __name__ == "__main__":
    app.run(debug=True)
