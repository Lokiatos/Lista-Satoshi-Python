# Objetivo: Calcule e mostre o quadrado dos números entre 10 e 150.
# Programador: Hugo Leça Ribeiro
# Data de Elaboração: 24.10.19


# Função
def Fquadrados(num):
    Quad = 0
    while num <= 149:
        Quad = (num ** 2)
        print(Quad)
        num = num + 1


# Algoritmo Principal
N = 11
Fquadrados(N)
