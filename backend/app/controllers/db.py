import psycopg2
import os
import psycopg2.extras
from passlib.hash import pbkdf2_sha256 as sha256

class DatabaseConnection:
    def __init__(self):
        db = 'sendit'
        conn = psycopg2.connect(host="localhost", database=db, user="postgres", password="Bumblebees1")
        conn.autocommit = True
        self.cursor = conn.cursor(cursor_factory=psycopg2.extras.RealDictCursor)
        print(self.cursor)
        print(db)


    def setUp(self):
        members_table = """CREATE TABLE IF NOT EXISTS members(
            user_id SERIAL PRIMARY KEY,
            name VARCHAR(100) NOT NULL,
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
            formerreligion VARCHAR(100) NOT NULL,
            image VARCHAR(10000000) NOT NULL)"""
        self.cursor.execute(members_table)
        
    def insert_member(self, name, gender, dateofbirth, maritalstatus,
                      cell, educationlevel, profession, occupation,
                      placeofwork, residence, phonecontact,
                      emailaddress, dateofbaptism, placeofbaptism,
                      baptisingpastor, formerreligion, imageurl):
        insert_member = "INSERT INTO members (name, gender, dateofbirth, maritalstatus,\
                                              cell, educationlevel, profession,\
                                              occupation, placeofwork, residence,\
                                              phonecontact, emailaddress,\
                                              dateofbaptism, placeofbaptism,\
                                              baptisingpastor, formerreligion, image)\
                                              values ('{}', '{}', '{}', '{}',\
                                              '{}', '{}', '{}', '{}','{}',\
                                              '{}', '{}', '{}','{}', '{}', \
                                              '{}', '{}', '{}')".format(name, gender, 
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
                                                            imageurl)
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
                      baptisingpastor, formerreligion, name):
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
                                      WHERE name = '{}' ".format(gender,
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
                                                                 name)
        self.cursor.execute(update)
        print(update)
