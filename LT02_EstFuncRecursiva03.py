# Calcular e mostrar a soma da série: 1/1 + 1/2 + 1/3 + ... + 1/N - Como recursiva

# Função Recursiva
def Fserie3(num):
    soma = 0
    if num == 1:
        return num
    else:
        soma = 1 / num + Fserie3(num - 1)
        return soma


# Algoritmo Principal
N = int(input("Digite aqui um número "))
print(Fserie3(N))
