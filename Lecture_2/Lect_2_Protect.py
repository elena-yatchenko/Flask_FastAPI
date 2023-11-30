# ЭКРАНИРОВАНИЕ пользовательских данных

"""Начнём занятие с того, что не каждый пользователь будет делать то, что вы от него
хотите. Например попросим пользователя передать путь до файла в адресной
строке."""

# from flask import Flask
# from flask import render_template

# app = Flask(__name__)

# @app.route('/')
# def index():
#     return 'Введи путь к файлу в адресной строке'

# @app.route('/<path:file>/')
# def get_file(file):
#     print(file)
#     return f'Ваш файл находится в: {file}!'

# # http://127.0.0.1:5000/test/2254/test/

# # Ваш файл находится в: test/2254/test!

"""А теперь вместо пути, передадим следующую строку:
http://127.0.0.1:5000/<script>alert("I am haсker")</script>/
"""
"""На страницу будет выведен текст без пути. И одновременно сработает js скрипт с
всплывающим сообщением о хакере. А ведь код может быть не таким безобидным
как в примере."""

"""!!! Для повышения безопасности необходимо экранировать пользовательский ввод.
Для этого используйте функцию escape из модуля markupsafe"""

from flask import Flask

from markupsafe import escape

app = Flask(__name__)

@app.route('/')
def index():
    return 'Введи путь к файлу в адресной строке'


@app.route('/<path:file>/')
def get_file(file):
    return f'Ваш файл находится в: {escape(file)}!'

# http://127.0.0.1:5000/%3Cscript%3Ealert(%22I%20am%20ha%D1%81ker%22)%3C/script%3E/

# Ваш файл находится в: <script>alert("I am haсker")</script>!

if __name__ == "__main__":
    app.run()