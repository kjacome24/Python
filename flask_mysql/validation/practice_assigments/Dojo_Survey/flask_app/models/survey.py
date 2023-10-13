from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash

class Survey:
    def __init__(self,data):
        self.id = data['id']
        self.name= data['name']
        self.name= data['gender_identity']
        self.bun = data['location']
        self.meat = data['favorite_language']
        self.calories = data['comments']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

    @classmethod
    def new_survey(cls,data):
        query = "insert into survey (name,gender_identity,location,favorite_language,comments,created_at,updated_at) values (%(name)s,%(gender_identity)s,%(location)s,%(favorite_language)s,%(comments)s,now(),now());"
        return connectToMySQL('schema_dojo_survey').query_db(query,data)
    @staticmethod
    def validate_survey(survey):
        is_valid = True # asumimos que esto es true
        if 'GenderIdentity' not in survey:
            flash("You should select an option in Gender Identity")
            is_valid = False
        if 'authorization' not in survey:
            flash("You should click on the authorization button to proceed")
            is_valid = False
        if len(survey['name'])< 3:
            flash("The name should have at least three characters")
            is_valid = False
        if survey['favoritelanguage']=="--Select a language--":
            flash("Please select a language")
            is_valid = False
        if survey['location']=="--Select a Location--":
            flash("Please select a Location")
            is_valid = False
        if len(survey['Comments']) < 10:
            flash("The Comment should have at least ten characters")
            is_valid = False
        return is_valid

