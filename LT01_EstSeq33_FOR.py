# Objetivo: Receber um número. Calcular e mostrar a série 1 + 1/2 + 1/3 + ... + 1/número
# Programador: Hugo Leça Ribeiro
# Data de Elaboração: 13.09.19

serie = 1
i = int(input("Digite aqui o valor desejado "))
if i >= 1:
    for i in range(i, 1, -1):
        serie = (float)(serie + 1 / i)
    print(serie)
else:
    print("O número precisa ser maior ou igual a 1")
