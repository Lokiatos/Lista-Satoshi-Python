# Objetivo: Receba o número da base e do expoente. Calcule e mostre o valor da potência.
# Programador: Hugo Leça Ribeiro
# Data de Elaboração: 17.09.2019

base = 0
pot = 0
result = 0

base = float(input("Digite aqui o número "))
pot = float(input("Digite aqui a potência "))
result = base

while pot > 1:
    result = (result * base)
    pot = pot - 1
print(result)
