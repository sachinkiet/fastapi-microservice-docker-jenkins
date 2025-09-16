import pytest
from httpx import AsyncClient
from user_app.main import app  # import your FastAPI app

@pytest.mark.asyncio
async def test_root_endpoint():
    """Test the root or health-check endpoint"""
    async with AsyncClient(app=app, base_url="http://test") as ac:
        response = await ac.get("/")
    assert response.status_code == 200
    assert "message" in response.json()

@pytest.mark.asyncio
async def test_create_user():
    """Test creating a user"""
    new_user = {
        "name": "Sachin",
        "email": "sachin@example.com"
    }
    async with AsyncClient(app=app, base_url="http://test") as ac:
        response = await ac.post("/users", json=new_user)
    assert response.status_code == 201
    data = response.json()
    assert data["name"] == "Sachin"
    assert data["email"] == "sachin@example.com"
