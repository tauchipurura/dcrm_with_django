import mysql.connector


database = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    password = 'h1213034k'
)

#prepare curso object
cursorObject = database.cursor()

#create database
cursorObject.execute("CREATE DATABASE tauchip")

print("All Done")
