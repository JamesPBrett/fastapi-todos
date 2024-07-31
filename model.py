from typing import List, Optional
from fastapi import Form
from pydantic import BaseModel


class TodoBase(BaseModel):
    item: str

    class Config:
        schema_extra = {
            "example": {
                "item": "Example item!"
            }
        }

class TodoCreate(TodoBase):
    @classmethod
    def as_form(
        cls,
        item: str = Form(...)
    ):
        return cls(item=item)


class TodoItem(TodoBase):
    id: Optional[int] = None

    @classmethod
    def as_form(
        cls,
        item: str = Form(...)
    ):
        return cls(item=item)

    class Config:
        schema_extra = {
            "example": {
                "id": 1,
                "item": "Example item!"
            }
        }


class TodoItems(BaseModel):
    todos: List[TodoItem]

    class Config:
        schema_extra = {
            "example": {
                "todos": [
                    {
                        "id": 1,
                        "item": "Example item 1!"
                    },
                    {
                        "id": 2,
                        "item": "Example item 2!"
                    }
                ]
            }
        }
