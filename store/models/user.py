from pydantic import BaseModel
import enum
from fastapi import Query


class Role(enum.Enum):
    admin: str = "admin"
    personal: str = "personal"


class User(BaseModel):
    name: str
    password: str
    #Validate mail format with regex, could change ... for adefault value
    mail: str = Query(..., regex="^([a-zA-Z0-9\-\.]+)@([a-zA-Z0-9\-\.]+)\.([a-zA-Z]{2,5})$")
    role: Role
