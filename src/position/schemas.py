from pydantic import BaseModel


class PositionReadSchema(BaseModel):
    id: int
    title: str
    duty: str


class PositionCreateSchema(BaseModel):
    title: str
    duty: str


class PositionUpdateSchema(BaseModel):
    title: str
    duty: str
