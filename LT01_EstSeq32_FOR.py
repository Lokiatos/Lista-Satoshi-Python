# Objetivo: Receba um número inteiro. Calcule e mostre o seu fatorial.
# Programador: Hugo Leça Ribeiro
# Data de Elaboração: 11.09.19

fat = 1
number = int(input("Digite aqui o número desejado: "))

if number < 0:
    fat = 0
else:
    for number in range(number, 0, -1):
        fat = (fat * number)
print(fat)
