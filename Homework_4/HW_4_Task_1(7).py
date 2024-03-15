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

import threading
import multiprocessing
import time
from random import randint

"""синхронный вариант"""
def synch():
    start_time = time.time()
    data = [randint(1, 100) for _ in range(1_000_000)]
    print(f'Синхронное выполнение.\nСумма: {sum(data)}, время выполнения: {time.time() - start_time:.2f}')

"""многопоточный вариант"""
summa = 0

def my_sum():
    global summa
    data = [randint(1, 100) for _ in range(1000)]
    summa += sum(data)

def thread_result():
    start_time = time.time()
    threads = []
    for i in range(1000):
        t = threading.Thread(target=my_sum)
        threads.append(t)
        t.start()

    for t in threads:
        t.join()
    print(f'Многопоточное выполнение.\nСумма: {summa}, время выполнения: {time.time() - start_time:.2f}')

"""многопроцессорный вариант"""
def multiproc_result():
    start_time = time.time()
    processes = []
    for i in range(3):
        p = multiprocessing.Process(target=my_sum)
        processes.append(p)
        p.start()

    for p in processes:
        p.join()
    print(f'Многопроцессорное выполнение.\nСумма: {summa}, время выполнения: {time.time() - start_time:.2f}')


if __name__ == "__main__":  
    #synch()
    thread_result()
   