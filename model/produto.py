class Produto:
    def __init__(self, nome: str, descricao: str, preco: float, 
                 quantidade_estoque: int, estoque_minimo: int, 
                 fornecedor_id: int, produto_id: int = None):
        """
        Inicializa um objeto Produto. 
        O produto_id é opcional, pois é gerado pelo banco na inserção.
        """
        self.produto_id = produto_id
        self.nome = nome
        self.descricao = descricao
        self.preco = preco
        self.quantidade_estoque = quantidade_estoque
        self.estoque_minimo = estoque_minimo
        self.fornecedor_id = fornecedor_id

    def to_string(self):
        """Retorna uma string formatada do objeto"""
        return (f"ID: {self.produto_id}, Nome: {self.nome}, Preço: R${self.preco}, "
                f"Qtd: {self.quantidade_estoque}")