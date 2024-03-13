# Задание №5
# Создать форму регистрации для пользователя.
# Форма должна содержать поля: имя, электронная почта,
# пароль (с подтверждением), дата рождения, согласие на
# обработку персональных данных.
# Валидация должна проверять, что все поля заполнены
# корректно (например, дата рождения должна быть в
# формате дд.мм.гггг).
# При успешной регистрации пользователь должен быть
# перенаправлен на страницу подтверждения регистрации.

from HW_form_5 import RegistrationForm
from flask import Flask, render_template, request, url_for, redirect, flash
from flask_wtf.csrf import CSRFProtect


app = Flask(__name__)
app.config["SECRET_KEY"] = (
    "03a6b22f466622563d9293c8a83683ff5d4bc32567bc6f0a5d94bda651f7a88b"
)
csrf = CSRFProtect(app)


@app.route("/")
def index():
    return redirect(url_for("register"))


@app.route("/hello/<name>/")
def hello(name):
    return f"Hello, {name}!"


@app.route("/register/", methods=["POST", "GET"])
def register():
    form = RegistrationForm()
    if request.method == "POST":
        # birthday = form.birthday.data
        # print(birthday)
        if form.validate():
            name = form.name.data
            flash("Поздравляем! Регистрация прошла успешно!", "success")
            return redirect(url_for("hello", name=name))

        else:
            flash("Ошибка регистрации. Данные заполнены некорректно", "danger")

    return render_template("register.html", form=form)


if __name__ == "__main__":
    app.run(debug=True)
