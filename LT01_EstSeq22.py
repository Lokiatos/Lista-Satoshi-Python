# Objetivo: Receber 2 valores inteiros e diferentes. Mostrar seus valores em ordem crescente.
# Programador: Hugo Leça Ribeiro
# Data de Elaboração: 04.09.2019

n1 = int(input("Digite aqui o valor do primeiro número: "))
n2 = int(input("Digite aqui o valor do segundo número: "))

if n1 > n2:
    print(n2, "e", n1)
elif n2 > n1:
    print(n1, "e", n2)
else:
    print("Os números são iguais, não há diferença entre eles")
