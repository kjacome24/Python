from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash
import re ### Regular expresion
import datetime #####for date funtions
from datetime import date #####for date funtions
from dateutil.relativedelta import relativedelta #####for date funtions
from flask_app.models import user

DB = 'sightings_schema'

EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
NAME_REGEX= re.compile(r'[a-zA-Z]+$') #### Regular expresion for jus letters
PASSWORD_REGEX= re.compile(r'^(?=.{8,})(?=.*[a-z])(?=.*[0-9])(?=.*[A-Z])(?=.*[@#$%^&+=]).*$')
NUMBER_REGEX= re.compile(r'^[0-9]*$') #######regular expresion just for numbers

class Sighting:
    def __init__( self , data ):
        self.id = data['id']
        self.location = data['location']
        self.description = data['description']
        self.date_of_sighting = data['date_of_sighting']
        self.number_of_sesquatches = data['number_of_sesquatches']
        self.updated_at = data['updated_at']
        self.created_at = data['created_at']
        self.validationx = 'No'
        self.owner_sighting = ''
        self.users = []
        self.likes_counter = 0

    @classmethod
    def get_sightins_with_likes(cls,data):
        query = "select * from sightings left join users on  sightings.user_id=users.id;"
        results= connectToMySQL(DB).query_db(query,data)
        all_sightings = []
        counter = 0
        for row_from_db in results:
            sighting = (cls(row_from_db))
            x = str(sighting.date_of_sighting)
            x = x[0:10]
            sighting.date_of_sighting = x
            users_data ={
                "id": row_from_db["users.id"],
                "first_name": row_from_db["first_name"],
                "last_name": row_from_db["last_name"],
                "email": row_from_db["email"],
                "password": "NA",
                "created_at": row_from_db["users.created_at"],
                "updated_at": row_from_db["users.updated_at"]
                }
            sighting.owner_sighting=user.User(users_data)
            data['sighting_id'] = sighting.id
            query = "select * from sightings left join believes on sightings.id=believes.sighting_id left join users on believes.user_id=users.id where sightings.id=%(sighting_id)s"
            results= connectToMySQL(DB).query_db(query,data)
            for row_from_db2 in results:
                users_data ={
                    "id": row_from_db["users.id"],
                    "first_name": row_from_db["first_name"],
                    "last_name": row_from_db["last_name"],
                    "email": row_from_db["email"],
                    "password": "NA",
                    "created_at": row_from_db["users.created_at"],
                    "updated_at": row_from_db["users.updated_at"]
                    }
                if row_from_db2["users.id"] is None:
                    pass
                elif row_from_db2["users.id"]==data['id']:
                    sighting.validationx = "Yes"
                    sighting.users.append(user.User(users_data))
                else:
                    sighting.users.append(user.User(users_data))
            sighting.likes_counter = len(sighting.users)
            all_sightings.append(sighting)
        return all_sightings


    @classmethod
    def get_all(cls):
        var_count = 0
        query = "select * from sightings left join users on sightings.user_id=users.id;"
        results = connectToMySQL(DB).query_db(query)
        sightings = []
        for sighting in results:
            sightings.append( cls(sighting) )
            user_data = {
                "id" : sighting["users.id"],
                "first_name" : sighting["first_name"],
                "last_name" : sighting["last_name"],
                "email" : sighting["email"],
                "password" : sighting["password"],
                "created_at" : sighting["users.created_at"],
                "updated_at" : sighting["users.updated_at"]
            }
            sightings[var_count].users.append( user.User( user_data ) )
            var_count += 1
        return sightings
    
    @classmethod
    def save( cls , data ):
        query = "INSERT INTO sightings (`location`, `description`, `date_of_sighting`, `number_of_sesquatches`, `updated_at`, `created_at`, `user_id`) VALUES (%(location)s,%(description)s, %(date_of_sighting)s, %(number_of_sesquatches)s, now(), now(), %(user_id)s);"
        return connectToMySQL(DB).query_db( query, data)

    @classmethod
    def get_one(cls,data):
        query = "SELECT * FROM sightings WHERE id = %(id)s;"
        row_from_db = connectToMySQL(DB).query_db(query,data)
        return cls(row_from_db[0])

    @classmethod
    def update(cls,data):
        query = "UPDATE sightings SET location = %(location)s , description = %(description)s, date_of_sighting = %(date_of_sighting)s, number_of_sesquatches = %(number_of_sesquatches)s, updated_at = now() WHERE id= %(id)s;"
        return connectToMySQL(DB).query_db(query,data)

    @classmethod
    def destroy(cls,data):
        query = "DELETE FROM believes WHERE sighting_id = %(id)s;"
        connectToMySQL(DB).query_db(query,data)
        query = "DELETE FROM sightings WHERE id = %(id)s;"
        return connectToMySQL(DB).query_db(query,data)
    
    @classmethod
    def get_sightings_with_users( cls , data ): 
        query = "select * from sightings as table1 left join believes as table2 on table1.id=table2.sighting_id  left join users as table3 on table2.user_id=table3.id left join users as table4 on table4.id=table1.user_id where table1.id=%(sighting_id)s"
        results= connectToMySQL(DB).query_db(query,data)
        print(results)
        sighting = cls( results[0] )
        users_data ={
                "id": results[0]["table4.id"],
                "first_name": results[0]["table4.first_name"],
                "last_name": results[0]["table4.last_name"],
                "email": results[0]["table4.email"],
                "password": "NA",
                "created_at": results[0]["table4.created_at"],
                "updated_at": results[0]["table4.updated_at"]
                }
        sighting.owner_sighting = user.User(users_data)
        print("here------")
        for row_from_db2 in results:
            users_data ={
                "id": row_from_db2["table3.id"],
                "first_name": row_from_db2["first_name"],
                "last_name": row_from_db2["last_name"],
                "email": row_from_db2["email"],
                "password": "NA",
                "created_at": row_from_db2["table3.created_at"],
                "updated_at": row_from_db2["table3.updated_at"]
                }
            if users_data["id"] is None:
                    pass
            elif users_data["id"]==data["id"]:
                sighting.validationx = "Yes"
                sighting.users.append(user.User(users_data))
            else:
                sighting.users.append(user.User(users_data))
        sighting.likes_counter = len(sighting.users)
        return sighting
    

    @staticmethod
    def validate_entry(data):
        is_valid = True
        if len(data['location']) <3:
            flash("The location should have at least 3 characters")
            is_valid= False
        if len(data['description']) <3:
            flash("The description of the sighting should have at least 3 characters")
            is_valid= False
        if data['date_of_sighting']=='':
            flash("Please insert sighting date")
            is_valid= False
        if data['number_of_sesquatches']=='' or int(data['number_of_sesquatches']) < 1:
            flash("You should at least mark 1 sesquatch to report")
            is_valid= False
        return is_valid
    

    @classmethod
    def add_skeptical(cls,data):
        query = "select count(*) as count from believes where user_id=%(user_id)s and sighting_id=%(sighting_id)s;"
        validator = connectToMySQL(DB).query_db( query, data )
        if validator[0]['count']==0:
            query = "INSERT INTO believes (user_id,sighting_id) VALUES (%(user_id)s,%(sighting_id)s);"
            return connectToMySQL(DB).query_db( query, data )
        else:
            return False
        

    @classmethod
    def remove_skeptical(cls,data):
        query = "DELETE FROM believes WHERE sighting_id = %(sighting_id)s and user_id= %(user_id)s;"
        connectToMySQL(DB).query_db(query,data)



