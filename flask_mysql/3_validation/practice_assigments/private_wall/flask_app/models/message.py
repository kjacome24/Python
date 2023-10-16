from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash
from flask_app.models import user
import re
import datetime #####for date funtions
from datetime import date #####for date funtions
from datetime import datetime
from dateutil.relativedelta import relativedelta #####for date funtions


DB = "private_wall_schema"



class Message:
    def __init__( self , data ):
        self.id = data['id']
        self.content = data['content']
        self.sender_id = data['sender_id']
        self.receiver_id = data['receiver_id']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

    def time_span(self):
        now = datetime.now()
        hours = now - (self.created_at)
        hours = int((hours.seconds/60)/60)
        return hours
    @classmethod
    def save(cls,data):
        query = "INSERT INTO messages ( content , sender_id , receiver_id, created_at, updated_at ) VALUES ( %(message)s , %(sender_id)s , %(receiver_id)s , NOW() , NOW() );"
        return connectToMySQL(DB).query_db(query,data)

    @classmethod
    def delete_message(cls,data):
        query = "delete from messages where id=%(id)s;"
        return connectToMySQL(DB).query_db( query, data )

    @staticmethod
    def validate_entry(data):
        is_valid = True
        if len(data['message']) <5:
            flash("The message should have at least 5 characters")
            is_valid= False
        return is_valid
    
    @classmethod
    def get_all(cls):
        query = "SELECT * FROM messages;"
        results = connectToMySQL(DB).query_db(query)
        messages = []
        for message in results:
            messages.append( cls(message) )
        return messages
    
    @classmethod
    def get_all_by_sender(cls,data):
        query = "SELECT * FROM messages where sender_id=%(sender_id)s;"
        results = connectToMySQL(DB).query_db(query,data)
        messages = []
        for message in results:
            messages.append( cls(message) )
        return messages

    @classmethod
    def get_all_by_receiver(cls,data):
        query = "select * from messages left join users on messages.sender_id=users.id where messages.receiver_id=%(receiver_id)s order by messages.created_at desc;"
        results = connectToMySQL(DB).query_db(query,data)
        print(results)
        messages = []
        for message in results:
            sender_data = {
                "id": message["users.id"],
                "first_name": message["first_name"],
                "last_name": message["last_name"],
                "email": message["email"],
                "password": message["password"],
                "created_at": message["users.created_at"],
                "updated_at": message["users.updated_at"],
            }
            sender = user.User(sender_data)
            message_data = {
                "id": message["id"],
                "content": message["content"],
                "sender_id": sender,
                "receiver_id": message["receiver_id"],
                "created_at": message["created_at"],
                "updated_at": message["updated_at"]
            }
            
            messages.append( cls(message_data) )
        return messages



def time_span(data):
    now = datetime.now()
    delta = now - (data)
    return delta

x = time_span(datetime(2023, 10, 14, 21, 3, 29))
print((x.seconds/60)/60)