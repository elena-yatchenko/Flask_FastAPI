
"""
Вопросы:
1) query = users.select().where(users.c.user_id == user_id)
как из этого запроса вытащить данные user.email, к примеру. Чтобы какую-то проверку сделать, на уникальность, к примеру? 
на вход функция получает только user_id. Я бы хотела вытащить все атрибуты отфильтрованного пользователя. 
Как с этми query дальше работать?
Пробовала как result = await database.execute(query) и потом вывести по ключам, не получается. 
Ответ: 
1) Для извлечения данных пользователя по user_id, включая его email, после выполнения запроса к базе данных 
с использованием database.fetch_one(query), вы должны работать с результатом, 
который эта функция возвращает. database.execute(query) используется для выполнения запросов, 
которые не возвращают записи (например, INSERT, UPDATE, DELETE), 
в то время как database.fetch_one(query) предназначен для запросов, которые возвращают одну запись, 
и database.fetch_all(query) — для запросов, возвращающих несколько записей.

Проверка: 
@app.get("/users/{user_id}", response_model=UserGet)
async def get_user(user_id: int):
    query = users.select().where(users.c.user_id == user_id)
    data = await database.fetch_one(query)
    # data - выбранный экземпляр класса User, его атрибуты можно получать и с ними можно работать.
    # но возвращать функция должна экзепляр или список экземпляров класса, не его отдельный атрибут, иначе будет
    # ошибка {'type': 'model_attributes_type', 'loc': ('response',), 
    # 'msg': 'Input should be a valid dictionary or object to extract fields from', 
    # 'input': 'mail1@mail.ru', 'url': 'https://errors.pydantic.dev/2.6/v/model_attributes_type'}
    print(data.email)
    return data

2) Как иначе обеспечить уникальность email? атрибут unique=True не работает, создается пользователь все равно с таким же email
class UserAdd(BaseModel):
    username: str = Field(..., title="Username", max_length=32)
    surname: str = Field(title="Surname", max_length=64)
    email: EmailStr = Field(title="Email", unique=True) - здесь уникальность не нужна, она прописывается для базы данных
    password: SecretStr = Field(title="Password")

Ответ:
2) В вашем случае, атрибут unique=True в pydantic модели UserAdd не обеспечивает уникальность 
на уровне базы данных. Это лишь указание для pydantic, которое может использоваться в документации 
или валидации, но не влияет на структуру базы данных.

Чтобы обеспечить уникальность email на уровне базы данных, вам необходимо определить столбец 
email как уникальный при создании таблицы.

users = sqla.Table(
    "users",
    metadata,
    sqla.Column("user_id", sqla.Integer, primary_key=True),
    sqla.Column("username", sqla.String(32)),
    sqla.Column("surname", sqla.String(64)),
    sqla.Column("email", sqla.String(64), unique=True),
    sqla.Column("password", sqla.String),
)
"""

from typing import List, Optional
import databases
import sqlalchemy as sqla
from fastapi import FastAPI
from pydantic import BaseModel, Field, EmailStr, SecretStr
import uvicorn
from contextlib import asynccontextmanager
from enum import Enum
from datetime import date, datetime
from random import randrange, choice

DATABASE_URL = "sqlite:///questions.db"
database = databases.Database(DATABASE_URL)
metadata = sqla.MetaData()
...

@asynccontextmanager
async def lifespan(app: FastAPI):
    await database.connect()
    print("База готова")
    yield
    await database.disconnect()
    print("База очищена")


class Status(str, Enum):
    in_process = "in_process"
    done = "done"
    canceled = "canceled"

app = FastAPI(lifespan=lifespan)

items = sqla.Table(
    "items",
    metadata,
    sqla.Column("item_id", sqla.Integer, primary_key=True),
    sqla.Column("name", sqla.String(32)),
    sqla.Column("description", sqla.String(150)),
    sqla.Column("price", sqla.Integer),
    sqla.Column("is_available", sqla.BOOLEAN),
)

users = sqla.Table(
    "users",
    metadata,
    sqla.Column("user_id", sqla.Integer, primary_key=True),
    sqla.Column("username", sqla.String(32)),
    sqla.Column("surname", sqla.String(64)),
    sqla.Column("email", sqla.String(64), unique=True),
    sqla.Column("password", sqla.String),
)

orders = sqla.Table(
    "orders",
    metadata,
    sqla.Column("order_id", sqla.Integer, primary_key=True),
    sqla.Column("user_id", sqla.Integer, sqla.ForeignKey("users.user_id")),
    sqla.Column("item_id", sqla.Integer, sqla.ForeignKey("items.item_id")),
    sqla.Column("order_date", sqla.Date),
    sqla.Column("status", sqla.Enum(Status)),
)
engine = sqla.create_engine(DATABASE_URL, connect_args={"check_same_thread": False})
metadata.create_all(engine)


class UserAdd(BaseModel):
    username: str = Field(..., title="Username", max_length=32)
    surname: str = Field(title="Surname", max_length=64)
    email: EmailStr = Field(title="Email")
    password: SecretStr = Field(title="Password")


class UserGet(UserAdd):
    user_id: int = Field(title="UserID")


class ItemAdd(BaseModel):
    name: str = Field(..., title="Name", max_length=32)
    description: Optional[str] = Field(title="Description")
    price: int = Field(..., title="Price", gt=0)
    is_available: bool = Field(title="Available", default=False)


class ItemGet(ItemAdd):
    item_id: int = Field(title="ItemID")


class OrderAdd(BaseModel):
    user_id: int = Field(title="Buyer_ID")
    item_id: int = Field(title="Pruduct_ID")
    order_date: date = Field(default=datetime.now().date(), title="Order Date", gt=0)
    status: Status = Field(title="Status of Order")
    # order_list: Optional[List[ItemGet]] = Field(title="List of Orders")


class OrderGet(OrderAdd):
    order_id: int = Field(title="Order_ID")


@app.get("/")
async def root():
    return "Hello"


# ОПЕРАЦИИ С ПОЛЬЗОВАТЕЛЯМИ
"""
database.fetch_one(query)
database.fetch_all(query)
"""

@app.get("/users/", response_model=List[UserGet])
async def get_users():
    query = users.select()
    return await database.fetch_all(query)


@app.get("/users/{user_id}", response_model=UserGet)
async def get_user(user_id: int):
    query = users.select().where(users.c.user_id == user_id)
    return await database.fetch_one(query)


@app.post("/users/", response_model=UserGet)
async def create_user(user: UserAdd):
    query = users.insert().values(
        username=user.username,
        surname=user.surname,
        email=user.email,
        password=user.password.get_secret_value(),
    )
    current_id = await database.execute(query)
    return {**user.model_dump(), "user_id": current_id}


@app.put("/users/{user_id}", response_model=UserGet)
async def update_user(user_id: int, new_user: UserAdd):
    query = (
        users.update()
        .where(users.c.user_id == user_id)
        .values(
            username=new_user.username,
            surname=new_user.surname,
            email=new_user.email,
            password=new_user.password.get_secret_value(),
        )
    )
    await database.execute(query)
    return {**new_user.model_dump(), "user_id": user_id}


@app.delete("/users/{user_id}")
async def delete_user(user_id: int):
    query = users.delete().where(users.c.user_id == user_id)
    await database.execute(query)
    return {"message": f"User id = {user_id} deleted"}


# ОПЕРАЦИИ С ТОВАРАМИ


@app.get("/items/", response_model=List[ItemGet])
async def get_items():
    query = items.select()
    return await database.fetch_all(query)


@app.get("/items/{item_name}", response_model=ItemGet)
async def get_item(item_name: str):
    query = items.select().where(items.c.name == item_name)
    return await database.fetch_one(query)


@app.post("/items/", response_model=ItemGet)
async def create_item(item: ItemAdd):
    query = items.insert().values(
        name=item.name,
        description=item.description,
        price=item.price,
        is_available=item.is_available,
    )
    current_id = await database.execute(query)
    return {**item.model_dump(), "item_id": current_id}


@app.put("/items/{item_id}", response_model=ItemGet)
async def update_item(item_id: int, new_item: ItemAdd):
    query = (
        items.update().where(items.c.item_id == item_id).values(**new_item.model_dump())
    )
    await database.execute(query)
    return {**new_item.model_dump(), "item_id": item_id}


@app.delete("/items/{item_id}")
async def delete_item(item_id: int):
    query = items.delete().where(items.c.item_id == item_id)
    await database.execute(query)
    return {"message": f"Product id = {item_id} deleted"}


# ОПЕРАЦИИ С ЗАКАЗАМИ


@app.get("/orders/", response_model=List[OrderGet])
async def get_orders():
    query = orders.select()
    return await database.fetch_all(query)


@app.get("/orders/{order_id}", response_model=OrderGet)
async def get_order(order_id: int):
    query = orders.select().where(orders.c.order_id == order_id)

    return await database.fetch_one(query)


@app.post("/orders/", response_model=OrderGet)
async def create_order(order: OrderAdd):
    query = orders.insert().values(
        user_id=order.user_id,
        item_id=order.user_id,
        order_date=order.order_date,
        status=order.status,
    )
    current_id = await database.execute(query)
    return {**order.model_dump(), "order_id": current_id}


"""
for key in database.fetch_one(query)
for user in database.fetch_all(query)
"""

@app.put("/orders/{order_id}", response_model=OrderGet)
async def update_order(order_id: int, new_order: OrderAdd):
    query = (
        orders.update()
        .where(orders.c.order_id == order_id)
        .values(**new_order.model_dump())
    )
    await database.execute(query)
    return {**new_order.model_dump(), "order_id": order_id}


@app.delete("/orders/{order_id}")
async def delete_order(order_id: int):
    query = orders.delete().where(orders.c.order_id == order_id)
    await database.execute(query)
    return {"message": f"Product id = {order_id} deleted"}


@app.get("/fake_data/")
async def create_note():
    for i in range(5):
        query = users.insert().values(
            username=f"user{i}",
            surname=f"surname{i}",
            email=f"mail{i}@mail.ru",
            password=f"123456_{i}",
        )
        await database.execute(query)

    for i in range(10):
        query = items.insert().values(
            name=f"name_00{i}",
            description=f"{'d'*i}",
            price=randrange(100, 2000, 100),
            is_available=choice([True, False]),
        )
        await database.execute(query)

    for i in range(7):
        query = orders.insert().values(
            user_id=choice(range(1, 6)),
            item_id=choice(range(1, 11)),
            order_date=datetime.now().date(),
            status=choice([Status.in_process, Status.done, Status.canceled]),
        )
        await database.execute(query)

    return {"Data base is created"}


# app = FastAPI()
# class Item(BaseModel):
# name: str
# price: float
# is_offer: bool = None
# class User(BaseModel):
# username: str
# full_name: str = None
# class Order(BaseModel):
# items: List[Item]
# user: User

if __name__ == "__main__":
    uvicorn.run("HW_6_questions:app", host="127.0.0.1", port=8000)
