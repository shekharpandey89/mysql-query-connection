#python create_a_database.py

#import the library
import mysql.connector

# creating connection
conn = mysql.connector.connect(
  host="localhost",
  user="sammy",
  password="password"
)
#print the connection
print(conn)
# import the cursor from the connection (conn)

mycursor = conn.cursor()
#print the mycursor
print(mycursor)

print(mycursor.execute("CREATE DATABASE Test"))