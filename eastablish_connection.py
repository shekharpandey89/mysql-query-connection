#python eastablish_connection.py

#import the library
import mysql.connector

# creating connection
conn = mysql.connector.connect(
  host="localhost",
  user="sammy",
  password="password"
)
# print the conn
print(conn)