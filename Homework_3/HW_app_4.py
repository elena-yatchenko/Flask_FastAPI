# Задание №4
# Создайте форму регистрации пользователя с использованием Flask-WTF. Форма должна
# содержать следующие поля:
# ○ Имя пользователя (обязательное поле)
# ○ Электронная почта (обязательное поле, с валидацией на корректность ввода email)
# ○ Пароль (обязательное поле, с валидацией на минимальную длину пароля)
# ○ Подтверждение пароля (обязательное поле, с валидацией на совпадение с паролем)
# После отправки формы данные должны сохраняться в базе данных (можно использовать SQLite)
# и выводиться сообщение об успешной регистрации. Если какое-то из обязательных полей не
# заполнено или данные не прошли валидацию, то должно выводиться соответствующее
# сообщение об ошибке.
# Дополнительно: добавьте проверку на уникальность имени пользователя и электронной почты в
# базе данных. Если такой пользователь уже зарегистрирован, то должно выводиться сообщение
# об ошибке.

from HW_form_4 import RegistrationForm
from flask import Flask, render_template, request, url_for, redirect, flash
from flask_wtf.csrf import CSRFProtect
from HW_model_4 import db, User

app = Flask(__name__)
app.config['SECRET_KEY'] = '03a6b22f466622563d9293c8a83683ff5d4bc32567bc6f0a5d94bda651f7a88b'
csrf = CSRFProtect(app)

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///db_users.db"
db.init_app(app)

@app.cli.command("init-db")
def init_db():
    db.create_all()
    print("OK")

@app.route('/')
def index():
    return redirect(url_for('register'))


@app.route('/register/', methods=['POST', 'GET'])
def register():
    form = RegistrationForm()
    if request.method == 'POST':
        if form.validate():
            # Обработка данных из формы
            login = form.username.data
            email = form.email.data
            password = form.password.data
            # print(login, email, password)
            """Вопрос преподавателю: подскажите, может есть более оптимальный вариант эти проверки делать, чем тот, 
            что я придумала?"""
            users = [user.username for user in User.query.filter_by(username = login).all()]
            emails = [user.email for user in User.query.filter_by(email = email).all()]
            new_user = User(
            username=login,
            email=email,
            password=password
            )
            if new_user.username in users:
                flash(f"Ошибка регистрации. Пользователь с логином {login} уже существует", "danger")
            elif new_user.email in emails:
                flash(f"Ошибка регистрации. Пользователь с электронным адресом {email} уже существует", "danger")
            else:
                db.session.add(new_user)
                db.session.commit()
                flash("Поздравляем! Регистрация прошла успешно!", "success")
        else:
            flash("Ошибка регистрации. Данные заполнены некорректно", "danger")

    return render_template('register.html', form=form)


if __name__ == "__main__":
    app.run(debug=True)
