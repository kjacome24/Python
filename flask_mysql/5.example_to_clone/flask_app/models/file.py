from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash
import re ### Regular expresion

EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$') ### Regular expresion for email validation

class File: ###The name of the object should be change when new project is created.
    def __init__( self , data ):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.email = data['email']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

####simple example to create query and create objects. 
    # @classmethod
    # def get_all(cls):
    #     query = "SELECT * FROM users;"
    #     results = connectToMySQL('users_schema').query_db(query)
    #     users = []
    #     for user in results:
    #         users.append( cls(user) )
    #     return users

####example to insert data in database, this can be also for delete or update
    # @classmethod
    # def save(cls,data):
    #     query = "INSERT INTO users ( first_name , last_name , email , created_at, updated_at ) VALUES ( %(fname)s , %(lname)s , %(email)s , NOW() , NOW() );"
    #     return connectToMySQL('users_schema').query_db( query, data )

####example to get last id    
    # @classmethod
    # def last_id(cls):
    #     query = "select id from users order by id desc limit 1;"
    #     results= connectToMySQL('users_schema').query_db(query)
    #     return results

#example to query with inputs
    # @classmethod
    # def filter_email(cls,data):
    #     query = "select * from users where id=%(id)s;"
    #     results= connectToMySQL('users_schema').query_db(query,data)
    #     users = []
    #     for user in results:
    #         users.append(cls(user))
    #     return users

########example to validate entry flash
    # @staticmethod
    # def validate_entry(data):
    #     is_valid = True
    #     if len(data['fname']) <3:
    #         flash("The name should have at least 3 characters")
    #         is_valid= False
    #     if len(data['lname']) <3:
    #         flash("The name should have at least 3 characters")
    #         is_valid= False
    #     if not EMAIL_REGEX.match(data['email']): 
    #         flash("Invalid email address!")
    #         is_valid = False
    #     return is_valid