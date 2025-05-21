
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
 

# Auto-generated tests (2025-05-21T14:40:46.115895)
def test_get_all_books(client):
    response = client.get('/api/books')
    assert response.status_code == 200
    assert len(response.json["books"]) == 3

def test_get_existing_book(client):
    response = client.get('/api/books/1')
    assert response.status_code == 200
    assert response.json["book"]["title"] == "The Great Gatsby"

def test_get_non_existing_book(client):
    response = client.get('/api/books/100')
    assert response.status_code == 404
    assert response.json["error"] == "Book not found"

def test_add_new_book(client):
    new_book = {"title": "Test Book", "author": "Test Author"}
    response = client.post('/api/books', json=new_book)
    assert response.status_code == 201
    assert response.json["book"]["title"] == "Test Book"

def test_add_book_with_missing_data(client):
    new_book = {"author": "Test Author"}
    response = client.post('/api/books', json=new_book)
    assert response.status_code == 400
    assert response.json["error"] == "Bad request"

def test_update_existing_book(client):
    updated_book = {"author": "Updated Author"}
    response = client.put('/api/books/1', json=updated_book)
    assert response.status_code == 200
    assert response.json["book"]["author"] == "Updated Author"

def test_update_non_existing_book(client):
    updated_book = {"title": "Updated Title"}
    response = client.put('/api/books/100', json=updated_book)
    assert response.status_code == 404
    assert response.json["error"] == "Book not found"

def test_delete_existing_book(client):
    response = client.delete('/api/books/1')
    assert response.status_code == 200
    assert response.json["result"] == "Book deleted"

def test_delete_non_existing_book(client):
    response = client.delete('/api/books/100')
    assert response.status_code == 404
    assert response.json["error"] == "Book not found"