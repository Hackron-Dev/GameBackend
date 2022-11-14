import hashlib

from fastapi import FastAPI

from SqlAlchemy import users, conn
from schemas import User_

app = FastAPI()


# Сделать запрос о добавление  user Done
# Сделать запрос о получение  user score
# Сделать запрос о редактирование cash user


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.post("/user/register")
async def create_user(user: User_):
    check_register = conn.execute(users.select().where(users.c.Login == user.Login_)).fetchone()
    hash_password = hashlib.md5(user.Password_.encode()).hexdigest()
    if check_register:
        return {"message": "User already exist"}
    else:
        insLogin = users.insert().values(Login=user.Login_, Hash_Password=hash_password)
        conn.execute(insLogin)
        return {"message": "User created"}


@app.post("/user/login/")
async def create_user(user: User_):
    check_login = conn.execute(users.select().where(users.c.Login == user.Login_)).fetchone()
    if check_login:
        check_password = conn.execute(users.select().where(users.c.Hash_Password == user.Password_)).fetchone()
        if check_password:
            return {"message": "User login"}
    else:
        return {"message": "User is not exist"}


@app.get("/user/get_score/{Login}")
async def get_user_score(Login: str):
    check_login = conn.execute(users.select().where(users.c.Login == Login)).fetchone()
    if check_login:
        return {"message": Login, "score": check_login.Score}
    else:
        return {"message": "User does not exist"}
