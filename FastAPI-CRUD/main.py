from fastapi import FastAPI, HTTPException
from uuid import uuid4, UUID
from typing import List
from models import User, Gender, Role, UserUpdateRequest

app = FastAPI()

db: List[User] = [
    User(
        id = uuid4(),
        first_name = "PATROCLO",
        last_name = "KHINDASVINTO",
        nickname = "Khintroclo",
        gender = Gender.male,
        roles = [Role.superadmin, Role.admin]
    ),
    User(
        id = UUID("6008d9ca-f63e-47f0-b75e-8699105c222c"),
        first_name = "SABAS",
        last_name = "CASAS",
        nickname = "trompetrompeteroERO",
        gender = Gender.male,
        roles = [Role.admin, Role.user]
    ),
    User(
        id = UUID("6008d9ca-f63e-47f0-b75e-8699105c222b"),
        first_name = "ANA",
        last_name = "TEMPLETON",
        nickname = "annaPle",
        gender = Gender.female,
        roles = [Role.editor]
    ),
]

@app.get("/")
async def root():
    return {"message": "Hello World."}

@app.get("/api/v1/users")
async def get_users():
    return db

@app.get("/api/v1/user/{user_id}")
async def get_user_by_id(user_id: UUID):
    for user in db:
        if user.id == user_id:
            return user
    raise HTTPException(status_code=404, detail="Usuario no encontrado.")

@app.post("/api/v1/users")
async def create_user(user: User):
    db.append(user)
    return {"message": "Se ha creado un nuevo usuario correctamente."}

@app.delete("/api/v1/user/{user_id}")
async def delete_user_by_id(user_id: UUID):
    for user in db:
        if user.id == user_id:
            db.remove(user)
            return {"message": "Se ha borrado el usuario correctamente."}
    raise HTTPException(status_code=404, detail="Usuario no encontrado.")

@app.patch("/api/v1/user/{user_id}")
async def edit_user_by_id(user_update: UserUpdateRequest, user_id: UUID):
    for user in db:
        if user.id == user_id:
            if user_update.first_name is not None:
                user.first_name = user_update.first_name
            if user_update.last_name is not None:
                user.last_name = user_update.last_name
            if user_update.nickname is not None:
                user.nickname = user_update.nickname
            if user_update.roles is not None:
                user.roles = user_update.roles
            return {"message": "El usuario ha sido actualizado correctamente."}
    raise HTTPException(status_code=404, detail="Usuario no encontrado.")
