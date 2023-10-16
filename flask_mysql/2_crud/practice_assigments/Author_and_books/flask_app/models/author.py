from flask_app.config.mysqlconnection import connectToMySQL
from flask_app.models import book

class Author:
    def __init__( self , data ):
        self.id = data['id']
        self.name = data['name']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.books = []

    @classmethod
    def get_all(cls):
        query = "SELECT * FROM users;"
        authors_from_db= connectToMySQL('schema_books').query_db(query)
        all_authors = []
        for i in authors_from_db:
            all_authors.append(cls(i))
        return all_authors

    @classmethod
    def get_authors_with_books(cls,data):
        query = "select * from users left join favorites on users.id=favorites.user_id left join books on favorites.book_id=books.id where users.id=%(id)s;"
        results = connectToMySQL('schema_books').query_db( query , data )
        if len(results) == 0:
            authors={}
        else:
            authors = cls(results[0])
            for row_from_db in results:
                books_data = {
                    "id": row_from_db["books.id"],
                    "title": row_from_db["title"],
                    "author": row_from_db["author"],
                    "num_pages": row_from_db["num_pages"],
                    "created_at" : row_from_db["books.created_at"],
                    "updated_at" : row_from_db["books.updated_at"]
                }
                authors.books.append(book.Book(books_data))
        return authors
    
    @classmethod
    def save(cls,data):
        query = "insert into users (name,created_at,updated_at) values (%(name)s,now(),now());"
        connectToMySQL('schema_books').query_db( query, data )

    @classmethod
    def save_favorite_in_author(cls,data):
        query = "insert into favorites (book_id,user_id) values (%(book_id)s,%(user_id)s);"
        return connectToMySQL('schema_books').query_db(query,data)