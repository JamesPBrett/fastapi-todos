from pydantic import BaseModel

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