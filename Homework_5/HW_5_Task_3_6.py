# Создайте API: модуль приложения и настройте сервер и маршрутизацию.
# Создайте класс User с полями id, name, email и password.
# Создайте список users для хранения пользователей.
# Создайте маршрут для добавления нового пользователя (метод POST).
# Создайте маршрут для обновления информации о пользователе (метод PUT)
# Создайте маршрут для удаления информации о пользователе (метод DELETE).
# Реализуйте валидацию данных запроса и ответа.

# Создать веб-страницу для отображения списка пользователей. Приложение
# должно использовать шаблонизатор Jinja для динамического формирования HTML
# страницы.
# Создайте HTML шаблон для отображения списка пользователей. Шаблон должен
# содержать заголовок страницы, таблицу со списком пользователей и кнопку для
# добавления нового пользователя.
# Создайте маршрут для отображения списка пользователей (метод GET).
# Реализуйте вывод списка пользователей через шаблонизатор Jinja.

from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

from typing import Optional
from pydantic import BaseModel
from random import choice
import uvicorn
import string

app = FastAPI()
templates = Jinja2Templates(directory='Homework_5\\templates')

class User(BaseModel):
    id: int
    name: str
    email: str
    password: str


users = []
for i in range(1, 6):
    id = i
    name = "name_" + str(i)
    email = str(i) + "00" + "@ya.ru"
    password = "".join(
        choice(string.ascii_lowercase + string.ascii_uppercase) for _ in range(6)
    )
    data = {"id": id, "name": name, "email": email, "password": password}
    user = User(**data)
    users.append(user)
#print(users)
    
@app.get("/")
async def root():
    return users

@app.get("/{page_name}", response_class=HTMLResponse)
async def read_list(request: Request, page_name: str):
    return templates.TemplateResponse('users.html', {'request': request, 'page_name': page_name, 'data': users})


# @app.get("/data/")
# async def user_data():
# шаблон HTML
#     return {"task_list": tasks}


@app.post("/users/")
async def create_user(user: User):
    users.append(user)
    return user


@app.put("/users/{id}")
async def updating(id: int, user: User):
    for i in range(len(users)):
        if users[i].id == id:
            users[i] = user
    return user


@app.delete("/users/{id}")
async def delete_user(id: int):
    for user in users:
        if user.id == id:
            users.remove(user)
    return {"deleted_id": id, "users": users}


if __name__ == "__main__":
    uvicorn.run("HW_5_Task_3_6:app", host="127.0.0.1", port=8000)
