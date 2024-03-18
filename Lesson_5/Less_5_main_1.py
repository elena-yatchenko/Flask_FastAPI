# Задание №1
# Создать API для управления списком задач. Приложение должно иметь
# возможность создавать, обновлять, удалять и получать список задач.
# Создайте модуль приложения и настройте сервер и маршрутизацию.
# Создайте класс Task с полями id, title, description и status.
# Создайте список tasks для хранения задач.
# Создайте маршрут для получения списка задач (метод GET).
# Создайте маршрут для создания новой задачи (метод POST).
# Создайте маршрут для обновления задачи (метод PUT).
# Создайте маршрут для удаления задачи (метод DELETE).
# Реализуйте валидацию данных запроса и ответа.


from fastapi import FastAPI

# import logging
from typing import Optional
from pydantic import BaseModel
from random import choice
import uvicorn


# logging.basicConfig(level=logging.INFO)
# logger = logging.getLogger(__name__)

app = FastAPI()


class Task(BaseModel):
    id: int
    title: str
    description: Optional[str] = None
    status: str


# print(tasks)

statuses = ["to do", "in progress", "done"]
tasks = []
for i in range(1, 6):
    id = i
    title = "name_" + str(i)
    description = "description_" + str(i) * 3
    status = choice(statuses)
    data = {"id": id, "title": title, "description": description, "status": status}
    task = Task(**data)
    tasks.append(task)
print(tasks)


@app.get("/")
async def root():
    return {"message": "Hello world"}


@app.get("/data/")
async def receive():

    return {"task_list": tasks}


@app.post("/tasks/")
async def create(task: Task):
    tasks.append(task)
    return task


@app.put("/tasks/{task_id}")
async def updating(task_id: int, task: Task):
    for i in range(len(tasks)):
        if tasks[i].id == task_id:
            tasks[i] = task
    return {"task_id": task_id, "task": task}


@app.delete("/tasks/{task_id}")
async def delete_data(task_id: int):
    for task in tasks:
        if task.id == task_id:
            tasks.remove(task)
    print(tasks)
    return {"task_id": task_id}


if __name__ == "__main__":
    uvicorn.run("Less_5_main_1:app", host="127.0.0.1", port=8000)


"""пример создания класса на основе BaseModel
from pydantic import BaseModel
from typing import Optional, List

class Person(BaseModel):
    first_name: str
    last_name: str
    interest: Optional[List[str]]

data = {"first_name": "Ahmed", "last_name": "Besbes"}
person = Person(**data)
print(person)

# first_name='Ahmed' last_name='Besbes' address=None interests=None
"""
