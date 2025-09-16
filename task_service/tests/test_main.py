import pytest
from httpx import AsyncClient
from task_app.main import app  # import your FastAPI app

@pytest.mark.asyncio
async def test_root_endpoint():
    """Test the root endpoint for task service"""
    async with AsyncClient(app=app, base_url="http://test") as ac:
        response = await ac.get("/")
    assert response.status_code == 200
    assert "message" in response.json()

@pytest.mark.asyncio
async def test_create_task():
    """Test creating a task"""
    new_task = {
        "title": "Test Task",
        "description": "Task created from pytest"
    }
    async with AsyncClient(app=app, base_url="http://test") as ac:
        response = await ac.post("/tasks", json=new_task)
    assert response.status_code == 201
    data = response.json()
    assert data["title"] == "Test Task"
