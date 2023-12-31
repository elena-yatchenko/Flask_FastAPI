# Написать функцию, которая будет выводить на экран HTML страницу с таблицей, содержащей информацию о студентах.
# Таблица должна содержать следующие поля: "Имя", "Фамилия", "Возраст", "Средний балл".
# Данные о студентах должны быть переданы в шаблон через контекст.
#
# people = [
#         {'Имя': 'Иван', 'Фамилия': 'Иванов', 'Возраст': 20,
#          'Средний бал': 4.5},
#         {'Имя': 'Петр', 'Фамилия': 'Петров', 'Возраст': 21,
#          'Средний бал': 4.2},
#         {'Имя': 'Сергей', 'Фамилия': 'Сергеев', 'Возраст': 19,
#          'Средний бал': 4.8},
#         {'Имя': 'Анна', 'Фамилия': 'Иванова', 'Возраст': 20,
#          'Средний бал': 4.7}
#     ]
from flask import Flask
from flask import render_template

app = Flask(__name__)


@app.route("/users/")
def user_table():
    people = [
        {"Имя": "Иван", "Фамилия": "Иванов", "Возраст": 20, "Средний бал": 4.5},
        {"Имя": "Петр", "Фамилия": "Петров", "Возраст": 21, "Средний бал": 4.2},
        {"Имя": "Сергей", "Фамилия": "Сергеев", "Возраст": 19, "Средний бал": 4.8},
        {"Имя": "Анна", "Фамилия": "Иванова", "Возраст": 20, "Средний бал": 4.7},
    ]
    """ точечная нотация тут не подходит, т.к. на русском языке ключи. 
    Передаем наш список словарей как ключевой (именованный) аргумент в render"""

    return render_template("users.html", students=people)


if __name__ == "__main__":
    app.run()

# http://127.0.0.1:5000/users/
# Имя	Фамилия	Возраст	Средний бал
# Иван	Иванов	20	4.5
# Петр	Петров	21	4.2
# Сергей	Сергеев	19	4.8
# Анна	Иванова	20	4.7
