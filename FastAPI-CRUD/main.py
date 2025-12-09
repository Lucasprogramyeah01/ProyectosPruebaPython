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
