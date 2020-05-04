# Receber o tipo de investimento (1 = poupança e 2 = renda fixa) e o valor do investimento. Calcular e mostrar o valor corrigido em 30 dias sabendo que a poupança rende 3% e a renda fixa rende 5%. Demais tipos não serão considerados.
# Programador: Hugo Leça Ribeiro
# Data de Elaboração: 05.09.2019

dias = 30  # inseri os dias para futuramente poder modificar facilmente
poupanca = 1.03
rendaFixa = 1.05
meses = int(dias / 30)

valor = float(input("Digite aqui o valor do investimento: "))
tipoDeInvestimento = int(input("Digite 1 para poupança, e 2 para renda fixa "))

if tipoDeInvestimento == 1:
    valorCorrigido = (valor * 1.03 * meses)
    print("Seu valor corrigido é de: ", valorCorrigido)
elif tipoDeInvestimento == 2:
    valorCorrigido = (valor * 1.05 * meses)
    print("Seu valor corrigido é de: ", valorCorrigido)
elif (tipoDeInvestimento != 1) or (tipoDeInvestimento != 2):
    print("Você digitou um tipo de investimento inexistente")
