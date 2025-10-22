from conexion import get_db_connection
from model.produto import Produto
from mysql.connector import Error

class ControllerProduto:
    
    def adicionar_produto(self, produto: Produto):
        """
        Adiciona um objeto Produto no banco de dados.
        Esta função substitui a antiga 'db_adicionar_produto'.
        """
        conn = get_db_connection()
        if conn is None:
            return False

        cursor = conn.cursor()
        query = """INSERT INTO produtos 
                   (nome, descricao, preco, quantidade_estoque, estoque_minimo, fornecedor_id) 
                   VALUES (%s, %s, %s, %s, %s, %s)"""
        
        # Pegamos os valores do objeto Produto
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
        """
        Lista todos os produtos do banco.
        Agora, esta função RETORNA os dados, em vez de imprimir.
        """
        conn = get_db_connection()
        if conn is None:
            return [] # Retorna lista vazia se a conexão falhar

        cursor = conn.cursor()
        query = "SELECT produto_id, nome, preco, quantidade_estoque FROM produtos"
        
        try:
            cursor.execute(query)
            rows = cursor.fetchall()
            return rows # Retorna os dados crus para o menu formatar
        except Error as e:
            print(f"\n[ERRO] O erro '{e}' ocorreu ao listar os produtos")
            return [] # Retorna lista vazia em caso de erro
        finally:
            cursor.close()
            conn.close()

    def get_contagem_produtos(self):
        """
        Retorna a contagem de registros na tabela produtos.
        (Função auxiliar para a Splash Screen [cite: 28])
        """
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
            # 1. VERIFICAÇÃO DE CHAVE ESTRANGEIRA (Requisito 6.c.5.i )
            # Vamos verificar se o produto existe na tabela 'compras'
            query_check_fk = "SELECT COUNT(1) FROM compras WHERE produto_id = %s"
            cursor.execute(query_check_fk, (produto_id,))
            resultado = cursor.fetchone()
            
            if resultado and resultado[0] > 0:
                # Se a contagem for > 0, o produto tem uma FK e não pode ser excluído
                print(f"\n[ERRO] O produto com ID {produto_id} não pode ser excluído, "
                      f"pois já está associado a {resultado[0]} compra(s).")
                return False

            # 2. SE A VERIFICAÇÃO PASSAR, REMOVE O PRODUTO
            query_delete = "DELETE FROM produtos WHERE produto_id = %s"
            cursor.execute(query_delete, (produto_id,))
            conn.commit()
            
            # cursor.rowcount armazena quantas linhas foram afetadas
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