from fastapi import APIRouter, Path, HTTPException, status, Request, Depends, Form
from fastapi.templating import Jinja2Templates
from typing import List

from model import TodoItem, TodoItems, TodoCreate

todo_router = APIRouter()
templates = Jinja2Templates(directory="templates/")

# Shared todo list (replace with a more persistent storage solution in a real application)
todo_list: List[TodoItem] = []

@todo_router.post("/todo", response_model=TodoItem)
async def add_todo(
    request: Request,
    todo: TodoCreate = Depends(TodoCreate.as_form)
):
    new_id = len(todo_list) + 1
    new_todo = TodoItem(id=new_id, item=todo.item)
    todo_list.append(new_todo)
    return templates.TemplateResponse("todo.html", {
        "request": request,
        "todos": todo_list
    })

@todo_router.get("/todo", response_model=TodoItems)
async def retrieve_todo(
    request: Request
):
    return templates.TemplateResponse("todo.html", {
        "request": request,
        "todos": todo_list
    })

@todo_router.get("/todo/{todo_id}", response_model=TodoItem)
async def get_single_todo(
    request: Request,
    todo_id: int = Path(..., title="The ID of the todo to retrieve.")
):
    for todo in todo_list:
        if todo.id == todo_id:
            return templates.TemplateResponse("todo.html", {
                "request": request,
                "todo": todo
            })
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail="Todo with supplied ID doesn't exist",
    )

@todo_router.put("/todo/{todo_id}", response_model=dict)
async def update_todo(
    request: Request,
    todo_data: TodoCreate,
    todo_id: int = Path(..., title="The ID of the todo to be updated.")
) -> dict:
    for todo in todo_list:
        if todo.id == todo_id:
            todo.item = todo_data.item
            return {
                "message": "Todo updated successfully."
            }
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail="Todo with supplied ID doesn't exist",
    )

@todo_router.delete("/todo/{todo_id}", response_model=dict)
async def delete_single_todo(
    request: Request,
    todo_id: int
) -> dict:
    for index, todo in enumerate(todo_list):
        if todo.id == todo_id:
            todo_list.pop(index)
            return {
                "message": "Todo deleted successfully."
            }
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail="Todo with supplied ID doesn't exist",
    )

@todo_router.delete("/todo", response_model=dict)
async def delete_all_todo() -> dict:
    todo_list.clear()
    return {
        "message": "Todos deleted successfully."
    }