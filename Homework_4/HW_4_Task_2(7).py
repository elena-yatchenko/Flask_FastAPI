# Задание №7
# � Напишите программу на Python, которая будет находить
# сумму элементов массива из 1000000 целых чисел.
# � Пример массива: arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, ...]
# � Массив должен быть заполнен случайными целыми числами
# от 1 до 100.
# � При решении задачи нужно использовать многопоточность,
# многопроцессорность и асинхронность.
# � В каждом решении нужно вывести время выполнения
# вычислений.

import multiprocessing
import time
from random import randint

"""синхронный вариант"""
def synch():
    start_time = time.time()
    data = [randint(1, 100) for _ in range(1_000_000)]
    print(f'Синхронное выполнение.\nСумма: {sum(data)}, время выполнения: {time.time() - start_time:.2f}')

"""многопроцессорный вариант"""

summa = multiprocessing.Value('i', 0)

def my_sum(s):
    with s.get_lock():
        data = [randint(1, 100) for _ in range(1000)]
        s.value += sum(data)
        # print(s.value)


def multiproc_result():
    start_time = time.time()
    processes = []
    for i in range(1000):
        p = multiprocessing.Process(target=my_sum, args=(summa,))
        processes.append(p)
        p.start()

    for p in processes:
        p.join()
    print(f'Многопроцессорное выполнение.\nСумма: {summa.value}, время выполнения: {time.time() - start_time:.2f}')


if __name__ == "__main__":
    #synch()
    multiproc_result()