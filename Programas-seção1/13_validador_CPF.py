# Exercício de conclusão do módulo 1
# Objetivo: Criar um programa para validar o CPF inserido

cpf = "74682489070"
nove_digitos = cpf[:9]  #Separa os 9 diígitos da String, através de fatiamento
contador_regressivo = 10
soma_cpf = 0

for digito in nove_digitos:
    soma_cpf += int(digito) * contador_regressivo # Int digito porque era uma Str
    contador_regressivo -= 1

primeiro_digito = (soma_cpf * 10) % 11
primeiro_digito = primeiro_digito if primeiro_digito <= 9 else 0
# Linha acima: Se o primeiro digito for maior que 9 então ele é 0