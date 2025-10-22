from utils.helpers import limpar_tela, pausar
from controller.controller_produto import ControllerProduto
from controller.controller_fornecedor import ControllerFornecedor
from controller.controller_compra import ControllerCompra

def exibir_splash_screen():
    """
    Exibe a tela de abertura do sistema, como pedido no edital.
    """
    # Instanciamos os controllers para buscar as contagens
    ctrl_produto = ControllerProduto()
    ctrl_fornecedor = ControllerFornecedor()
    ctrl_compra = ControllerCompra()
    
    limpar_tela()
    print("##############################################")
    print("#                                            #")
    print("#           SISTEMA DE GESTÃO DE ESTOQUE     #")
    print("#                                            #")
    print("##############################################")
    print("\nCRIADO POR:")
    print(" - Adriano Ferraz Guimarães")       # PREENCHA COM SEU NOME
    print(" - Ricardo Vasconcellos")  # PREENCHA COM O NOME DO GRUPO
    
    print("\nDISCIPLINA: BANCO DE DADOS") # [cite: 31]
    print("PROFESSOR: HOWARD ROATTI")     # [cite: 3, 31]
    
    print("\n----------------------------------------------")
    print("TOTAL DE REGISTROS EXISTENTES:")
    
    # Busca a contagem das 3 tabelas 
    print(f" 1 - FORNECEDORES: {ctrl_fornecedor.get_contagem_fornecedores()}")
    print(f" 2 - PRODUTOS:     {ctrl_produto.get_contagem_produtos()}")
    print(f" 3 - COMPRAS:      {ctrl_compra.get_contagem_compras()}")
    
    print("----------------------------------------------")
    pausar()