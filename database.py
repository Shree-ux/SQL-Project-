import mysql.connector

def create_connection():
    connection = mysql.connector.connect(
        host="localhost",
        user="root",
        password="shreejit",
        database="EduSchema"
    )
    return connection
