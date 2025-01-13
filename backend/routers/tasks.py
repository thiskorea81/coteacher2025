# backend/routers/tasks.py

from fastapi import APIRouter, Depends, HTTPException
from pydantic import BaseModel
from sqlalchemy.orm import Session
from ..database import SessionLocal
from ..models import Task

router = APIRouter()

# Pydantic 스키마
class TaskCreate(BaseModel):
    title: str
    description: str
    is_done: bool = False

# FastAPI의 의존성(dependency)으로 DB 세션 관리
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.get("/")
def read_tasks(db: Session = Depends(get_db)):
    tasks = db.query(Task).all()
    return tasks

@router.get("/{task_id}")
def read_task(task_id: int, db: Session = Depends(get_db)):
    task = db.query(Task).filter(Task.id == task_id).first()
    if not task:
        raise HTTPException(status_code=404, detail="Task not found")
    return task

@router.post("/")
def create_task(task_data: TaskCreate, db: Session = Depends(get_db)):
    new_task = Task(
        title=task_data.title,
        description=task_data.description,
        is_done=task_data.is_done
    )
    db.add(new_task)
    db.commit()
    db.refresh(new_task)  # INSERT 후 새로고침하여 PK 등 획득
    return {"inserted_id": new_task.id}

@router.put("/{task_id}")
def update_task(task_id: int, task_data: TaskCreate, db: Session = Depends(get_db)):
    task = db.query(Task).filter(Task.id == task_id).first()
    if not task:
        raise HTTPException(status_code=404, detail="Task not found")
    task.title = task_data.title
    task.description = task_data.description
    task.is_done = task_data.is_done
    db.commit()
    db.refresh(task)
    return {"msg": "Task updated"}

@router.delete("/{task_id}")
def delete_task(task_id: int, db: Session = Depends(get_db)):
    task = db.query(Task).filter(Task.id == task_id).first()
    if not task:
        raise HTTPException(status_code=404, detail="Task not found")
    db.delete(task)
    db.commit()
    return {"msg": "Task deleted"}
