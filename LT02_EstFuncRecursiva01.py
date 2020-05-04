# Calcular e mostrar a soma da seguinte série: 1 + 2 + 3 + ... + 100 - Como recursiva
n = 0


# Função Recursiva
def Fserie1(num):
    soma = 0
    if num == 1:
        return num
    else:
        soma = num + Fserie1(num - 1)
        return soma


# Algoritmo Principal
n = 100
print(Fserie1(n))
