

# Auto-generated tests (2025-05-21T11:46:11.909058)
# test_get_all_books
def test_get_all_books(client):
    response = client.get('/api/books')
    assert response.status_code == 200
    assert len(response.json['books']) == 3

# test_get_book_existing
def test_get_book_existing(client):
    response = client.get('/api/books/1')
    assert response.status_code == 200
    assert response.json['book']['id'] == 1

# test_get_book_not_found
def test_get_book_not_found(client):
    response = client.get('/api/books/10')
    assert response.status_code == 404
    assert response.json['error'] == 'Book not found'

# test_add_book
def test_add_book(client):
    new_book = {"title": "New Book", "author": "New Author"}
    response = client.post('/api/books', json=new_book)
    assert response.status_code == 201
    assert response.json['book']['title'] == 'New Book'

# test_add_book_missing_fields
def test_add_book_missing_fields(client):
    response = client.post('/api/books', json={})
    assert response.status_code == 400
    assert response.json['error'] == 'Bad request'

# test_update_book
def test_update_book(client):
    updated_book = {"title": "Updated Title"}
    response = client.put('/api/books/1', json=updated_book)
    assert response.status_code == 200
    assert response.json['book']['title'] == 'Updated Title'

# test_update_book_not_found
def test_update_book_not_found(client):
    response = client.put('/api/books/10', json={})
    assert response.status_code == 404
    assert response.json['error'] == 'Book not found'

# test_delete_book
def test_delete_book(client):
    response = client.delete('/api/books/2')
    assert response.status_code == 200
    assert response.json['result'] == 'Book deleted'

# test_delete_book_not_found
def test_delete_book_not_found(client):
    response = client.delete('/api/books/10')
    assert response.status_code == 404
    assert response.json['error'] == 'Book not found'