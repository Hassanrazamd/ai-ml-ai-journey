from fastapi import FastAPI, HTTPException
from pydantic import BaseModel  
from datetime import datetime


app = FastAPI(title= "My First AI Backend", version= "0.1.0")

tasks_db = []
task_id_counter = 1

class Task(BaseModel):
    title: str
    description: str = None
    done : bool = False

class TaskResponse(Task):
    id: int
    created_at: str

@app.get("/")
def root():
    return {
        "message": "Welcome to ai ml journey",
        "day": 1
    }

@app.get("/health")
def health():
    return {
        "status": "ok",
        "timestamp": datetime.utcnow().isoformat(),
        
    }

@app.post("/tasks", response_model=TaskResponse)
def create_task(task: Task):
    global task_id_counter
    new_task = TaskResponse(
        id=task_id_counter,
        created_at=datetime.utcnow().isoformat(),
        **task.model_dump(),
    )
    tasks_db.append(new_task)
    task_id_counter += 1
    return new_task


@app.get("/tasks", response_model=list[TaskResponse])
def list_tasks():
    return tasks_db

