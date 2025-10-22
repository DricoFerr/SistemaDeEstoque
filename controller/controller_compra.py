from conexion import get_db_connection
from mysql.connector import Error

class ControllerCompra:
    
    def get_contagem_compras(self):
        """
        Retorna a contagem de registros na tabela compras.
        (Função auxiliar para a Splash Screen)
        """
        conn = get_db_connection()
        if conn is None:
            return -1

        cursor = conn.cursor()
        query = "SELECT COUNT(1) FROM compras"
        
        try:
            cursor.execute(query)
            result = cursor.fetchone()
            return result[0] if result else 0
        except Error as e:
            print(f"\n[ERRO] Não foi possível contar compras: {e}")
            return -1
        finally:
            cursor.close()
            conn.close()