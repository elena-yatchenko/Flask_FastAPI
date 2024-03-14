# Задание №7
# Создайте форму регистрации пользователей в приложении Flask. Форма должна
# содержать поля: имя, фамилия, email, пароль и подтверждение пароля. При отправке
# формы данные должны валидироваться на следующие условия:
# ○ Все поля обязательны для заполнения.
# ○ Поле email должно быть валидным email адресом.
# ○ Поле пароль должно содержать не менее 8 символов, включая хотя бы одну букву и
# одну цифру.
# ○ Поле подтверждения пароля должно совпадать с полем пароля.
# ○ Если данные формы не прошли валидацию, на странице должна быть выведена
# соответствующая ошибка.
# ○ Если данные формы прошли валидацию, на странице должно быть выведено
# сообщение об успешной регистрации.

from HW_form_7 import RegistrationForm
from flask import Flask, render_template, request, url_for, redirect, flash
from flask_wtf.csrf import CSRFProtect
from datetime import datetime, timedelta, date

app = Flask(__name__)
app.config["SECRET_KEY"] = (
    "03a6b22f466622563d9293c8a83683ff5d4bc32567bc6f0a5d94bda651f7a88b"
)
csrf = CSRFProtect(app)


@app.route("/")
def index():
    return redirect(url_for("register"))


# @app.route("/hello/<name>/")
# def hello(name):
#     return f"Hello, {name}!"


@app.route("/register/", methods=["POST", "GET"])
def register():
    form = RegistrationForm()
    if request.method == "POST":
        if form.validate():
            password = form.password.data  
            if any([symb.isalpha() for symb in password]) and any([symb.isdigit() for symb in password]):
                flash("Поздравляем! Регистрация прошла успешно!", "success")
            else:
                flash("Пароль должен содержать хотя бы одну букву и одну цифру", "danger")
        else:
            flash("Ошибка регистрации. Данные заполнены некорректно", "danger")

    return render_template("register.html", form=form)


if __name__ == "__main__":
    app.run(debug=True)