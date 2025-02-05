# backend/models.py
from sqlalchemy import Column, Integer, String, DateTime
from database import Base
import datetime

class Schedule(Base):
    __tablename__ = "schedules"
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True)
    description = Column(String)
    scheduled_time = Column(DateTime, default=datetime.datetime.utcnow)
