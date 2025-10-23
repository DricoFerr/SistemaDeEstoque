from datetime import datetime

class Compra:
    def __init__(self, produto_id: int, fornecedor_id: int, quantidade: int, 
                 valor_total: float, data_compra: datetime = None, compra_id: int = None):
        """
        Inicializa um objeto Compra.
        O compra_id é opcional, pois é gerado pelo banco.
        A data_compra pode ser gerada automaticamente.
        """
        self.compra_id = compra_id
        self.produto_id = produto_id
        self.fornecedor_id = fornecedor_id
        self.quantidade = quantidade
        self.valor_total = valor_total
        # Se a data não for fornecida, usa a data e hora atuais
        self.data_compra = data_compra if data_compra is not None else datetime.now()

    def to_string(self):
        """ Retorna uma string formatada do objeto """
        return (f"ID Compra: {self.compra_id}, ID Produto: {self.produto_id}, "
                f"Qtd: {self.quantidade}, Valor: R${self.valor_total}, "
                f"Data: {self.data_compra.strftime('%Y-%m-%d %H:%M')}")
