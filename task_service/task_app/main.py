from fastapi import FastAPI
from .database import engine
from .models import Base
from .routes import router as task_router

# Create all database tables
Base.metadata.create_all(bind=engine)

# Initialize the FastAPI task_app
app = FastAPI()

# Include the task router with the specified prefix and tags
app.include_router(task_router, prefix="/tasks", tags=["tasks"])


@app.get("/")
def index():
    return {"message": "Welcome to the Task Service"}


@app.get("/callme")
def tasks():
    return {"message": "you have called me from another service"}


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(
        "task-service.task_app.main:task_app", host="127.0.0.1", port=8001, reload=True
    )
