# Создать страницу, на которой будет форма для ввода числа
# и кнопка "Отправить"
# При нажатии на кнопку будет произведено
# перенаправление на страницу с результатом, где будет
# выведено введенное число и его квадрат.

from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)


@app.route("/<int:number>")
def show_result(number):
    result = number**2
    return f"Квадрат числа {number} равен {result}"


@app.route("/", methods=["POST", "GET"])
def square():
    if request.method == "POST":
        num = int(request.form.get("number"))
        return redirect(url_for("show_result", number=num))

    return render_template("square.html")


if __name__ == "__main__":
    app.run(debug=True)
