# Задание №3
# � Написать программу, которая считывает список из 10 URLадресов и одновременно загружает данные с каждого
# адреса.
# � После загрузки данных нужно записать их в отдельные
# файлы.
# � Используйте асинхронный подход.

import asyncio # модуль для асинхронной загрузки страниц
import aiohttp # модуль для асинхронного получения http страницы и загрузки ее в файл 
import aiofiles
"""!!!!в асинхронной программе нужны асинхронные библиотеки, иначе нет большого смысла, будет работать
как обычная синхронная"""
import time
import os

urls = ['https://www.google.ru/',
        'https://gb.ru/',
        'https://ya.ru/',
        'https://www.python.org/',
        'https://habr.com/ru/all/',
        ]


async def download(url):
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            text = await response.text()
            filename = 'async_' + url.replace('https://', '').replace('.', '_').replace('/', '') + '.html'
            file_path = os.path.join(os.getcwd(), 'Lesson_4', 'files', filename)
            async with aiofiles.open(file_path, "w", encoding='utf-8') as f:
                f.write(text)
                print(f"Downloaded {url} in {time.time()-start_time:.2f} seconds")


async def main():
    tasks = []
    for url in urls:
        task = asyncio.ensure_future(download(url))
        tasks.append(task)
    await asyncio.gather(*tasks)

start_time = time.time()

if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())