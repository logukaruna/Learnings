import mysql.connector

mydb = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "@Logu2002"
)

mycursor = mydb.cursor()

mycursor.execute("SHOW DATABASES")

for i in mycursor:
    print(i)

print(mydb)