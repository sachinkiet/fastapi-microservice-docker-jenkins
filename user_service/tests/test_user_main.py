import uuid
import pytest
from httpx import AsyncClient, ASGITransport
from user_service.user_app.main import (
    app,
)  # or from task_service.task_app.main import app


@pytest.mark.asyncio
async def test_root_endpoint():
    """Test the root or health-check endpoint"""
    transport = ASGITransport(app=app)  # use ASGITransport
    async with AsyncClient(transport=transport, base_url="http://test") as ac:
        response = await ac.get("/")
    assert response.status_code == 200


@pytest.mark.asyncio
async def test_create_user():
    new_user = {
        "username": f"Sachin_{uuid.uuid4()}",
        "email": f"sachin_{uuid.uuid4()}@example.com",
        "full_name": "Sachin Shukla",
    }
    transport = ASGITransport(app=app)
    async with AsyncClient(transport=transport, base_url="http://test") as ac:
        response = await ac.post("/users/", json=new_user)
    assert response.status_code in (200, 201)
