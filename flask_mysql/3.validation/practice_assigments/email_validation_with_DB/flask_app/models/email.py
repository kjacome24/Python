from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash
import re ### Regular expresion

EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$') ### Regular expresion for email validation

class Email: ###The name of the object should be change when new project is created.
    def __init__( self , data ):
        self.id = data['id']
        self.emails = data['emails']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
    @classmethod####simple example to create query and create objects. 
    def get_all(cls):
        query = "SELECT * FROM emails order by id desc"
        results = connectToMySQL('emails_schema').query_db(query)
        emails = []
        for user in results:
            emails.append( cls(user) )
        return emails
    @classmethod####example to insert data in database, this can be also for delete or update
    def save(cls,data):
        query = "INSERT INTO emails (emails,created_at,updated_at ) VALUES (%(email)s , NOW() , NOW() );"
        return connectToMySQL('emails_schema').query_db( query, data )
    @classmethod
    def delete_by_user(cls,data):
        query = "delete from emails where id=%(id)s;"
        return connectToMySQL('emails_schema').query_db( query, data )

    @staticmethod########example to validate entry flash
    def validate_entry(data):
        is_valid = True
        if not EMAIL_REGEX.match(data['email']): 
            flash(["Email is not valid!","red"])
            is_valid = False
        else:
            query = "select count(*) as count from emails where emails=%(email)s;"
            x= connectToMySQL('emails_schema').query_db( query, data )
            if x[0]['count']>0:
                flash(["FLASHHHH!!!!! AHHH. EMail already taken","red"])

                is_valid = False
            else:
                flash(["The email addess you entered is a VALID email address! THank you!","green"])
        return is_valid








