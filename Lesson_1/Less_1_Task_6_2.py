# Написать функцию, которая будет выводить на экран HTML страницу с таблицей, содержащей информацию о студентах.
# Таблица должна содержать следующие поля: "Имя", "Фамилия", "Возраст", "Средний балл".
# Данные о студентах должны быть переданы в шаблон через контекст.

# !!! Другие варианты заполнения таблицы HTML
# 1- через TABULATE

from flask import Flask
from flask import render_template
from tabulate import tabulate

# pip install tabulate

# import pandas as pd
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
    """tabulate принимает СПИСОК СЛОВАРЕЙ в качестве аргумента, преобразовывая его в html-таблицу"""
    html_table = tabulate(people, headers="keys", tablefmt="html")
    #     html_table = pd.DataFrame(people).to_html()

    # print(html_table)
    return render_template("users1.html", people=html_table)


if __name__ == "__main__":
    app.run()

# Имя	Фамилия	Возраст	Средний бал
# Иван	Иванов	20	4.5
# Петр	Петров	21	4.2
# Сергей	Сергеев	19	4.8
# Анна	Иванова	20	4.7


# <table>
# <thead>
# <tr><th>Имя   </th><th>Фамилия  </th><th style="text-align: right;">  Возраст</th><th style="text-align: right;">  Средний бал</th></tr>
# </thead>
# <tbody>
# <tr><td>Иван  </td><td>Иванов   </td><td style="text-align: right;">       20</td><td style="text-align: right;">
#  4.5</td></tr>
# <tr><td>Петр  </td><td>Петров   </td><td style="text-align: right;">       21</td><td style="text-align: right;">
#  4.2</td></tr>
# <tr><td>Сергей</td><td>Сергеев  </td><td style="text-align: right;">       19</td><td style="text-align: right;">
#  4.8</td></tr>
# <tr><td>Анна  </td><td>Иванова  </td><td style="text-align: right;">       20</td><td style="text-align: right;">
#  4.7</td></tr>
# </tbody>
# </table>
