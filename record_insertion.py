#python record_insertion.py

#import the library
import mysql.connector

# creating connection to the database
conn = mysql.connector.connect(
  host="localhost",
  user="sammy",
  password="password",
  database="dbTest"
)

mycursor = conn.cursor()

# execute the query with their record value
query = 'insert into MOVIE(id, name, year)  \
       values (1, "Bruce Almighty", 2003 )'
mycursor.execute(query)

# we commit(save) the records to the table
conn.commit()

