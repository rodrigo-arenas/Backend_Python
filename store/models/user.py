from pydantic import BaseModel
import enum


class Role(enum.Enum):
    admin = "admin"
    personal = "personal"


class Users(BaseModel):
    name: str
    password: str
    mail: str
    role: Role


