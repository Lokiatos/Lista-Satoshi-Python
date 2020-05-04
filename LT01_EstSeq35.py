# Objetivo: Receber 2 números inteiros, verificar qual é o maior entre eles. Calcular e mostrar o resultado da somatória dos números ímpares entre esses valores.
# Programador: Hugo Leça Ribeiro
# Data de Elaboração: 13.09.19

n1 = 0
n2 = 0
aux = 0
soma = 0

n1 = int(input("Digite aqui o primeiro número "))
n2 = int(input("Digite aqui o segundo número "))

if n1 > n2:
    if n2 % 2 == 0:
        aux = n2 + 1
    else:
        aux = n2 + 2
    while aux < n1:
        soma = (aux + soma)
        aux = aux + 2
    print("A soma dos números ímpares entre ", n2, " e ", n1, " é de: ", soma)
else:
    if n1 % 2 == 0:
        aux = n1 + 1
    else:
        aux = n1 + 2
    while aux < n2:
        soma = (aux + soma)
        aux = (aux + 2)
    print("A soma dos números ímpares entre ", n1, " e ", n2, " é de: ", soma)
