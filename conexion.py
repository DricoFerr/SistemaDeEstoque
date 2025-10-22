import mysql.connector
from mysql.connector import Error

def get_db_connection():
    try:
        connection = mysql.connector.connect(
            host="localhost",
            user="root",
            password="Dico1707.",
            database="estoque"
        )
        return connection
    except mysql.connector.Error as err:
        print(f"Erro ao conectar com o MySQL: {err}")
        return None