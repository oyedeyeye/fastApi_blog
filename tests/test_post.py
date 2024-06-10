from fastapi.testclient import TestClient
from app.main import app

# Create a test client
client = TestClient(app)

def test_add_post():
    """
    Test add post endpoint.
    """
    login_response = client.post("/auth/login", json={"email": "test@example.com", "password": "password123"})
    token = login_response.json()["access_token"]
    headers = {"Authorization": f"Bearer {token}"}
    response = client.post("/posts/addpost", json={"text": "My first post"}, headers=headers)
    assert response.status_code == 200
    assert response.json()["text"] == "My first post"

def test_get_posts():
    """
    Test get posts endpoint.
    """
    login_response = client.post("/auth/login", json={"email": "test@example.com", "password": "password123"})
    token = login_response.json()["access_token"]
    headers = {"Authorization": f"Bearer {token}"}
    response = client.get("/posts/getposts", headers=headers)
    assert response.status_code == 200
    assert isinstance(response.json(), list)

def test_delete_post():
    """
    Test delete post endpoint.
    """
    login_response = client.post("/auth/login", json={"email": "test@example.com", "password": "password123"})
    token = login_response.json()["access_token"]
    headers = {"Authorization": f"Bearer {token}"}
    add_post_response = client.post("/posts/addpost", json={"text": "Post to be deleted"}, headers=headers)
    post_id = add_post_response.json()["id"]
    delete_response = client.delete(f"/posts/deletepost/{post_id}", headers=headers)
    assert delete_response.status_code == 200
    assert delete_response.json()["detail"] == "Post deleted"
