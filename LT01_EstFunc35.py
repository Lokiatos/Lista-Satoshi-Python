# Objetivo: Receber 2 números inteiros, verificar qual é o maior entre eles. Calcular e mostrar o resultado da somatória dos números ímpares entre esses valores.
# Programador: Hugo Leça Ribeiro
# Data de Elaboração: 24.10.19


# Função
def Fsomar(n1, n2):
    aux = 0
    soma = 0
    if n1 > n2:
        if n2 % 2 == 0:
            aux = n2 + 1
        else:
            aux = n2 + 2
        while aux < n1:
            soma = (aux + soma)
            aux = aux + 2
        return (soma)
    else:
        if n1 % 2 == 0:
            aux = n1 + 1
        else:
            aux = n1 + 2
        while aux < n2:
            soma = (aux + soma)
            aux = (aux + 2)
        return (soma)


# Algoritmo principal
n1 = int(input("Digite aqui o primeiro número: "))
n2 = int(input("Digite aqui o segundo número: "))

if n1 < n2:
    print(f'A soma dos números ímpares entre {n1} e {n2} é de: {Fsomar(n1, n2)}')  # Caso n1 seja menor que n2
else:
    print(f'A soma dos números ímpares entre {n2} e {n1} é de: {Fsomar(n1, n2)}')  # Caso n2 seja menor que n1
