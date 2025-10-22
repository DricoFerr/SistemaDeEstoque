import os
import time

def limpar_tela():
    """ Limpa o console para melhorar a legibilidade """
    # 'nt' é para Windows, 'posix' é para Mac/Linux
    os.system('cls' if os.name == 'nt' else 'clear')

def pausar(mensagem: str = "\nPressione Enter para continuar..."):
    """ Pausa a execução e espera o usuário pressionar Enter """
    print(mensagem)
    input()