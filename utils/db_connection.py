import mysql.connector
from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

# Get MySQL connection details from environment variables
host = os.getenv("MYSQL_HOST")
user = os.getenv("MYSQL_USER")
password = os.getenv("MYSQL_PASSWORD")
database = os.getenv("MYSQL_DATABASE")

# Connect to the MySQL server
cnx = mysql.connector.connect(
    host=host,
    user=user,
    password=password,
    database=database
)

def conn():
    # Connect to the MySQL server
    cnx = mysql.connector.connect(
        host=host,
        user=user,
        password=password,
        database=database
    )

    # Check if the connection is successful
    if cnx.is_connected():
        print("Connected to MySQL database")

    return cnx