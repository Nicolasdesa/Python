# Exercício de fixação de estrutura de repetição (for/in)
# Objetivo: Criar um jogo de forca

palavra_secreta = "programa"
numero_tentativas = 0

while True:
    tentativa = input("Digite uma letra: ")
    palavra_oculta = ""
    numero_tentativas += 1 

    if len(tentativa) > 1:
        print("Digite somente uma letra.")
        continue

    for i in palavra_secreta:
        if tentativa == palavra_secreta[i]:
            palavra_oculta += tentativa
        elif palavra_oculta[i] != "*":
            palavra_oculta += "*"
    
    print(palavra_oculta)