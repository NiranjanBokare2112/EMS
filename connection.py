import mysql.connector
from mysql.connector import Error

def create_connection():
    try:
        connection = mysql.connector.connect(
            host='localhost',        # Replace with your database host
            database='emp_mng',      # Replace with your actual database name
            user='root',             # Replace with your MySQL username
            password='Manisha@21'    # Replace with your MySQL password
        )
        if connection.is_connected():
            print()
        return connection
    except Error as e:
        print(f"Error while connecting to MySQL: {e}")
        return None
