from flask_app.config.mysqlconnection import connectToMySQL
from flask_app.models import ninja

class Dojo:
    def __init__( self , data ):
        self.id = data['id']
        self.dojo_name = data['dojo_name']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.ninjas = []
    @classmethod
    def get_all(cls):
        query = "SELECT * FROM dojos;"
        dojos_from_db= connectToMySQL('dojos_and_ninjas').query_db(query)
        all_dojos = []
        for i in dojos_from_db:
            all_dojos.append(cls(i))
        return all_dojos

    @classmethod
    def get_dojos_with_ninjas(cls,data):
        query = "select * from dojos join ninjas on dojos.id=ninjas.dojo_id where dojos.id=%(id)s;"
        results = connectToMySQL('dojos_and_ninjas').query_db( query , data )
        if len(results) == 0:
            dojos={}
        else:
            dojos = cls(results[0])
            for row_from_db in results:
                ninja_data = {
                    "id": row_from_db["ninjas.id"],
                    "first_name": row_from_db["first_name"],
                    "last_name": row_from_db["last_name"],
                    "age": row_from_db["age"],
                    "created_at" : row_from_db["ninjas.created_at"],
                    "updated_at" : row_from_db["ninjas.updated_at"]
                }
                dojos.ninjas.append(ninja.Ninja(ninja_data))
        return dojos
    
    @classmethod
    def save(cls,data):
        query = "insert into dojos (dojo_name,created_at,updated_at) values (%(dojo_name)s,now(),now());"
        connectToMySQL('dojos_and_ninjas').query_db( query, data )


