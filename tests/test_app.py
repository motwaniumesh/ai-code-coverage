

# Auto-generated tests (2025-05-21T14:11:32.286023)
# test_app.py

from src.app import app
import pytest

@pytest.fixture
def client():
    with app.test_client() as client:
        yield client

def test_get_books(client):
    response = client.get('/api/books')
    assert response.status_code == 200
    assert "books" in response.json

def test_get_book(client):
    response = client.get('/api/books/1')
    assert response.status_code == 200
    assert "book" in response.json

    response = client.get('/api/books/10')
    assert response.status_code == 404
    assert "error" in response.json

def test_add_book(client):
    data = {
        "title": "New Book",
        "author": "Author Name"
    }
    response = client.post('/api/books', json=data)
    assert response.status_code == 201
    assert "book" in response.json

def test_update_book(client):
    data = {
        "title": "Updated Book Title"
    }
    response = client.put('/api/books/1', json=data)
    assert response.status_code == 200
    assert "book" in response.json
    assert response.json["book"]["title"] == "Updated Book Title"

    response = client.put('/api/books/10', json=data)
    assert response.status_code == 404
    assert "error" in response.json

def test_delete_book(client):
    response = client.delete('/api/books/1')
    assert response.status_code == 200
    assert "result" in response.json

    response = client.delete('/api/books/10')
    assert response.status_code == 404
    assert "error" in response.json