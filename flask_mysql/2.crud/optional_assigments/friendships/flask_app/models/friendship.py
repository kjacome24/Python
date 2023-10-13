from flask_app.config.mysqlconnection import connectToMySQL
from flask_app.models import user

class Friendship:
    def __init__( self , data ):
        self.id = data['id']
        self.user_id = data['user_id']
        self.friend_id = data['friend_id']
        self.updated_at = data['updated_at']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

    @classmethod
    def new_friendship(cls,data):
        query = "insert into friendships (user_id,friend_id,created_at,updated_at) values (%(user_id)s,%(friend_id)s,now(),now());"
        return connectToMySQL('friendships_schema').query_db(query,data)
    
    @classmethod
    def check_friendship(cls,data):
        query = "select count(*) as count from friendships where user_id=%(user_id)s and friend_id=%(friend_id)s;"
        return connectToMySQL('friendships_schema').query_db(query,data)
