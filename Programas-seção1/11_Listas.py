# Exercício de fixação de listas
# Objetivo: Identificar qual o indice de cada nome na lista
# Exemplo: 0 - Maria /n 1 - Helena /n 2 - Luiz

lista = ["Maria", "Helena", "Luiz", "Nicolas",]
contador = 0

for nome in lista:
    print(f"{contador} - {lista[contador]}")
    contador += 1