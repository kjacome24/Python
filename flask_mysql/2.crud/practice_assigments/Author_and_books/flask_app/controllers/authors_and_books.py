from flask_app import app
from flask import render_template,redirect,request,session,flash
from flask_app.models.book import Book
from flask_app.models.author import Author

@app.route('/')
@app.route('/authors')
def index():
    authors = Author.get_all()
    return render_template("index.html",authors=authors)

@app.route('/authors/<int:id>')
def authors_favorites(id):
    data = {"id": id}
    authors=Author.get_authors_with_books(data)
    books = Book.get_all()
    return render_template("authors.html",authors=authors,books=books)

@app.route('/add_favorite', methods=["POST"])
def add_favorite():
    data = {
        "user_id": request.form.get("user_id"),
        "book_id": request.form.get("book_id"),
    }
    Author.save_favorite_in_author(data)
    if request.form.get("route")=='books':
        return redirect(f"/books/{data['book_id']}")
    else:
        return redirect(f"/authors/{data['user_id']}")

@app.route('/add_author', methods=["POST"])
def add_author():
    data = {
        "name": request.form.get("name"),
    }
    Author.save(data)
    return redirect('/')


@app.route('/books')
def list_books():
    books = Book.get_all()
    return render_template("index_2.html",books=books)

@app.route('/books/<int:id>')
def books_favorites(id):
    data = {"id": id}
    authors=Author.get_all()
    books = Book.get_books_with_favorites(data)
    return render_template("favoriteby.html",authors=authors,books=books)

@app.route('/add_book', methods=["POST"])
def add_book():
    data = {
        "title": request.form.get("title"),
        "num_pages": request.form.get("num_pages"),
    }
    Book.save(data)
    return redirect('/books')

