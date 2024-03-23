# Создать API для получения списка фильмов по жанру.
# Приложение должно иметь возможность получать список фильмов по заданному жанру.
# ●	Создайте модуль приложения и настройте сервер и маршрутизацию.
# ●	Создайте класс Movie с полями id, title, description и genre.
# ●	Создайте список movies для хранения фильмов.
# ●	Создайте маршрут для получения списка фильмов по жанру (метод GET).
# ●	Реализуйте валидацию данных запроса и ответа.

from fastapi import FastAPI

# import logging
from typing import Optional
from pydantic import BaseModel
from random import choice
import uvicorn


# logging.basicConfig(level=logging.INFO)
# logger = logging.getLogger(__name__)

app = FastAPI()


class Movie(BaseModel):
    num: int
    title: str
    description: Optional[str] = None
    genre: str


# print(tasks)

movies = [
    Movie(num=1, title="Movie Шляпа", description="Description 1", genre="Action"),
    Movie(num=2, title="Movie Перчатки", description="Description 2", genre="Comedy"),
    Movie(num=3, title="Movie Вокзал", description="Description 3", genre="Action"),
    Movie(num=4, title="Movie Вокзал", description="Description 3", genre="Action"),
    Movie(num=5, title="Movie Вокзал", description="Description 3", genre="Action"),
    Movie(num=6, title="Movie Упырь", description="Description 4", genre="Drama"),
]


@app.get("/")
async def root():
    return movies


@app.get("/genre/")
async def filter_genre(genre: str):
    genre_movies = []
    for m in movies:
        if m.genre == genre:
            genre_movies.append(m.title)
    return genre_movies


@app.post("/movies/")
async def create(movie: Movie):
    movies.append(movie)
    return movie


# @app.put("/tasks/{task_id}")
# async def updating(task_id: int, task: Task):
#     for i in range(len(tasks)):
#         if tasks[i].id == task_id:
#             tasks[i] = task
#     return {"task_id": task_id, "task": task}


# @app.delete("/tasks/{task_id}")
# async def delete_data(task_id: int):
#     for task in tasks:
#         if task.id == task_id:
#             tasks.remove(task)
#     print(tasks)
#     return {"task_id": task_id}


if __name__ == "__main__":
    uvicorn.run("Less_5_main_2:app", host="127.0.0.1", port=8000)
