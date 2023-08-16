# Exercício de fixação de funções
# Objetivo: criar um programa que possa multiplicar qualquer numero em qualquer
# multiplicador (utilizando high order e closure)

def criar_multiplicador(multiplicador):
    def multiplicar(numero):
            resultado = multiplicador * numero
            return resultado
    return multiplicar

duplicar = criar_multiplicador(2)
triplicar = criar_multiplicador(3)
quadruplicar = criar_multiplicador(4)

print(duplicar(5))
print(triplicar(5))
print(quadruplicar(5))