from app import app
from flask import Flask, jsonify, flash, request, redirect, url_for
from werkzeug.utils import secure_filename
import os
from flask import Flask, flash, request, redirect, url_for
from app.controllers.user_controller import User_Controller
from flask_jwt_extended import (
    jwt_required, jwt_refresh_token_required, get_jwt_identity, get_raw_jwt)



@app.route('/api/v1/auth/login', methods=['POST'])
def login_admin():
    return User_Controller.login()


@app.route('/api/v1/auth/register', methods=['POST'])
def register():
    return User_Controller.register_member()


@app.route('/api/v1/members', methods=['GET'])
# @jwt_required
def get_all_members():
    return User_Controller.get_members()


@app.route('/api/v1/members/<int:user_id>', methods=['GET'])
# @jwt_required
def get_one_member(user_id):
    return User_Controller.get_a_member(user_id)


@app.route('/api/v1/members/cells/<cell>', methods=['GET'])
# @jwt_required
def get_cell_details(cell):
    return User_Controller.get_a_cell_details(cell)


@app.route('/api/v1/members/<name>/edit', methods=['PUT'])
# @jwt_required
def modify_member(name):
    return User_Controller.edit_member(gender, dateofbirth, maritalstatus,
                                       cell, educationlevel, profession, occupation,
                                       placeofwork, residence, phonecontact,
                                       emailaddress, dateofbaptism, placeofbaptism,
                                       baptisingpastor, formerreligion, name)

