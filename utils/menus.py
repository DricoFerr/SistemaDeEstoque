from utils.helpers import limpar_tela, pausar
from controller.controller_produto import ControllerProduto
from model.produto import Produto
from controller.controller_relatorios import ControllerRelatorios
# Importaremos os outros controllers conforme formos implementando
# from controller.controller_fornecedor import ControllerFornecedor
# from controller.controller_compra import ControllerCompra

def menu_principal():
    """
    Exibe o menu principal em loop, como pedido no edital[cite: 19, 35].
    """
    # Instanciamos o controller de produto uma vez para ser usado nos submenus
    ctrl_produto = ControllerProduto()

    while True:
        limpar_tela()
        print("##############################################")
        print("#            MENU PRINCIPAL                #")
        print("##############################################")
        print("\nEscolha uma das opções abaixo:")
        print("1 - Relatórios")      # [cite: 20]
        print("2 - Inserir Registros") # [cite: 21]
        print("3 - Remover Registros") # [cite: 22]
        print("4 - Atualizar Registros") # [cite: 23]
        print("5 - Sair")               # [cite: 24]
        
        opcao = input("\nDigite sua escolha: ")
        
        if opcao == '1':
            menu_relatorios()
        elif opcao == '2':
            # Passamos o controller para a função não precisar recriá-lo
            menu_inserir(ctrl_produto) 
        elif opcao == '3':
            menu_remover(ctrl_produto)
        elif opcao == '4':
            menu_atualizar(ctrl_produto)
        elif opcao == '5':
            print("\nSaindo do sistema. Até logo!")
            break # Quebra o loop 'while True'
        else:
            print("\nOpção inválida. Tente novamente.")
            pausar()

# --- SUBMENUS ---

def menu_inserir(ctrl_produto: ControllerProduto):
    """
    Menu para inserir registros[cite: 44].
    """
    while True:
        limpar_tela()
        print("##############################################")
        print("#            INSERIR REGISTROS             #")
        print("##############################################")
        
        # Requisito 6.b.1: Exibir menu de entidades [cite: 45]
        print("\nEm qual entidade você deseja inserir?")
        print("1 - Produtos")
        print("2 - Fornecedores (Não implementado)")
        print("3 - Compras (Não implementado)")
        print("4 - Voltar ao menu principal")
        opcao = input("Escolha uma opção: ")

        if opcao == '1':
            # Requisito 6.b.3: Solicitar atributos [cite: 47]
            print("\n--- Inserindo novo Produto ---")
            print("Por favor, informe os dados:")
            nome = input("Nome: ")
            descricao = input("Descrição: ")
            preco = float(input("Preço (ex: 150.75): "))
            qtd = int(input("Quantidade em Estoque: "))
            minimo = int(input("Estoque Mínimo: "))
            id_forn = int(input("ID do Fornecedor (deve existir): "))
            
            # 1. Criamos o objeto Model
            novo_produto = Produto(nome, descricao, preco, qtd, minimo, id_forn)
            
            # 2. Passamos o objeto para o Controller fazer a inserção [cite: 48]
            ctrl_produto.adicionar_produto(novo_produto)
            
            # Requisito 6.b.5: Perguntar se deseja inserir mais [cite: 49, 50]
            if not perguntar_sim_ou_nao("Deseja inserir mais um produto? (S/N): "):
                break # Sai do loop do 'menu_inserir' e volta pro principal

        elif opcao == '4':
            break # Sai do loop do 'menu_inserir' e volta pro principal
        else:
            print("\nOpção não implementada.")
            pausar()

def menu_remover(ctrl_produto: ControllerProduto):
    """
    Menu para remover registros, conforme Requisito 6.c.
    """
    while True:
        limpar_tela()
        print("##############################################")
        print("#             REMOVER REGISTROS            #")
        print("##############################################")
        
        # Requisito 6.c.1 e 6.c.2: Menu de entidades (simplificado por enquanto)
        print("\nQual entidade você deseja remover?")
        print("1 - Produtos")
        print("2 - Fornecedores (Não implementado)")
        print("3 - Voltar ao menu principal")
        opcao_entidade = input("Escolha uma opção: ")

        if opcao_entidade == '1':
            # Requisito 6.c.3: Listar os registros (ID e campo descritivo)
            # (Usamos a função auxiliar que já criamos)
            exibir_lista_produtos(ctrl_produto)
            
            try:
                # Requisito 6.c.4: Usuário seleciona a tupla (registro)
                produto_id_para_remover = int(input("Digite o ID do produto que deseja remover: "))
            except ValueError:
                print("\n[ERRO] ID inválido. Por favor, digite apenas números.")
                pausar()
                continue # Volta ao início do loop

            # Requisito 6.c.5: Confirmar com o usuário
            if perguntar_sim_ou_nao(f"Tem certeza que deseja remover o produto ID {produto_id_para_remover}? (S/N): "):
                # Requisito 6.c.5.i: (A verificação da FK é feita dentro do controller)
                ctrl_produto.remover_produto(produto_id_para_remover)
            else:
                print("\nOperação cancelada.")
            
            # Requisito 6.c.6: Perguntar se deseja remover mais algum
            if not perguntar_sim_ou_nao("Deseja remover mais algum produto? (S/N): "):
                break # Sai do loop do 'menu_remover' e volta pro principal

        elif opcao_entidade == '3':
            break # Sai do loop do 'menu_remover'
        else:
            print("\nOpção não implementada.")
            pausar()

def menu_atualizar(ctrl_produto: ControllerProduto):
    """
    Menu para atualizar registros, conforme Requisito 6.d.
    """
    while True:
        limpar_tela()
        print("##############################################")
        print("#           ATUALIZAR REGISTROS            #")
        print("##############################################")
        
        # Requisito 6.d.1 e 6.d.2: Menu de entidades
        print("\nQual entidade você deseja atualizar?")
        print("1 - Produtos")
        print("2 - Fornecedores (Não implementado)")
        print("3 - Voltar ao menu principal")
        opcao_entidade = input("Escolha uma opção: ")

        if opcao_entidade == '1':
            # Requisito 6.d.3: Listar os registros (ID e campo descritivo)
            exibir_lista_produtos(ctrl_produto)
            
            try:
                # Requisito 6.d.4: Usuário seleciona a tupla (registro)
                produto_id_para_atualizar = int(input("Digite o ID do produto que deseja atualizar: "))
            except ValueError:
                print("\n[ERRO] ID inválido. Por favor, digite apenas números.")
                pausar()
                continue # Volta ao início do loop

            # Requisito 6.d.5: Solicitar todos os atributos (exceto PK)
            print(f"\n--- Atualizando Produto ID {produto_id_para_atualizar} ---")
            print("Por favor, informe os NOVOS dados:")
            nome = input("Novo Nome: ")
            descricao = input("Nova Descrição: ")
            preco = float(input("Novo Preço (ex: 150.75): "))
            qtd = int(input("Nova Quantidade em Estoque: "))
            minimo = int(input("Novo Estoque Mínimo: "))
            id_forn = int(input("Novo ID do Fornecedor (deve existir): "))

            # Criamos um novo objeto Produto com todos os dados, incluindo o ID
            produto_atualizado = Produto(nome, descricao, preco, qtd, minimo, id_forn, produto_id_para_atualizar)

            # Passamos o objeto para o controller
            if ctrl_produto.atualizar_produto(produto_atualizado):
                # Requisito 6.d.7: Exiba o registro atualizado
                print("\nRegistro atualizado:")
                print(produto_atualizado.to_string())
            
            # Requisito 6.d.8: Perguntar se deseja atualizar mais algum
            if not perguntar_sim_ou_nao("\nDeseja atualizar mais algum produto? (S/N): "):
                break # Sai do loop do 'menu_atualizar' e volta pro principal

        elif opcao_entidade == '3':
            break # Sai do loop do 'menu_atualizar'
        else:
            print("\nOpção não implementada.")
            pausar()

def menu_relatorios():
    """
    Menu para exibir relatórios, conforme Requisito 6.a.
    """
    # Instanciamos o controller de relatórios
    ctrl_relatorios = ControllerRelatorios()
    
    while True:
        limpar_tela()
        print("##############################################")
        print("#            MENU DE RELATÓRIOS            #")
        print("##############################################")
        
        # O edital pede pelo menos duas opções 
        print("\nEscolha um relatório:")
        print("1 - Compras Agrupadas por Fornecedor (Sumarização)")
        print("2 - Relatório Detalhado de Compras (Junção)")
        print("3 - Voltar ao menu principal")
        opcao = input("Escolha uma opção: ")

        if opcao == '1':
            # Requisito 6.a.i: Sumarização 
            limpar_tela()
            print("--- Relatório: Compras Agrupadas por Fornecedor ---")
            rows = ctrl_relatorios.gerar_relatorio_compras_por_fornecedor()
            if not rows:
                print("Nenhum dado encontrado.")
            else:
                print(f"{'FORNECEDOR':<20} | {'Nº DE COMPRAS':<15} | {'VALOR TOTAL (R$)':<15}")
                print("-" * 55)
                for row in rows:
                    print(f"{row[0]:<20} | {row[1]:<15} | {row[2]:<15.2f}")
            pausar()

        elif opcao == '2':
            # Requisito 6.a.ii: Junção 
            limpar_tela()
            print("--- Relatório: Detalhado de Compras ---")
            rows = ctrl_relatorios.gerar_relatorio_detalhado_compras()
            if not rows:
                print("Nenhum dado encontrado.")
            else:
                print(f"{'ID':<4} | {'DATA':<20} | {'PRODUTO':<18} | {'FORNECEDOR':<18} | {'QTD':<5} | {'VALOR (R$)':<10}")
                print("-" * 83)
                for row in rows:
                    data_formatada = row[1].strftime('%Y-%m-%d %H:%M') # Formata a data
                    print(f"{row[0]:<4} | {data_formatada:<20} | {row[2]:<18} | {row[3]:<18} | {row[4]:<5} | {row[5]:<10.2f}")
            pausar()
            
        elif opcao == '3':
            break # Volta ao menu principal
        else:
            print("\nOpção inválida.")
            pausar()

# --- FUNÇÕES AUXILIARES DE MENU ---

def perguntar_sim_ou_nao(pergunta: str) -> bool:
    """ Função auxiliar para perguntas de 'Sim' ou 'Não' """
    while True:
        resposta = input(pergunta).strip().upper()
        if resposta == 'S':
            return True
        elif resposta == 'N':
            return False
        else:
            print("Resposta inválida. Por favor, digite 'S' para Sim ou 'N' para Não.")

def exibir_lista_produtos(ctrl_produto: ControllerProduto):
    """
    Busca e exibe a lista de produtos formatada.
    (Será usada nos menus de atualizar e remover)
    """
    print("\n--- Lista de Produtos Cadastrados ---")
    
    # 1. Busca os dados crus do controller
    produtos = ctrl_produto.listar_produtos()
    
    if not produtos:
        print("Nenhum produto encontrado no estoque.")
    else:
        # 2. Formata e exibe os dados
        for row in produtos:
            print(f"ID: {row[0]}, Nome: {row[1]}, Preço: R${row[2]}, Qtd em Estoque: {row[3]}")
    print("-------------------------------------\n")