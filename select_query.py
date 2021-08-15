#python select_query.py

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

# execute the query  and fetch all the records
query = 'SELECT * FROM MOVIE'
mycursor.execute(query)
result = mycursor.fetchall()

# we print our result
print(result)

# now we do iteration on each record and print
for record in result:
  print(record)

