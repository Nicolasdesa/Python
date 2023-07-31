# Exercício de conclusão do módulo 1
# Objetivo: Criar um programa para validar o CPF inserido

cpf_enviado = "746.824.890-70" \
    .replace(".", "") \
    .replace("-", "")   # Substituição de caracteres para o CPF ficar integro

nove_digitos = cpf_enviado[:9]  #Separa os 9 diígitos da String
contador_regressivo1 = 10
soma_cpf = 0

if cpf_enviado[0] * len(cpf_enviado) == cpf_enviado:
    print("CPF inválido")

for digito in nove_digitos:
    soma_cpf += int(digito) * contador_regressivo1 # Int digito porque era uma Str
    contador_regressivo1 -= 1

primeiro_digito = (soma_cpf * 10) % 11
primeiro_digito = primeiro_digito if primeiro_digito <= 9 else 0
# Linha acima: Se o primeiro digito for maior que 9 então ele é 0

dez_digitos = nove_digitos + str(primeiro_digito)
contador_regressivo2 = 11

resultado_digito2 = 0
for digito in dez_digitos:
    resultado_digito2 += int(digito) * contador_regressivo2
    contador_regressivo2 -= 1
segundo_digito = (resultado_digito2 * 10) % 11
segundo_digito = segundo_digito if segundo_digito <= 9 else 0

cpf_verificador = f"{nove_digitos}{primeiro_digito}{segundo_digito}"

if cpf_enviado == cpf_verificador:
    print("O CPF enviado é válido")
else:
    print("O CPF enviado é invalido")