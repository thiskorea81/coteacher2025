# backend/routers/schedules.py
from fastapi import APIRouter, HTTPException
from ..database import db
from ..models import Schedule
from bson import ObjectId

router = APIRouter()

@router.get("/")
async def get_schedules():
    schedules = []
    cursor = db["schedules"].find()
    async for schedule in cursor:
        schedules.append(Schedule(**schedule))
    return schedules

@router.get("/{schedule_id}")
async def get_schedule(schedule_id: str):
    schedule = await db["schedules"].find_one({"_id": ObjectId(schedule_id)})
    if schedule:
        return Schedule(**schedule)
    raise HTTPException(status_code=404, detail="Schedule not found")

@router.post("/")
async def create_schedule(schedule: Schedule):
    result = await db["schedules"].insert_one(schedule.dict(by_alias=True))
    return {"inserted_id": str(result.inserted_id)}

@router.put("/{schedule_id}")
async def update_schedule(schedule_id: str, schedule: Schedule):
    result = await db["schedules"].update_one(
        {"_id": ObjectId(schedule_id)},
        {"$set": schedule.dict(by_alias=True, exclude={"id"})}
    )
    if result.matched_count:
        return {"msg": "Schedule updated"}
    raise HTTPException(status_code=404, detail="Schedule not found")

@router.delete("/{schedule_id}")
async def delete_schedule(schedule_id: str):
    result = await db["schedules"].delete_one({"_id": ObjectId(schedule_id)})
    if result.deleted_count:
        return {"msg": "Schedule deleted"}
    raise HTTPException(status_code=404, detail="Schedule not found")
