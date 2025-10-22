from conexion import get_db_connection
from mysql.connector import Error

class ControllerFornecedor:
    
    def get_contagem_fornecedores(self):
        """
        Retorna a contagem de registros na tabela fornecedores.
        (Função auxiliar para a Splash Screen)
        """
        conn = get_db_connection()
        if conn is None:
            return -1 # Retorna -1 em caso de erro

        cursor = conn.cursor()
        query = "SELECT COUNT(1) FROM fornecedores"
        
        try:
            cursor.execute(query)
            result = cursor.fetchone()
            # Retorna o primeiro item da tupla (a contagem), ou 0 se a tabela estiver vazia
            return result[0] if result else 0
        except Error as e:
            print(f"\n[ERRO] Não foi possível contar fornecedores: {e}")
            return -1
        finally:
            cursor.close()
            conn.close()