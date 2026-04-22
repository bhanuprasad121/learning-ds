import mysql.connector

def mysql_connection():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="pujari121000",
        database="pythondb"
    )
conn=mysql_connection()

    