# Objetivo: Receber um número N. Calcular e mostrar a série 1 + 1/1! + 1/2! + ... + 1/N!
# Programador: Hugo Leça Ribeiro
# Data de Elaboração: 25.10.19


# Função
def Fserie(num):
    seq = 1
    fat = 1
    ifat = num
    while num >= 1:
        while ifat >= 1:
            fat = fat * ifat
            ifat = ifat - 1
        seq = seq + (1 / fat)
        num = num - 1
        ifat = num
        fat = 1
    return (seq)


# Algoritmo Principal
n = int(input('Digite aqui o número desejado: '))
if n >= 1:
    print(f'A soma dessa sequência será de: {Fserie(n)}')
else:
    print('O número deve ser igual ou maior do que 1')
