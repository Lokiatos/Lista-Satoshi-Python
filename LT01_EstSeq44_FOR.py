# Objetivo: Receba o número da base e do expoente. Calcule e mostre o valor da potência.
# Programador: Hugo Leça Ribeiro
# Data de Elaboração: 17.09.2019

base = 0
pot = 0

base = int(input("Digite aqui o número "))
pot = int(input("Digite aqui a potência "))
result = base

for pot in range(pot, 1, -1):
    result = (result * base)
print(result)
