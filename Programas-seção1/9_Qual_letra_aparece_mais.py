# Exercício de fixação (treino de lógica) sem usar for
# Objetivo: Identificar qual letra apareceu mais vezes na frase

frase = "O Python é uma linguagem de programação multiparadigma" \
"Python foi criado por Guido van Rossum."

indice = 0
maior_quantidade = 0
letra_mais_vezes = ""

while indice < len(frase):
    letra_atual = frase[indice]
    letra_atual_apareceu = frase.count(letra_atual)

    if letra_atual == " ":
        indice += 1
        continue

    if maior_quantidade < letra_atual_apareceu:
        maior_quantidade = letra_atual_apareceu
        letra_mais_vezes = letra_atual

    print(letra_atual, letra_atual_apareceu)

    indice += 1

print(f'A letra que apareceu mais vezes foi "{letra_mais_vezes}" que apareceu {maior_quantidade} vezes')