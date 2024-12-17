from typing import Union
from pydantic import BaseModel
from fastapi import FastAPI
from model import engine, Task as TaskModel
from sqlalchemy.orm import sessionmaker
import random
from sqlalchemy import or_, not_, and_
from sqlalchemy import func


Session = sessionmaker(bind=engine)

# create a fastapi app
app = FastAPI()

# create a task model this is handle the request and response
class Task(BaseModel):
    title: str
    description: str
    completed: bool = False

    class Config:
        from_attributes = True

class task_response(BaseModel):
    message: str
# Create a new task
@app.post("/tasks", response_model=task_response)
async def create_task(task:Task):
    db_task = TaskModel(
        title = task.title,
        description = task.description,
        completed = task.completed
    )
    with Session() as session:
        session.add(db_task)
        session.commit()
        session.refresh(db_task)
    return {"message": "Task created successfully"}

@app.get("/tasks", response_model=list[Task])
async def get_tasks():
    with Session() as session:
        tasks = session.query(TaskModel).all()
    return tasks

@app.get("/tasks/{task_id}", response_model= task_response | Task)
async def get_task(task_id:int):
    with Session() as session:
        task = session.query(TaskModel).filter(TaskModel.id == task_id).first();
        if not task:
            return {"message": "Task not found"}

        return task


@app.delete("/tasks/{task_id}", response_model= task_response)
async def delete_task(task_id : int):
    with Session() as session:
        task = session.query(TaskModel).filter(TaskModel.id == task_id).first()
        if not task:
            return {"message": "Task not found"}
        session.delete(task)
        session.commit()
        return {"message": "Task deleted successfully"}
            

@app.put("/tasks/{task_id}", response_model= task_response)
async def update_task(task_id:int, new_task:Task ):
    with Session() as session:
        task = session.query(TaskModel).filter(TaskModel.id == task_id).first()
        if not task:
            return {"message: Task not found"}
        
        task.title = new_task.title
        task.description = new_task.description
        task.completed = new_task.completed
        session.commit()
        session.refresh(task)
        return {"message": "Task updated successfully"}
