# Exercício de fixação de listas e suas funcionalidades
# Objetivo: Criar uma lista de compra onde o usuário tem a opção de:
# Adicionar, excluir e listar itens.
import os

print("Bem vindo a sua lista de compras!")
lista = []

while True:
    funcao = input("Que tarefa você deseja realizar: \n \t [a]dicionar, [e]xcluir, [l]istar itens: ")

    if funcao.lower().startswith("a"): # Bloco de adição de itens
        adicionar = input("Qual item você deseja adicionar? ")
        lista.append(adicionar)

    elif funcao.lower().startswith("e"): # Bloco de exclusão
        try: excluir = int(input("Qual indice você deseja excluir? "))
        except: print("Coloque apenas numeros disponveis na lista")
        print(f"O item {lista[excluir]} foi removido")
        del lista[excluir]

    elif funcao.lower().startswith("l"): # Bloco de listagem
        os.system("cls")
        for i in enumerate(lista):
            indice, item = i
            print(indice, item)

    else:
        print("Selecione apenas as opções disponíveis")
        continue