from utils.helpers import limpar_tela, pausar
from controller.controller_produto import ControllerProduto
from controller.controller_fornecedor import ControllerFornecedor
from controller.controller_compra import ControllerCompra

def exibir_splash_screen():
    # Exibe a tela de abertura do sistema.
    
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
    print(" - Adriano Ferraz Guimarães")
    print(" - Filippo Salles Morais")
    print(" - Mário Márcio Holsbach")
    print(" - Ricardo Vasconcellos Drumond")
    
    print("\nDISCIPLINA: BANCO DE DADOS")
    print("PROFESSOR: HOWARD ROATTI")
    
    print("\n----------------------------------------------")
    print("TOTAL DE REGISTROS EXISTENTES:")
    
    print(f" 1 - FORNECEDORES: {ctrl_fornecedor.get_contagem_fornecedores()}")
    print(f" 2 - PRODUTOS:     {ctrl_produto.get_contagem_produtos()}")
    print(f" 3 - COMPRAS:      {ctrl_compra.get_contagem_compras()}")
    
    print("----------------------------------------------")
    pausar()