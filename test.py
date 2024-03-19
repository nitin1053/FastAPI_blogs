# test_api.py
import pytest
import requests

BASE_URL = "http://localhost:8000"  # Update with your API base URL

def test_create_blog():
    payload = {"title": "Test Blog", "content": "Test content", "tags": ["test"]}
    response = requests.post(f"{BASE_URL}/blogs/", json=payload)
    assert response.status_code == 200
    assert "message" in response.json()
    assert response.json()["message"] == "Blog created successfully"

def test_get_all_blogs():
    response = requests.get(f"{BASE_URL}/blogs/")
    assert response.status_code == 200
    assert isinstance(response.json(), list)

# Add more test functions for other endpoints

if __name__ == "__main__":
    pytest.main()
