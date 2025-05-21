

# Auto-generated tests (2025-05-21T11:53:46.760790)
def test_get_books():
    response = app.test_client().get('/api/books')
    assert response.status_code == 200
    assert response.json['books'] == books

def test_get_book():
    response = app.test_client().get('/api/books/1')
    assert response.status_code == 200
    assert response.json['book'] == {"id": 1, "title": "The Great Gatsby", "author": "F. Scott Fitzgerald"}

def test_get_book_not_found():
    response = app.test_client().get('/api/books/999')
    assert response.status_code == 404
    assert response.json['error'] == "Book not found"

def test_add_book():
    new_book_data = {"title": "New Book", "author": "New Author"}
    response = app.test_client().post('/api/books', json=new_book_data)
    assert response.status_code == 201
    assert response.json['book']['title'] == "New Book"
    assert response.json['book']['author'] == "New Author"

def test_add_book_invalid_request():
    response = app.test_client().post('/api/books', json={})
    assert response.status_code == 400
    assert response.json['error'] == "Bad request"

def test_update_book():
    updated_book_data = {"title": "Updated Title"}
    response = app.test_client().put('/api/books/1', json=updated_book_data)
    assert response.status_code == 200
    assert response.json['book']['title'] == "Updated Title"

def test_update_book_not_found():
    response = app.test_client().put('/api/books/999', json={})
    assert response.status_code == 404
    assert response.json['error'] == "Book not found"

def test_update_book_invalid_request():
    response = app.test_client().put('/api/books/1')
    assert response.status_code == 400
    assert response.json['error'] == "Bad request"

def test_delete_book():
    response = app.test_client().delete('/api/books/1')
    assert response.status_code == 200
    assert response.json['result'] == "Book deleted"

def test_delete_book_not_found():
    response = app.test_client().delete('/api/books/999')
    assert response.status_code == 404
    assert response.json['error'] == "Book not found"