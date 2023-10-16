from flask_app.config.mysqlconnection import connectToMySQL

class Ninja:
    def __init__( self , data ):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.age = data['age']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
    @classmethod
    def new_ninja(cls,data):
        query = "insert into ninjas (first_name,last_name,age,created_at,updated_at,dojo_id) values (%(fname)s , %(lname)s , %(age)s,now(),now(),%(dojo_id)s);" 
        return connectToMySQL('dojos_and_ninjas').query_db( query, data )