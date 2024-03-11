# НАСЛЕДОВАНИЕ ШАБЛОНОВ

"""Начнём с классической ситуации дублирования кода, который нарушает принцип
DRY. Рассмотрим две html-страницы с большим объёмом одинакового кода.
Шаблон main.html и Шаблон data.htm
"""

"""Для того, чтобы выводить эту пару страниц достаточно несколько строк кода на Flask"""

from flask import Flask
from flask import render_template

app = Flask(__name__)


# @app.route("/main/")
# def main():
#     context = {"title": "Главная"}
#     return render_template("main.html", **context)


# @app.route("/data/")
# def data():
#     context = {"title": "База статей"}
#     return render_template("data.html", **context)


"""На каждой странице всего несколько различных строк в середине. Остальной код
дублируется, Представьте, что у вас большой проект на десятки аналогичных
страниц. Сколько же времени вы затратите, чтобы изменить шапку или футер во всём проекте?
"""

# БАЗОВЫЙ И ДОЧЕРНИЕ ШАБЛОНЫ

"""Создадим базовый шаблон base.html, который будет включать весь одинаковый код. 
Шаблон base.html"""

"""Исключённый текст для заголовка сайта был заменён на: """

# {% block title %} Мой сайт {% endblock %}

"""Для содержимого страницы код заменён на: """

# {% block content %}
# Страница не заполнена
# {% endblock %}

"""Количество блоков в базовом шаблоне и их названия зависят от задачи, которую
решает разработчик. Содержимое внутри block впоследствии будет заполнено
дочерними шаблонами. Инструкция block принимает один аргумент — название
блока. Внутри шаблона это название должно быть уникальным, иначе возникнет
ошибка.
Если в дочернем шаблоне блок отсутствует, выводится информация из базового
шаблона. В нашем примере, если в дочернем шаблоне не прописать блок title, будет
выведено значение «Мой сайт» из базового шаблона, а вместо содержимого увидим
что “Страница не заполнена”
"""

"""Теперь из main.html и data.html можно удалить дублирующиеся строки и указать, что эти шаблоны расширяют базовый - 
{% extends 'base.html' %} в первой же строке дочернего шаблона.

(Создаю шаблоны main1.html и data1.html - см. соответствующие файлы в папке templates)
"""

"""Содержимое одноимённых блоков в дочерних шаблонах будет подставлено в соответствующее место базового.
"""

"""🔥 Внимание! Использование переменной {{ super() }} в дочерних шаблонах
позволяет выводить содержимое родительского блока, а не заменять его!
"""

"""После такой оптимизации достаточно внести изменение в базовом шаблоне, чтобы
обновить одинаковую информацию на всех страницах сайта.

Дочерние шаблоны компакты и содержат только специфичную для страницы
информацию. А при отрисовке через Jinja в них легко передавать динамически
изменяемую информацию"""

"""🔥 Важно! Сохранять текстовую информацию внутри html файла как в data1.html нелогично. 
Она должна храниться в базе данных. А шаблон в этом случае может получать её через контекст (распаковка) и выводить в цикле.
"""


@app.route("/")
def base():
    return render_template("base.html")


@app.route("/main/")
def main():
    context = {"title": "Главная"}
    return render_template("main1.html", **context)


@app.route("/data/")
def data():
    context = {"title": "Данные"}
    return render_template("data1.html", **context)


if __name__ == "__main__":
    app.run()

"""!!!!!
Чтобы упростить доступ к форме входа, базовый шаблон должен включать в себя ссылку на панель навигации:
<div>
    Microblog:
    <a href="/index">Home</a>
    <a href="/login">Login</a>
</div>"""