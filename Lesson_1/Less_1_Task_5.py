# Написать функцию, которая будет выводить на экран HTML страницу с заголовком "Моя первая HTML страница" и абзацем "Привет, мир!".

from flask import Flask

app = Flask(__name__)


@app.route("/")
def html_str():
    html_text = """
    <h1>Hello world!</h1>
    <p>Second string</p>
    """
    return html_text


if __name__ == "__main__":
    app.run()
