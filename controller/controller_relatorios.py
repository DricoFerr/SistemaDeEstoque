from conexion import get_db_connection
from mysql.connector import Error

class ControllerRelatorios:

    def gerar_relatorio_compras_por_fornecedor(self):
        """
        Relatório de Sumarização (Requisito 6.a.i):
        Mostra o valor total e a contagem de compras agrupados por fornecedor.
        """
        conn = get_db_connection()
        if conn is None:
            return []

        cursor = conn.cursor()
        # Query para sumarizar as compras por fornecedor
        query = """
           SELECT 
  f.nome AS fornecedor,
  COUNT(c.compra_id) AS total_compras,
  SUM(c.quantidade * p.preco) AS total_gasto
FROM compras c
JOIN fornecedores f ON f.fornecedor_id = c.fornecedor_id
JOIN produtos p ON p.produto_id = c.produto_id
GROUP BY f.fornecedor_id, f.nome
ORDER BY total_gasto DESC;
        """
        
        try:
            cursor.execute(query)
            rows = cursor.fetchall()
            return rows
        except Error as e:
            print(f"\n[ERRO] O erro '{e}' ocorreu ao gerar o relatório de sumarização")
            return []
        finally:
            cursor.close()
            conn.close()

    def gerar_relatorio_detalhado_compras(self):
        """
        Relatório de Junção (Requisito 6.a.ii):
        Lista todas as compras, mostrando os nomes do produto e do fornecedor.
        """
        conn = get_db_connection()
        if conn is None:
            return []

        cursor = conn.cursor()
        # Query para juntar as tabelas de compras, produtos e fornecedores
        query = """
            SELECT 
                c.compra_id,
                c.data_compra,
                p.nome AS nome_produto,
                f.nome AS nome_fornecedor,
                c.quantidade,
                c.valor_total
            FROM Compras c
            JOIN Produtos p ON c.produto_id = p.produto_id
            JOIN Fornecedores f ON c.fornecedor_id = f.fornecedor_id
            ORDER BY c.data_compra DESC
        """
        
        try:
            cursor.execute(query)
            rows = cursor.fetchall()
            return rows
        except Error as e:
            print(f"\n[ERRO] O erro '{e}' ocorreu ao gerar o relatório de junção")
            return []
        finally:
            cursor.close()
            conn.close()

    def gerar_relatorio_estoque_baixo(self):
        """
        Relatório de Estoque Baixo (Requisito do Tema):
        Lista produtos onde a quantidade atual está abaixo do estoque mínimo.
        """
        conn = get_db_connection()
        if conn is None:
            return []

        cursor = conn.cursor()
        # Query para selecionar produtos com estoque < minimo, juntando com fornecedores
        query = """
            SELECT 
                p.produto_id,
                p.nome,
                p.quantidade_estoque,
                p.estoque_minimo,
                p.estoque_minimo - p.quantidade_estoque AS necessita_comprar,
                f.nome AS nome_fornecedor,
                f.telefone AS telefone_fornecedor
            FROM produtos p
            JOIN fornecedores f ON p.fornecedor_id = f.fornecedor_id
            WHERE p.quantidade_estoque < p.estoque_minimo
            ORDER BY necessita_comprar DESC;
        """
        
        try:
            cursor.execute(query)
            rows = cursor.fetchall()
            return rows
        except Error as e:
            print(f"\n[ERRO] O erro '{e}' ocorreu ao gerar o relatório de estoque baixo")
            return []
        finally:
            cursor.close()
            conn.close()