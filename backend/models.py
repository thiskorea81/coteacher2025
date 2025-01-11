# backend/models.py
from pydantic import BaseModel, Field
from typing import Optional, List
from bson import ObjectId

class Schedule(BaseModel):
    id: Optional[str] = Field(alias="_id")
    title: str
    date: str
    description: Optional[str] = None

    class Config:
        allow_population_by_field_name = True
        arbitrary_types_allowed = True
        json_encoders = {
            ObjectId: str
        }

class Task(BaseModel):
    id: Optional[str] = Field(alias="_id")
    title: str
    due_date: str
    is_done: bool = False

    class Config:
        allow_population_by_field_name = True
        arbitrary_types_allowed = True
        json_encoders = {
            ObjectId: str
        }
