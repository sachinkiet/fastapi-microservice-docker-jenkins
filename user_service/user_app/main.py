from fastapi import FastAPI

from . import database
from .routes import router as user_router
from . import models
import httpx

# Create all database tables
models.Base.metadata.create_all(bind=database.engine)

# Initialize the FastAPI task_app
app = FastAPI()

# Include the task router with the specified prefix and tags
app.include_router(user_router, prefix="/users", tags=["users"])


@app.get("/")
def read_root():
    return {"message": "Welcome to the user Service"}
    
@app.get("/call-task-service")
async def read_root():
    async with httpx.AsyncClient() as client:
        response = await client.get("http://task_service:8001/tasks")
    return {"task_response": response.json()}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("user_service.user_app.main:app", host="127.0.0.1", port=8002, reload=True)
