# Objetivo: Receber 2 valores inteiros. Calcular e mostrar o resultado da diferença do maior pelo menor.
# Programador: Hugo Leça Ribeiro
# Data de Elaboração: 04.09.2019

n1 = int(input("Digite aqui o valor do primeiro número: "))
n2 = int(input("Digite aqui o valor do segundo número: "))

if (n1 >= n2):
    diferenca = (n1 - n2)
else:
    diferenca = (n2 - n1)

print("A diferença entre os números é de: ", diferenca)
