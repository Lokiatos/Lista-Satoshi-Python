# Objetivo: Receber 2 números inteiros. Verificar e mostrar se o maior número é múltiplo do menor.
# Programador: Hugo Leça Ribeiro
# Data de Elaboração: 24.10.2019


# Procedimento
def p_verificar(number1, number2):
    if (number1 > number2):
        if ((number1 % number2) == 0):
            print("O maior número é múltiplo do menor")
        else:
            print("O maior número não é múltiplo do menor")
    elif (number2 > number1):
        if ((number2 % number1) == 0):
            print("O maior número é múltiplo do menor")
        else:
            print("O maior número não é múltiplo do menor")
    else:
        print("Os números são iguais")


# Principal
n1 = int(input("Digite aqui o primeiro número: "))
n2 = int(input("Digite aqui o segundo número: "))
p_verificar(n1, n2)  # Chamamento do Procedimento
