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

import asyncio
from random import randint
import time

"""синхронный вариант"""

def synch():
    start_time = time.time()
    data = [randint(1, 100) for _ in range(1_000_000)]
    print(f'Синхронное выполнение.\nСумма: {sum(data)}, время выполнения: {time.time() - start_time:.2f}')

"""асинхронный вариант"""

summa = 0

async def my_sum():
    global summa
    data = [randint(1, 100) for _ in range(1000)]
    summa += sum(data)


async def asynch():
    start_time = time.time()
    for i in range(1000):
        task = asyncio.create_task(my_sum())
        await task
    
    print(f'Асинхронное выполнение.\nСумма: {summa}, время выполнения: {time.time() - start_time:.2f}')




if __name__ == "__main__":
    synch()
    asyncio.run(asynch())