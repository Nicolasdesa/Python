# Exercício 1
num = input("Informe um numero inteiro: ")

if num.isdigit:
    num = int(num)

    if (num % 2) == 0:
        print("Este numero é par")
    else : 
        print("Este numero é impar")
        
else:
    print("Você não digitou um numero inteiro")


# Exercício 2
hora = input("Digite um horario: ")

if hora.isdigit:
    hora = float(hora)

    if hora >= 0 and hora <= 11:
        print("Bom dia usuário!")
    elif hora >= 12 and hora <=17:
        print("Boa tarde usuário!")
    else:
        print("Boa noite usuário!")

else:
    print("Digite uma hora válida")


# Exercício 3
nome = input("Digite seu primeiro nome: ")

if len(nome) <= 4:
    print("Seu nome é curto")
elif len(nome) == 5 or len(nome) == 6:
    print("Seu nome tem um tamanho normal")
else:
    print("Seu nome é muito grande")