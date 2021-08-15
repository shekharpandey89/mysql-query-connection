#python create_table.py

#import the library
import mysql.connector

# creating connection to the database
conn = mysql.connector.connect(
  host="localhost",
  user="sammy",
  password="password",
  database="dbTest"
)
# we create a mycursor object using the conn.cursor()
mycursor = conn.cursor()
mycursor.execute("DROP TABLE IF EXISTS MOVIE")

# we write a query to create a table
query = "CREATE TABLE MOVIE(id INT PRIMARY KEY,name varchar(30),year INT)"

# We execute the query here
mycursor.execute(query)

# after done the process, we close the connection
conn.close()
