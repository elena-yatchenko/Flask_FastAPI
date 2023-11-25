# Написать функцию, которая будет принимать на вход строку и выводить на экран ее длину.

from flask import Flask

app = Flask(__name__)


@app.route("/len/<my_text>")
def get_len(my_text):
    return f"Длина строки {my_text} равна {len(my_text)}"


if __name__ == "__main__":
    app.run()
