from conexion import get_db_connection
from model.produto import Produto
from mysql.connector import Error

class ControllerProduto:
    
    def adicionar_produto(self, produto: Produto):
        """Adiciona um objeto Produto no banco de dados."""
        conn = get_db_connection()
        if conn is None:
            return False

        cursor = conn.cursor()
        query = """INSERT INTO produtos 
                   (nome, descricao, preco, quantidade_estoque, estoque_minimo, fornecedor_id) 
                   VALUES (%s, %s, %s, %s, %s, %s)"""
        
        values = (produto.nome, produto.descricao, produto.preco, 
                  produto.quantidade_estoque, produto.estoque_minimo, produto.fornecedor_id)

        try:
            cursor.execute(query, values)
            conn.commit()
            print(f"\n[SUCESSO] Produto '{produto.nome}' adicionado com o ID: {cursor.lastrowid}")
            return True
        except Error as e:
            print(f"\n[ERRO] O erro '{e}' ocorreu ao inserir o produto")
            conn.rollback()
            return False
        finally:
            cursor.close()
            conn.close()

    def listar_produtos(self):
        """Lista todos os produtos do banco."""
        conn = get_db_connection()
        if conn is None:
            return [] 

        cursor = conn.cursor()
        query = "SELECT produto_id, nome, preco, quantidade_estoque FROM produtos"
        
        try:
            cursor.execute(query)
            rows = cursor.fetchall()
            return rows
        except Error as e:
            print(f"\n[ERRO] O erro '{e}' ocorreu ao listar os produtos")
            return [] 
        finally:
            cursor.close()
            conn.close()

    def get_produto_por_id(self, produto_id: int):
        """
        Busca um produto específico pelo seu ID.
        Retorna os dados do produto (incluindo preço) se encontrado, caso contrário None.
        """
        conn = get_db_connection()
        if conn is None:
            return None

        cursor = conn.cursor()
        # Retornamos mais campos para ter o preço e o nome
        query = "SELECT produto_id, nome, preco, quantidade_estoque FROM produtos WHERE produto_id = %s"
        
        try:
            cursor.execute(query, (produto_id,))
            row = cursor.fetchone()
            return row # Retorna a tupla com os dados do produto
        except Error as e:
            print(f"\n[ERRO] O erro '{e}' ocorreu ao buscar o produto")
            return None
        finally:
            cursor.close()
            conn.close()

    def get_contagem_produtos(self):
        """Retorna a contagem de registros na tabela produtos."""
        conn = get_db_connection()
        if conn is None:
            return -1

        cursor = conn.cursor()
        query = "SELECT COUNT(1) FROM produtos"
        
        try:
            cursor.execute(query)
            result = cursor.fetchone()
            return result[0] if result else 0
        except Error as e:
            print(f"\n[ERRO] Não foi possível contar produtos: {e}")
            return -1
        finally:
            cursor.close()
            conn.close()

    def get_totais_estoque(self):
        """Retorna a quantidade total de itens e o valor total do estoque."""
        conn = get_db_connection()
        if conn is None:
            return (0, 0.0)

        cursor = conn.cursor()
        query = """
            SELECT 
                SUM(quantidade_estoque) as total_itens,
                SUM(quantidade_estoque * preco) as valor_total
            FROM produtos
        """
        
        try:
            cursor.execute(query)
            result = cursor.fetchone()
            return (result[0] or 0, result[1] or 0.0)  # Retorna 0 se for None
        except Error as e:
            print(f"\n[ERRO] Não foi possível calcular totais do estoque: {e}")
            return (0, 0.0)
        finally:
            cursor.close()
            conn.close()

    def remover_produto(self, produto_id: int):
        """
        Remove um produto do banco de dados, se não houver FKs (compras)
        associadas a ele.
        Retorna True se removido, False se houver erro ou FK.
        """
        conn = get_db_connection()
        if conn is None:
            return False

        cursor = conn.cursor()
        
        try:
            # Requisito 6.c.5.i: Verifica se o registro é uma FK em outra tabela
            query_check_fk = "SELECT COUNT(1) FROM compras WHERE produto_id = %s"
            cursor.execute(query_check_fk, (produto_id,))
            resultado = cursor.fetchone()
            
            if resultado and resultado[0] > 0:
                print(f"\n[ERRO] O produto com ID {produto_id} não pode ser excluído, "
                      f"pois já está associado a {resultado[0]} compra(s).")
                return False

            # Se a verificação passar, remove o produto
            query_delete = "DELETE FROM produtos WHERE produto_id = %s"
            cursor.execute(query_delete, (produto_id,))
            conn.commit()
            
            if cursor.rowcount > 0:
                print(f"\n[SUCESSO] Produto com ID {produto_id} foi removido.")
                return True
            else:
                print(f"\n[AVISO] Nenhum produto com ID {produto_id} foi encontrado.")
                return False

        except Error as e:
            print(f"\n[ERRO] O erro '{e}' ocorreu ao remover o produto")
            conn.rollback()
            return False
        finally:
            cursor.close()
            conn.close()

    def atualizar_produto(self, produto: Produto):
        """
        Atualiza um produto no banco de dados usando seu 'produto_id'.
        O objeto 'produto' deve conter o 'produto_id' do registro a ser atualizado.
        Retorna True se atualizado, False se houver erro.
        """
        conn = get_db_connection()
        if conn is None:
            return False

        cursor = conn.cursor()
        
        # Requisito 6.d.6: Realiza a atualização da tupla
        query = """UPDATE produtos SET 
                       nome = %s, 
                       descricao = %s, 
                       preco = %s, 
                       quantidade_estoque = %s, 
                       estoque_minimo = %s, 
                       fornecedor_id = %s 
                   WHERE produto_id = %s"""
        
        values = (produto.nome, produto.descricao, produto.preco, 
                  produto.quantidade_estoque, produto.estoque_minimo, 
                  produto.fornecedor_id, produto.produto_id)

        try:
            cursor.execute(query, values)
            conn.commit()
            
            if cursor.rowcount > 0:
                print(f"\n[SUCESSO] Produto ID {produto.produto_id} foi atualizado.")
                return True
            else:
                print(f"\n[AVISO] Nenhum produto com ID {produto.produto_id} foi encontrado para atualizar.")
                return False

        except Error as e:
            print(f"\n[ERRO] O erro '{e}' ocorreu ao atualizar o produto")
            conn.rollback()
            return False
        finally:
            cursor.close()
            conn.close()

    def get_produto_completo_por_id(self, produto_id: int):
        """
        Busca um produto específico pelo seu ID com TODOS os campos.
        Retorna uma tupla com os dados se encontrado, caso contrário None.
        """
        conn = get_db_connection()
        if conn is None:
            return None

        cursor = conn.cursor()
        # Query para retornar todos os campos necessários para o objeto Produto
        query = """SELECT produto_id, nome, descricao, preco, 
                          quantidade_estoque, estoque_minimo, fornecedor_id 
                   FROM produtos WHERE produto_id = %s"""
        
        try:
            cursor.execute(query, (produto_id,))
            row = cursor.fetchone()
            return row # Retorna a tupla com todos os dados do produto
        except Error as e:
            print(f"\n[ERRO] O erro '{e}' ocorreu ao buscar o produto completo")
            return None
        finally:
            cursor.close()
            conn.close()

    def get_fornecedor_por_id(self, fornecedor_id: int):
        """
        Busca um fornecedor específico pelo seu ID com TODOS os campos.
        Retorna uma tupla com os dados se encontrado, caso contrário None.
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
            return row # Retorna a tupla com todos os dados do fornecedor
        except Error as e:
            print(f"\n[ERRO] O erro '{e}' ocorreu ao buscar o fornecedor")
            return None
        finally:
            cursor.close()
            conn.close()