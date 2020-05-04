# Objetivo: Receber os coeficientes A, B e C de uma equação do 2º grau (AX²+BX+C=0). Calcular e mostrar as raízes reais (considerar que a equação possui 2 raízes)
# Programador: Hugo Leça Ribeiro
# Data de Elaboração: 28/08/2019

A = float(input("digite aqui o valor de A "))
B = float(input("digite aqui o valor de B"))
C = float(input("Digite aqui o valor de C "))
delta = (B ** 2) - (4 * A * C)

print("O valor de delta é de: ", delta)

X1 = (-B + (delta ** 0.5)) / (2 * A)
X2 = (-B - (delta ** 0.5)) / (2 * A)

print("O valor de X1 é de ", X1)
print("O valor de X2 é de ", X2)
