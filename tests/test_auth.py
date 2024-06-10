from fastapi.testclient import TestClient
from app.main import app

# Create a test client
client = TestClient(app)

def test_signup():
    """
    Test user signup endpoint.
    """
    response = client.post("/auth/signup", json={"email": "test@example.com", "password": "password123"})
    assert response.status_code == 200
    assert response.json()["email"] == "test@example.com"

def test_login():
    """
    Test user login endpoint.
    """
    response = client.post("/auth/login", json={"email": "test@example.com", "password": "password123"})
    assert response.status_code == 200
    assert "access_token" in response.json()
