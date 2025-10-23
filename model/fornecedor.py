class Fornecedor:
    def __init__(self, nome: str, telefone: str, email: str, 
                 endereco: str, fornecedor_id: int = None):
        """
        Inicializa um objeto Fornecedor. 
        O fornecedor_id é opcional, pois é gerado pelo banco na inserção.
        """
        self.fornecedor_id = fornecedor_id
        self.nome = nome
        self.telefone = telefone
        self.email = email
        self.endereco = endereco

    def to_string(self):
        """ Retorna uma string formatada do objeto """
        return (f"ID: {self.fornecedor_id}, Nome: {self.nome}, Telefone: {self.telefone}, "
                f"Email: {self.email}")
