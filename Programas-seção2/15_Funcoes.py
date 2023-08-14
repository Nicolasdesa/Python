# Exercício de fixação de funções
# Objetivos: 1 - Criar uma função que multiplica argumentos não nomeados
# 2 - Criar uma função que retorna se o número é impar ou par

def multiplicar(*args):
    total = 1 # 1 porque qualquer numero * 0 é 0
    for numero in args:
        total *= numero
    return total

resultado = multiplicar(1, 3, 4, 6, 23, 4, 7)
print(resultado)

def impar_ou_par(numero):
    if numero % 2 == 0:
        return "O número das multiplicações é par"
    return "O número das multiplicações é impar"
    
print(impar_ou_par(resultado))