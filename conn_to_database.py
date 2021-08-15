#python conn_to_database.py

#import the library
import mysql.connector

# creating connection to the database
conn = mysql.connector.connect(
  host="localhost",
  user="sammy",
  password="password",
  database="dbTest"
)
# print the conn
print(conn)
