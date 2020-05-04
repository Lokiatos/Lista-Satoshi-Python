# Objetivo: Receber um número N. Calcular e mostrar a série 1 + 1/1! + 1/2! + ... + 1/N!
# Programador: Hugo Leça Ribeiro
# Data de Elaboração: 13.09.19

seq = 1
n = 0
fat = 1
n = int(input("Digite aqui o número desejado: "))
ifat = n

if n >= 1:
    while n >= 1:
        while ifat >= 1:
            fat = fat * ifat
            ifat = ifat - 1
        seq = seq + (1 / fat)
        n = n - 1
        ifat = n
        fat = 1
    print("A soma dessa sequência será de: ", seq)
else:
    print("O número deve ser igual ou maior do que 1")
