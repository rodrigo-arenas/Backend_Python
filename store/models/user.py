from pydantic import BaseModel
import enum


class Role(enum.Enum):
    admin = "admin"
    personal = "personal"


class User(BaseModel):
    name: str
    password: str
    mail: str
    role: Role


