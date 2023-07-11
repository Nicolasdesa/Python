#Exercício de fixação com input() para coleta de dados
#Exercício de fixação de condições e comparações

primeiro_valor = input("Digite um valor: ")
segundo_valor = input("Digite outro valor: ")

if primeiro_valor > segundo_valor:
    print(f"{primeiro_valor=} é maior que o {segundo_valor=}")
elif segundo_valor > primeiro_valor:
    print(f"{segundo_valor=} é maior que o {primeiro_valor=}")
else:
    print(f"O {primeiro_valor=} e o {segundo_valor=} são iguais")