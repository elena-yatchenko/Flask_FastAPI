from pydantic import BaseModel
from random import choice
import uvicorn
import string

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

print(users)

for key in users[0]:
    print(key[0])