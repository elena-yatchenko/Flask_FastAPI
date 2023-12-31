# Написать функцию, которая будет выводить на экран HTML страницу с таблицей, содержащей информацию о студентах.
# Таблица должна содержать следующие поля: "Имя", "Фамилия", "Возраст", "Средний балл".
# Данные о студентах должны быть переданы в шаблон через контекст.

# !!! Другие варианты заполнения таблицы HTML
# 1- через PANDAS (таблица выходит с рамками)

from flask import Flask
from flask import render_template
import pandas as pd

# pip install pandas

app = Flask(__name__)


@app.route("/students/")
def fill_table():
    people = [
        {"Имя": "Иван", "Фамилия": "Иванов", "Возраст": 20, "Средний бал": 4.5},
        {"Имя": "Петр", "Фамилия": "Петров", "Возраст": 21, "Средний бал": 4.2},
        {"Имя": "Сергей", "Фамилия": "Сергеев", "Возраст": 19, "Средний бал": 4.8},
        {"Имя": "Анна", "Фамилия": "Иванова", "Возраст": 20, "Средний бал": 4.7},
    ]
    """DataFrame принимает СПИСОК СЛОВАРЕЙ в качестве аргумента, преобразовывая его в html-таблицу"""
    html_table = pd.DataFrame(people).to_html()

    # print(html_table)
    return render_template("users1.html", people=html_table)


if __name__ == "__main__":
    app.run()
