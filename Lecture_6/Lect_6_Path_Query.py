# Больше про валидацию данных

"""
Ранее мы рассматривали возможность указать тип для переменной, чтобы FastAPI
сделал проверку данных по типу. В начале лекции поговорили о модели данных и
возможностях pydantic.Field для валидации полей модели. Рассмотрим работу с
fastapi.Path и fastapi.Query
"""

# Проверка параметра пути через Path
"""
fastapi.Path — это класс, который используется для работы с параметрами пути
(path parameters) в URL и проверки данных. Он позволяет определять параметры
пути, которые будут передаваться в URL, а также задавать для них ограничения на
тип данных и значения.

Пример 1:
"""
from fastapi import FastAPI, Path

app = FastAPI()


@app.get("/items/{item_id}")
async def read_item(item_id: int = Path(..., ge=1), q: str = None):
    return {"item_id": item_id, "q": q}


"""
В этом примере мы создаем маршрут "/items/{item_id}" с параметром пути "item_id".
Параметр "item_id" имеет тип int и должен быть больше или равен 1. Мы используем
многоточие (...) в качестве значения по умолчанию для параметра "item_id", что
означает, что параметр обязателен для передачи в URL. Если параметр не передан
или его значение меньше 1, то будет сгенерировано исключение.

Пример 2:
"""
from fastapi import FastAPI, Path

app = FastAPI()


@app.get("/items/{item_id}")
async def read_item(
    item_id: int = Path(..., title="The ID of the item"), q: str = None
):
    return {"item_id": item_id, "q": q}


"""
В этом примере мы создаем маршрут "/items/{item_id}" с параметром пути "item_id".
Кроме ограничений на тип данных и значения, мы также задаем для параметра
"item_id" заголовок "The ID of the item". Это заголовок будет использоваться при
генерации документации API: http://127.0.0.1:8000/redoc.

Примеры демонстрируют использование fastapi.Path для работы с параметрами
пути и проверки данных. При использовании Path мы можем определять параметры
пути, задавать для них ограничения на тип данных и значения, а также указывать
заголовки для документации API.

"""
# Проверка параметра запроса через Query

"""
fastapi.Query — это класс, который используется для работы с параметрами запроса
и проверки строк. Он позволяет определять параметры запроса, которые будут
передаваться в URL, а также задавать для них ограничения на тип данных и
значения.

Пример 1
"""
from fastapi import FastAPI, Query

app = FastAPI()


@app.get("/items/")
async def read_items(q: str = Query(None, min_length=3, max_length=50)):
    results = {"items": [{"item_id": "Spam"}, {"item_id": "Eggs"}]}
    if q:
        results.update({"q": q})
    return results


"""
В этом примере мы создаем маршрут "/items/" с параметром запроса "q". Параметр
"q" имеет тип str и может быть длиной от 3 до 50 символов. Если параметр "q" не
передан в запросе, то ему будет присвоено значение None. Если же параметр "q"
передан, то его значение будет добавлено к результатам запроса.

Пример 2:
"""
from fastapi import FastAPI, Query

app = FastAPI()


@app.get("/items/")
async def read_items(q: str = Query(..., min_length=3)):
    results = {"items": [{"item_id": "Spam"}, {"item_id": "Eggs"}]}
    if q:
        results.update({"q": q})
    return results


"""
В этом примере мы создаем маршрут "/items/" с параметром запроса "q". Параметр
"q" имеет тип str и должен быть длиной не менее 3 символов. В отличие от первого
примера, здесь мы используем многоточие (...) в качестве значения по умолчанию
для параметра "q". Это означает, что параметр "q" обязателен для передачи в
запросе. Если параметр не передан, то будет сгенерировано исключение.

Примеры демонстрируют использование fastapi.Query для работы с параметрами
запроса и проверки строк. При использовании Query мы можем определять
параметры запроса, задавать для них ограничения на тип данных и значения, а
также указывать значения по умолчанию.
"""
# Общая основа в виде Param

"""
На самом деле Query, Path, Field и другие фильтры создают объекты подклассов
общего класса Param, который сам является подклассом класса FieldInfo из модуля
Pydantic. Все они возвращают объекты подкласса FieldInfo.

� Внимание! Помните, что когда вы импортируете Query, Path, и другие из
fastapi, это на самом деле функции, которые возвращают специальные
классы.

ак результат Field работает так же Query, как Path, имеет все те же параметры и т.
д. Важно лишь выбрать нужную в текущей реализации функцию
"""