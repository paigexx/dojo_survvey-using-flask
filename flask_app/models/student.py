import re
from flask.helpers import flash
from flask_app.config.mysqlconnection import  connectToMySQL
from flask import session

class Student:
    def __init__(self, data):
        self.id = data["id"]
        self.name = data["name"]
        self.language = data["language"]
        self.location = data["location"]
        self.comment = data["comment"]
        self.updated_at = data["updated_at"]
        self.created_at - data["created_at"]


    #  this method is necessary to access the dictionary of the student
    @classmethod
    def show_student(cls, data):
        query = "SELECT * FROM students WHERE id = %(student_id)s"
        results = connectToMySQL("dojo_survey").query_db(query, data)
        return results[0]

    # this data is from the request.form. This will return the id in the terminal.
    @classmethod
    def create_student(cls, data):
        query = "INSERT INTO students (name, location, language, comment, created_at, updated_at) VALUES ( %(name)s, %(location)s, %(language)s, %(comment)s, NOW(), NOW());"

        return connectToMySQL("dojo_survey").query_db(query, data)

    # this data will be from the request.form
    @staticmethod
    def validate_data(data):
        is_valid = True

        if len(data["name"]) == 0:
            flash("Must enter a first name")
            is_valid = False

        return is_valid
        
