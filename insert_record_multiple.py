#python insert_record_multiple.py

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
query = 'INSERT INTO MOVIE (id, name, year) VALUES (%s, %s, %s)'
val = [(2, "Kung Fu panda", 2014),
       (4, "Frozen", 2014),
       (5, "Frozen2", 2020),
       (6, "Iron Man", 2013)

       ]

mycursor.executemany(query,val)

# we commit(save) the records to the table
conn.commit()

print(mycursor.rowcount, "record(s) inserted.")