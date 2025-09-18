import httpx
from fastapi import FastAPI
from . import database
from . import models
from .routes import router as user_router

# Create all database tables
models.Base.metadata.create_all(bind=database.engine)

# Initialize the FastAPI task_app
app = FastAPI()

# Include the task router with the specified prefix and tags
app.include_router(user_router, prefix="/users", tags=["users"])


@app.get("/")
def index():
    return {"message": "Welcome to the user Service"}


@app.get("/call-task-service")
async def call_task_service():
    async with httpx.AsyncClient() as client:
        response = await client.get("http://task_service:8001/tasks")
    return {"message": response.json()}


if __name__ == "__main__":
    import uvicorn

    uvicorn.run("user_service.user_app.main:app", host="127.0.0.1", port=8002, reload=True)
