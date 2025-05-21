import pytest
from src.app import app

def test_get_books(client):
    response = client.get('/api/books')
    assert response.status_code == 200
    assert len(response.json['books']) == 3