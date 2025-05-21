from flask import Flask, jsonify, request

# Initialize Flask app
app = Flask(__name__)

# Sample data (simulating a database)
books = [
    {"id": 1, "title": "The Great Gatsby", "author": "F. Scott Fitzgerald"},
    {"id": 2, "title": "To Kill a Mockingbird", "author": "Harper Lee"},
    {"id": 3, "title": "1984", "author": "George Orwell"}
]

# GET all books
@app.route('/api/books', methods=['GET'])
def get_books():
    return jsonify({"books": books})

# GET a specific book by ID
@app.route('/api/books/<int:book_id>', methods=['GET'])
def get_book(book_id):
    book = next((book for book in books if book["id"] == book_id), None)
    if book is None:
        return jsonify({"error": "Book not found"}), 404
    return jsonify({"book": book})

# POST a new book
@app.route('/api/books', methods=['POST'])
def add_book():
    if not request.json or 'title' not in request.json or 'author' not in request.json:
        return jsonify({"error": "Bad request"}), 400
    
    new_book = {
        "id": books[-1]["id"] + 1 if books else 1,
        "title": request.json["title"],
        "author": request.json["author"]
    }
    books.append(new_book)
    return jsonify({"book": new_book}), 201

# PUT/UPDATE a book
@app.route('/api/books/<int:book_id>', methods=['PUT'])
def update_book(book_id):
    book = next((book for book in books if book["id"] == book_id), None)
    if book is None:
        return jsonify({"error": "Book not found"}), 404
    
    if not request.json:
        return jsonify({"error": "Bad request"}), 400

    book["title"] = request.json.get("title", book["title"])
    book["author"] = request.json.get("author", book["author"])
    return jsonify({"book": book})

# DELETE a book
@app.route('/api/books/<int:book_id>', methods=['DELETE'])
def delete_book(book_id):
    book = next((book for book in books if book["id"] == book_id), None)
    if book is None:
        return jsonify({"error": "Book not found"}), 404
    
    books.remove(book)
    return jsonify({"result": "Book deleted"})

if __name__ == '__main__':
    app.run(debug=True)