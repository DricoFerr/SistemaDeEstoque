from conexion import get_db_connection
from mysql.connector import Error
from model.fornecedor import Fornecedor

class ControllerFornecedor:
    
    def adicionar_fornecedor(self, fornecedor: Fornecedor):
        """
        Adiciona um novo fornecedor ao banco de dados.
        """
        conn = get_db_connection()
        if conn is None:
            return False
        cursor = conn.cursor()
        query = "INSERT INTO Fornecedores (nome, telefone, email, endereco) VALUES (%s, %s, %s, %s)"
        values = (fornecedor.nome, fornecedor.telefone, fornecedor.email, fornecedor.endereco)
        try:
            cursor.execute(query, values)
            conn.commit()
            print(f"\n[SUCESSO] Fornecedor '{fornecedor.nome}' adicionado com o ID: {cursor.lastrowid}")
            return True
        except Error as e:
            print(f"\n[ERRO] O erro '{e}' ocorreu ao inserir o fornecedor")
            conn.rollback()
            return False
        finally:
            cursor.close()
            conn.close()

    def listar_fornecedores(self):
        """
        Lista todos os fornecedores do banco.
        """
        conn = get_db_connection()
        if conn is None:
            return []
        cursor = conn.cursor()
        query = "SELECT fornecedor_id, nome, telefone, email FROM Fornecedores"
        try:
            cursor.execute(query)
            rows = cursor.fetchall()
            return rows
        except Error as e:
            print(f"\n[ERRO] O erro '{e}' ocorreu ao listar os fornecedores")
            return []
        finally:
            cursor.close()
            conn.close()

    def atualizar_fornecedor(self, fornecedor: Fornecedor):
        """
        Atualiza um fornecedor existente no banco de dados.
        """
        conn = get_db_connection()
        if conn is None:
            return False
        cursor = conn.cursor()
        query = """UPDATE Fornecedores SET 
                       nome = %s, 
                       telefone = %s, 
                       email = %s, 
                       endereco = %s 
                   WHERE fornecedor_id = %s"""
        values = (fornecedor.nome, fornecedor.telefone, fornecedor.email, 
                  fornecedor.endereco, fornecedor.fornecedor_id)
        try:
            cursor.execute(query, values)
            conn.commit()
            if cursor.rowcount > 0:
                print(f"\n[SUCESSO] Fornecedor ID {fornecedor.fornecedor_id} foi atualizado.")
                return True
            else:
                print(f"\n[AVISO] Nenhum fornecedor com ID {fornecedor.fornecedor_id} foi encontrado para atualizar.")
                return False
        except Error as e:
            print(f"\n[ERRO] O erro '{e}' ocorreu ao atualizar o fornecedor")
            conn.rollback()
            return False
        finally:
            cursor.close()
            conn.close()

    def remover_fornecedor(self, fornecedor_id: int):
        """
        Remove um fornecedor do banco de dados.
        A remoção falhará se o fornecedor estiver associado a produtos ou compras.
        """
        conn = get_db_connection()
        if conn is None:
            return False
        cursor = conn.cursor()
        try:
            query_delete = "DELETE FROM Fornecedores WHERE fornecedor_id = %s"
            cursor.execute(query_delete, (fornecedor_id,))
            conn.commit()
            if cursor.rowcount > 0:
                print(f"\n[SUCESSO] Fornecedor com ID {fornecedor_id} foi removido.")
                return True
            else:
                print(f"\n[AVISO] Nenhum fornecedor com ID {fornecedor_id} foi encontrado.")
                return False
        except Error as e:
            if e.errno == 1451:
                print(f"\n[ERRO] O fornecedor com ID {fornecedor_id} não pode ser excluído, "
                      f"pois está associado a produtos ou compras existentes.")
            else:
                print(f"\n[ERRO] O erro '{e}' ocorreu ao remover o fornecedor")
            conn.rollback()
            return False
        finally:
            cursor.close()
            conn.close()
    
    def get_fornecedor_por_id(self, fornecedor_id: int):
        """
        Busca um fornecedor específico pelo seu ID.
        Retorna uma tupla com todos os dados do fornecedor se encontrado, caso contrário None.
        """
        conn = get_db_connection()
        if conn is None:
            return None

        cursor = conn.cursor()
        query = """SELECT fornecedor_id, nome, telefone, email, endereco 
                   FROM Fornecedores WHERE fornecedor_id = %s"""
        
        try:
            cursor.execute(query, (fornecedor_id,))
            row = cursor.fetchone()
            return row
        except Error as e:
            print(f"\n[ERRO] O erro '{e}' ocorreu ao buscar o fornecedor")
            return None
        finally:
            cursor.close()
            conn.close()

    def get_contagem_fornecedores(self):
        """Retorna a contagem de registros na tabela fornecedores."""
        conn = get_db_connection()
        if conn is None:
            return -1

        cursor = conn.cursor()
        query = "SELECT COUNT(1) FROM fornecedores"
        
        try:
            cursor.execute(query)
            result = cursor.fetchone()
            return result[0] if result else 0
        except Error as e:
            print(f"\n[ERRO] Não foi possível contar fornecedores: {e}")
            return -1
        finally:
            cursor.close()
            conn.close()