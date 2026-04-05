import mysql.connector
import os
from dotenv import load_dotenv
from contextlib import contextmanager
# import logging

# Carrega as variáveis de ambiente
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

# Gerenciador de contexto para a conexão com o banco de dados
@contextmanager
def connection_manager():
    cnx = get_db_connection()

    try:
        cursor = cnx.cursor()
        yield cursor
    finally:
        cnx.commit()
        cursor.close()
        cnx.close()
