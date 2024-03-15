import asyncio
import os
import aiofiles
import time

MY_PATH = 'Lecture_3_SQLA, WTF'


async def worker(file_):
    async with aiofiles.open(file_, "r", encoding="utf-8") as f:
        content = await f.read()
        print(f"Слов в {file_} : {len(content.split())}")


async def main():
    for root, dirs, files in os.walk(MY_PATH):
        if not dirs:
            continue
        for file in files:
            file_path = os.path.join(root, file)
            task = asyncio.create_task(worker(file_path))
            await task


if __name__ == "__main__":
    asyncio.run(main())


"""
if __name__ == '__main__':
    start_time = time.time()
    asyncio.run(main())
    stop_time = time.time()
    print(f'time.time() - start_time):.2f')
"""
