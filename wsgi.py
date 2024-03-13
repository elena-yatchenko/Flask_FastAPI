# ОПТИМИЗАЦИЯ

"""Внесём изменения в проект. В КОРНЕВОМ каталоге создадим файл wsgi.py со
следущим кодом.
"""

# from Lecture_1.Lect_1_Flask_base import app
from Homework_3.HW_app_4 import app

if __name__ == "__main__":
    app.run(debug=True)

"""Импортируем из файла проекта переменную приложения. Параметр debug=True
включает режим отладки (для разработки. для пользователя его отключают).
"""

"""
Теперь для запуска сервера из командной строки достаточно выполнить команду

flask run --debug

Файл с именем wsgi.py будет найден автоматически.
"""
"""🔥 Важно! В рамках урока будут использоваться различные, зачастую не
связанные между собой примеры кода. Поэтому в каждом файле будет
использоваться своя конструкция app.run() для запуска именно этого
файла в качестве Flask сервера.
"""
