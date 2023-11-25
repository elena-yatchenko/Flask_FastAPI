# Выводим HTML
"""Рассмотрим два варианта вывода HTML."""

# МНОГОСТРАНИЧНЫЙ ТЕКСТ С ТЕГАМИ

"""Python легко может сохранить многостраничный документ в переменной, если
заключить его в три двойные кавычки."""
from flask import Flask

app = Flask(__name__)

html = """
<h1>Привет, меня зовут Алексей</h1>
<p>Уже много лет я создаю сайты на Flask.<br/>Посмотрите на мой сайт.</p>
"""

"""Содержимое переменной можно вернуть, используя функцию представления. При
этом браузер выведет текст с учётом тегов.
"""


@app.route("/text/")
def text():
    return html


"""Как вы видите, html теги не выводятся в браузере как текст, а преобразуются в теги."""

"""При желании можно сделать страницу динамической. В примере ниже каждая
строчка стихотворения хранится как элемент списка list. Для примера в первой
лекции этого достаточно. Но вы должны понимать, что аналогичным образом можно
использовать данные из БД, внешних источников и т.п.
"""


@app.route("/poems/")
def poems():
    poem = [
        "Вот не думал, не гадал,",
        "Программистом взял и стал.",
        "Хитрый знает он язык,",
        "Он к другому не привык.",
    ]
    txt = "<h1>Стихотворение</h1>\n<p>" + "<br/>".join(poem) + "</p>"
    return txt


"""При желании можно прописать любую логику внутри функции, в зависимости от
задач программиста и того, какую информацию необходимо вывести на странице
сайта."""

# РЕНДЕРИНГ HTML файла

"""Попробуем вывести файл index.html, используя локальный сервер Flask."""
"""
<!doctype html>
<html lang="ru">
<head>
    <meta charset="utf-8">
    <link rel="stylesheet" href="/static/css/bootstrap.min.css">
    <title>Главная</title>
</head>
<body>
    <h1 class="text-monospace">Привет, меня зовут Алексей</h1>
    <img src="/static/image/foto.jpg" alt="Моё фото" width="300">
    <p class="text-body text-justify">Lorem ipsum dolor sit amet,
consectetur adipisicing elit. Ad cupiditate doloribus ducimus nam
provident quo similique! Accusantium aperiam fugit magnam quas
reprehenderit sapiente temporibus voluptatum!</p>
    <p class="alert-dark">Все права защищены &copy;</p>
</body>
</html>
"""

"""Начнём с того, что импортируем функцию отрисовки шаблонов. render_template()
принимает в качестве первого аргумента название html-файла, который
необходимо вывести в браузер.

from flask import render_template
"""
"""Добавим функцию рендеринга в функцию представления и укажем ей на файл
index.html. Общий код будет выглядеть так:"""

from flask import Flask
from flask import render_template

app = Flask(__name__)


@app.route("/index/")
def html_index():
    return render_template("index.html")


"""После перехода по локальному адресу получим сообщение об ошибке:

TemplateNotFound
jinja2.exceptions.TemplateNotFound: index.html
"""
"""!!!! Функция render_template() ищет файл index.html в папке templates. Необходимо
перенести его в нужную папку. Другие html-файлы также необходимо складывать в
указанную папку.
"""

"""После перезагрузки сервер выводит страницу в браузер."""

"""🔥 Внимание! Если изображения или стили отсутствуют, необходимо
переместить их в соответствующие каталоги: стили в static/css, а
изображения — в static/image. В самом html проверить путь к файлам(для index.html из примера):

<link rel="stylesheet" href="/static/css/style.css">
<img src="/static/image/foto.png" alt="Моё фото" width="300">

После очередной перезагрузки сервера мы получим полноценную html-страницу."""

if __name__ == "__main__":
    app.run()
