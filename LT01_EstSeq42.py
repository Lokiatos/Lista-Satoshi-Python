# Objetivo: Calcule e mostre a sére 1 + 2/3 + 3/5 + ... + 50/99
# Programador: Hugo Leça Ribeiro
# Data de Elaboração: 16.09.2019

num = 1
den = 1
soma = 0

while num <= 50:
    soma = (soma + (num / den))
    num = (num + 1)
    den = (den + 2)
print(soma)
