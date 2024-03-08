# Задание №4
# Создать страницу, на которой будет форма для ввода текста и
# кнопка "Отправить"
# При нажатии кнопки будет произведен подсчет количества слов
# в тексте и переход на страницу с результатом.

from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)


@app.route("/<int:result>")
def show_result(result):
    return f"Строка содержит {result} слов"


@app.route("/", methods=["POST", "GET"])
def count():
    if request.method == "POST":
        data = request.form.get("data").split()
        count = len(data)
        return redirect(url_for("show_result", result=count))
    return render_template("text.html")


if __name__ == "__main__":
    app.run(debug=True)
