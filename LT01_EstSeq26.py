# Objetivo: Receber 2 números inteiros. Verificar e mostrar se o maior número é múltiplo do menor.
# Programador: Hugo Leça Ribeiro
# Data de Elaboração: 05.09.2019

n1 = int(input("Digite aqui o primeiro número: "))
n2 = int(input("Digite aqui o segundo número: "))

if (n1 > n2):
    if ((n1 % n2) == 0):
        print("O maior número é múltiplo do menor")
    else:
        print("O maior número não é múltiplo do menor")
elif (n2 > n1):
    if ((n2 % n1) == 0):
        print("O maior número é múltiplo do menor")
    else:
        print("O maior número não é múltiplo do menor")
else:
    print("Os números são iguais")
