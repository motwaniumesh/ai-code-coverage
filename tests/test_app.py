

# Auto-generated tests (2025-05-21T14:25:17.604683)
def test_get_books(client):
    response = client.get('/api/books')
    assert response.status_code == 200
    assert response.json == {"books": [
        {"id": 1, "title": "The Great Gatsby", "author": "F. Scott Fitzgerald"},
        {"id": 2, "title": "To Kill a Mockingbird", "author": "Harper Lee"},
        {"id": 3, "title": "1984", "author": "George Orwell"}
    ]}

def test_get_book(client):
    response = client.get('/api/books/1')
    assert response.status_code == 200
    assert response.json == {"book": {"id": 1, "title": "The Great Gatsby", "author": "F. Scott Fitzgerald"}}
    
def test_get_book_not_found(client):
    response = client.get('/api/books/100')
    assert response.status_code == 404
    assert response.json == {"error": "Book not found"}

def test_add_book(client):
    response = client.post('/api/books', json={"title": "New Book", "author": "Anonymous"})
    assert response.status_code == 201
    assert response.json == {"book": {"id": 4, "title": "New Book", "author": "Anonymous"}}

def test_add_book_bad_request(client):
    response = client.post('/api/books', json={})
    assert response.status_code == 400
    assert response.json == {"error": "Bad request"}

def test_update_book(client):
    response = client.put('/api/books/1', json={"title": "Updated Title"})
    assert response.status_code == 200
    assert response.json == {"book": {"id": 1, "title": "Updated Title", "author": "F. Scott Fitzgerald"}}

def test_update_book_not_found(client):
    response = client.put('/api/books/100', json={"title": "Updated Title"})
    assert response.status_code == 404
    assert response.json == {"error": "Book not found"}

def test_delete_book(client):
    response = client.delete('/api/books/1')
    assert response.status_code == 200
    assert response.json == {"result": "Book deleted"}

def test_delete_book_not_found(client):
    response = client.delete('/api/books/100')
    assert response.status_code == 404
    assert response.json == {"error": "Book not found"}