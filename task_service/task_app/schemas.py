from pydantic import BaseModel


# Define the TaskCreate schema
class TaskCreate(BaseModel):
    title: str
    description: str


# Define the Task schema
class Task(BaseModel):
    id: int
    title: str
    description: str

    class Config:
        from_attributes = True  # Enable ORM mode to work with SQLAlchemy models