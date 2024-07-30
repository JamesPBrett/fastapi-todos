from pydantic import BaseModel
from typing import List

class Todo(BaseModel):
    id: int
    item: str
    class Config:
        json_schema_extra = {
            "example": {
                "id": 1,
                "item": "Write shopping list"
            }
        }
        
class TodoItem(BaseModel):
    item: str
    class Config:
        json_schema_extra = {
            "example": {
                "item": "Buy Biscuits"
            }
        }
class TodoItems(BaseModel):
    todos: List[TodoItem]
    class Config:
        json_schema_extra = {
            "example": {
                "todos": [
                    {
                        "item": "Buy Biscuits"
                    },
                    {
                        "item": "Buy Cucumber"
                    }
                ]
            }
        }