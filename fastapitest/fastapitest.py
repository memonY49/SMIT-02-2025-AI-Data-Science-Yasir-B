from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()


todos = []


class Todo(BaseModel):
    id: int
    title: str
    completed: bool = False


# 1. Root API
@app.get("/")
def read_root():
    return {"message": "Welcome to Todo API"}


# 2. Get all todos
@app.get("/todos")
def get_todos():
    return todos


# 3. Get single todo by ID
@app.get("/todos/{todo_id}")
def get_todo(todo_id: int):
    for todo in todos:
        if todo["id"] == todo_id:
            return todo
    raise HTTPException(status_code=404, detail="Todo not found")


# 4. Create new todo
@app.post("/todos")
def create_todo(todo: Todo):
    todos.append(todo.dict())
    return {"message": "Todo added", "todo": todo}


# 5. Update todo
@app.put("/todos/{todo_id}")
def update_todo(todo_id: int, updated_todo: Todo):
    for index, todo in enumerate(todos):
        if todo["id"] == todo_id:
            todos[index] = updated_todo.dict()
            return {"message": "Todo updated"}
    raise HTTPException(status_code=404, detail="Todo not found")


# 6. Delete todo
@app.delete("/todos/{todo_id}")
def delete_todo(todo_id: int):
    for index, todo in enumerate(todos):
        if todo["id"] == todo_id:
            todos.pop(index)
            return {"message": "Todo deleted"}
    raise HTTPException(status_code=404, detail="Todo not found")