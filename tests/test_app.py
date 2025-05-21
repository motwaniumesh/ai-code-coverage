

# Auto-generated tests (2025-05-21T14:22:15.820294)
import pytest
from src.app import app

def test_get_books():
    response = app.test_client().get('/api/books')
    assert response.status_code == 200
    assert len(response.json['books']) == 3

def test_get_book_found():
    response = app.test_client().get('/api/books/1')
    assert response.status_code == 200
    assert response.json['book']['id'] == 1

def test_get_book_not_found():
    response = app.test_client().get('/api/books/10')
    assert response.status_code == 404
    assert response.json['error'] == 'Book not found'

def test_add_book():
    new_book = {"title": "New Book", "author": "New Author"}
    response = app.test_client().post('/api/books', json=new_book)
    assert response.status_code == 201
    assert 'book' in response.json

def test_add_book_bad_request():
    response = app.test_client().post('/api/books', json={})
    assert response.status_code == 400
    assert response.json['error'] == 'Bad request'

def test_update_book():
    updated_book = {"title": "Updated Title"}
    response = app.test_client().put('/api/books/1', json=updated_book)
    assert response.status_code == 200
    assert response.json['book']['title'] == 'Updated Title'

def test_update_book_not_found():
    response = app.test_client().put('/api/books/10')
    assert response.status_code == 404
    assert response.json['error'] == 'Book not found'

def test_delete_book():
    response = app.test_client().delete('/api/books/1')
    assert response.status_code == 200
    assert response.json['result'] == 'Book deleted'

def test_delete_book_not_found():
    response = app.test_client().delete('/api/books/10')
    assert response.status_code == 404
    assert response.json['error'] == 'Book not found'