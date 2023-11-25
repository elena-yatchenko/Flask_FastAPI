"""Создать базовый шаблон для интернет-магазина, содержащий общие элементы дизайна 
(шапка, меню, подвал), и дочерние шаблоны для страниц категорий товаров и отдельных товаров. 
Например, создать страницы «Одежда», «Обувь» и «Куртка», используя базовый шаблон."""


from flask import Flask
from flask import render_template
import pandas as pd

app = Flask(__name__)


@app.route("/")
def base():
    return render_template("base.html")


@app.route("/clothes/")
def clothes():
    cl_brends = ["Calvin Klein", "ZARA", "Massimo Dutti", "Guess", "Marks&Spencer"]
    context = {"data": cl_brends}
    return render_template("clothes.html", **context)


@app.route("/shoes/")
def shoes():
    sh_brends = ["Valentino Garavani", "Jimmy Choo", "Calvin Klein", "Emporio Armani"]
    context = {"title": "Коллекция женской обуви", "data": sh_brends}
    return render_template("shoes.html", **context)


@app.route("/clothes/jacket/")
def jacket():
    size = [
        {"EUR": "34", "USA": "XS", "RUS": 42},
        {"EUR": "36", "USA": "S", "RUS": 44},
        {"EUR": "38", "USA": "M", "RUS": 46},
        {"EUR": "40", "USA": "L", "RUS": 48},
    ]
    html_table = pd.DataFrame(size).to_html()

    context = {"title": "Куртки", "size_table": html_table}
    return render_template("jacket.html", **context)


if __name__ == "__main__":
    app.run()
