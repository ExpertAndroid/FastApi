from fastapi import APIRouter, HTTPException
from pymongo import MongoClient
from bson import ObjectId
from models import Task

# Create a router instance
router = APIRouter()

# Connect to MongoDB
conn = MongoClient("mongodb+srv://shafqatullahkhan5555:b7amMWAZebkaDeZu@fluttercluster.3slffsu.mongodb.net/")
db = conn["task_management"]  # Use your database name
tasks_collection = db["tasks"]  # Use your collection name

# Define route handlers
@router.get("/tasks", response_model=list[Task])
async def read_tasks():
    docs= list(tasks_collection.find())
    print(docs)
    return docs

@router.post("/tasks", response_model=Task)
async def create_new_task(task: Task):
    result = tasks_collection.insert_one(task.dict())
    created_task = tasks_collection.find_one({"_id": result.inserted_id})
    return created_task

@router.put("/tasks/{task_id}", response_model=Task)
async def update_existing_task(task_id: str, task: Task):
    updated_task = tasks_collection.update_one({"_id": ObjectId(task_id)}, {"$set": task.dict()})
    if updated_task.modified_count == 0:
        raise HTTPException(status_code=404, detail="Task not found")
    return task

@router.delete("/tasks/{task_id}")
async def delete_existing_task(task_id: str):
    deleted_task = tasks_collection.delete_one({"_id": ObjectId(task_id)})
    if deleted_task.deleted_count == 0:
        raise HTTPException(status_code=404, detail="Task not found")
    return {"message": "Task deleted", "task_id": task_id}
