import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="yuvrajRasal"
)

mycursor = mydb.cursor()

mycursor.execute("CREATE DATABASE python_new_pract_db")