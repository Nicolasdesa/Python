# Exercício de fixação cm dicionários
# Objetivo: Sitema de perguntas e respostas

perguntas = [
    {
        "Pergunta": "Quanto é 2+2?",
        "Opções": ["1", "3", "4", "5"],
        "Resposta": "4"
    },
    {
        "Pergunta": "Quanto é 5x5?",
        "Opções": ["25", "55", "10", "51"],
        "Resposta": "25"
    },
    {
        "Pergunta": "Quanto é 10/2?",
        "Opções": ["4", "5", "2", "1"],
        "Resposta": "5"
    }
]


qntd_acertos = 0
for pergunta in perguntas:
    print("Pergunta:", pergunta["Pergunta"])
    print()

    opcoes = pergunta["Opções"]
    for i, opcao in enumerate(opcoes):
        print(f"{i})", opcao)
    print()

    escolha = input("Escolha uma opção: ")

    acertou = False
    escolha_int = None
    qntd_opcoes = len(opcoes)

    if escolha.isdigit():
        escolha_int = int(escolha)
    
    if escolha_int is not None:
        if escolha_int >= 0 and escolha_int < qntd_opcoes:
            if opcoes[escolha_int] == pergunta["Resposta"]:
                acertou = True

    if acertou:
        qntd_acertos += 1
        print("Acertou")
    else:
        print("Errou")
    
print(f"Você acertou {qntd_acertos} vezes de {len(perguntas)}")