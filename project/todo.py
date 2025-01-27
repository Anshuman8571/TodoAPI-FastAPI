from fastapi import FastAPI,Depends
from pydantic import BaseModel
from typing import Optional,List
import os
from dotenv import load_dotenv
from model import Todomodel
from database import engine
from database import Sessionlocal
from mysql import connector
from sqlalchemy.orm import Session
load_dotenv()

print(os.getenv("ANSHUMAN"))

app = FastAPI()
todos = []
Todomodel.metadata.create_all(bind = engine) # create the table in database

# List to store the todos

# class Todo(BaseModel):
#     id : int
#     title : str
#     description : Optional[str] = None
#     completed : bool = False

class TodoBase(BaseModel):
    title : str
    description : Optional[str] = None
    completed : bool = False    

class TodoCreate(TodoBase):
    pass

class TodoUpdate(TodoBase):
    pass

class TodoResponse(TodoBase):
    id:int
    class Config:
        orm_mode =True

def get_db():
    db = Sessionlocal()
    try:
        yield db
    finally:
        db.close()

@app.get("/todos",response_model=List[TodoResponse])
def get_todos(db:Session = Depends(get_db)):    
    todos = db.query(Todomodel).all()
    return todos

@app.get("/todos/{todo_id}",response_model=TodoResponse)
def get_todo(todo_id: int,db:Session = Depends(get_db)):
    # for todo in todos:
    #     if todo['id'] == todo_id:
    #         return todo
    # return {"error" : "Todo not found"}
    todo = db.query(Todomodel).filter(Todomodel.id == todo_id)
    print(todo.first())
    return todo.first()
    
@app.post("/todos",response_model=TodoResponse)
def create_todo(todo: TodoBase,db: Session = Depends(get_db)):
    db_todo = Todomodel(title=todo.title,description=todo.description,completed = todo.completed)
    db.add(db_todo)
    db.commit()
    db.refresh(db_todo)
    return db_todo

@app.delete("/todos/{todo_id}",response_model=TodoResponse)
def delete_todo(todo_id: int,db:Session = Depends(get_db)):
    # for todo in todos:
    #     if todo['id'] == todo_id:
    #         todos.remove(todo)
    #         return {"message":"Todo-deleted successfully"}
    # return {"error" : "Todo not found"}
    todo = db.query(Todomodel).filter(Todomodel.id == todo_id).first()
    db.delete(todo)
    db.commit()
    return todo
    

@app.put("/todos/{todo_id}")
def update_todo(todo_id: int,todo: TodoBase):
    for index,t in enumerate(todos):
        if t['id'] == todo_id:
            todos[index] = todo.dict()
            return {"message" : "Todo updated successfully"}
    return {"error" : "Todo not found"}