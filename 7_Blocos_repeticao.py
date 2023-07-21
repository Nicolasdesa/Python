# Exercício de fixação dos blocos de repetição
# Objetivo: printar um nome com um * antes de todas as letras

nome = "Nicolas de Sá"
indice = 0
nova_string = ""

while indice < len(nome):
    nova_string += f"*{nome[indice]}"
    indice += 1
    print(nova_string)

print(nova_string)