from utils.helpers import limpar_tela, pausar
from controller.controller_produto import ControllerProduto
from model.produto import Produto
from controller.controller_relatorios import ControllerRelatorios
from controller.controller_fornecedor import ControllerFornecedor
from model.fornecedor import Fornecedor
from controller.controller_compra import ControllerCompra
from model.compra import Compra

def menu_principal():
    """Exibe o menu principal em loop (Requisito 5.a)."""
    # Instancia os controllers que serão usados pelos submenus
    ctrl_produto = ControllerProduto()
    ctrl_fornecedor = ControllerFornecedor()
    ctrl_compra = ControllerCompra()

    def exibir_totais():
        """Função auxiliar para exibir os totais atualizados"""
        print("\n----------------------------------------------")
        print("TOTAL DE REGISTROS EXISTENTES:")
        print(f" - FORNECEDORES: {ctrl_fornecedor.get_contagem_fornecedores()}")
        print(f" - PRODUTOS:     {ctrl_produto.get_contagem_produtos()}")
        print(f" - COMPRAS:      {ctrl_compra.get_contagem_compras()}")
        
        # Busca e exibe os totais do estoque
        qtd_total, valor_total = ctrl_produto.get_totais_estoque()
        print("\nINFORMAÇÕES DO ESTOQUE:")
        print(f" - QUANTIDADE TOTAL DE ITENS: {qtd_total}")
        print(f" - VALOR TOTAL DO ESTOQUE: R$ {valor_total:.2f}")
        print("----------------------------------------------")

    while True:
        limpar_tela()
        print("##############################################")
        print("#            MENU PRINCIPAL                  #")
        print("##############################################")
        print("\nEscolha uma das opções abaixo:")
        print("1 - Relatórios")
        print("2 - Inserir Registros")
        print("3 - Remover Registros")
        print("4 - Atualizar Registros")
        print("5 - Estoque")
        print("6 - Sair")
        
        # Exibe os totais atualizados
        exibir_totais()
        
        opcao = input("\nDigite sua escolha: ")
        
        if opcao == '1':
            menu_relatorios()
        elif opcao == '2':
            menu_inserir(ctrl_produto, ctrl_fornecedor, ctrl_compra) 
        elif opcao == '3':
            menu_remover(ctrl_produto, ctrl_fornecedor)
        elif opcao == '4':
            menu_atualizar(ctrl_produto, ctrl_fornecedor)
        elif opcao == '5':
            menu_estoque(ctrl_produto)
        elif opcao == '6':
            print("\nSaindo do sistema. Até logo!")
            break
        else:
            print("\nOpção inválida. Tente novamente.")
            pausar()

# --- SUBMENUS ---

def menu_inserir(ctrl_produto: ControllerProduto, ctrl_fornecedor: ControllerFornecedor, ctrl_compra: ControllerCompra):
    """Menu para inserir registros (Requisito 6.b)."""
    while True:
        limpar_tela()
        print("##############################################")
        print("#            INSERIR REGISTROS             #")
        print("##############################################")
        
        # Requisito 6.b.1: Exibe menu de entidades
        print("\nEm qual entidade você deseja inserir?")
        print("1 - Produtos")
        print("2 - Fornecedores")
        print("3 - Compras")
        print("4 - Voltar ao menu principal")
        opcao = input("Escolha uma opção: ")

        if opcao == '1':
            # Requisito 6.b.3: Solicita atributos da entidade
            print("\n--- Inserindo novo Produto ---")
            exibir_lista_fornecedores(ctrl_fornecedor)
            print("Por favor, informe os dados:")
            nome = input("Nome: ")
            
            # --- VALIDAÇÃO DE NOME VAZIO ---
            if not nome.strip():
                print("\n[ERRO] O nome do produto não pode ser vazio.")
                pausar()
                continue
            # --- FIM DA VALIDAÇÃO ---

            descricao = input("Descrição: ")
            try:
                preco = float(input("Preço (ex: 150.75): "))
                qtd = int(input("Quantidade em Estoque: "))
                minimo = int(input("Estoque Mínimo: "))
                id_forn = int(input("ID do Fornecedor (deve existir): "))
            except ValueError:
                print("\n[ERRO] Entrada inválida para preço, quantidade ou ID. Tente novamente.")
                pausar()
                continue
            
            novo_produto = Produto(nome, descricao, preco, qtd, minimo, id_forn)
            ctrl_produto.adicionar_produto(novo_produto)
            
            # Requisito 6.b.5: Pergunta ao usuário se deseja inserir mais registros
            if not perguntar_sim_ou_nao("Deseja inserir mais um registro? (S/N): "):
                break

        elif opcao == '2':
            print("\n--- Inserindo novo Fornecedor ---")
            print("Por favor, informe os dados:")
            nome = input("Nome: ")

            # --- VALIDAÇÃO DE NOME VAZIO ---
            if not nome.strip():
                print("\n[ERRO] O nome do fornecedor não pode ser vazio.")
                pausar()
                continue
            # --- FIM DA VALIDAÇÃO ---

            telefone = input("Telefone (ex: (27) 99999-8888): ")
            email = input("Email: ")
            endereco = input("Endereço: ")
            
            novo_fornecedor = Fornecedor(nome, telefone, email, endereco)
            ctrl_fornecedor.adicionar_fornecedor(novo_fornecedor)
            
            if not perguntar_sim_ou_nao("Deseja inserir mais um registro? (S/N): "):
                break

        elif opcao == '3':
            print("\n--- Registrando nova Compra ---")
            print("Isso também irá atualizar o estoque do produto.")
            exibir_lista_produtos(ctrl_produto)
            exibir_lista_fornecedores(ctrl_fornecedor)
            
            try:
                produto_id = int(input("ID do Produto comprado: "))
                
                produto_dados = ctrl_produto.get_produto_por_id(produto_id)
                if not produto_dados:
                    print(f"\n[ERRO] Produto com ID {produto_id} não encontrado.")
                    pausar()
                    continue

                preco_unitario = produto_dados[2]  # O preço é o 3º item (índice 2)
                nome_produto = produto_dados[1]
                print(f"Produto selecionado: {nome_produto} (Preço Unitário: R$ {preco_unitario:.2f})")

                fornecedor_id = int(input("ID do Fornecedor que vendeu: "))
                quantidade = int(input("Quantidade comprada: "))

                valor_total = preco_unitario * quantidade
                print(f"O valor total da compra é: R$ {valor_total:.2f}")

                if perguntar_sim_ou_nao("Deseja confirmar o registro desta compra? (S/N)"):
                    nova_compra = Compra(produto_id, fornecedor_id, quantidade, valor_total)
                    ctrl_compra.adicionar_compra(nova_compra)
                else:
                    print("\nRegistro de compra cancelado.")

            except ValueError:
                print("\n[ERRO] Entrada inválida. Por favor, use números para IDs e quantidade.")
                pausar()
                continue

            if not perguntar_sim_ou_nao("Deseja registrar mais uma compra? (S/N): "):
                break

        elif opcao == '4':
            break
        else:
            print("\nOpção inválida.")
            pausar()

def menu_remover(ctrl_produto: ControllerProduto, ctrl_fornecedor: ControllerFornecedor):
    """Menu para remover registros (Requisito 6.c)."""
    while True:
        limpar_tela()
        print("##############################################")
        print("#             REMOVER REGISTROS            #")
        print("##############################################")
        
        # Requisito 6.c.1 e 6.c.2: Menu de entidades
        print("\nQual entidade você deseja remover?")
        print("1 - Produtos")
        print("2 - Fornecedores")
        print("3 - Voltar ao menu principal")
        opcao_entidade = input("Escolha uma opção: ")

        if opcao_entidade == '1':
            # Requisito 6.c.3: Lista os registros da entidade selecionada
            exibir_lista_produtos(ctrl_produto)
            try:
                produto_id_para_remover = int(input("Digite o ID do produto que deseja remover: "))
            except ValueError:
                print("\n[ERRO] ID inválido. Por favor, digite apenas números.")
                pausar()
                continue

            # Requisito 6.c.5: Confirma a remoção
            if perguntar_sim_ou_nao(f"Tem certeza que deseja remover o produto ID {produto_id_para_remover}? (S/N): "):
                ctrl_produto.remover_produto(produto_id_para_remover)
            else:
                print("\nOperação cancelada.")
            
            # Requisito 6.c.6: Pergunta se deseja remover mais algum
            if not perguntar_sim_ou_nao("Deseja remover mais algum registro? (S/N): "):
                break

        elif opcao_entidade == '2':
            exibir_lista_fornecedores(ctrl_fornecedor)
            try:
                fornecedor_id_para_remover = int(input("Digite o ID do fornecedor que deseja remover: "))
            except ValueError:
                print("\n[ERRO] ID inválido. Por favor, digite apenas números.")
                pausar()
                continue

            if perguntar_sim_ou_nao(f"Tem certeza que deseja remover o fornecedor ID {fornecedor_id_para_remover}? (S/N): "):
                ctrl_fornecedor.remover_fornecedor(fornecedor_id_para_remover)
            else:
                print("\nOperação cancelada.")
            
            if not perguntar_sim_ou_nao("Deseja remover mais algum registro? (S/N): "):
                break

        elif opcao_entidade == '3':
            break
        else:
            print("\nOpção inválida.")
            pausar()

def menu_atualizar(ctrl_produto: ControllerProduto, ctrl_fornecedor: ControllerFornecedor):
    """Menu para atualizar registros (Requisito 6.d)."""
    while True:
        limpar_tela()
        print("##############################################")
        print("#           ATUALIZAR REGISTROS            #")
        print("##############################################")
        
        # Requisito 6.d.1 e 6.d.2: Menu de entidades
        print("\nQual entidade você deseja atualizar?")
        print("1 - Produtos")
        print("2 - Fornecedores")
        print("3 - Voltar ao menu principal")
        opcao_entidade = input("Escolha uma opção: ")

        if opcao_entidade == '1':
            # Requisito 6.d.3: Lista os registros
            exibir_lista_produtos(ctrl_produto)
            try:
                produto_id_para_atualizar = int(input("Digite o ID do produto que deseja atualizar: "))
            except ValueError:
                print("\n[ERRO] ID inválido. Por favor, digite apenas números.")
                pausar()
                continue
            
            # --- NOVA LÓGICA: BUSCAR DADOS ANTIGOS ---
            produto_antigo_tupla = ctrl_produto.get_produto_completo_por_id(produto_id_para_atualizar)
            
            if not produto_antigo_tupla:
                print(f"\n[ERRO] Produto com ID {produto_id_para_atualizar} não encontrado.")
                pausar()
                continue
            
            # Converte a tupla em um objeto Produto para fácil acesso
            # (id, nome, desc, preco, qtd, min, forn_id)
            produto_antigo = Produto(
                nome=produto_antigo_tupla[1], 
                descricao=produto_antigo_tupla[2], 
                preco=produto_antigo_tupla[3], 
                quantidade_estoque=produto_antigo_tupla[4], 
                estoque_minimo=produto_antigo_tupla[5], 
                fornecedor_id=produto_antigo_tupla[6], 
                produto_id=produto_antigo_tupla[0]
            )

            # Requisito 6.d.5: Solicita os novos dados
            print(f"\n--- Atualizando Produto ID {produto_id_para_atualizar} ---")
            print("(Pressione Enter para manter o valor atual)")

            try:
                # Se o input for vazio, usa o valor antigo
                nome = input(f"Novo Nome (Atual: {produto_antigo.nome}): ") or produto_antigo.nome
                if not nome.strip(): # Validação para não deixar o nome ficar vazio
                     print("\n[AVISO] Nome mantido. Não é permitido salvar um nome vazio.")
                     nome = produto_antigo.nome

                descricao = input(f"Nova Descrição (Atual: {produto_antigo.descricao}): ") or produto_antigo.descricao

                # Lógica especial para números (float/int)
                preco_input = input(f"Novo Preço (Atual: {produto_antigo.preco:.2f}): ")
                preco = float(preco_input) if preco_input.strip() else produto_antigo.preco

                qtd_input = input(f"Nova Qtd em Estoque (Atual: {produto_antigo.quantidade_estoque}): ")
                qtd = int(qtd_input) if qtd_input.strip() else produto_antigo.quantidade_estoque
                
                minimo_input = input(f"Novo Estoque Mínimo (Atual: {produto_antigo.estoque_minimo}): ")
                minimo = int(minimo_input) if minimo_input.strip() else produto_antigo.estoque_minimo

                id_forn_input = input(f"Novo ID do Fornecedor (Atual: {produto_antigo.fornecedor_id}): ")
                id_forn = int(id_forn_input) if id_forn_input.strip() else produto_antigo.fornecedor_id

            except ValueError:
                print("\n[ERRO] Entrada numérica inválida (preço, quantidade ou ID). A atualização foi cancelada.")
                pausar()
                continue

            produto_atualizado = Produto(nome, descricao, preco, qtd, minimo, id_forn, produto_id_para_atualizar)

            # Requisito 6.d.6 e 6.d.7: Realiza a atualização e exibe o registro atualizado
            if ctrl_produto.atualizar_produto(produto_atualizado):
                print("\nRegistro atualizado:")
                print(produto_atualizado.to_string())
            
            # Requisito 6.d.8: Pergunta se deseja atualizar mais algum
            if not perguntar_sim_ou_nao("\nDeseja atualizar mais algum registro? (S/N): "):
                break

        elif opcao_entidade == '2':
            exibir_lista_fornecedores(ctrl_fornecedor)
            try:
                fornecedor_id_para_atualizar = int(input("Digite o ID do fornecedor que deseja atualizar: "))
            except ValueError:
                print("\n[ERRO] ID inválido. Por favor, digite apenas números.")
                pausar()
                continue
            
            # --- NOVA LÓGICA: BUSCAR DADOS ANTIGOS ---
            fornecedor_antigo_tupla = ctrl_fornecedor.get_fornecedor_por_id(fornecedor_id_para_atualizar)

            if not fornecedor_antigo_tupla:
                print(f"\n[ERRO] Fornecedor com ID {fornecedor_id_para_atualizar} não encontrado.")
                pausar()
                continue
            
            # Converte a tupla em um objeto Fornecedor
            # (id, nome, tel, email, end)
            fornecedor_antigo = Fornecedor(
                nome=fornecedor_antigo_tupla[1], 
                telefone=fornecedor_antigo_tupla[2], 
                email=fornecedor_antigo_tupla[3], 
                endereco=fornecedor_antigo_tupla[4], 
                fornecedor_id=fornecedor_antigo_tupla[0]
            )

            print(f"\n--- Atualizando Fornecedor ID {fornecedor_id_para_atualizar} ---")
            print("(Pressione Enter para manter o valor atual)")

            nome = input(f"Novo Nome (Atual: {fornecedor_antigo.nome}): ") or fornecedor_antigo.nome
            if not nome.strip(): 
                print("\n[ERRO] O nome do fornecedor não pode ser vazio.")
                continue
                
            telefone = input(f"Novo Telefone (Atual: {fornecedor_antigo.telefone}): ") or fornecedor_antigo.telefone
            email = input(f"Novo Email (Atual: {fornecedor_antigo.email}): ") or fornecedor_antigo.email
            endereco = input(f"Novo Endereço (Atual: {fornecedor_antigo.endereco}): ") or fornecedor_antigo.endereco

            fornecedor_atualizado = Fornecedor(nome, telefone, email, endereco, fornecedor_id_para_atualizar)

            if ctrl_fornecedor.atualizar_fornecedor(fornecedor_atualizado):
                print("\nRegistro atualizado:")
                print(fornecedor_atualizado.to_string())
            
            if not perguntar_sim_ou_nao("\nDeseja atualizar mais algum registro? (S/N): "):
                break

        elif opcao_entidade == '3':
            break
        else:
            print("\nOpção inválida.")
            pausar()



def menu_relatorios():
    """Menu para exibir relatórios (Requisito 6.a)."""
    ctrl_relatorios = ControllerRelatorios()
    ctrl_produto = ControllerProduto() # Adicionado para buscar dados do fornecedor
    
    while True:
        limpar_tela()
        print("##############################################")
        print("#            MENU DE RELATÓRIOS            #")
        print("##############################################")
        
        print("\nEscolha um relatório:")
        print("1 - Compras Agrupadas por Fornecedor (Sumarização)")
        print("2 - Relatório Detalhado de Compras (Junção)")
        print("3 - Produtos com Estoque Baixo (Necessário Repor)")
        print("4 - Voltar ao menu principal")
        opcao = input("Escolha uma opção: ")

        if opcao == '1':
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
            limpar_tela()
            print("--- Relatório: Detalhado de Compras ---")
            rows = ctrl_relatorios.gerar_relatorio_detalhado_compras()
            if not rows:
                print("Nenhum dado encontrado.")
            else:
                print(f"{'ID':<4} | {'DATA':<20} | {'PRODUTO':<18} | {'FORNECEDOR':<18} | {'QTD':<5} | {'VALOR (R$)':<10}")
                print("-" * 83)
                for row in rows:
                    data_formatada = row[1].strftime('%Y-%m-%d %H:%M')
                    print(f"{row[0]:<4} | {data_formatada:<20} | {row[2]:<18} | {row[3]:<18} | {row[4]:<5} | {row[5]:<10.2f}")
            pausar()
            
        elif opcao == '3':
            limpar_tela()
            print("--- Relatório: Produtos com Estoque Baixo ---")
            
            rows = ctrl_relatorios.gerar_relatorio_estoque_baixo() 
            
            if not rows:
                print("Nenhum produto com estoque baixo encontrado.")
            else:
                print("Os seguintes produtos precisam de reposição (contatar fornecedor):")
                print(f"\n{'ID':<4} | {'PRODUTO':<25} | {'QTD ATUAL':<10} | {'MÍNIMO':<10} | {'NECESSITA':<10} | {'FORNECEDOR':<20} | {'TELEFONE':<15}")
                print("-" * 110)
                for row in rows:
                    # Agora a query no controller_relatorios.py foi modificada para retornar 7 colunas
                    # (produto_id, nome, quantidade_estoque, estoque_minimo, necessita_comprar, nome_fornecedor, telefone_fornecedor)
                    # Então, podemos acessar row[5] e row[6]
                    print(f"{row[0]:<4} | {row[1]:<25} | {row[2]:<10} | {row[3]:<10} | {row[4]:<10} | {row[5]:<20} | {row[6]:<15}")
            pausar()

        elif opcao == '4':
            break
        else:
            print("\nOpção inválida.")
            pausar()

def menu_estoque(ctrl_produto: ControllerProduto):
    """Menu para visualizar o estoque completo."""
    while True:
        limpar_tela()
        print("##############################################")
        print("#               ESTOQUE                      #")
        print("##############################################")
        
        produtos = ctrl_produto.listar_produtos()
        
        if not produtos:
            print("\nNenhum produto encontrado no estoque.")
        else:
            print("\nProdutos em Estoque:")
            print(f"{'ID':<4} | {'NOME':<30} | {'PREÇO (R$)':<12} | {'QTD ESTOQUE':<12}")
            print("-" * 65)
            for produto in produtos:
                print(f"{produto[0]:<4} | {produto[1]:<30} | {produto[2]:<12.2f} | {produto[3]:<12}")
        
        print("\nOpções:")
        print("1 - Atualizar visualização")
        print("2 - Voltar ao menu principal")
        
        opcao = input("\nEscolha uma opção: ")
        
        if opcao == '2':
            break
        elif opcao == '1':
            continue
        else:
            print("\nOpção inválida!")
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
    """Busca e exibe a lista de produtos de forma formatada."""
    print("\n--- Lista de Produtos Cadastrados ---")
    produtos = ctrl_produto.listar_produtos()
    
    if not produtos:
        print("Nenhum produto encontrado no estoque.")
    else:
        print(f"{'ID':<4} | {'NOME':<25} | {'PREÇO (R$)':<12} | {'QTD ESTOQUE':<12}")
        print("-" * 60)
        for row in produtos:
            # row[0]: id, row[1]: nome, row[2]: preco, row[3]: qtd
            print(f"{row[0]:<4} | {row[1]:<25} | {row[2]:<12.2f} | {row[3]:<12}")
    print("------------------------------------------------------------\n")


def exibir_lista_fornecedores(ctrl_fornecedor: ControllerFornecedor):
    """Busca e exibe a lista de fornecedores de forma formatada."""
    print("\n--- Lista de Fornecedores Cadastrados ---")
    fornecedores = ctrl_fornecedor.listar_fornecedores()
    if not fornecedores:
        print("Nenhum fornecedor encontrado.")
    else:
        print(f"{'ID':<4} | {'NOME':<25} | {'TELEFONE':<20} | {'EMAIL':<25}")
        print("-" * 80)
        for row in fornecedores:
            # row[0]: id, row[1]: nome, row[2]: telefone, row[3]: email
            print(f"{row[0]:<4} | {row[1]:<25} | {row[2]:<20} | {row[3]:<25}")
    print("--------------------------------------------------------------------------------\n")