from conexion import get_db_connection
from mysql.connector import Error
from model.compra import Compra

class ControllerCompra:
    
    def adicionar_compra(self, compra: Compra):
        """
        Adiciona um novo registro de compra e atualiza o estoque do produto.
        Tudo é feito dentro de uma transação para garantir a consistência dos dados.
        """
        conn = get_db_connection()
        if conn is None:
            return False
        cursor = conn.cursor()
        
        try:
            # A transação garante que ambas as operações (inserir compra e atualizar estoque)
            # ocorram com sucesso, ou nenhuma delas é aplicada.
            conn.start_transaction()

            # 1. Insere o registro na tabela de compras
            query_insert_compra = """INSERT INTO Compras 
                                     (produto_id, fornecedor_id, quantidade, data_compra, valor_total) 
                                     VALUES (%s, %s, %s, %s, %s)"""
            values_compra = (compra.produto_id, compra.fornecedor_id, compra.quantidade, 
                             compra.data_compra, compra.valor_total)
            cursor.execute(query_insert_compra, values_compra)
            compra_id = cursor.lastrowid

            # 2. Atualiza o estoque do produto
            query_update_estoque = """UPDATE Produtos 
                                      SET quantidade_estoque = quantidade_estoque + %s 
                                      WHERE produto_id = %s"""
            values_estoque = (compra.quantidade, compra.produto_id)
            cursor.execute(query_update_estoque, values_estoque)

            conn.commit()
            print(f"\n[SUCESSO] Compra ID {compra_id} registrada e estoque do produto ID {compra.produto_id} atualizado.")
            return True

        except Error as e:
            # Se ocorrer qualquer erro, desfaz todas as alterações (rollback)
            print(f"\n[ERRO] O erro '{e}' ocorreu ao registrar a compra. A operação foi cancelada.")
            conn.rollback()
            return False
        finally:
            cursor.close()
            conn.close()

    def get_contagem_compras(self):
        """Retorna a contagem de registros na tabela compras."""
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