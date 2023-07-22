# Exercício de fixação dos blocos de repetição e tratamento de erros
# Objetivo: criar uma calculadora

while True:
    numero_1 = input("Digite um número:")
    operador = input("Digite um operador para o calculo (+, -, *, /): ")
    numero_2 = input("Digite o outro numero: ")
    
    numeros_validos = None
    num_1_float = 0
    num_2_float = 0

    try:
        num_1_float = float(numero_1)
        num_2_float = float(numero_2)
        numeros_validos = True
    except:
        numeros_validos = None
    
    if numeros_validos is None:    
        print("Um ou ambos os números são invalidos!")
        continue

    operadores_permitidos = "+-*/"

    if operador not in operadores_permitidos:
        print("Operador inválido")
        continue
    
    if len(operador) > 1:
        print("Digite somente um operador")
        continue

    calculo = 0

    if operador == "+":
        calculo = num_1_float + num_2_float
    elif operador == "-":
        calculo = num_1_float - num_2_float
    elif operador == "*":
        calculo = num_1_float * num_2_float 
    elif operador == "/":
        calculo = num_1_float / num_2_float
    else: 
        print("Você não deveria estar aqui kk")

    print(f"{num_1_float} {operador} {num_2_float} = {calculo}")

    sair = input("Quer sair? [s]im: ").lower().startswith("s")
    
    if sair is True:
        break