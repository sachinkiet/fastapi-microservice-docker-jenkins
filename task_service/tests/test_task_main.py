from task_service.task_app.main import app
from httpx import AsyncClient, ASGITransport
import pytest

@pytest.mark.asyncio
async def test_root_endpoint():
    """Test the root endpoint for task service"""
    transport = ASGITransport(app=app)
    async with AsyncClient(transport=transport, base_url="http://test") as ac:
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
    transport = ASGITransport(app=app)
    async with AsyncClient(transport=transport, base_url="http://test") as ac:
        response = await ac.post("/tasks/", json=new_task)
    assert response.status_code in (200, 201)
    data = response.json()
    assert data["title"] == "Test Task"
