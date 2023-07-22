# Exercício de fixação de estrutura de repetição (for/in)
# Objetivo: Criar um jogo de forca

palavra_secreta = "programa"

while True:
    tentativa = input("Digite uma letra: ")
    palavra_oculta = "*" * len(palavra_secreta) 

    if len(tentativa) > 1:
        print("Digite somente uma letra.")
        continue

    for i in palavra_secreta:
        if tentativa == i:
            palavra_oculta[i] = tentativa
    print(palavra_oculta)