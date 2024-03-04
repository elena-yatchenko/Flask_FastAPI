# from flask import Flask
# from flask import render_template
# from tabulate import tabulate
# import pandas as pd

# app = Flask(__name__)


# @app.route("/students/")
# def fill_table():
#     people = [
#         {"Имя": "Иван", "Фамилия": "Иванов", "Возраст": 20, "Средний бал": 4.5},
#         {"Имя": "Петр", "Фамилия": "Петров", "Возраст": 21, "Средний бал": 4.2},
#         {"Имя": "Сергей", "Фамилия": "Сергеев", "Возраст": 19, "Средний бал": 4.8},
#         {"Имя": "Анна", "Фамилия": "Иванова", "Возраст": 20, "Средний бал": 4.7},
#     ]

#     # html_table = tabulate(people, headers='keys', tablefmt='html')
#     html_table = pd.DataFrame(people).to_html()

#     print(html_table)
#     return render_template("students.html", people=html_table)


# if __name__ == "__main__":
#     app.run()


# <!DOCTYPE html>
# <html lang="en">
# <head>
#     <meta charset="UTF-8">
#     <title>Студенты</title>
# </head>
# <body>
# {% autoescape false %}
# {{ people }}
# {% endautoescape %}
# <!--{{ people | safe }}-->
# </body>
# </html>


# https://share.vidyard.com/watch/Tfq5BWqxoyaKnh2QRfnXBB?

# Как отправлять домашку по питону.
# 1. Создаём репозиторий на гх
# 2. Линкуем его с пайчармом или делаем локальный репозиторий.
# 3. Создаём НОВУЮ ветку и пишем там домашнее задание
# 4. Делаем пулл на гитхаб
# 5. На странице репозитория переходим в новую ветку
# 6. Нажимает кнопку создать пулл-реквест из новой ветки в ветку main
# 7. Откроется страница пулл-реквеста
# 8. Копируем ссылку и отправляем на проверку
# 9.....
# 10. Profit

