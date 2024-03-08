# Задание №5
# Создать страницу, на которой будет форма для ввода двух
# чисел и выбор операции (сложение, вычитание, умножение
# или деление) и кнопка "Вычислить"
# При нажатии на кнопку будет произведено вычисление
# результата выбранной операции и переход на страницу с
# результатом.

from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)


@app.route("/<int:result>")
def show_result(result):
    return f"Результат вычисления равен {result}"


@app.route("/", methods=["POST", "GET"])
def operation():
    if request.method == "POST":
        num1 = int(request.form.get("num1"))
        num2 = int(request.form.get("num2"))
        oper = request.form.get("operation")
        if oper == "sum":
            result = num1 + num2
        elif oper == "dif":
            result = num1 - num2
        elif oper == "div":
            result = num1 / num2
        elif oper == "mult":
            result = num1 * num2
        return redirect(url_for("show_result", result=result))

    return render_template("math.html")


if __name__ == "__main__":
    app.run(debug=True)
