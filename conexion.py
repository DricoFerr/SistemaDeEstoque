import mysql.connector
from mysql.connector import Error

def get_db_connection():
    try:
        connection = mysql.connector.connect(
            host="localhost", #Ajuste conforme necessário
            user="",
            password="",
            database="estoque"
        )
        if connection.is_connected():
            return connection
        else:
            print("\n[ERRO] Não foi possível estabelecer uma conexão com o banco de dados")
            return None
    except mysql.connector.Error as err:
        if err.errno == 2003:
            print("\n[ERRO] Não foi possível conectar ao servidor MySQL. Verifique se o servidor está rodando.")
        elif err.errno == 1045:
            print("\n[ERRO] Acesso negado. Verifique as credenciais de acesso (usuário/senha).")
        elif err.errno == 1049:
            print("\n[ERRO] Banco de dados 'estoque' não existe. Execute o script estoque.sql primeiro.")
        else:
            print(f"\n[ERRO] Erro ao conectar com o MySQL: {err}")
        return None