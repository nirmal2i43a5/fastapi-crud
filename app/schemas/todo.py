
from pydantic import BaseModel
from datetime import datetime

# Shared properties
class ItemBase(BaseModel):
    title: str
    description: str


class ItemCreate(ItemBase):
    pass

class ItemUpdate(ItemBase):
    pass


# For reading item we need all attributes
class ItemRead(ItemBase):
    id: int

    class Config:
        orm_mode = True#use same rules as sqlalchemy