# Objetivo: Receba um número inteiro. Calcule e mostre o seu fatorial.
# Programador: Hugo Leça Ribeiro
# Data de Elaboração: 11.09.19

fat = 1
number = int(input("Digite um número para vermos seu fatorial: "))

if number >= 0:
    while number > 0:
        fat = (fat * number)
        number = (number - 1)
    print("O fatorial será de : ", fat)
else:
    print("O fatorial será de 0")
