

# Auto-generated tests (2025-05-21T11:30:12.753073)
import pytest
from app import app

@pytest.fixture
def client():
    with app.test_client() as client:
        yield client

def test_get_books(client):
    response = client.get('/api/books')
    assert response.status_code == 200
    assert len(response.json['books']) == 3

def test_get_book(client):
    response = client.get('/api/books/1')
    assert response.status_code == 200
    assert response.json['book']['title'] == "The Great Gatsby"

    response = client.get('/api/books/4')
    assert response.status_code == 404
    assert response.json['error'] == "Book not found"

def test_add_book(client):
    data = {"title": "NewBook", "author": "NewAuthor"}
    response = client.post('/api/books', json=data)
    assert response.status_code == 201
    assert response.json['book']['title'] == "NewBook"

def test_update_book(client):
    data = {"title": "UpdatedTitle"}
    response = client.put('/api/books/1', json=data)
    assert response.status_code == 200
    assert response.json['book']['title'] == "UpdatedTitle"

    response = client.put('/api/books/4', json=data)
    assert response.status_code == 404
    assert response.json['error'] == "Book not found"

def test_delete_book(client):
    response = client.delete('/api/books/1')
    assert response.status_code == 200
    assert response.json['result'] == "Book deleted"

    response = client.delete('/api/books/5')
    assert response.status_code == 404
    assert response.json['error'] == "Book not found"