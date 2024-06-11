from pydantic import BaseModel

class UserReadSchema(BaseModel):
    id: int
    name: str
    age: str
    email: str
    address: str


class UserCreateSchema(BaseModel):
    name: str
    age: str
    email: str
    address: str
    password: str
