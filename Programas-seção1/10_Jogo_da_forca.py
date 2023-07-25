# Exercício de fixação de estrutura de repetição (for/in)
# Objetivo: Criar um jogo de forca

import os

palavra_secreta = "programa"
numero_tentativas = 0
letras_acertadas = ""

while True:
    tentativa = input("Digite uma letra: ")
    numero_tentativas += 1 

    if len(tentativa) > 1:
        print("Digite somente uma letra.")
        continue

    if tentativa in palavra_secreta:
        letras_acertadas += tentativa

    palavra_formada = ""
    for letra_secreta in palavra_secreta:
        if letra_secreta in letras_acertadas:
            palavra_formada += letra_secreta
        else:
            palavra_formada += "*"
    
    print(palavra_formada)

    if palavra_formada == palavra_secreta:
        os.system("cls") #limpar o terminal
        print(f'Parábens, a palavra é "{palavra_secreta}"!')
        print(f"Você acertou em {numero_tentativas} tentativas")
        break