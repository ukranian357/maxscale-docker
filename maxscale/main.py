# This is a sample Python script.
import mysql.connector

def connect_to_db () :
    con = mysql.connector.connect(
        user = 'maxuser',
        password = 'maxpwd',
        host= '127.0.0.1',
        port = '4000'
    )
    return con

def query(cursor, query):
    cursor.execute("SELECT * FROM `zipcodes_two` WHERE State=%s", [Kentucky])
        query = return cursor.fetchall()



