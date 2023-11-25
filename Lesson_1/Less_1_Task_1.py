"""Напишите простое веб-приложение на Flask, которое будет выводить на экран текст "Hello, World!"."""

from flask import Flask

app = Flask(__name__)


@app.route("/")
def hello():
    return "Hello, world"


if __name__ == "__main__":
    app.run()

# (venv) PS D:\My Documents\docs\Geek Brains\Flask_FastAPI> cd Lesson_1
# (venv) PS D:\My Documents\docs\Geek Brains\Flask_FastAPI\Lesson_1> python .\Less_1_Task_1.py
