# Exercício de fixação de listas e suas funcionalidades
# Objetivo: Criar uma lista de compra onde o usuário tem a opção de:
# Adicionar, excluir e listar itens.
import os

print("Bem vindo a sua lista de compras!")
lista = []

while True:
    funcao = input("Que tarefa você deseja realizar: \n \t [a]dicionar, [e]xcluir, [l]istar itens: ")

    if funcao.lower().startswith("a"): # Bloco de adição de itens
        os.system("cls")
        adicionar = input("Qual item você deseja adicionar? ")
        lista.append(adicionar)
        print(f"Item {adicionar} foi adicionado")

    elif funcao.lower().startswith("e"): # Bloco de exclusão
        try: 
            excluir = int(input("Qual indice você deseja excluir? "))
            del lista[excluir]
            print(f"O item {lista[excluir]} foi removido")
        except: print("Coloque apenas numeros disponveis na lista")

    elif funcao.lower().startswith("l"): # Bloco de listagem
        os.system("cls")
        if len(lista) > 0:
            for indice, item in enumerate(lista):
                print(indice, item)
        else: print("Sua lista esta vazia")

    else:
        os.system("cls")
        print("Selecione apenas as opções disponíveis")
        continue