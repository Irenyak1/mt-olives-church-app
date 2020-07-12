import re
from flask import jsonify, request
from passlib.hash import pbkdf2_sha256 as sha256
from app import app
from app.models.users_model import User
from app.controllers.db import DatabaseConnection
from app.validator import Validator
from flask_jwt_extended import (create_access_token, get_jwt_identity)
import datetime
from werkzeug import secure_filename
import os

db = DatabaseConnection()

class User_Controller:

    @staticmethod
    def login():
        ''' Method to login the admin and return a token'''
        user_input = request.get_json(force=True)        
        username = user_input.get("user_name")
        password = user_input.get("user_password")

        if not username:
            return jsonify({'error': "Enter user name"})
        if not password:
            return jsonify({'error':"Please enter password"})

        if username != 'Admin' or password != 'Admin123':
            return jsonify({'error': "Invalid login credentials, try again"})
        else:
            expiry = datetime.timedelta(days=1)
            user_data = {"username": username, "password": password[2]}
            access_token = create_access_token(identity=user_data, expires_delta=expiry)
            return jsonify({
                        'success': f"You have successfully been logged in as {username}",
                        'access_token': access_token
                        }), 200

    @staticmethod
    def saveToFolder():
        user_input = request.get_json(force=True)
        file = user_input.get("image")
        print("the file is", file)
        return file


    
    @staticmethod
    def register_member():
        """Method to register a member"""
        db = DatabaseConnection()
    
        user_input = request.get_json(force=True)

        name = user_input.get("name")
        gender = user_input.get("gender")
        dateofbirth = user_input.get("dateofbirth")
        maritalstatus = user_input.get("maritalstatus")
        cell = user_input.get("cell")
        educationlevel = user_input.get("educationlevel")
        profession = user_input.get("profession")
        occupation = user_input.get("occupation")
        placeofwork = user_input.get("placeofwork")
        residence = user_input.get("residence")
        phonecontact = user_input.get("phonecontact")
        emailaddress = user_input.get("emailaddress")
        dateofbaptism = user_input.get("dateofbaptism")
        placeofbaptism = user_input.get("placeofbaptism")
        baptisingpastor = user_input.get("baptisingpastor")
        formerreligion = user_input.get("formerreligion")
        image = user_input.get("image")

        register_member = db.insert_member(name, gender, dateofbirth, maritalstatus,
                      cell, educationlevel, profession, occupation,
                      placeofwork, residence, phonecontact,
                      emailaddress, dateofbaptism, placeofbaptism,
                      baptisingpastor, formerreligion, image)
        return jsonify({'Success': "Member has been successfully registered"}), 201

    @staticmethod
    def get_members():
        """Retrieve all registered members"""
        print(db.get_all_members())
        return jsonify({'message': db.get_all_members()})
    
    @staticmethod
    def get_a_member(name):
        """Retrieve one member"""
        return jsonify({'message': db.get_one_member(name)})

    @staticmethod
    def get_a_cell_details(cell):
        """Retrieve all members' details in a particular cell"""
        return jsonify({'message': db.get_cell_details(cell)})
    

  