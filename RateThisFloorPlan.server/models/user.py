import uuid

from pydantic import BaseModel


class user(BaseModel):
    id: uuid.uuid4
    email: str
