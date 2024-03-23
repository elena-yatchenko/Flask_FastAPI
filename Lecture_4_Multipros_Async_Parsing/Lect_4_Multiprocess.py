# Многопроцессорный подход

"""
Многопроцессорный код — это подход к многозадачности, при котором программа
может выполнять несколько задач одновременно в разных процессах. Каждый
процесс выполняет свою задачу независимо от других процессов, что позволяет
улучшить производительность программы. При этом процессы могут быть
запущены на разных процессорах многопроцессорного сервера.

Примеры многопроцессорных операций в Python:
● параллельная обработка большого объема данных
● одновременное выполнение нескольких запросов к базе данных
● многопроцессорный веб-сервер, обрабатывающий несколько запросов
одновременно

Преимущества многопроцессорного кода:
● возможность использования нескольких ядер процессора для выполнения
программы
● увеличение производительности программы за счет параллельного
выполнения задач
● возможность выполнения нескольких задач одновременно без блокировки

Недостатки многопроцессорного кода:
● возможность возникновения конкуренции за ресурсы
● сложность управления и координации процессов
● возможность блокировки процессов выполнения

Для решения проблем, связанных с конкуренцией за ресурсы и блокировками
процессов, можно использовать механизмы синхронизации, такие как блокировки
и семафоры. Однако, неправильное использование этих механизмов может
привести к дедлокам (deadlock) и другим проблемам.

При разработке многопроцессорных программ необходимо учитывать особенности
языка Python, такие как использование модуля multiprocessing для создания и
управления процессами. Также следует учитывать потребление ресурсов
процессами и оптимизировать их работу.

В целом, многопроцессорный подход позволяет использовать несколько ядер
процессора для выполнения программы и улучшить ее производительность.
Однако, при разработке многопроцессорных программ необходимо учитывать
особенности языка Python и правильно использовать механизмы синхронизации
для избежания проблем.

Примеры программа на Python

Пример 1:
"""
import multiprocessing
import time


def worker(num):
    print(f"Запущен процесс {num}")
    time.sleep(3)
    print(f"Завершён процесс {num}")


if __name__ == "__main__":
    processes = []

    for i in range(5):
        p = multiprocessing.Process(target=worker, args=(i,))
        processes.append(p)
        p.start()

    for p in processes:
        p.join()

print("Все процессы завершили работу")

"""
Эта программа создает 5 процессов и запускает функцию worker() в каждом из них.
Функция worker() просто выводит сообщение о запуске процесса, ждёт 3 секунды и
сообщает о завершении. Весь код работает многопроцессорно, то есть каждый
процесс работает независимо от других, и выполнение программы не блокируется
на время выполнения функции.

Пример 2:
"""
import multiprocessing
import time


def worker(num):
    print(f"Запущен процесс {num}")
    time.sleep(3)
    print(f"Завершён процесс {num}")


if __name__ == "__main__":
    processes = []
    for i in range(5):
        p = multiprocessing.Process(target=worker, args=(i,))
        processes.append(p)

    for p in processes:
        p.start()
        p.join()

print("Все процессы завершили работу")

"""
Эта программа создает 5 процессов и запускает функцию worker() в каждом из них.
Функция worker() просто выводит сообщение о запуске процессаа, ждёт 3 секунды
и сообщает о завершении. Весь код работает многопроцессорно, но в отличие от
предыдущего примера, процессы запускаются и завершаются последовательно,
блокируя выполнение программы на время выполнения каждого процесса.

Пример 3:
"""
import multiprocessing

counter = 0


def increment():
    global counter
    for _ in range(10_000):
        counter += 1
    print(f"Значение счетчика: {counter:_}")


if __name__ == "__main__":
    processes = []
    for i in range(5):
        p = multiprocessing.Process(target=increment)
        processes.append(p)
        p.start()

    for p in processes:
        p.join()

print(f"Значение счетчика: {counter:_}")

"""
Эта программа создает 5 процессов и запускает функцию increment() в каждом из
них. Функция increment() увеличивает значение глобальной переменной counter на
10 тысяч раз. Весь код работает многопроцессорно, но из-за того, что несколько
процессов работают с одной переменной, может возникнуть проблема гонки
данных (race condition), когда результат выполнения программы может быть
непредсказуемым.

В нашем случае каждый из процессов работает со своей переменной counter. 5
процессов — 5 переменных со значением 10000 в финале.

Чтобы избежать этой проблемы, используется объект multiprocessing.Value, который
обеспечивает безопасный доступ к общей переменной через механизм блокировки
(lock). Каждый процесс получает доступ к переменной только после получения
блокировки, что гарантирует правильность ее изменения. Для этого код
необходимо изменить следующим образом.
"""
import multiprocessing

counter = multiprocessing.Value("i", 0)


def increment(cnt):
    for _ in range(10_000):
        with cnt.get_lock():
            cnt.value += 1

    print(f"Значение счетчика: {cnt.value:_}")

    if __name__ == "__main__":
        processes = []

        for i in range(5):
            p = multiprocessing.Process(target=increment, args=(counter,))
            processes.append(p)
            p.start()

        for p in processes:
            p.join()


print(f"Значение счетчика в финале: {counter.value:_}")

"""
Теперь 5 процессов используя доступ к одному объекту увеличивают его значение
до 50 тысяч — 5 процессов по 10к каждый.
"""
