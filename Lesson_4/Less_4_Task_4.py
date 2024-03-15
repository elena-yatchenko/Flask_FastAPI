# Задание №4
# � Создать программу, которая будет производить подсчет
# количества слов в каждом файле в указанной директории и
# выводить результаты в консоль.
# � Используйте потоки.

import threading
import os

# MY_PATH = os.path.join(os.getcwd(), 'Lecture_3_SQLA, WTF')
MY_PATH = 'Lecture_3_SQLA, WTF'

def worker(file_):
    with open(file_, "r", encoding="utf-8") as f:
        content = f.read()
        num_words = len(content.split())
        print(f"Слов в {file_}: {num_words}")


def main(directory):
    threads = []

    for root, dirs, files in os.walk(directory):
        # пропускаем тот случай, когда функция итерируется по файлам папки _pycache_, вызывая ошибку при чтении их форматов
        # т.к. в этом случае список dirs будет пустым, поэтому добавляем это условие. Но это решение только для данной
        # конкретной папки, чтобы не заморачиваться с pycache так делать не нужно, иначе будем пропускать ряд нужных файлов
        if not dirs:
            continue
        for file in files:
            # print(dirs)
            file_path = os.path.join(root, file)
            t = threading.Thread(target=worker, args=(file_path,))
            threads.append(t)
            t.start()

    for t in threads:
        t.join()


if __name__ == "__main__":
    main(MY_PATH)
