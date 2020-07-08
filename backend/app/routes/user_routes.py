from app import app
from flask import jsonify
from app.controllers.user_controller import User_Controller
from flask_jwt_extended import (
    jwt_required, jwt_refresh_token_required, get_jwt_identity, get_raw_jwt)


# @app.route('/')
# def index():
#     """Index page"""
#     return jsonify({'message': "Welcome to Mt-Olives Church Database"})

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


# @app.route('/api/v1/auth/login', methods=['POST'])
# def login():
#     return User_Controller.login()

# @app.route('/api/v1/auth/register', methods =['POST'])
# def user_signup():
#     return User_Controller.sign_up()

# @app.route('/api/v1/users', methods = ['GET'])
# @jwt_required
# def get_registered_users():
#     return User_Controller.get_registered_users()

# @app.route('/api/v1/users/<user_name>', methods = ['GET'])
# @jwt_required
# def get_user(user_name):
#     return User_Controller.get_user(user_name)

# @app.route('/api/v1/users/<user_name>/edit', methods = ['PUT'])
# @jwt_required
# def modify_user(user_name):
#     return User_Controller.edit_user(user_name)

# @app.route('/api/v1/users/<user_name>/parcels', methods = ['GET'])
# @jwt_required
# def number_of_parcels(user_name):
#     return User_Controller.no_user_parcels(user_name)

# @app.route('/api/v1/users/<user_name>/parcels/cancelled', methods = ['GET'])
# @jwt_required
# def number_of_cancelled_parcels(user_name):
#     return User_Controller.no_cancelled_user_parcels(user_name)

# @app.route('/api/v1/users/<user_name>/parcels/pending', methods = ['GET'])
# @jwt_required
# def number_of_pending_parcels(user_name):
#     return User_Controller.no_pending_user_parcels(user_name)

# @app.route('/api/v1/users/<user_name>/parcels/intransit', methods = ['GET'])
# @jwt_required
# def number_of_intransit_parcels(user_name):
#     return User_Controller.no_intransit_user_parcels(user_name)

# @app.route('/api/v1/users/<user_name>/parcels/delivered', methods = ['GET'])
# @jwt_required
# def number_of_delivered_parcels(user_name):
#     return User_Controller.no_delivered_user_parcels(user_name)

# @app.route('/api/v1/users/<int:user_id>/role', methods = ['PUT'])
# @jwt_required
# def change_user_role(user_id):
#     return User_Controller.switch_user_role(user_id)
