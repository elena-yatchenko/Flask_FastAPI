# Задание №8
# Создать страницу, на которой будет форма для ввода имени и кнопка "Отправить"
# При нажатии на кнопку будет произведено перенаправление на страницу
# с flash сообщением, где будет выведено "Привет, {имя}!".

from flask import Flask, flash, redirect, render_template, request, url_for

app = Flask(__name__)
app.secret_key = "078364629db24c89dc3813891c9f5e9e515ab18ca6985729c972c265b06ff33a"


@app.route("/")
def index():
    return redirect(url_for("form"))


@app.route("/form", methods=["GET", "POST"])
def form():
    if request.method == "POST":
        name = request.form.get("name")
        # Проверка данных формы
        if not name.isalpha():
            flash("В имени должны быть только буквы", "danger")
            return redirect(url_for("form"))
        # Обработка данных формы
        flash(f"Привет, {name}!", "success")
        return redirect(url_for("form"))
    return render_template("form.html")


if __name__ == "__main__":
    app.run(debug=True)
    # app.run()
