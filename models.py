from pydantic import BaseModel, Field
from enum import Enum
from typing import List

class TaskStatus(str, Enum):
    todo = "To Do"
    in_progress = "In Progress"
    completed = "Completed"

class Task(BaseModel):
    title: str
    description: str
    status: TaskStatus

class UserRole(str, Enum):
    admin = "Admin"
    manager = "Manager"
    user = "User"

class Permission(BaseModel):
    name: str
    description: str

class Role(BaseModel):
    name: str
    description: str
    permissions: List[Permission] = []

class User(BaseModel):
    username: str
    email: str
    hashed_password: str
    role: UserRole = Field(default=UserRole.user, title="User Role")
    disabled: bool = False
