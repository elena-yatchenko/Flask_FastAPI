# Дорабатываем задачу 1.
# Добавьте две дополнительные страницы в ваше веб-приложение:
# страницу "about"
# страницу "contact".

from Less_1_Task_1 import *
from flask import Flask


@app.route("/about/")
def about():
    return "about"


@app.route("/contact/")
def contact():
    return "contact"


if __name__ == "__main__":
    app.run()
