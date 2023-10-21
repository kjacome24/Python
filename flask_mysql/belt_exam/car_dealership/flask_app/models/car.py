from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash
import re ### Regular expresion
import datetime #####for date funtions
from datetime import date #####for date funtions
from dateutil.relativedelta import relativedelta #####for date funtions
from flask_app.models import user

DB = 'car_dealership_schema'

EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
NAME_REGEX= re.compile(r'[a-zA-Z]+$') #### Regular expresion for jus letters
PASSWORD_REGEX= re.compile(r'^(?=.{8,})(?=.*[a-z])(?=.*[0-9])(?=.*[A-Z])(?=.*[@#$%^&+=]).*$')
NUMBER_REGEX= re.compile(r'^[0-9]*$') #######regular expresion just for numbers

class Car:
    def __init__( self , data ):
        self.id = data['id']
        self.price = data['price']
        self.model = data['model']
        self.make = data['make']
        self.year = data['year']
        self.description = data['description']
        self.created_at = data['created_at']
        self.created_at = data['created_at']
        self.status = "None"
        self.owner = "None"
        self.buyer = "None"


###########Many to many
    @classmethod
    def get_all(cls):
        var_count = 0
        query = "select * from cars as table1 left join purchases as table2 on table1.id=table2.car_id left join users as table3 on table2.user_id=table3.id left join  users as table4 on table1.user_id=table4.id;"
        results = connectToMySQL(DB).query_db(query)
        cars = []
        for car in results:
            cars.append( cls(car) )
            user_data = {
                "id" : car["table3.id"],
                "first_name" : car["first_name"],
                "last_name" : car["last_name"],
                "email" : car["email"],
                "password" : car["password"],
                "created_at" : car["table3.created_at"],
                "updated_at" : car["table3.updated_at"]
            }
            cars[var_count].buyer = ( user.User( user_data ) )
            if car["table3.id"] is None:
                cars[var_count].status = "On-Sale"
            else:
                cars[var_count].status = "Sold"
            user_data = {
                "id" : car["table4.id"],
                "first_name" : car["table4.first_name"],
                "last_name" : car["table4.last_name"],
                "email" : car["table4.email"],
                "password" : car["table4.password"],
                "created_at" : car["table4.created_at"],
                "updated_at" : car["table4.updated_at"]
            }
            cars[var_count].owner = ( user.User( user_data ) )
            var_count += 1
        return cars

    @classmethod
    def get_one(cls,data):
        query = "SELECT * FROM cars WHERE id = %(id)s;"
        burger_from_db = connectToMySQL(DB).query_db(query,data)
        return cls(burger_from_db[0])

    @classmethod
    def add_purchase(cls,data):
        query = "select count(*) as count from purchases where user_id=%(user_id)s and car_id=%(car_id)s;"
        validator = connectToMySQL(DB).query_db( query, data )
        if validator[0]['count']==0:
            query = "INSERT INTO purchases (user_id,car_id) VALUES (%(user_id)s,%(car_id)s);"
            return connectToMySQL(DB).query_db( query, data )
        else:
            return False

    @classmethod
    def destroy(cls,data):
        query = "DELETE FROM cars WHERE id = %(id)s;"
        return connectToMySQL(DB).query_db(query,data)

    @staticmethod
    def validate_entry(data):
        is_valid = True
        if data['price']=="" or int(data['price']) <0 :
            flash("Please remember that the price can not be 0 or null")
            is_valid= False
        if len(data['model']) <3:
            flash("The model should have at least 3 characters")
            is_valid= False
        if len(data['make']) <3:
            flash("The make should have at least 3 characters")
            is_valid= False
        if data['year']=="" or int(data['year']) <1900:
            flash("Hey buddy no one is gonna buy the car of your grandfather, it should be above 1900")
            is_valid= False
        if len(data['description']) <3:
            flash("The description should have at least 10 characters")
            is_valid= False
        return is_valid

    @classmethod
    def save(cls,data):
        query = "INSERT INTO cars (price, model, make, year, description, updated_at, created_at, user_id) VALUES ( %(price)s,  %(model)s,  %(make)s,  %(year)s,  %(description)s,  now(), now(), %(user_id)s);"
        return connectToMySQL(DB).query_db(query,data)
    
    @classmethod
    def update(cls,data):
        query = "UPDATE cars SET price = %(price)s, model = %(model)s , make = %(make)s , year = %(year)s , description = %(description)s, updated_at = now() , created_at = now() WHERE id = %(car_id)s;"
        return connectToMySQL(DB).query_db(query,data)
