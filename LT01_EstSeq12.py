# Objetivo: Receber o ano de nascimento e o ano atual. Calcular e mostrar a sua idade e quantos anos terá daqui 17 anos.
# Observação: Neste exercício não estão inclusos os meses e dias.
# Programador: Hugo Leça Ribeiro
# Data de Elaboração: 04.09.2019

anoAtual = 2019
anoDeNascimento = int(input("Digite aqui seu ano de nascimento: "))
idade = (anoAtual - anoDeNascimento)
idadeDaqui17Anos = (idade + 17)

print("Sua idade atual é de: ", idade, "anos" "\nE sua idade daqui 17 anos será de: ", idadeDaqui17Anos, "anos")
