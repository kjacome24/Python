from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash
import re ### Regular expresion
import datetime #####for date funtions
from datetime import date #####for date funtions
from dateutil.relativedelta import relativedelta #####for date funtions
from flask_app.models import user

DB = 'recipes_schema'

EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
NAME_REGEX= re.compile(r'[a-zA-Z]+$') #### Regular expresion for jus letters
PASSWORD_REGEX= re.compile(r'^(?=.{8,})(?=.*[a-z])(?=.*[0-9])(?=.*[A-Z])(?=.*[@#$%^&+=]).*$')
NUMBER_REGEX= re.compile(r'^[0-9]*$') #######regular expresion just for numbers

class Recipe:
    def __init__( self , data ):
        self.id = data['id']
        self.name = data['name']
        self.description = data['description']
        self.instructions = data['instructions']
        self.under_30_min = data['under_30_min']
        self.date_cooked = data['date_cooked']
        self.updated_at = data['updated_at']
        self.created_at = data['created_at']
        self.users = []
    
    @classmethod
    def get_all(cls):
        var_count = 0
        query = "select * from recipes left join users on recipes.user_id=users.id;"
        results = connectToMySQL(DB).query_db(query)
        recipes = []
        for recipe in results:
            recipes.append( cls(recipe) )
            user_data = {
                "id" : recipe["users.id"],
                "first_name" : recipe["first_name"],
                "last_name" : recipe["last_name"],
                "email" : recipe["email"],
                "password" : recipe["password"],
                "created_at" : recipe["users.created_at"],
                "updated_at" : recipe["users.updated_at"]
            }
            recipes[var_count].users.append( user.User( user_data ) )
            var_count += 1
        return recipes
    
    @classmethod
    def save( cls , data ):
        query = "INSERT INTO recipes ( name , description , instructions , under_30_min , date_cooked, user_id , created_at , updated_at ) VALUES (%(name)s,%(description)s,%(instructions)s,%(under_30_min)s,%(date_cooked)s,%(user_id)s,NOW(),NOW());"
        return connectToMySQL(DB).query_db( query, data)

    @classmethod
    def get_one(cls,data):
        query = "SELECT * FROM recipes WHERE id = %(id)s;"
        burger_from_db = connectToMySQL(DB).query_db(query,data)
        return cls(burger_from_db[0])

    @classmethod
    def update(cls,data):
        query = "UPDATE recipes SET name=%(name)s, description=%(description)s, instructions=%(instructions)s, under_30_min=%(under_30_min)s,user_id=%(user_id)s,  date_cooked=%(date_cooked)s, updated_at = NOW(), created_at = NOW() WHERE id = %(id)s;"
        return connectToMySQL(DB).query_db(query,data)

    @classmethod
    def destroy(cls,data):
        query = "DELETE FROM recipes WHERE id = %(id)s;"
        return connectToMySQL(DB).query_db(query,data)
    
    @classmethod
    def get_recipies_with_users( cls , data ):
        query = "select * from recipes left join users on recipes.user_id=users.id where recipes.id=%(id)s;"
        results = connectToMySQL(DB).query_db( query , data )
        recipe = cls( results[0] )
        for row_from_db in results:
            user_data = {
                "id" : row_from_db["users.id"],
                "first_name" : row_from_db["first_name"],
                "last_name" : row_from_db["last_name"],
                "email" : row_from_db["email"],
                "password" : row_from_db["password"],
                "created_at" : row_from_db["users.created_at"],
                "updated_at" : row_from_db["users.updated_at"]
            }
            recipe.users.append( user.User( user_data ) )
        return recipe
    
    @staticmethod
    def validate_entry(data):
        is_valid = True
        if len(data['name']) <3:
            flash("The name of the recipe should have at least 3 characters")
            is_valid= False
        if len(data['description']) <3:
            flash("The description of the recipe should have at least 3 characters")
            is_valid= False
        if len(data['instructions']) <3:
            flash("The instructions of the recipe should have at least 3 characters")
            is_valid= False
        if data['date_cooked']=='':
            flash("Please insert the cooked date")
            is_valid= False
        if "under_30_min" not in data:
            flash("Please do not forget to confirm if the recipe took under 30 minutes")
            is_valid= False
        return is_valid
    


