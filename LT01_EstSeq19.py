# Objetivo: Receber 2 valores reais. Calcular e mostrar o maior deles.
# Programador: Hugo Leça Ribeiro
# Data de Elaboração: 04.09.2019

n1 = float(input("Digite aqui o valor do primeiro número: "))
n2 = float(input("Digite aqui o valor do segundo número: "))

if (n1 > n2):
    print("O maior número entre os dois é: ", n1)
elif n2 > n1:
    print("O maior número entre os dois é: ", n2)
else:
    print("Os números são iguais")
