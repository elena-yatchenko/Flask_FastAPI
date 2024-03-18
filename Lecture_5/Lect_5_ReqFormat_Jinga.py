# Форматирование ответов API

"""FastAPI позволяет форматировать ответы API в различных форматах, например, в
JSON или HTML. Для этого нужно использовать соответствующие функции модуля
fastapi.responses.

● HTML текст

Например:"""
from fastapi import FastAPI
from fastapi.responses import HTMLResponse

app = FastAPI()

@app.get("/", response_class=HTMLResponse)
async def read_root():
    return "<h1>Hello World</h1>"

"""Этот код создает конечную точку для корневого URL-адреса, которая возвращает
HTML-страницу с текстом "Hello World". Функция read_root() использует класс
HTMLResponse для форматирования ответа в HTML.

● JSON объект

В этом примере возвращается ответ JSON с настраиваемым сообщением и кодом
состояния
"""
from fastapi import FastAPI
from fastapi.responses import JSONResponse

app = FastAPI()

@app.get("/message")
async def read_message():
    message = {"message": "Hello World"}
    return JSONResponse(content=message, status_code=200)

"""В этом примере мы импортируем класс JSONResponse из модуля FastAPI.responses.
Внутри функции read_message мы определяем словарь, содержащий ключ
сообщения со значением «Hello World». Затем мы возвращаем объект
JSONResponse со словарем сообщений в качестве содержимого и кодом состояния
200.
"""

"""!!!
Применяются оба варианта оформления: либо объявлять response_class=HTMLResponse в маршруте, либо 
возвращать через return - JSONResponse(content=message, status_code=200). Оба варианта, и JSON, и HTML могут 
оформляться одинаково"""

# Динамический HTML через шаблонизатор Jinja

"""В следующем примере используется шаблонизация Jinja2 для создания ответа
HTML с динамическим содержимым."""

from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

app = FastAPI()
templates = Jinja2Templates(directory="templates")

@app.get("/{name}", response_class=HTMLResponse)
async def read_item(request: Request, name: str):
    return templates.TemplateResponse("item.html", {"request": request, "name": name})

"""В этом примере мы импортируем класс Jinja2Templates из модуля
FastAPI.templating. Мы создаем экземпляр этого класса и передаем каталог, в
котором расположены наши шаблоны. В функции read_item мы получаем параметр
имени из пути URL и генерируем динамический HTML-ответ, используя шаблон
Jinja2 (item.html). 

Шаблон получает объект запроса и параметр имени в качестве
переменных контекста для отображения в ответе HTML.

Простейший шаблон - item.html
"""


