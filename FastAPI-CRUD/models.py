from enum import Enum
from typing import Optional, List
from uuid import UUID, uuid4
from pydantic import BaseModel

class Gender(str, Enum):
    male = "MALE"
    female = "FEMALE"
    other = "OTHER"

class Role(str, Enum):
    superadmin = "SUPERADMIN"
    admin = "ADMIN"
    editor = "EDITOR"
    user = "USER"

class User(BaseModel):
    id: Optional[UUID] = uuid4()
    first_name: str
    last_name: str
    nickname: Optional[str]
    gender: Gender
    roles: List[Role]

class UserUpdateRequest(BaseModel):
    first_name: Optional[str] = None
    last_name: Optional[str] = None
    nickname: Optional[str] = None

