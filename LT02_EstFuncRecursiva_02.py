# Calcular e mostrar a soma da série (N) + (N-1) +(N - 2) ... (1) - Como recursiva

# Função Recursiva
def Fserie2(num):
    soma = 0
    if num == 1:
        return num
    else:
        soma = num + Fserie2(num - 1)
        return soma


# Algoritmo Principal
n = int(input('Digite aqui um número '))
print(Fserie2(n))
