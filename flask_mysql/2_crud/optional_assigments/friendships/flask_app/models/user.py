from flask_app.config.mysqlconnection import connectToMySQL
from flask_app.models import friendship

class User:
    
    def __init__( self , data ):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.friends = []

    @classmethod
    def get_all(cls):
        query = "select * from users;"
        users_from_db= connectToMySQL('friendships_schema').query_db(query)
        all_users = []
        for i in users_from_db:
            all_users.append(cls(i))
        return all_users
    
    @classmethod
    def save(cls,data):
        query = "insert into users (first_name,last_name,created_at,updated_at) values (%(first_name)s,%(last_name)s,now(),now());"
        connectToMySQL('friendships_schema').query_db( query, data )

    @classmethod
    def get_users_with_friends(cls):
        query = "select * from users as t1 join friendships as t2 on t1.id=t2.user_id join users as t3 on t2.friend_id=t3.id order by t1.id;"
        results= connectToMySQL('friendships_schema').query_db(query)
        all_users = []
        for row_from_db in results:
            if 'user_data' in locals():
                if row_from_db["id"]==user_data["id"]:
                    user_data = {"id": row_from_db["id"]}
                    friends_data ={"id": row_from_db["t3.id"],
                                "first_name": row_from_db["t3.first_name"],
                                "last_name": row_from_db["t3.last_name"],
                                "created_at": row_from_db["t3.created_at"],
                                "updated_at": row_from_db["t3.updated_at"],
                                }
                    all_users[len(all_users)-1].friends.append(cls(friends_data))
                else:
                    user_data = {"id": row_from_db["id"]}
                    all_users.append(cls(row_from_db))
                    friends_data ={"id": row_from_db["t3.id"],
                                "first_name": row_from_db["t3.first_name"],
                                "last_name": row_from_db["t3.last_name"],
                                "created_at": row_from_db["t3.created_at"],
                                "updated_at": row_from_db["t3.updated_at"],
                                }
                    all_users[len(all_users)-1].friends.append(cls(friends_data))
            else:
                user_data = {"id": row_from_db["id"]}
                all_users.append(cls(row_from_db))
                friends_data ={"id": row_from_db["t3.id"],
                                "first_name": row_from_db["t3.first_name"],
                                "last_name": row_from_db["t3.last_name"],
                                "created_at": row_from_db["t3.created_at"],
                                "updated_at": row_from_db["t3.updated_at"],
                                }
                all_users[len(all_users)-1].friends.append(cls(friends_data))
        return all_users
    


