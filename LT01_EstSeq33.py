# Objetivo: Receber um número. Calcular e mostrar a série 1 + 1/2 + 1/3 + ... + 1/número
# Programador: Hugo Leça Ribeiro
# Data de Elaboração: 11.09.19

n = int(input("Digite aqui o número desejado "))

if n >= 1:
    while n > 1:
        seq = seq + 1 / n
        n = (n - 1)
    print(seq)
else:
    print("O número precisa ser maior ou igual a 1")
