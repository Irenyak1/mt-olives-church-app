import psycopg2
import os
import psycopg2.extras
from passlib.hash import pbkdf2_sha256 as sha256

class DatabaseConnection:
    def __init__(self):

#         db = 'd8l5eq5eakmkcm'
        db = 'sendit'
        # if os.getenv('APP_SETTINGS') == 'testing':
        #     db = 'test_db'
        conn = psycopg2.connect(host="localhost", database=db, user="postgres", password="Bumblebees1")
        # password="Bumblebees1"
#         conn = psycopg2.connect(host="ec2-23-23-101-25.compute-1.amazonaws.com", database=db, user="etpyvilhgiqvvw", password="999f624546819f9983ca1f6885672a281c4fe8ea23cbe3af4e42b98254b57cdd", port=5432)
        conn.autocommit = True
        self.cursor = conn.cursor(cursor_factory=psycopg2.extras.RealDictCursor)
        print(self.cursor)
        print(db)

    # def generate_hash(password):
    #     return sha256.hash(password)

    def setUp(self):
        members_table = """CREATE TABLE IF NOT EXISTS members(
            user_id SERIAL PRIMARY KEY,
            user_id VARCHAR(100) NOT NULL,
            gender VARCHAR(100) NOT NULL,
            dateofbirth VARCHAR(100), 
            maritalstatus VARCHAR(100) NOT NULL,
            cell VARCHAR(100) NOT NULL,
            educationlevel VARCHAR(100) NOT NULL,
            profession VARCHAR(100) NOT NULL,
            occupation VARCHAR(100) NOT NULL,
            placeofwork VARCHAR(100) NOT NULL,
            residence VARCHAR(100) NOT NULL,
            phonecontact VARCHAR(100) NOT NULL,
            emailaddress VARCHAR(100) UNIQUE NOT NULL,
            dateofbaptism VARCHAR(100) NOT NULL,
            placeofbaptism VARCHAR(100) NOT NULL,
            baptisingpastor VARCHAR(100) NOT NULL,
            formerreligion VARCHAR(100) NOT NULL)"""
        self.cursor.execute(members_table)


    #     parcels_table = """CREATE TABLE IF NOT EXISTS parcels(
    #         parcel_id SERIAL PRIMARY KEY,
    #         description VARCHAR NOT NULL,
    #         user_id INTEGER NOT NULL,
    #         user_user_id VARCHAR(25) NOT NULL,
    #         recipient_user_id VARCHAR(25) NOT NULL,
    #         recipient_mobile VARCHAR(25) NOT NULL,    
    #         pickup_location VARCHAR(225) NOT NULL,
    #         destination VARCHAR(225) NOT NULL,
    #         weight INTEGER NOT NULL,
    #         total_price INTEGER NOT NULL,
    #         status VARCHAR(25) DEFAULT 'pending',
    #         present_location VARCHAR(25) NOT NULL,
    #         date_created DATE NOT NULL DEFAULT CURRENT_DATE
    #     )"""
    #     self.cursor.execute(parcels_table)

    #     password = DatabaseConnection.generate_hash("rootsroot")
    #     check_no_of_rows = "SELECT * FROM users"
    #     self.cursor.execute(check_no_of_rows)
    #     result = self.cursor.fetchall()
    #     if len(result)==0:
    #         insert_admin = "INSERT INTO users (user_user_id, user_email, user_mobile, user_password) values ('admin', 'admin@gmail.com', '0780456734', '{}')".format(password)
    #         update_to_admin = "UPDATE users set admin_status = True where user_user_id = 'admin'"
    #         # insert_img = "UPDATE users SET img = bytea('/home/daizy/Andela/Bootcamp14/Send_IT_APIs/app/controllers/dee.jpg') where user_user_id = 'admin'"
    #         self.cursor.execute(insert_admin)
    #         self.cursor.execute(update_to_admin)
    #         # self.cursor.execute(insert_img)
          
    def insert_member(self, user_id, gender, dateofbirth, maritalstatus,
                      cell, educationlevel, profession, occupation,
                      placeofwork, residence, phonecontact,
                      emailaddress, dateofbaptism, placeofbaptism,
                      baptisingpastor, formerreligion):
        insert_member = "INSERT INTO members (user_id, gender, dateofbirth, maritalstatus,\
                                              cell, educationlevel, profession,\
                                              occupation, placeofwork, residence,\
                                              phonecontact, emailaddress,\
                                              dateofbaptism, placeofbaptism,\
                                              baptisingpastor, formerreligion)\
                                              values ('{}', '{}', '{}', '{}',\
                                              '{}', '{}', '{}', '{}','{}',\
                                              '{}', '{}', '{}','{}', '{}', \
                                              '{}', '{}')".format(user_id, gender, 
                                                            dateofbirth,
                                                            maritalstatus,
                                                            cell,
                                                            educationlevel,
                                                            profession,
                                                            occupation,
                                                            placeofwork,
                                                            residence,
                                                            phonecontact,
                                                            emailaddress,
                                                            dateofbaptism,
                                                            placeofbaptism,
                                                            baptisingpastor,
                                                            formerreligion)
        self.cursor.execute(insert_member)

    def get_all_members(self):
        get_all_members = "SELECT * FROM members"
        self.cursor.execute(get_all_members)
        all_members = self.cursor.fetchall()
        return all_members

    def get_one_member(self, user_id):
        get_one_member = "SELECT * FROM members WHERE user_id = {}".format(user_id)
        self.cursor.execute(get_one_member)
        one_member = self.cursor.fetchone()
        return one_member
    
    def get_cell_details(self, cell):
        get_cell_details = "SELECT * FROM members WHERE cell = '{}'".format(cell)
        self.cursor.execute(get_cell_details)
        cell_members = self.cursor.fetchall()
        return cell_members
    
    def modify_member(self, gender, dateofbirth, maritalstatus,
                      cell, educationlevel, profession, occupation,
                      placeofwork, residence, phonecontact,
                      emailaddress, dateofbaptism, placeofbaptism,
                      baptisingpastor, formerreligion, user_id):
        update = " UPDATE members SET (gender, dateofbirth,\
                                       maritalstatus, cell,\
                                       educationlevel, profession,\
                                       occupation, placeofwork,\
                                       residence, phonecontact,\
                                       emailaddress, dateofbaptism,\
                                       placeofbaptism, baptisingpastor,\
                                       formerreligion) = ('{}', '{}', '{}',\
                                      '{}', '{}', '{}', '{}', '{}', '{}',\
                                      '{}', '{}', '{}', '{}', '{}','{}')\
                                      WHERE user_id = '{}' ".format(gender,
                                                                 dateofbirth,
                                                                 maritalstatus,
                                                                 cell,
                                                                 educationlevel,
                                                                 profession,
                                                                 occupation,
                                                                 placeofwork,
                                                                 residence,
                                                                 phonecontact,
                                                                 emailaddress,
                                                                 dateofbaptism,
                                                                 placeofbaptism,
                                                                 baptisingpastor,
                                                                 formerreligion,
                                                                 user_id)
        self.cursor.execute(update)
        print(update)


    # def get_user(self, user_user_id):
    #     get_user = "SELECT * FROM users WHERE user_user_id = '{}'".format(user_user_id)
    #     self.cursor.execute(get_user)
    #     result = self.cursor.fetchone()
    #     return result

    # def clear_data(self, user_user_id):
    #     delete_content = "UPDATE users SET user_email = '' WHERE user_user_id = '{}'".format(user_user_id)
    #     self.cursor.execute(delete_content)
    #     return user_user_id

    # def edit_user(self, user_email, user_mobile, default_pickup_location, user_user_id):
    #     update = " UPDATE users SET (user_email, user_mobile, default_pickup_location) = ('{}', '{}', '{}') WHERE user_user_id = '{}' ".format(user_email, user_mobile, default_pickup_location, user_user_id)
    #     self.cursor.execute(update)
    #     print(update)

    # def login_user(self, user_user_id, user_password):
    #     select_user = "SELECT user_user_id, user_password FROM users WHERE user_user_id = '{}' and user_password = '{}'".format(user_user_id, user_password)
    #     self.cursor.execute(select_user)
    #     return [user_user_id,user_password]

    # def add_parcel(self, description, user_id, user_user_id, recipient_user_id, recipient_mobile, pickup_location, destination, weight, total_price):
    #     insert_parcel = "INSERT INTO parcels (description, user_id, user_user_id, recipient_user_id, recipient_mobile, pickup_location, destination,  weight, total_price, present_location) values ('{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}')".format(description, user_id, user_user_id, recipient_user_id, recipient_mobile, pickup_location, destination, weight, total_price, pickup_location)
    #     self.cursor.execute(insert_parcel)

    # def get_all_parcels(self):
    #     get_parcels = "SELECT * FROM parcels ORDER BY parcel_id ASC"
    #     self.cursor.execute(get_parcels)
    #     result = self.cursor.fetchall()
    #     return result

    # def get_a_parcel(self, parcel_id):
    #     get_parcel = "SELECT * FROM parcels WHERE parcel_id = '{}'".format(parcel_id)
    #     self.cursor.execute(get_parcel)
    #     result = self.cursor.fetchone()
    #     return result

    # def get_user_parcels_by_status(self, user_id, status):
    #     get_user_parcels = "SELECT * FROM parcels WHERE user_id = '{}' and status = '{}' ORDER BY parcel_id ASC".format(user_id, status)
    #     self.cursor.execute(get_user_parcels)
    #     result = self.cursor.fetchall()
    #     return result

    # def get_parcels_by_user(self, user_id):
    #     get_user_parcels = "SELECT * FROM parcels WHERE user_id = '{}' ORDER BY parcel_id ASC".format(user_id)
    #     self.cursor.execute(get_user_parcels)
    #     result = self.cursor.fetchall()
    #     return result

    # def change_location(self, parcel_id, present_location):
    #     location = "UPDATE parcels SET present_location = '{}' WHERE parcel_id = '{}'".format(present_location, parcel_id)
    #     self.cursor.execute(location)
    #     return present_location

    # def change_destination(self, parcel_id, destination, price):
    #     destination = "UPDATE parcels SET destination = '{}', total_price = '{}' WHERE parcel_id = '{}'".format(destination, price, parcel_id)
    #     self.cursor.execute(destination)
    #     return destination

    # def change_status(self, parcel_id, status):
    #     status = "UPDATE parcels SET status = '{}' WHERE parcel_id = '{}'".format(status, parcel_id)
    #     self.cursor.execute(status)

    # def get_user(self, user_user_id):
    #     get_user = "SELECT * FROM users WHERE user_user_id = '{}'".format(user_user_id)
    #     self.cursor.execute(get_user)
    #     result = self.cursor.fetchone()
    #     return result

    # def get_user_by_id(self, user_id):
    #     get_user = "SELECT * FROM users WHERE user_id = '{}'".format(user_id)
    #     self.cursor.execute(get_user)
    #     result = self.cursor.fetchone()
    #     return result

    # def get_users(self):
    #     get_users = "SELECT * FROM users ORDER BY user_id ASC"
    #     self.cursor.execute(get_users)
    #     result = self.cursor.fetchall()
    #     return result

    # def change_user_role_to_admin(self, user_id):
    #     update_role_to_admin = "UPDATE users set admin_status = True where user_id = '{}'".format(user_id)
    #     self.cursor.execute(update_role_to_admin)

    # def change_user_role_to_user(self, user_id):
    #     update_role_to_regular_user = "UPDATE users set admin_status = False where user_id = '{}'".format(user_id)
    #     self.cursor.execute(update_role_to_regular_user)

    # def delete_tables(self):
    #     delete = "DROP TABLE users, parcels"
    #     self.cursor.execute(delete)

    
    # def select_no_of_user_parcels(self, useruser_id):
    #     query = "SELECT COUNT(user_user_id) FROM parcels WHERE user_user_id = '{}'".format(useruser_id)
    #     self.cursor.execute(query)
    #     result = self.cursor.fetchone()
    #     return result

    # def select_no_of_user_parcels_cancelled(self, useruser_id):
    #     query = "SELECT COUNT(user_user_id) FROM parcels WHERE user_user_id = '{}' and status = 'cancelled'".format(useruser_id)
    #     self.cursor.execute(query)
    #     result = self.cursor.fetchone()
    #     return result

    # def select_no_of_user_parcels_pending(self, useruser_id):
    #     query = "SELECT COUNT(user_user_id) FROM parcels WHERE user_user_id = '{}' and status = 'pending'".format(useruser_id)
    #     self.cursor.execute(query)
    #     result = self.cursor.fetchone()
    #     return result

    # def select_no_of_user_parcels_intransit(self, useruser_id):
    #     query = "SELECT COUNT(user_user_id) FROM parcels WHERE user_user_id = '{}' and status = 'intransit'".format(useruser_id)
    #     self.cursor.execute(query)
    #     result = self.cursor.fetchall()
    #     return result

    # def select_no_of_user_parcels_delivered(self, useruser_id):
    #     query = "SELECT COUNT(user_user_id) FROM parcels WHERE user_user_id = '{}' and status = 'delivered'".format(useruser_id)
    #     self.cursor.execute(query)
    #     result = self.cursor.fetchone()
    #     return result
