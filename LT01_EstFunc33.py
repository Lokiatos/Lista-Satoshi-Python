# Objetivo: Receber um número. Calcular e mostrar a série 1 + 1/2 + 1/3 + ... + 1/número
# Programador: Hugo Leça Ribeiro
# Data de Elaboração: 11.09.19


# Função
def Fserie(num):
    seq = 1
    while num > 1:
        seq = seq + 1 / num
        num = (num - 1)
    return (seq)


# Principal
n = 0

n = int(input("Digite aqui o número desejado: "))
if n >= 1:
    print(Fserie(n))  # Print da Função
else:
    print("O número precisa ser maior ou igual a 1")
