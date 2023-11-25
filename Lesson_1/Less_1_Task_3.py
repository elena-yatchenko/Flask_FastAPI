# Написать функцию, которая будет принимать на вход два числа и выводить на экран их сумму.

from Less_1_Task_2 import *


@app.route("/summa/<int:num1>/<int:num2>/")
def summa(num1, num2):
    summa = num1 + num2
    return f"Получили сумму {summa}"


if __name__ == "__main__":
    app.run()
