import mysql.connector
import os
from dotenv import load_dotenv

load_dotenv()

def get_db_connection():
    cnx = mysql.connector.connect(
        user=os.getenv('MYSQL_USER'),
        password=os.getenv('MYSQL_PASSWORD'),
        host=os.getenv('MYSQL_HOST'),
        database=os.getenv('MYSQL_DATABASE'),
        port=3307
    )
    return cnx
