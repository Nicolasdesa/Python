#Exercício de fixação dos operadores aritméticos e suas precedências
#Utilização de f-strings
#Algoritmo que calcula o IMC de uma pessoa

nome = "Luiz Otávio"
altura = 1.80
peso = 95
imc = peso / (altura ** 2) #Índice de massa corporal

print(f"{nome} seu IMC é: {imc:.2f}") #Uso da formatação