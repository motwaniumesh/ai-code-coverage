

# Auto-generated tests (2025-05-21T11:50:13.484903)
def test_get_books(client):
    response = client.get('/api/books')
    assert response.status_code == 200
    assert "books" in response.json

def test_get_book(client):
    response = client.get('/api/books/1')
    assert response.status_code == 200
    assert "book" in response.json

def test_get_book_nonexistent(client):
    response = client.get('/api/books/999')
    assert response.status_code == 404
    assert "error" in response.json

def test_add_book(client):
    new_book = {"title": "New Book", "author": "Author Name"}
    response = client.post('/api/books', json=new_book)
    assert response.status_code == 201
    assert "book" in response.json

def test_add_book_bad_request(client):
    response = client.post('/api/books', json={})
    assert response.status_code == 400
    assert "error" in response.json

def test_update_book(client):
    updated_book = {"title": "Updated Title", "author": "Updated Author"}
    response = client.put('/api/books/1', json=updated_book)
    assert response.status_code == 200
    assert "book" in response.json

def test_update_book_nonexistent(client):
    response = client.put('/api/books/999', json={})
    assert response.status_code == 404
    assert "error" in response.json

def test_delete_book(client):
    response = client.delete('/api/books/1')
    assert response.status_code == 200
    assert "result" in response.json