# Задание №8
# Создать форму для регистрации пользователей на сайте.
# Форма должна содержать поля "Имя", "Фамилия", "Email",
# "Пароль" и кнопку "Зарегистрироваться".
# При отправке формы данные должны сохраняться в базе
# данных, а пароль должен быть зашифрован.

from HW_form_8 import RegistrationForm
from flask import Flask, render_template, request, url_for, redirect, flash
from flask_wtf.csrf import CSRFProtect
from HW_model_8 import db, User

app = Flask(__name__)
app.config['SECRET_KEY'] = '03a6b22f466622563d9293c8a83683ff5d4bc32567bc6f0a5d94bda651f7a88b'
csrf = CSRFProtect(app)

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///db_users_8.db"
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
            name = form.name.data
            surname = form.surname.data
            email = form.email.data
            password = form.password.data

            new_user = User(
            name=name,
            surname=surname,
            email=email,
            password=password
            )
           
            db.session.add(new_user)
            db.session.commit()
            flash("Поздравляем! Регистрация прошла успешно!", "success")
        else:
            flash("Ошибка регистрации. Данные заполнены некорректно", "danger")

    return render_template('register.html', form=form)


if __name__ == "__main__":
    app.run(debug=True)
