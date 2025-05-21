
import pytest

import os

from unittest.mock import MagicMock  

from src.app import app;

from flask import json
 
@pytest.fixture

def client():

    app.config['TESTING'] = True

    with app.test_client() as client:

        yield client
 

# Auto-generated tests (2025-05-21T15:15:28.233838)
def test_get_books():
    response = app.test_client().get('/api/books')
    assert response.status_code == 200
    assert len(response.json['books']) == 3

def test_get_book_found():
    response = app.test_client().get('/api/books/1')
    assert response.status_code == 200
    assert response.json['book']['title'] == 'The Great Gatsby'
    assert response.json['book']['author'] == 'F. Scott Fitzgerald'

def test_get_book_not_found():
    response = app.test_client().get('/api/books/10')
    assert response.status_code == 404
    assert response.json['error'] == 'Book not found'

def test_add_book():
    response = app.test_client().post('/api/books', json={"title": "New Book", "author": "New Author"})
    assert response.status_code == 201
    assert response.json['book']['title'] == 'New Book'
    assert response.json['book']['author'] == 'New Author'

def test_add_book_bad_request():
    response = app.test_client().post('/api/books', json={})
    assert response.status_code == 400
    assert response.json['error'] == 'Bad request'

def test_update_book():
    response = app.test_client().put('/api/books/1', json={"title": "Updated Title"})
    assert response.status_code == 200
    assert response.json['book']['title'] == 'Updated Title'

def test_update_book_not_found():
    response = app.test_client().put('/api/books/10', json={"title": "Updated Title"})
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