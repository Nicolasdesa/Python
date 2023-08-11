# Exercício de fixação de funções
# Objetivos: 1 - Criar uma função que multiplica argumentos não nomeados
# 2 - Criar uma função que retorna se o número é impar ou par

def multiplicar(*args):
    total = 1 # 1 porque qualquer numero * 0 é 0
    for numero in args:
        total += numero
    return total