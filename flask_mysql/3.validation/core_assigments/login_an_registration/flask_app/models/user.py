from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash
import re
import datetime #####for date funtions
from datetime import date #####for date funtions
from dateutil.relativedelta import relativedelta #####for date funtions

EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
NAME_REGEX= re.compile(r'[a-zA-Z]+$') #### Regular expresion for jus letters
PASSWORD_REGEX= re.compile(r'^(?=.{8,})(?=.*[a-z])(?=.*[0-9])(?=.*[A-Z])(?=.*[@#$%^&+=]).*$')
NUMBER_REGEX= re.compile(r'^[0-9]*$') #######regular expresion just for numbers


class User:
    def __init__( self , data ):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.email = data['email']
        self.password = data['password']
        self.birthdate = data['birthdate']
        self.favorite_language = data['favorite_language']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
    @classmethod
    def save(cls,data):
        query = "INSERT INTO user ( first_name , last_name , email , password , birthdate , favorite_language, created_at, updated_at ) VALUES ( %(first_name)s , %(last_name)s , %(email)s , %(password)s , %(birthdate)s , %(favorite_language)s , NOW() , NOW() );"
        mysql = connectToMySQL('login_and_registration_schema')
        result = mysql.query_db(query, data)
        print(result)
        data_usuario = {'id': result}
        return cls.getId(data_usuario)
    
    @classmethod
    def getId(cls, data):
        query = "select * from user where id = %(id)s;"
        mysql = connectToMySQL('login_and_registration_schema')
        result = mysql.query_db(query, data)
        if len(result) > 0:
            return cls(result[0])
        else:
            return None
    @classmethod
    def getbyemail(cls, data):
        query = "select * from user where email = %(email)s;"
        mysql = connectToMySQL('login_and_registration_schema')
        result = mysql.query_db(query, data)
        if len(result) > 0:
            return cls(result[0])
        else:
            return None

    @staticmethod
    def validate_entry(data):
        is_valid = True
        if data['which_form']=='register_user':
            if len(data['first_name']) <2:
                flash(["The first name should have at least 2 characters",0])
                is_valid= False
            if not NAME_REGEX.match(data['first_name']):
                flash(["Your first name should not have numbers",0])
                is_valid= False
            if len(data['last_name']) <2:
                flash(["The last name should have at least 2 characters",0])
                is_valid= False
            if not NAME_REGEX.match(data['last_name']):
                flash(["Your last name should not have numbers",0])
                is_valid= False
            if not EMAIL_REGEX.match(data['email']): 
                flash(["Invalid email address!",0])
                is_valid = False
            if len(data['password']) <8:
                flash(["The password should have at least 8 characters",0])
                is_valid = False
            if data['passwordconfir'] !=data['password']:
                flash(["The password confirmation is not matching with the original password",0])
                is_valid= False
            if not PASSWORD_REGEX.match(data['password']):
                flash(["Your password should have at least 8 characters with at least one lowercase and one uppercase ASCII character and also at least one character from the set @#$%^&+=, plus a number",0])
                is_valid= False
            x=data['birthdate']
            if data['birthdate'] =='':
                flash(["Please select your birthdate",0])
                is_valid= False
            elif datetime.date(int(x[0:4]),int(x[5:7]),int(x[8:10])) > (date.today() - relativedelta(years=10)):
                flash(["You must be at least 10 years old to register",0])
                is_valid= False
            if data['favorite_language'] =='':
                flash(["Please select your favorite language",0])
                is_valid= False
        else:
            if not EMAIL_REGEX.match(data['email']): 
                flash(["Invalid email address!",1])
                is_valid = False
            if len(data['password']) <8:
                flash(["The password should have at least 8 characters",1])
                is_valid = False
        return is_valid








####simple example to create query and create objects. 
    # @classmethod
    # def get_all(cls):
    #     query = "SELECT * FROM user;"
    #     results = connectToMySQL('login_and_registration_schema').query_db(query)
    #     users = []
    #     for user in results:
    #         users.append( cls(user) )
    #     return users

####example to insert data in database, this can be also for delete or update


####example to get last id    
    # @classmethod
    # def last_id(cls):
    #     query = "select id FROM user order by id desc limit 1;"
    #     results= connectToMySQL('login_and_registration_schema').query_db(query)
    #     return results

#example to query with inputs
    # @classmethod
    # def filter_email(cls,data):
    #     query = "select * FROM user where id=%(id)s;"
    #     results= connectToMySQL('login_and_registration_schema').query_db(query,data)
    #     users = []
    #     for user in results:
    #         users.append(cls(user))
    #     return users

########example to validate entry flash
