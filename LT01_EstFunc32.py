# Objetivo: Receba um número inteiro. Calcule e mostre o seu fatorial.
# Programador: Hugo Leça Ribeiro
# Data de Elaboração: 24.10.19


# Função
def Ffat(n):
    fat = 1
    while n > 0:
        fat = (fat * n)
        n = (n - 1)
    return fat


# Principal
n = int(input("Digite um número para vermos seu fatorial: "))
if n >= 0:
    print("O fatorial será de : ", Ffat(n))  # Print da função
else:
    print("O fatorial será de 0")
