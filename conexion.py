from pymongo import MongoClient
from pymongo.errors import ConnectionFailure

def get_db_connection():
    try:

        client = MongoClient("mongodb://localhost:27017/")
        
        # Verifica se a conexão está ativa
        client.admin.command('ping')
        
        db = client["estoque"] 
        return db

    except ConnectionFailure as e:
        print(f"\n[ERRO] Não foi possível conectar ao MongoDB: {e}")
        return None