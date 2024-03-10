# ХРАНЕНИЕ ДАННЫХ

""" Рассмотрим возможность сохранения данных между запросами."""

# Работа с COOKIE файлами в Flask

"""Cookie файлы — это небольшие текстовые файлы, которые хранятся в браузере
пользователя и используются для хранения информации о пользователе и его
предпочтениях на сайте. В Flask, работа с cookie файлами очень проста и может
быть выполнена с помощью самого фреймворка, без установки дополнительных
модулей."""

"""Для работы с cookie файлами, необходимо импортировать модуль Flask и объект
request, который позволяет получить доступ к cookie файлам. 

Подобное мы проделывали несколько раз за лекцию. Разберем куки на примере """

from flask import Flask, request, make_response

app = Flask(__name__)


# @app.route("/")
# def index():
#     # устанавливаем cookie
#     response = make_response("Cookie установлен")
#     response.set_cookie("username", "admin")
#     return response


# @app.route("/getcookie/")
# def get_cookies():
#     # получаем значение cookie
#     name = request.cookies.get("username")
#     return f"Значение cookie: {name}"


"""Мы устанавливаем значение cookie файла с ключом "username" и значением
"admin" в функции index(). Затем мы получаем значение cookie файла с ключом
"username" в функции get_cookies() и выводим его на экран."""


# СОЗДАНИЕ ОТВЕТА - функция MAKE_RESPONSE()

"""Несколько слов о функции make_response(). 


Фреймворк Flask устанавливает файлы cookie в объект ответа flask.Response. 
Для того, что бы установить cookie клиенту, сначала необходимо получить объект ответа 
Response в функции-представлении при помощи функции flask.make_response(). 
После этого можно изменить ответ, установив cookie, используя метод Response.set_cookie().

Во всех прошлых примерах мы
возвращали из view функций обычный текст, текст форматированный как HTML,
динамически сгенерированные страницы через render_template и даже запросы
переадресации благодаря функциям redirect и url_for. Каждый раз Flask неявно
формировал объект ответа - response. 

Если же мы хотим внести изменения в ответ, можно воспользоваться функцией make_response.
"""

"""Изменим прошлый пример. Для начала создадим шаблон main.html 

Шаблон принимает заголовок и имя пользователя. Для отрисовки он расширяет
базовый шаблон. Ничего нового и никаких упоминаний “печенек”(cookies)."""

"""А теперь модифицируем представление """

from flask import Flask, request, make_response, render_template


@app.route("/")
def index():
    context = {"title": "Главная", "name": "Елена"}
    response = make_response(render_template("main.html", **context))
    response.headers["new_head"] = "New value"
    response.set_cookie("username", context["name"])
    return response


"""Используя render_template пробрасываем контекст в шаблон, но не возвращаем его,
а передаём результат в функцию make_response. Ответ сформирован, но мы можем
внести в него изменения перед возвратом. В нашем примере добавили в заголовки
пару ключ-значение(используется для передачи какой-то доп.служебной инфо между клиентом и сервером, при использовании API) 
и установили куки для имени пользователя.
"""
"""� Важно! Не путайте заголовки ответа и содержимое блок head в теле ответа. """


if __name__ == "__main__":
    app.run(debug=True)
    # app.run()

"""
!!!!!!!
Увидеть файлы cookie на странице браузера: F12 - вкладка Приложение в верхней панели вкладок -  раздел слева - "Хранилище" 
Увидеть заголовки (headers): F12 - вкладка Cеть - обновить html страницу - Заголовки

Там же файлы куки может стереть даже обычный пользователь (в отличие от сессии)
"""

"""
!!!
Удаление куки
Чтобы удалить куки, нужно вызвать метод set_cookie() с названием куки, любым значением и указать срок max_age=0. 
В файле main2.py это можно сделать, добавив следующий код после функции представления cookie().

#...
@app.route('/delete-cookie/')
def delete_cookie():
    res = make_response("Cookie Removed")
    res.set_cookie('foo', 'bar', max_age=0)
    return res
#...

Во Flask для настройки куки используется метод объекта ответа set_cookie(). Синтаксис set_cookie() следующий:

set_cookie(key, value="", max_age=None)
key — обязательный аргумент, это название куки. value — данные, которые нужно сохранить в куки. 
По умолчанию это пустая строка. max_age — это срок действия куки в секундах. 
Если не указать срок, срок истечет при закрытии браузера пользователем.

from flask import Flask, render_template, request, redirect, url_for, flash, make_response
#...
@app.route('/cookie/')
def cookie():
    res = make_response("Setting a cookie")
    res.set_cookie('foo', 'bar', max_age=60*60*24*365*2)
    return res
#...
Это пример создание куки под названием foo со значением bar, срок которых — 2 года.
"""


"""
!!! другой источник:

Фреймворк Flask упрощает работу с этим типом заголовка, предоставляя три метода, для управления cookie:

чтение файлов cookie осуществляется из контекста запроса методом request.cookies.get('cookie_name').
установка файлов cookie осуществляется в объект ответа, методом response.set_cookies('cookie_name', value, ...).
удаление файлов cookie осуществляется так же, из объект ответа, методом response.del_cookies('cookie_name').

Метод Response.set_cookie() принимает следующие аргументы:

key: строка, ключ/имя устанавливаемого файла cookie.
value: строка, значение куки.
max_age: время жизни cookie, указывается в секундах. По умолчанию None, это означает что cookie уничтожиться, 
после окончания сеанса браузера. Может быть int или datetime.timedelta().

@app.route('/delcookie')
def delcookie():
   context = {}
   context['text'] = 'Привет Мир!'
   name = 'nikolay'
   # получаем объект ответа
   resp = make_response(render_template('index.html', content=context))
   # удаляем cookie 'user'
   resp.del_cookie('user')
   # возвращаем измененный ответ
   return resp
"""
