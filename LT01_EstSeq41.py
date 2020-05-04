# Objetivo: Mostre todas as possibilidades de 2 dados de forma que a soma tenha como resultado 7.
# Programador: Hugo Leça Ribeiro
# Data de Elaboração: 16.09.2019

d1 = 1
d2 = 1
soma = 0

while d1 <= 6:
    while d2 <= 6:
        soma = (d1 + d2)
        if soma == 7:
            print(d1, d2)
        d2 = (d2 + 1)
    d2 = 1
    d1 = (d1 + 1)
