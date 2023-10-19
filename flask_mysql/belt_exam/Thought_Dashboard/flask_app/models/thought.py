from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash
import re ### Regular expresion
import datetime #####for date funtions
from datetime import date #####for date funtions
from dateutil.relativedelta import relativedelta #####for date funtions
from flask_app.models import user

DB = 'thoughts_schema'

EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
NAME_REGEX= re.compile(r'[a-zA-Z]+$') #### Regular expresion for jus letters
PASSWORD_REGEX= re.compile(r'^(?=.{8,})(?=.*[a-z])(?=.*[0-9])(?=.*[A-Z])(?=.*[@#$%^&+=]).*$')
NUMBER_REGEX= re.compile(r'^[0-9]*$') #######regular expresion just for numbers

class Thought:
    
    def __init__( self , data ):
        self.id = data['id']
        self.thought = data['thought']
        self.updated_at = data['updated_at']
        self.created_at = data['created_at']
        self.user_id = data['user_id']
        self.validationx = data['validationx']
        self.owner_user = ''
        self.users = []
        self.likes_counter = 0
    
    @classmethod
    def get_thought_with_likes(cls,data):
        query = "select * from (select new2.*,new.validationx  from thoughts as new2 left join (select thoughts.id as idx, 'Yes' as validationx  from thoughts left join likes on likes.thought_id=thoughts.id left join users on likes.user_id=users.id where users.id=%(id)s) as new on new2.id=new.idx) as table1 left join  likes as table2 on table2.thought_id=table1.id left join users as table3 on table2.user_id=table3.id;"
        results= connectToMySQL(DB).query_db(query,data)
        all_thoughts = []
        counter = 0
        for row_from_db in results:
            users_data ={
                                "id": row_from_db["table3.id"],
                                "first_name": row_from_db["first_name"],
                                "last_name": row_from_db["last_name"],
                                "email": row_from_db["email"],
                                "password": "NA",
                                "created_at": row_from_db["table3.created_at"],
                                "updated_at": row_from_db["table3.updated_at"]
                                }
            if 'thought_data' in locals():
                if row_from_db["id"]==thought_data["id"]:
                    thought_data = {"id": row_from_db["id"]}
                    # print(f"Contador es:{counter}")
                    all_thoughts[len(all_thoughts)-1].users.append(user.User(users_data))
                    counter -=1
                    # print(f"though counter es:{len(all_thoughts)-1}")
                    # print("A---------------------")
                else:
                    thought_data = {"id": row_from_db["id"]}
                    all_thoughts.append(cls(row_from_db))
                    # print(f"Contador es:{counter}")
                    all_thoughts[len(all_thoughts)-1].users.append(user.User(users_data))
                    # print(f"though counter es:{len(all_thoughts)-1}")
                    # print("B---------------------")
            else:
                thought_data = {"id": row_from_db["id"]}
                all_thoughts.append(cls(row_from_db))
                # print(f"Contador es:{counter}")
                all_thoughts[len(all_thoughts)-1].users.append(user.User(users_data))
                # print(f"though counter es:{len(all_thoughts)-1}")
                # print("C---------------------")
                
            print(f"though counter es:{len(all_thoughts)-1}")
            print(f"Contador es:{counter}")
            if all_thoughts[counter].users[0].id is None:
                # print("---------------------")
                all_thoughts[counter].likes_counter = len(all_thoughts[counter].users)-1
            else:
                all_thoughts[counter].likes_counter = len(all_thoughts[counter].users)
                # print("---------------------")
            data = {"id" : row_from_db["user_id"]}
            all_thoughts[counter].owner_user = user.User.getId(data)
            # data = {'thought_id': row_from_db["id"]}
            # all_thoughts[len(all_thoughts)-1].likes_counter = (Thought.counter_likes(data))
            
            counter +=1
        return all_thoughts


    @classmethod
    def save(cls,data):
        query = "INSERT INTO thoughts (thought, updated_at, created_at, user_id) VALUES (%(new_thought)s,now(),now(), %(user_id)s);"
        connectToMySQL(DB).query_db( query, data )

    @staticmethod
    def validate_entry(data):
        is_valid = True
        if len(data['new_thought']) <5:
            flash("The name of the recipe should have at least 5 characters")
            is_valid= False
        if data['new_thought'] =="Post a thought here":
            flash("Please type a thought")
            is_valid= False
        if data['new_thought'] =='':
            flash("Please type a thought")
            is_valid= False
        return is_valid    

    @classmethod
    def destroy(cls,data):
        query = "DELETE FROM likes WHERE thought_id = %(id)s;"
        connectToMySQL(DB).query_db(query,data)
        query = "DELETE FROM thoughts WHERE id = %(id)s;"
        return connectToMySQL(DB).query_db(query,data)

    @classmethod
    def destroy_like(cls,data):
        query = "DELETE FROM likes WHERE thought_id = %(thought_id)s and user_id= %(user_id)s;"
        connectToMySQL(DB).query_db(query,data)

    @classmethod
    def user_like(cls,data):
        query = "select count(*) as count from likes where user_id=%(user_id)s and thought_id=%(thought_id)s;"
        validator = connectToMySQL(DB).query_db( query, data )
        if validator[0]['count']==0:
            query = "INSERT INTO likes (user_id,thought_id) VALUES (%(user_id)s,%(thought_id)s);"
            return connectToMySQL(DB).query_db( query, data )
        else:
            return False

    @classmethod
    def counter_likes(cls,data):
        query = "select count(*) as counter from thoughts join likes on likes.thought_id=thoughts.id  where thoughts.id=%(thought_id)s;"
        return connectToMySQL(DB).query_db( query, data )
    



