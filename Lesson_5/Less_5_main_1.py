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
""""todo", "in progress", "done".
"""

from fastapi import FastAPI
# import logging
from typing import Optional
from pydantic import BaseModel
from random import choice


# logging.basicConfig(level=logging.INFO)
# logger = logging.getLogger(__name__)

app = FastAPI()

class Task(BaseModel):
    id: int
    title: str
    description: Optional[str] = None
    status: str

#print(tasks)

@app.get('/')
async def root():
    return {'message': 'Hello world'}

@app.get('/data/')
async def receive():
    statuses = ['to do', 'in progress', 'done']
    tasks = []
    for i in range(1, 6):
        id = i
        title = 'name_' + str(i)
        description = 'description_' + str(i)*3
        status = choice(statuses)
        data = {'id': id, 'title': title, 'description': description, 'status': status}
        task = Task(**data)
        tasks.append(task)
    return {'task_list': tasks}
    

# @app.post("/tasks/")
# async def create(task: Task):
#     return task


# @app.put("/tasks/{task_id}")
# async def updating(task_id: int, task: Task):
#     return {"task_id": task_id, "task": task}


# @app.delete("/tasks/{task_id}")
# async def delete_data(task_id: int):
#     return {"task_id": task_id}


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