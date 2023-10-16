from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash
import re ### Regular expresion

EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$') 

class User:
    def __init__( self , data ):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.email = data['email']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
    # ahora usamos métodos de clase para consultar nuestra base de datos
    @classmethod
    def get_all(cls):
        query = "SELECT * FROM users;"
        # asegúrate de llamar a la función connectToMySQL con el esquema al que te diriges
        results = connectToMySQL('users_schema').query_db(query)
        # crear una lista vacía para agregar nuestras instancias de friends
        users = []
        # Iterar sobre los resultados de la base de datos y crear instancias de friends con cls
        for user in results:
            users.append( cls(user) )
        return users
            
    @classmethod
    def save(cls,data):
        query = "INSERT INTO users ( first_name , last_name , email , created_at, updated_at ) VALUES ( %(fname)s , %(lname)s , %(email)s , NOW() , NOW() );"
        # data es un diccionario que se pasará al método de guardar desde server.py
        return connectToMySQL('users_schema').query_db( query, data )
    
    @classmethod
    def last_id(cls):
        query = "select id from users order by id desc limit 1;"
        results= connectToMySQL('users_schema').query_db(query)
        return results
    
    @classmethod
    def filter_email(cls,data):
        query = "select * from users where id=%(id)s;"
        results= connectToMySQL('users_schema').query_db(query,data)
        users = []
        for user in results:
            users.append(cls(user))
        return users

    @classmethod
    def delete_by_user(cls,data):
        query = "delete from users where id=%(id)s;"
        return connectToMySQL('users_schema').query_db( query, data )
    
    @classmethod
    def update_user(cls,data):
        query = "UPDATE users SET first_name = %(fname)s, last_name = %(lname)s, email = %(email)s, updated_at=now() WHERE (id = %(id)s);"
        return connectToMySQL('users_schema').query_db(query,data)

    @staticmethod
    def validate_entry(data):
        is_valid = True
        if len(data['fname']) <3:
            flash("The name should have at least 3 characters")
            is_valid= False
        if len(data['lname']) <3:
            flash("The name should have at least 3 characters")
            is_valid= False
        if not EMAIL_REGEX.match(data['email']): 
            flash("Invalid email address!")
            is_valid = False
        return is_valid