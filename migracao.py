import mysql.connector
from pymongo import MongoClient
import os
from dotenv import load_dotenv


load_dotenv()

def migrar_dados():
    
    print("Conectando ao MySQL...")
    try:
        conexao_sql = mysql.connector.connect(
            host="localhost", 
            user="root",      
            password="senha", 
            database="estoque"
        )
        cursor_sql = conexao_sql.cursor(dictionary=True)
    except Exception as e:
        print(f"Erro no MySQL: {e}")
        return

   
    print("Conectando ao MongoDB...")
    client_mongo = MongoClient("mongodb://localhost:27017/")
    db_mongo = client_mongo["sistema_estoque"]

    
    tabelas = ["fornecedores", "produtos"] 

    for tabela in tabelas:
        print(f"Migrando {tabela}...")
        cursor_sql.execute(f"SELECT * FROM {tabela}")
        dados = cursor_sql.fetchall()

        if dados:
            colecao = db_mongo[tabela]
            colecao.delete_many({}) 
            colecao.insert_many(dados)
            print(f"✅ {len(dados)} registros inseridos em '{tabela}'")
        else:
            print(f"⚠️ Tabela {tabela} vazia.")

    
    cursor_sql.close()
    conexao_sql.close()
    client_mongo.close()
    print("Migração Finalizada!")

if __name__ == "__main__":
    migrar_dados()