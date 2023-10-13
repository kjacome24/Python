from flask_app.config.mysqlconnection import connectToMySQL
from flask_app.models import author

class Book:
    def __init__( self , data ):
        self.id = data['id']
        self.title = data['title']
        self.author = data['author']
        self.num_pages = data['num_pages']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.authors = []

    @classmethod
    def get_all(cls):
        query = "SELECT * FROM books;"
        books_from_db= connectToMySQL('schema_books').query_db(query)
        all_books = []
        for i in books_from_db:
            all_books.append(cls(i))
        return all_books

    @classmethod
    def get_books_with_favorites(cls,data):
        query = "select * from books left join favorites on favorites.book_id=books.id left join users on users.id=favorites.user_id  where books.id=%(id)s;"
        results = connectToMySQL('schema_books').query_db( query , data )
        if len(results) == 0:
            books={}
        else:
            books = cls(results[0])
            for row_from_db in results:
                books_data = {
                    "id": row_from_db["users.id"],
                    "name": row_from_db["name"],
                    "created_at" : row_from_db["users.created_at"],
                    "updated_at" : row_from_db["users.updated_at"]
                }
                books.authors.append(author.Author(books_data))
        return books
    
    @classmethod
    def save(cls,data):
        query = "insert into books (title,author,num_pages,created_at,updated_at) values (%(title)s,'NA',%(num_pages)s,now(),now());"
        connectToMySQL('schema_books').query_db( query, data )