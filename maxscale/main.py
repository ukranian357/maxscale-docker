# Igor Nikolaev
#CNE 370 Maxscale_Docker Assignment
#W3Schools SQL was used for helping with remembering and find new SQL solutions along with old reference material from class with christine sutton learning SQL
# This is a working python Python script to query two sharded databses using Max-Scale Horizontal Load Balancing.
import mysql.connector

db = mysql.connector.connect(
        user = 'maxuser',
        password = 'maxpwd',
        host= '127.0.0.1',
        port = '4000'
    )
print("LARGEST ZIPCODE FROM DATABASE ONE SHARD1 ARCHIVE DISPLAYED BELOW")   
cursor = db.cursor()
cursor.execute("select max(zipcode) as max_zipcode from zipcodes_one.zipcodes_one;") 
maxzip = cursor.fetchall()
for maxzip in maxzip:
    print(maxzip)
    
print("ALL STATES WITH THE STATE KENTUCKY ARE DISPLAYED BELOW")  
cursor = db.cursor()
cursor.execute("select * from zipcodes_one.zipcodes_one where State='ky';")
KYstate = cursor.fetchall()
for KYstate in KYstate:
    print(KYstate)
    
print("ZIPCODES BETWEEN 40 and 41K DISPLAYED BELOW") 
cursor = db.cursor()
cursor.execute("select * from zipcodes_one.zipcodes_one where zipcode between 40000 and 41000;")
between = cursor.fetchall()
for between in between:
    print(between)
    
print("ALL WAGES IN THE STATE OF PA RECORDED IN ARCHIVE DISPLAYED BELOW!")    
cursor = db.cursor()
cursor.execute("select totalwages from zipcodes_one.zipcodes_one where state='pa';")
pawages = cursor.fetchall()
for pawages in pawages:
    print(pawages)
    
    
    
    
    
    



