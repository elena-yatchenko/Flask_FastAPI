# ОБРАБОТКА ОШИБОК

"""Что будет, если пользователь перешёл на несуществующую страницу? Если ничего
не предпринимать, получим следующий вывод:

*** Not Found
*** The requested URL was not found on the server. If you entered the URL manually
*** please check your spelling and try again.
"""

# ДЕКОРАТОР ERRORHANDLER

"""Flask предоставляет возможности для обработки ошибок и способен заменить
стандартный текст на симпатичную страницу в стиле вашего сайта.
Обработка ошибок в Flask происходит с помощью декоратора errorhandler(). Этот
декоратор позволяет определить функцию-обработчик ошибок, которая будет
вызываться в случае возникновения ошибки в приложении.

Например, чтобы обработать ошибку 404 (страница не найдена), необходимо
определить функцию, которая будет вызываться при возникновении этой ошибки:"""

# import logging
# from flask import Flask, render_template, request

# app = Flask(__name__)
# logger = logging.getLogger(__name__)


# @app.route("/")
# def index():
#     return "<h1>Hello world!</h1>"


# @app.errorhandler(404)
# def page_not_found(e):
#     logger.warning(e)
#     context = {
#         "title": "Страница не найдена",
#         "url": request.base_url,
#     }
#     return render_template("404.html", **context), 404


"""В этом примере мы определяем функцию page_not_found(), которая будет
вызываться при ошибке 404. Функция возвращает шаблон HTML страницы 404 и
код ошибки 404. Обратите внимание, что в переменную e попадает текст той самой
ошибки о “Not Found…”. Её мы выводим в логи как предупреждение.
В качестве контекста пробрасываем в шаблон заголовок страницы и адрес, по
которому пытался перейти пользователь. 

Свойство base_url у объекта request
возвращает тот адрес, который видит пользователь в адресной строке браузера."""

"""Что касается шаблона, возьмём базовый из прошлой лекции - Шаблон base.html"""

"""В этом случае шаблон для ошибки 404 может выглядеть например так - 404.html:
"""

"""Обратите внимание, что адрес главной страницы указан не явно, а генерируется
через url_for. Подобная практика должна использоваться во всех шаблонах проекта
для удобства масштабирования."""


# ФУНКЦИЯ ABORT

"""Функция abort() также используется для обработки ошибок в Flask. Она позволяет
вызвать ошибку и передать ей код ошибки и сообщение для отображения
пользователю.

Например, чтобы вызвать ошибку 404 с сообщением "Страница не найдена",
необходимо использовать функцию abort():"""

# import logging
# from flask import Flask, render_template, request, abort

# from db import get_blog

# app = Flask(__name__)
# logger = logging.getLogger(__name__)


# @app.route("/")
# def index():
#     return "<h1>Hello world!</h1>"


# @app.route("/blog/<int:id>")
# def get_blog_by_id(id):
#     # делаем запрос в БД (базу данных) для поиска статьи по id
#     result = get_blog(id)
#     if result is None:
#         abort(404)

#     # возвращаем найденную в БД статью


# @app.errorhandler(404)
# def page_not_found(e):
#     logger.warning(e)
#     context = {
#         "title": "Страница не найдена",
#         "url": request.base_url,
#     }
#     return render_template("404.html", **context), 404


"""В этом примере мы используем функцию abort() внутри get_blog_by_id для вызова
ошибки 404 в случае отсутствия статьи в базе данных"""

"""💡 Внимание! Чтобы код внутри представления отработал без ошибок,
написана следующая функция заглушка в файле db.py:

def get_blog(id):
return None

"""

"""Некоторые коды ошибок

● 400: Неверный запрос
● 401: Не авторизован
● 403: Доступ запрещен
● 404: Страница не найдена
● 500: Внутренняя ошибка сервера
"""

# пример ОБРАБОТКИ ОШИБКИ 500

"""Иногда из-за ошибок в коде сервер может возвращать ошибку 500. В идеальном
мире код предусматривает все возможные ситуации и не отдаёт ошибку 500. Но
почему бы не подстелить соломки."""

"""Удалим функции get_blog из примера выше. Теперь при попытке найти статью по id
получаем сообщение на странице:

Internal Server Error
The server encountered an internal error and was unable to complete your request.
Either the server is overloaded or there is an error in the application.
"""

"""🔥 Важно! Если вы запускаете сервер в режиме отладки (debug=True), будет выведена
трассировка ошибки, а не сообщение. Перезапустите сервер с параметром debug=False 

!!! Все, что выводим для пользователя (более приятное сообщение об ошибке, например) НЕ РАБОТАЕТ, ЕСЛИ DEBUG=TRUE)"""


import logging
from flask import Flask, render_template, request, abort

# from db import get_blog

app = Flask(__name__)
logger = logging.getLogger(__name__)


@app.route("/")
def index():
    return "<h1>Hello world!</h1>"


@app.route("/blog/<int:id>")
def get_blog_by_id(id):
    # делаем запрос в БД (базу данных) для поиска статьи по id
    result = get_blog(id)
    if result is None:
        abort(404)

    # возвращаем найденную в БД статью


@app.errorhandler(404)
def page_not_found(e):
    logger.warning(e)
    context = {
        "title": "Страница не найдена",
        "url": request.base_url,
    }
    return render_template("404.html", **context), 404


"""И напишем обработчик для вывода сообщения об ошибке 500 в стиле проекта.

По сути взяли за основу обработчик ошибки 404, но лог фиксирует не
предупреждение, а ошибку. Плюс новый шаблон, и возврат кода 500 клиенту"""


@app.errorhandler(500)
def page_not_found(e):
    logger.error(e)
    context = {
        "title": "Ошибка сервера",
        "url": request.base_url,
    }
    return render_template("500.html", **context), 500


"""При запуске получаем user-friendly сообщение об ошибке"""


if __name__ == "__main__":
    app.run(debug=False)
